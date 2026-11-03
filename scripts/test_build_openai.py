"""Package trust boundaries must hold with Python optimization enabled too."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "scripts" / "build-openai.py"
SPEC = importlib.util.spec_from_file_location("build_openai", BUILDER)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


def package_files():
    return {
        "plugin.json": (ROOT / "openai/prometheor/plugin.json").read_bytes(),
        "mcp.json": (ROOT / "openai/prometheor/mcp.json").read_bytes(),
        "assets/icon.svg": (ROOT / "assets/icon.svg").read_bytes(),
        "assets/logo.png": (ROOT / "assets/logo.png").read_bytes(),
    }


# Run the actual entry point, with public fixture files in a disposable tree.
# No endpoint is contacted and no artifact can be written outside that tree.
PROBE = r'''
import importlib.util, json, pathlib, sys, tempfile
root = pathlib.Path(sys.argv[1])
spec = importlib.util.spec_from_file_location("build_openai", root / "scripts/build-openai.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
with tempfile.TemporaryDirectory(dir=root / "out/security-611") as temp:
    temp = pathlib.Path(temp)
    paths = {
        "openai/prometheor/plugin.json": root / "openai/prometheor/plugin.json",
        "openai/prometheor/mcp.json": root / "openai/prometheor/mcp.json",
        "assets/icon.svg": root / "assets/icon.svg",
        "assets/logo.png": root / "assets/logo.png",
    }
    for name, source in paths.items():
        target = temp / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    kind = sys.argv[2]
    if kind == "endpoint":
        path = temp / "openai/prometheor/mcp.json"
        data = json.loads(path.read_bytes())
        data["mcpServers"]["prometheor"]["url"] = "https://attacker.example/mcp"
        path.write_text(json.dumps(data))
    if kind == "private_metadata":
        path = temp / "openai/prometheor/plugin.json"
        data = json.loads(path.read_bytes())
        data["client_secret"] = "synthetic-fixture-only"
        path.write_text(json.dumps(data))
    if kind == "symlink":
        path = temp / "assets/logo.png"
        path.unlink()
        path.symlink_to(root / "assets/logo.png")
    if kind == "asset_limit":
        path = temp / "assets/icon.svg"
        path.write_bytes(path.read_bytes() + b" " * (5 * 1024 * 1024))
    m.ROOT = temp
    m.SOURCE = temp / "openai/prometheor"
    m.OUTPUT = temp / "out/package.zip"
    m.main()
'''


class PackageSecurityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        (ROOT / "out/security-611").mkdir(parents=True, exist_ok=True)

    def test_actual_package_remains_valid_and_reproducible(self):
        files = package_files()
        builder.validate(files)
        data = builder.archive(files)
        self.assertEqual(data, builder.archive(files))
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), set(files))
            self.assertEqual({n: archive.read(n) for n in archive.namelist()}, files)

    def test_exact_public_file_allowlist_is_enforced(self):
        files = package_files()
        files["reviewer-instructions.txt"] = b"synthetic-fixture-only"
        with self.assertRaises(ValueError):
            builder.validate(files)

    def test_main_writes_only_a_valid_package(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "out/security-611") as temp:
            previous = builder.OUTPUT
            try:
                builder.OUTPUT = Path(temp) / "package.zip"
                with contextlib.redirect_stdout(io.StringIO()):
                    builder.main()
                self.assertEqual(builder.OUTPUT.read_bytes(), builder.archive(package_files()))
            finally:
                builder.OUTPUT = previous

    def test_entry_point_keeps_security_checks_under_all_optimization_modes(self):
        modes = [([], None), (["-O"], None), (["-OO"], None), ([], "1")]
        for args, optimize in modes:
            for kind in ["valid", "endpoint", "private_metadata", "symlink", "asset_limit"]:
                with self.subTest(args=args, optimize=optimize, kind=kind):
                    env = {k: v for k, v in os.environ.items() if k != "PYTHONOPTIMIZE"}
                    if optimize is not None:
                        env["PYTHONOPTIMIZE"] = optimize
                    result = subprocess.run(
                        [sys.executable, *args, "-c", PROBE, str(ROOT), kind],
                        env=env, capture_output=True, timeout=15,
                    )
                    if kind == "valid":
                        self.assertEqual(result.returncode, 0, result.stderr.decode())
                    else:
                        self.assertNotEqual(result.returncode, 0, "Unsafe package was accepted")


if __name__ == "__main__":
    unittest.main()
