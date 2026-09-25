---
description: Publish approved Finow pages safely, validate production, indexing assets and measurement baseline.
argument-hint: "[optional page/path/batch]"
---

# /finow-publish

## Purpose

Move only approved `Ready` content to production and verify that the production result is healthy.

## Read first

- `AGENTS.md`
- `context/setup.md`
- `context/finow-product-facts.md`
- `references/on-page-seo.md`
- `references/technical-seo.md`
- `references/content-quality.md`
- `website-index.md`
- `keyword-map.md`

## Step 1 - Select publish set

Use explicit arguments when supplied; otherwise consider items marked `Ready`.

Do not publish `Draft` or unresolved `Review` items.

## Step 2 - Product fact gate

For every selected page, inspect financial/payment claims.

Block publication if a live claim relies on `REVERIFY`, contradictory or missing facts.

Report the exact claims blocking the release.

## Step 3 - Content/SEO preflight

Verify:

- quality gate at least 9/10 for new/reworked content
- unique primary intent
- no known cannibalization conflict
- title/meta/H1/canonical/index state
- schema validity where present
- internal link path
- no broken links
- mobile readability
- CTA/form destination works

## Step 4 - Build/test

Detect platform and run the real build/test workflow before production deployment.

Do not assume a push equals a successful deployment.

## Step 5 - Deploy

Use the configured site platform/repository/deployment workflow.

If write/deploy access is missing, stop at the exact access dependency. Do not fabricate deployment success.

## Step 6 - Production verification

Open/check the production URL(s) and verify:

- 200/expected status
- correct canonical
- intended indexability
- correct rendered content
- working CTA/form
- no obvious RTL/layout breakage

## Step 7 - Discovery assets

Confirm as applicable:

- robots policy
- sitemap contains canonical live URLs
- no staging URLs in sitemap/canonicals
- structured data remains valid

## Step 8 - Search Console baseline

When GSC is connected:

- ensure sitemap property/state is reasonable
- capture baseline for important published pages
- note reindex/inspection action when needed

Do not promise immediate indexing or ranking movement.

## Step 9 - Registry

Update `website-index.md` to `Published` only after production verification.

Keep `keyword-map.md` focused on page/intent planning and current build status without creating conflicting state definitions.
