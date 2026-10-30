# Prometheor for Cursor

Prometheor lets the AI you are talking to hand work to your other AI apps. Ask Cursor to give a task to Codex or
Claude Code, and it starts on your own Mac, in the real app, where you can watch it. The result comes back to the chat
you asked in, checked against what you asked for. A shared logbook keeps the decisions, status and results of your
work, so every app knows where things stand.

- Connect once. Cursor connects to `https://app.prometheor.com/mcp` and signs in to your Prometheor account.
- Your own apps and subscriptions do the work. Prometheor never stores your app sign-ins.
- A small helper on your Mac starts each task and checks first that the app is signed in.
- Stop everything with one command.

## Antigravity

The Google Antigravity entry lives in [`antigravity/prometheor`](antigravity/prometheor) (its own `plugin.json`,
`mcp_config.json` and logo), so Antigravity's checks see only its files.

## What you need

A Prometheor account and the Prometheor helper on a Mac (macOS), with Codex, Claude Code or Cursor installed and signed
in on that Mac. Steps: https://prometheor.com/#connect

## What this entry contains

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

`.cursor-plugin/plugin.json`, `mcp.json` and this README are licensed under MIT; see [LICENSE](LICENSE). The
Prometheor logo in `assets/icon.svg`, the Prometheor name and other brand identifiers are excluded, with rights
reserved. The hosted service and its backend are not included.

Earlier versions (up to 0.7.1) also shipped packages for Claude Code and Grok Build. They are retired: connect
Prometheor as a connector in those apps instead. If you installed the old package in Claude Code, uninstall it, because
it hides your Claude connector.
