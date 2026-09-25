---
description: Optimize one Finow page mechanically for on-page SEO, technical quality, performance and GEO without silently rewriting approved copy.
argument-hint: "[url/path] [full|meta|headings|images|links|schema|faq|ai|proof|speed|content-gap]"
---

# /finow-seo-optimization

## Purpose

Improve an existing page while protecting approved body copy and measuring before/after changes.

## Read first

- `AGENTS.md`
- `context/finow-product-facts.md` when relevant
- `references/on-page-seo.md`
- `references/technical-seo.md`
- `references/geo-ai.md`
- `references/internal-linking.md`
- `references/schema.md`
- `references/audit-scoring.md`
- `optimization-log.md`

## Step 1 - Resolve target and focus

A target URL/path is required.

If a focus is provided, run only that slice at full depth.

Supported focus:

- full
- meta
- headings
- images
- links
- schema
- faq
- ai
- proof
- speed
- content-gap

## Step 2 - Baseline

Record what can be measured before changes:

- current metadata/index/canonical
- relevant checklist status
- production performance metrics when accessible
- GSC baseline if connected

Never run performance scoring against a known dev build and report it as production quality.

## Step 3 - Grade

Grade applicable on-page, technical and GEO items.

State scope and confidence.

## Step 4 - Fix mechanical issues

Allowed by default:

- title/meta
- heading tag hierarchy
- alt text
- canonical/index directives
- internal links/anchors
- schema
- broken markup
- image format/dimensions/loading
- script/font/CSS loading improvements that preserve required functionality
- crawl/index technical fixes

Do not silently rewrite approved body paragraphs.

If content gaps require meaningful writing, produce a recommendation and route to the appropriate content command.

## Step 5 - Performance

When `speed` or `full`:

- test a production-equivalent build
- use mobile performance as the primary quality view
- inspect LCP/INP/CLS and blocking resources
- make reversible engineering fixes
- retest

If an external platform/script caps performance, record the exact constraint rather than hiding it.

## Step 6 - Product-fact integrity

If optimization exposes stale financial/product copy, flag it. Do not replace it with a guessed value.

## Step 7 - Verify and log

Run relevant build/tests.

Update `optimization-log.md` with:

- date
- page
- reason
- before state
- changes
- after state
- baseline metrics
- remeasurement target

If metadata/schema/indexing changed, note that recrawl/reindex may be needed.
