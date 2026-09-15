# Audit scoring and confidence

## Confidence labels

- **Verified:** directly observed in source data, live response, code or authoritative first-party evidence.
- **Strong evidence:** multiple aligned observations support it.
- **Likely:** evidence is meaningful but incomplete.
- **Heuristic:** prioritization/practitioner rule, explicitly not a Google law.
- **Needs data:** cannot be responsibly concluded yet.

## Scope rule

Every audit states:

- site/page scope
- number of pages/items in scope
- number actually checked
- whether sampling was used

Site-wide layers should not be silently inferred from a small page sample.

## Severity

- Critical: blocks crawling/indexing/conversion or exposes materially wrong financial/brand information
- High: strong impact on important pages or demand capture
- Medium: meaningful quality/coverage opportunity
- Low: polish or low-impact issue

## Fix score vs raw score

If a platform/business constraint prevents a fix, preserve the raw finding and record the constraint. Never make an issue disappear merely because it is waived.
