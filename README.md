# Finow SEO Agent

A repository-native SEO, GEO and organic growth operating system for **Finow**.

It adapts the workflow pattern of a command-driven SEO agent to Finow's actual context: Persian RTL content, Iran-first search intelligence, B2C + B2B funnels, financial/product fact controls, merchant SEO, technical SEO, AI/GEO discovery, publishing and measurement.

## What you get

Seven canonical command specs:

1. `finow-keyword-research`
2. `finow-build-website`
3. `finow-blog-post`
4. `finow-service-page`
5. `finow-seo-optimization`
6. `finow-publish`
7. `finow-audit`

Plus persistent context, reference rules, registries, validation scripts and native Claude Code command wrappers.

## Claude Code

Open a terminal in this repository and start Claude Code:

```bash
claude
```

Project commands are exposed through `.claude/commands/`, so you can run:

```text
/finow-audit https://finow.pro
/finow-keyword-research b2c dental
/finow-keyword-research expand dental
/finow-service-page دندان‌پزشکی اقساطی
/finow-blog-post ایمپلنت اقساطی چیست
/finow-seo-optimization https://finow.pro/... full
/finow-publish
```

`CLAUDE.md` tells Claude Code to use `AGENTS.md` and the canonical command specs under `commands/`.

## Codex

Codex reads `AGENTS.md` as persistent repository instructions. The dispatcher in `AGENTS.md` defines the same command vocabulary. Use a task such as:

```text
Run /finow-audit https://finow.pro
```

or, in clients that reserve unknown slash commands:

```text
Run the finow-audit command against https://finow.pro.
```

The behavior is sourced from the same `commands/*.md` files, so Claude Code and Codex do not maintain separate SEO logic.

## First run for the existing Finow website

```text
/finow-audit https://finow.pro
```

Recommended sequence after the audit:

1. Critical technical/indexing fixes
2. Existing-page optimization
3. Iran-first keyword reality map
4. Missing high-intent B2C and B2B money pages
5. Internal linking
6. GEO/AI readiness
7. Publish
8. Search Console baseline and measurement loop

## Data hierarchy for Iran

The agent MUST NOT treat a third-party country database as the source of truth for Iran.

Priority:

1. Google Search Console first-party data
2. Live Persian Google SERPs, autocomplete, related searches and visible SERP features
3. Google Trends and seasonality
4. Competitor pages and query overlap
5. Third-party keyword/backlink tools when relevant data actually exists

All estimates are labeled as estimates.

## Product and financial facts

`context/finow-product-facts.md` is the source of truth for volatile commercial claims such as providers, credit limits, repayment, fees, settlement and eligibility.

If a page contains a financial/product claim that is missing or stale in that file, publishing is blocked until the fact is verified.

## Validate the repository

```bash
python scripts/validate_repo.py
```

The validator checks that all command specs, Claude wrappers, required context/reference files and registries exist.

## Repository map

```text
finow-seo-agent/
├── AGENTS.md
├── CLAUDE.md
├── commands/
├── context/
├── references/
├── .claude/commands/
├── data/
├── scripts/
├── keyword-map.md
├── website-index.md
├── optimization-log.md
└── audit-report.md
```

## Safety model

- Never invent proof, financial terms, partnerships, medical facts or reviews.
- Never perform destructive SEO changes silently.
- Existing approved body copy is protected during mechanical optimization.
- New or rewritten content is drafted through the content commands.
- Draft and publish are separate states.
- Every material recommendation carries evidence/confidence.
