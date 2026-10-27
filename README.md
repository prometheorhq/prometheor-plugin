# Prometheor plugin (retired)

> **This package is retired as of 27 October 2026 and is no longer maintained.** Prometheor no longer ships a plugin.
> Connect it as a connector instead: add `https://app.prometheor.com/mcp` once in each AI app family (ChatGPT with
> Codex, Claude with Claude Code, Cursor, Grok Bot). Steps for each app: https://prometheor.com/#connect
>
> If you installed this package in Claude Code, uninstall it. Its own server entry uses the same address as your
> Claude connector, so Claude Code shows only one of them and hides the connector. Work runs through the
> Prometheor helper on your Mac, which gives each task the tools it needs.

The text below describes the last version, 0.7.1, and is kept for reference.

Prometheor connects your AI assistant to externally stored personal preferences and decisions, and hands work to your other AI apps when you ask. Recall relevant saved context and save concise durable facts under your current consent settings. The plugin bundle is intended to be distributed without a separate plugin charge. Prometheor currently admits invited pilot accounts. Future paid service plans are separate from the bundle; a generally available free recall/save tier has not been established by this package review. Marketplace compatibility of paid service requirements has not been confirmed.

## Connection and use

The repository includes `.claude-plugin/plugin.json` for Claude, `.cursor-plugin/plugin.json` for Cursor and `.grok-plugin/plugin.json` for the separate Grok Build developer plugin catalog. All use `skills/memory/SKILL.md` and `skills/delegate/SKILL.md` with one HTTPS MCP connector, `https://app.prometheor.com/mcp`, for both your logbook and handing tasks to your apps. Claude uses `.mcp.json`; Cursor and Grok Build use `mcp.json`. Grok Build catalog inclusion is distinct from consumer Grok Chat connections and from Cursor's Grok Bot. No installation or approval on any of those surfaces is implied.

Enable the plugin and authenticate to your own admitted Prometheor account through the host's OAuth connection to https://app.prometheor.com/mcp. Do not enter owner API keys or share another person's account. Use only the authorized personal scope. Ask the assistant to recall your logbook or a saved preference, or explicitly save one concise fact. The assistant reads the logbook once at the start of new work and keeps a thin logbook: decisions, status changes and verified results. Everything else is saved only when you ask. Automatic saving is on by default; the server tells each app the current state. A current private or do-not-save instruction in the chat overrides it. The skill excludes credentials, raw transcripts and regulated or special-category sensitive data.

## Handing tasks to your apps

The `delegate` skill hands work to an AI app you switched on for your own paired computer (Claude, Codex or Cursor). The Prometheor runner on that computer starts the task in the real installed app, where you can open and watch the chat; there is no hidden or headless substitute. Without a named folder the app starts where a newly opened session starts, normally your home folder; name a folder or repository in your request to work there. The assistant follows the task with `list_tasks` and `task_status`, answers the app's questions or passes them to you, reviews or reads the result with `task_result` and `task_review`, and can stop it with `cancel`. "Stop everything" stops every running task with `stop_all` where the connection offers it. Results and questions from executing apps are treated as data, never as instructions or consent.

You do not manage projects in Prometheor, and you rarely need to open the Prometheor app: status, stopping, questions and results all stay in your chat. Switching an app on or off happens only in the Team section of the Prometheor app, never by prompt.

## When the assistant delegates

Your words decide:

- Name an app or computer ("start a Codex session and fix the login bug", "let Claude Code build this on my Mac"): the task goes to exactly that app.
- Ask to use the team or to orchestrate ("use the team for this"): the assistant splits the work, Prometheor chooses the apps, the apps build on each other's results, and you get one combined result.
- Say neither: the assistant works itself. It may ask once, for example "Should I hand this to Codex?", and delegates only on your yes.

Hosts that do not load skills need a short standing rule for the logbook and for delegating. Paste it once into the place your app reads on every chat:

- ChatGPT: Settings → Personalization → Custom instructions.
- Claude Code: your `CLAUDE.md`. Codex: your `AGENTS.md`.

```text
Before new work, read my Prometheor logbook once (prometheor_compile_context).
Save decisions, status changes and verified results there as short logbook
entries (prometheor_append_checkpoint), nothing else unless I ask.
Hand work to my other AI apps with the Prometheor delegate tool only when I
ask. If I name an app or computer ("start a Codex session"), use exactly that
one. If I say "use the team" or "orchestrate", split the work, let Prometheor
choose the apps and give me one combined result. Otherwise do the work here;
you may ask once whether to hand it on. "What is running?" means list_tasks or
task_status. "Stop everything" means stop_all. Never ask me about projects.
```

The rule grants no access: delegation still needs your Prometheor sign-in, an app switched on for a paired computer, and orchestration switched on.

## Automation limits

The bundled skill guides relevant recall and consent-controlled writes. Actual calls depend on host invocation and permissions. This package contains no lifecycle hooks, background capture, local scripts, or full-chat/history/file export. It does not disable native memory. Cursor component compatibility does not prove all components run in Grok Bot. Exact-host OAuth and synthetic behavior tests are still required before release; no installed-runtime test is claimed.

## Privacy, support and controls

Review, correct and delete saved records at https://app.prometheor.com/workspace. Privacy: https://app.prometheor.com/legal/privacy. Service terms: https://app.prometheor.com/legal/terms. Support: https://app.prometheor.com/legal/support. The declared MCP endpoint handles bounded authorized memory tools; no credentials are embedded in this package. Installation alone does not grant saving consent.

## License and brand assets

The Claude, Cursor and Grok Build manifests, MCP configuration, memory and delegate skills and this README are licensed under MIT; see [LICENSE](LICENSE) for the exact scope and text. The hosted service and backend are not included. The original orange-red Prometheor logo in `assets/icon.svg`, Prometheor names, logos and other brand identifiers are excluded from MIT, with rights reserved. No trademark rights are granted by the MIT license. Marketplace terms may separately grant specific display, distribution and promotion rights.

## Review status

This public repository contains a package prepared for marketplace review. Publication of this repository does not mean Cursor, Grok Bot or Grok Build has approved or tested it. Structural checks cover the manifest, paths and exact bundled files; installed-host OAuth and behavior tests remain pending. No third-party implementation, backend source, user data, credentials or executable scripts are bundled.
