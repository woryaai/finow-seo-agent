# Finow SEO Agent

This repository contains the shared operating context for Finow SEO work.

## Command routing

Use the matching canonical specification under `commands/` for these project commands:

- `/finow-keyword-research`
- `/finow-build-website`
- `/finow-blog-post`
- `/finow-service-page`
- `/finow-seo-optimization`
- `/finow-publish`
- `/finow-audit`

Before a command, read `context/setup.md`, `context/finow-brand.md`, any relevant product facts, and the references named by that command.

## Core rules

- Keep B2C and B2B search intent distinct unless a page is intentionally a router.
- For Iran, prefer Search Console and live Persian search evidence over unsupported third-party volume estimates.
- `context/finow-product-facts.md` is the source of truth for volatile commercial claims.
- Do not invent numbers, reviews, partnerships, medical claims or product terms.
- Keep new content in draft/review until it passes the project quality checks.
- Use `keyword-map.md`, `website-index.md`, `optimization-log.md` and `audit-report.md` as persistent registries.
- Follow `references/persian-writing.md` for Persian RTL output.
- Run `python scripts/validate_repo.py` after changes to the agent repository.
