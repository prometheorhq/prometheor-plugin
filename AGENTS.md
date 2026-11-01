# Prometheor connector packages

- Owner: Prometheor
- Product: Prometheor
- Role: Connector SDK / marketplace packages
- Data classification: Public
- Deployment: Source repository `prometheorhq/prometheor-plugin`; marketplace uploads are separate, explicit actions. No automatic deployment workflow is configured here.

Follow the ancestor workspace rules. Work only on `main`; pull with `--ff-only` before edits, validate scoped changes, then commit and push them. Preserve the existing package identity `prometheor` and original brand assets.

OpenAI package sources are in `openai/prometheor`. Build and validate with `python3 scripts/build-openai.py`. Generated artifacts belong in ignored `out/`. Never include credentials, private reviewer instructions, unrelated marketplace files, or build tooling in the upload ZIP. A local package validation does not establish OAuth, live tool availability, reviewer access, submission, or publication.
