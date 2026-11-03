#!/usr/bin/env python3
"""Validate and deterministically package the OpenAI connector, without credentials."""

import hashlib
import io
import json
from pathlib import Path
import re
import struct
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "openai" / "prometheor"
OUTPUT = ROOT / "out" / "openai" / "prometheor-openai.zip"


def require(condition, message="Invalid connector package"):
    """A security gate that remains active under -O and PYTHONOPTIMIZE."""
    if not condition:
        raise ValueError(message)


def validate(files):
    require(set(files) == {"plugin.json", "mcp.json", "assets/icon.svg", "assets/logo.png"})
    manifest = json.loads(files["plugin.json"])
    mcp = json.loads(files["mcp.json"])
    require(manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
    require(manifest["name"] == "prometheor" and manifest["version"] == "1.0.0")
    require(manifest["author"]["name"] == "Kian Peters")
    extension = manifest["extensions"]["com.openai"]
    # Preserve saved review details, release notes and country targeting on reupload.
    require(set(extension) == {"interface"})
    interface = extension["interface"]
    for field, limit in (("displayName", 30), ("shortDescription", 30),
                         ("longDescription", 4000), ("developerName", 80)):
        value = interface[field]
        require(isinstance(value, str) and 0 < len(value) <= limit, field)
        require(not re.search(r"[\x00-\x1f\x7f]", value), field)
    require(len(manifest["description"]) <= 4000)
    require(interface["developerName"] == "Kian Peters")
    require(len(interface["defaultPrompt"]) <= 3)
    require(all(0 < len(prompt) <= 128 for prompt in interface["defaultPrompt"]))
    require(len(interface["capabilities"]) <= 20)
    require(all(0 < len(value) <= 120 for value in interface["capabilities"]))
    require(interface["websiteURL"] == "https://prometheor.com")
    for field, suffix in (("supportURL", "support"), ("privacyPolicyURL", "privacy"),
                          ("termsOfServiceURL", "terms")):
        require(interface[field] == "https://app.prometheor.com/legal/" + suffix)
    require(interface["composerIcon"] == "./assets/icon.svg")
    require(interface["logo"] == "./assets/logo.png")
    require(mcp == {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
        "mcpServers": {"prometheor": {
            "type": "streamable-http", "url": "https://app.prometheor.com/mcp"}},
    })
    # Only explicit public metadata and original assets enter the archive.
    text = files["plugin.json"] + files["mcp.json"] + files["assets/icon.svg"]
    require(not re.search(rb"(?i)(client.?secret|access.?token|refresh.?token|password|"
                         rb"test_credentials|reviewer_instructions|authorization|"
                         rb"-----BEGIN.*PRIVATE KEY|sk-[a-z0-9]{20})", text))
    png = files["assets/logo.png"]
    require(png[:8] == b"\x89PNG\r\n\x1a\n" and png[12:16] == b"IHDR")
    require(struct.unpack(">II", png[16:24]) == (512, 512))
    svg = ET.fromstring(files["assets/icon.svg"])
    require(svg.attrib["viewBox"] == "0 0 128 128")
    require(svg.attrib["width"] == svg.attrib["height"] == "512")
    require(all(len(files[name]) <= 5 * 1024 * 1024 for name in files if name.startswith("assets/")))


def archive(files):
    result = io.BytesIO()
    with zipfile.ZipFile(result, "w", compression=zipfile.ZIP_STORED) as bundle:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, files[name])
    return result.getvalue()


def main():
    paths = {
        "plugin.json": SOURCE / "plugin.json",
        "mcp.json": SOURCE / "mcp.json",
        "assets/icon.svg": ROOT / "assets" / "icon.svg",
        "assets/logo.png": ROOT / "assets" / "logo.png",
    }
    require(all(not path.is_symlink() and path.is_file() for path in paths.values()))
    files = {name: path.read_bytes() for name, path in paths.items()}
    validate(files)
    data = archive(files)
    require(data == archive(files), "Packaging must be reproducible")
    with zipfile.ZipFile(io.BytesIO(data)) as bundle:
        require(bundle.testzip() is None)
        require(len(bundle.namelist()) == len(files))
        require({name: bundle.read(name) for name in bundle.namelist()} == files)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(data)
    print(json.dumps({"path": str(OUTPUT), "sha256": hashlib.sha256(data).hexdigest(),
                      "bytes": len(data), "files": sorted(files),
                      "text_lengths": {key: len(value) for key, value in
                                       json.loads(files["plugin.json"])["extensions"]["com.openai"]["interface"].items()
                                       if isinstance(value, str)},
                      "validation": "passed", "reproducible": True}, indent=2))


if __name__ == "__main__":
    main()
