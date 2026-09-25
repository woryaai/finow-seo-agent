---
description: Build or expand Finow's Iran-first keyword and page map for B2C/B2B search demand.
argument-hint: "[b2c|b2b] [health|beauty|wellness|dental|cross] [expand optional] [topic optional]"
---

# /finow-keyword-research

## Purpose

Create a page-first search opportunity map for Finow using Iran-appropriate evidence. Never invent Iranian monthly volume or keyword difficulty.

## Read first

- `AGENTS.md`
- `context/setup.md`
- `context/finow-audiences.md`
- `context/finow-product-facts.md`
- `references/iran-search.md`
- `references/internal-linking.md`
- existing `keyword-map.md`
- existing `website-index.md`

## Roadmap to show

State: audience/vertical being researched, evidence sources available, whether this is base or expand mode, and what artifact will be updated.

Do not ask the user to approve the roadmap.

## Step 1 - Resolve scope

Infer scope from arguments and existing context when clear.

Required dimensions:

- B2C or B2B
- health, beauty, wellness, dental or cross-sector
- primary business outcome

If a required business choice genuinely cannot be inferred, ask one concise question. Do not ask the user to choose tools or research methods.

## Step 2 - Inventory before research

Read the current keyword map and website registry.

Summarize:

- existing hubs
- existing money pages
- existing support content
- already-owned primary intents
- obvious gaps

Never overwrite an existing map silently. Default to merge/append and preserve statuses.

## Step 3 - Gather evidence

Use the evidence ladder in `references/iran-search.md`.

Prefer Search Console when connected. Then inspect live Persian SERPs for important roots and variants.

Collect:

- real query wording
- intent
- ranking page types
- competitors
- SERP features
- observed demand signals
- existing Finow ranking URL if any
- whether the query is brand/non-brand

Third-party metrics may be included only when their market coverage is valid. Label them.

## Step 4 - Generate topic families

Build families around real problems and commercial jobs-to-be-done.

B2C examples of families, not guaranteed keywords:

- credit/installment payment for service categories
- eligibility and how-it-works
- provider/payment comparisons where appropriate
- specific dental/beauty procedures
- cost/conditions/without cheque/without guarantor only when product facts and SERP intent support them

B2B examples:

- credit payment for clinics/salons/dentists
- merchant settlement
- increasing conversion/sales
- CRM/customer club/campaign/analytics only if Finow actually offers the capability

## Step 5 - Intent verification

For priority queries, inspect the live SERP and classify:

- Transactional
- Commercial investigation
- Informational
- Navigational
- Local
- Mixed

Route by intent:

- commercial/transactional → service/money page
- informational → blog/support page
- top-level broad category → hub
- brand/support query → appropriate brand/help page

Never create both an article and a money page with the same primary intent.

## Step 6 - Opportunity scoring

Use an internal heuristic based on:

- business value
- intent strength
- observed demand
- competition
- existing Finow visibility
- expected click opportunity
- product fit

Label the score as a heuristic. Do not present it as a Google metric.

## Step 7 - Page map

For every recommended page record:

- Page name
- Primary topic/query
- Audience
- Vertical
- Intent
- Page type
- Proposed route
- Business priority
- Opportunity evidence
- Demand label
- Existing ranking URL
- Parent hub
- Supporting terms/questions
- Internal link targets
- Cannibalization notes
- Status

Keep human-readable blocks concise. No giant keyword dump.

## Expand mode

If arguments contain `expand`, deepen one existing root/cluster rather than starting over.

Expansion must search:

- sub-services/procedures
- condition/eligibility questions
- comparison/decision queries
- cost and payment questions
- high-intent long-tail variants
- recurring SERP questions

Merge new rows into the existing map and preserve history/status.

## Exit gate

Before finishing:

- no duplicate primary intent
- no invented volume/KD
- every money page maps to a real Finow offering
- every volatile claim remains sourced from product facts
- every new page has a parent/linking plan

Update `keyword-map.md` and, if tooling is available, regenerate a readable `keyword-map.html`.

Run:

```bash
python scripts/validate_repo.py
```

## Final report

Report top opportunities first, then newly added page count, conflicts/cannibalization, evidence limitations and the next page/cluster to build.
