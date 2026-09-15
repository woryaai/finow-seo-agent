# Claude Code entry point

This project uses `AGENTS.md` as the shared cross-agent operating contract.

Before executing any Finow command:

1. Read `AGENTS.md`.
2. Resolve the requested `/finow-*` command to the canonical file in `commands/`.
3. Read the context/reference files required by that command.
4. Execute the command, updating registries and artifacts as specified.

Native project slash-command wrappers live under `.claude/commands/`.

Do not duplicate business facts inside this file. Persist reusable setup in `context/setup.md` and volatile product facts in `context/finow-product-facts.md`.
