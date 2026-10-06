# Prometheor memory plugin

Prometheor connects your AI assistant to externally stored personal preferences and project decisions. Recall relevant saved context and save concise durable facts under your current consent settings. The plugin bundle is intended to be distributed without a separate plugin charge. Prometheor currently admits invited pilot accounts. Future paid service plans are separate from the bundle; a generally available free recall/save tier has not been established by this package review. Marketplace compatibility of paid service requirements has not been confirmed.

## Connection and use

The repository includes `.claude-plugin/plugin.json` for Claude, `.cursor-plugin/plugin.json` for Cursor and `.grok-plugin/plugin.json` for the separate Grok Build developer plugin catalog. All use `skills/memory/SKILL.md` and the same HTTPS MCP endpoint. Claude uses `.mcp.json`; Cursor and Grok Build use `mcp.json`. Grok Build catalog inclusion is distinct from consumer Grok Chat connections and from Cursor's Grok Bot. No installation or approval on any of those surfaces is implied.

Enable the plugin and authenticate to your own admitted Prometheor account through the host's OAuth connection to https://app.prometheor.com/mcp. Do not enter owner API keys or share another person's account. Use only the authorized personal scope. Ask the assistant to recall a relevant saved preference or explicitly save one concise durable fact. Prometheor Settings controls account saving choices. Only enable automatic saving after giving explicit account-wide consent. A current private or do-not-save instruction overrides the setting. The skill excludes credentials, raw transcripts and regulated or special-category sensitive data.

## Automation limits

The bundled skill guides relevant recall and consent-controlled writes. Actual calls depend on host invocation and permissions. This package contains no lifecycle hooks, background capture, local scripts, or full-chat/history/file export. It does not disable native memory. Cursor component compatibility does not prove all components run in Grok Bot. Exact-host OAuth and synthetic behavior tests are still required before release; no installed-runtime test is claimed.

## Privacy, support and controls

Review, correct and delete saved records at https://app.prometheor.com/workspace. Privacy: https://app.prometheor.com/legal/privacy. Service terms: https://app.prometheor.com/legal/terms. Support: https://app.prometheor.com/legal/support. The declared MCP endpoint handles bounded authorized memory tools; no credentials are embedded in this package. Installation alone does not grant saving consent.

## License and brand assets

The Claude, Cursor and Grok Build manifests, MCP configuration, memory skill and this README are licensed under MIT; see [LICENSE](LICENSE) for the exact scope and text. The hosted service and backend are not included. The original orange-red Prometheor logo in `assets/icon.svg`, Prometheor names, logos and other brand identifiers are excluded from MIT, with rights reserved. No trademark rights are granted by the MIT license. Marketplace terms may separately grant specific display, distribution and promotion rights.

## Review status

This public repository contains a package prepared for marketplace review. Publication of this repository does not mean Cursor, Grok Bot or Grok Build has approved or tested it. Structural checks cover the manifest, paths and exact bundled files; installed-host OAuth and behavior tests remain pending. No third-party implementation, backend source, user data, credentials or executable scripts are bundled.
