# GitHub Copilot / Agent instructions for this repository

This file guides GitHub Copilot Chat and other AI assistants when working in this workspace. Keep changes small, test-driven, and aligned with the repository's learning-first goals.

## Quick summary

- Project: Learn Claude Code — a progressive, educational set of Python agent examples (s01..s12 + s_full) with a Next.js `web/` UI and example MCP servers in `my-mcp-server/`.
- Primary languages: Python (agent examples & servers), TypeScript (Next.js web).

## Important commands

- Setup (Python):
  - python -m venv .venv
  - .venv\Scripts\activate  # Windows
  - pip install -r requirements.txt
  - copy .env.example .env   # then edit .env (do NOT commit secrets)

- Run examples (start here):
  - python agents/s01_agent_loop.py
  - python agents/s_full.py

- Run tests:
  - python -m pytest -q

- Web platform (dev):
  - cd web && npm install && npm run dev

- MCP example servers (stdio transport):
  - cd my-mcp-server && python my_server.py

## Key files & directories

- `agents/` — Python reference implementations (s01..s12, s_full)
- `docs/{en,zh,ja}/` — session docs (mental-model-first)
- `skills/` — SKILL.md examples for s05
- `my-mcp-server/` — example MCP servers (file_server, weather_server, my_server)
- `web/` — interactive learning UI (Next.js)

## Conventions for AI assistance

- Make small, focused edits. Prefer incremental, test-covered changes.
- Preserve educational clarity: keep examples explicit and readable.
- Do not add heavy new dependencies unless justified and discussed.
- Avoid shipping secrets — reference `.env` and `.env.example` only.

## Anti-patterns

- Rewriting large sections of session code to be “generic” — these examples are intentionally minimal and explanatory.
- Adding production-grade orchestration or hidden state without tests and docs.
- Modifying `web/` layout or i18n files without updating corresponding docs in `docs/`.

## When you create code changes

- Run tests locally (`python -m pytest`). Add or update tests for behavioral changes.
- For new features, add a short note in `README.md` or appropriate `docs/en/` page.
- Use a feature branch and open a PR with a focused description and test results.

## Suggested prompts for Copilot Chat

- "Add a new tool to `my-mcp-server` that returns JSON metadata for a directory. Include tests and update `my-mcp-server/README.md` with usage." 
- "Implement a retry wrapper for agent tool calls in `agents/`, add a unit test, and document the behavior in `docs/en/s02-tool-use.md`."

## Contact / context

This repo is educational: prefer clarity over cleverness. When in doubt, ask for a small code review before large refactors.
