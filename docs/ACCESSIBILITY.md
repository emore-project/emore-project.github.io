# Accessibility guide — E-MORE website

Target: **WCAG 2.2 level AA** (self-assessed; no external audit). Public statement: `accessibility.html`.

## Rules for every change
1. **Edit `tools/build.py`, not the generated HTML**, then run `python3 tools/build.py`. Header, footer, skip link and display options are shared.
2. **Colours**: only tokens from `css/style.css`. Run `python3 tools/contrast.py` after any colour change (text ≥ 4.5:1, UI and large text ≥ 3:1; high-contrast theme ≥ 7:1).
3. **Structure**: one `h1` per page, no skipped heading levels, landmarks (`header`, `nav`, `main`, `footer`), skip link first in the body.
4. **Images**: informative → descriptive `alt`; decorative → `alt=""`. Diagrams: say what they show, not "diagram of". Text inside an SVG must also exist in the page text or in the `alt`.
5. **Links**: purpose clear from text or context (use `<span class="sr-only">` for "Read more…"). Foreign-language text gets `lang="xx"`.
6. **Keyboard/focus**: everything reachable and operable with the keyboard, visible focus (3 px, ≥ 3:1), targets ≥ 44 px, `scroll-padding-top` for the sticky header.
7. **Responsive**: no horizontal scroll at 320 px; use a mobile variant of a diagram instead of shrinking it (`<picture>`).
8. **Motion**: none by default; anything animated must honour `prefers-reduced-motion`.
9. **Display options** (`assets/js/a11y.js`): high contrast (also from `prefers-contrast: more`), larger text, wider spacing, underlined links. New components must work in all of them.

## Test routine before publishing
1. `python3 tools/contrast.py`.
2. axe-core on every page, normal and high contrast (0 violations expected): load `https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.10.0/axe.min.js` in the page and run `axe.run()` with tags `wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa, best-practice`.
3. Keyboard only: Tab through the whole page, open/close the Accessibility panel (Esc closes and returns focus).
4. Zoom 200 % and 320 px width.
5. Screen reader pass (VoiceOver on Safari) when the structure changes — **not yet done**.

## Not a certificate
A certificate of conformance (e.g. UNE 139803 / EN 301 549) needs an external audit. Until then the statement says "self-assessment". Update `UPDATED` in `tools/build.py` when the review is repeated.
