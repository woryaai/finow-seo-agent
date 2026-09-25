---
description: Create a new Finow SEO site/microsite foundation only when a new build is actually required.
argument-hint: "[new-site|microsite|seo-section] [optional scope]"
---

# /finow-build-website

## Purpose

Build a new Finow web surface without unnecessarily replacing an existing production site.

## Read first

- `AGENTS.md`
- `context/setup.md`
- `context/finow-brand.md`
- `context/finow-voice.md`
- `references/persian-writing.md`
- `references/technical-seo.md`
- `references/schema.md`

## Gate 0 - Existing site check

If the task is the current `finow.pro` site and no rebuild/microsite/new section was explicitly requested, do NOT rebuild. Route to `/finow-audit`.

Use this command only for a genuinely new site, microsite or separately scoped SEO section.

## Step 1 - Detect platform and constraints

Inspect the actual repository/site when available.

Choose the implementation that matches the project. Do not ask the user to choose framework/library unless this is a real business decision.

Preserve existing design systems when extending an existing codebase.

## Step 2 - Minimum information architecture

A new general Finow site should support, as applicable:

- homepage
- B2C hub
- B2B/merchant hub
- service/vertical indexes
- blog/content index
- about
- contact/support
- FAQ/help
- legal/privacy/terms
- thank-you state
- 404
- robots
- sitemap
- canonical system
- structured data foundation
- OpenGraph/social metadata
- optional `llms.txt` as a discovery aid

Do not create routes that have no actual content purpose.

## Step 3 - RTL and brand implementation

Implement full Persian RTL behavior.

Use Kalameh FaNum only when available/authorized within the project. Never package or redistribute font files unless the project already owns/provides them.

Apply Finow visual identity without overriding an approved design system unnecessarily.

## Step 4 - Content scaffolding

Use verified brand/product facts. Never fill unknown proof with plausible numbers.

Place volatile terms behind a single source-of-truth/config approach where technically appropriate.

## Step 5 - Forms

Every active form must have a real destination.

If a lead destination is unknown, keep the page in draft/non-production state and record the blocker. Never publish a form that silently discards submissions.

## Step 6 - SEO foundation

Implement:

- unique metadata system
- canonicals
- sitemap
- robots
- structured data base
- internal navigation
- breadcrumbs where useful
- accessible semantic HTML
- image optimization primitives

## Step 7 - Test

Run the actual build and project tests.

Check representative desktop and mobile pages.

Validate:

- no broken internal links
- no visible placeholder claims
- no broken RTL
- no active form without destination
- no unintended indexable duplicate template routes

Update `website-index.md` for created routes.

## Publishing

Do NOT production-publish from this command. Handoff to `/finow-publish` after the build is reviewed and ready.
