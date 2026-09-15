# Finow technical SEO

## Crawl and index

Check:

- robots.txt
- sitemap coverage
- canonical consistency
- noindex intent
- HTTP status codes
- redirect chains/loops
- soft 404s
- duplicate routes
- parameter/index traps

## Rendering

Verify important content is present in crawlable rendered HTML. Flag content that only appears after unsupported or broken client-side behavior.

## Performance

Assess mobile production builds, not dev servers.

Prioritize:

- LCP
- INP
- CLS
- render-blocking fonts/CSS/JS
- oversized images
- image dimensions
- caching/compression where controlled
- third-party script cost

Target when technically realistic:

- Lighthouse SEO: 100
- Accessibility: 100
- Best Practices: 100
- Mobile Performance: 95+

Treat these as engineering quality targets, not ranking guarantees.

## CMS/framework traps

Inspect the actual platform before fixing:

- duplicate metadata ownership
- plugin conflicts
- JS-only content
- generated archives/tags
- dynamic route duplication
- client-rendering failures
- canonical/noindex injected by more than one layer

Never remove a plugin/script solely because a crawler flags it. Identify purpose and risk first.
