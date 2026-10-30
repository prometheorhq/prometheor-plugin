# Prometheor for Antigravity

Prometheor lets the AI you are talking to hand work to your other AI apps. Ask Antigravity to give a task to Codex,
Claude Code or Cursor, and it starts on your own Mac, in the real app, where you can watch it. The result comes back
to the chat you asked in, checked against what you asked for. A shared logbook keeps the decisions, status and results
of your work, so every app knows where things stand.

- Connect once. Antigravity connects to `https://app.prometheor.com/mcp` and you sign in to your Prometheor account.
- Your own apps and subscriptions do the work. Prometheor never stores your app sign-ins.
- The Prometheor app on your Mac starts each task and checks first that the app is signed in.
- Stop everything with one sentence: "stop everything".

## What you need

A Prometheor account and the Prometheor app on a Mac (macOS), with Codex, Claude Code or Cursor installed and signed in
on that Mac. Steps: https://prometheor.com/#connect

## Install

In Antigravity: Customizations → Marketplace → Prometheor → Install. Then Customizations → Installed MCP Servers →
Prometheor → Authenticate, and sign in to your Prometheor account in the browser that opens.

Without the Marketplace, add the server to `~/.gemini/config/mcp_config.json` (used by the Antigravity app, IDE and
CLI), then authenticate as above:

```json
{
  "mcpServers": {
    "prometheor": { "serverUrl": "https://app.prometheor.com/mcp" }
  }
}
```

## What this plugin contains

Only the connection: `plugin.json`, `mcp_config.json` with the address `https://app.prometheor.com/mcp`, the logo and
this README. There are no scripts, hooks, skills or credentials in it. Sign-in uses OAuth with dynamic client
registration; never paste API keys or another person's account details.

## How to use it

- Name an app: "start a Codex session and fix the login bug" hands the task to exactly that app.
- Ask for the team: "use the team for this" lets Prometheor split the work and give you one combined result.
- Ask "what is running?" or "stop everything" at any time.

Apps are switched on and off only in the Prometheor app on your Mac, never by a prompt.

## Privacy, terms and support

- Review and delete your logbook: https://app.prometheor.com/workspace
- Privacy: https://app.prometheor.com/legal/privacy
- Terms: https://app.prometheor.com/legal/terms
- Support: https://app.prometheor.com/legal/support · info@prometheor.com

## License

`plugin.json`, `mcp_config.json` and this README are licensed under MIT; see [LICENSE](../../LICENSE). The Prometheor
logo, name and other brand identifiers are excluded, with rights reserved. The hosted service is not included.
