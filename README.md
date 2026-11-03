# Prometheor

Prometheor lets every AI you use hand work off to your other AIs. Ask in one AI app, and the task starts in another AI
app on your own Mac, in the real app, where you can watch it. The result comes back to the chat you asked in, checked
against what you asked for. A shared logbook keeps the decisions, status and results of your work, so every app knows
where things stand.

The service is closed source; this repo holds the connector files.

## Connect

Every app connects to the same address and signs in to your Prometheor account with OAuth:

```
https://app.prometheor.com/mcp
```

| App | How to connect |
| --- | --- |
| ChatGPT | Install Prometheor from the ChatGPT app directory, or add a connector with the address above. |
| Claude (web, desktop, Claude Code) | Settings, Connectors, add a custom connector with the address above. |
| Cursor | Install the Prometheor plugin from this repository (`.cursor-plugin/plugin.json`), or add the address above as a remote MCP server. |
| Grok Bot | Add Prometheor as a connector with the address above. |
| Muse | Add Prometheor as a connector with the address above. |
| Google Antigravity | Use the entry in [`antigravity/prometheor`](antigravity/prometheor). |
| Any other MCP client | Add a remote (streamable HTTP) MCP server with the address above. |

Step-by-step guides with screenshots: https://prometheor.com/#connect

- Your own apps and subscriptions do the work. Prometheor never stores your app sign-ins.
- The Prometheor app on your Mac starts each task and checks first that the app is signed in.
- Stop everything with one command.

The registry entry for the [MCP Registry](https://registry.modelcontextprotocol.io) is [`server.json`](server.json)
(`com.prometheor/prometheor`).

## Antigravity

The Google Antigravity entry lives in [`antigravity/prometheor`](antigravity/prometheor) (its own `plugin.json`,
`mcp.json` and logo), so Antigravity's checks see only its files.

## OpenAI

The OpenAI submission sources are in [`openai/prometheor`](openai/prometheor).
Run `python3 scripts/build-openai.py` to validate the metadata and build the
reproducible `out/openai/prometheor-openai.zip`. It contains the portable
`plugin.json`, `mcp.json`, and the unmodified original logo assets only.

The package keeps the `prometheor` identity and version `1.0.0` for reuploading
the existing draft. Review credentials, test cases, release notes and country
targeting are intentionally omitted to preserve the dashboard's saved values.
Review those values separately before submission. OAuth remains discovered
from the existing MCP endpoint; this package adds no authentication override.
Local validation does not establish working reviewer access, live tool scans,
submission approval or publication. Follow the current
[OpenAI submission guide](https://developers.openai.com/plugins/deploy/submission).

## What you need

A Prometheor account and the Prometheor app on a Mac (macOS), with Codex, Claude Code or Cursor installed and signed
in on that Mac. Steps: https://prometheor.com/#connect

## What the Cursor entry contains

Only the connection: `.cursor-plugin/plugin.json`, `mcp.json` with the address `https://app.prometheor.com/mcp`, and
the logo. There are no scripts, hooks, skills or credentials in this repository. Sign-in uses OAuth in Cursor; never
paste API keys or another person's account details.

## How to use it

- Name an app: "start a Codex session and fix the login bug" hands the task to exactly that app.
- Ask for the team: "use the team for this" lets Prometheor split the work and give you one combined result.
- Ask "what is running?" or "stop everything" at any time.

Apps are switched on and off only in the Prometheor app, never by a prompt.

## Privacy, terms and support

- Review and delete your logbook: https://app.prometheor.com/workspace
- Privacy: https://app.prometheor.com/legal/privacy
- Terms: https://app.prometheor.com/legal/terms
- Support: https://app.prometheor.com/legal/support · info@prometheor.com

## License and brand assets

`.cursor-plugin/plugin.json`, `mcp.json`, `server.json` and this README are licensed under MIT; see [LICENSE](LICENSE). The
Prometheor logo in `assets/icon.svg`, the Prometheor name and other brand identifiers are excluded, with rights
reserved. The hosted service and its backend are not included.

Earlier versions (up to 0.7.1) also shipped packages for Claude Code and Grok Build. They are retired: connect
Prometheor as a connector in those apps instead. If you installed the old package in Claude Code, uninstall it, because
it hides your Claude connector.
