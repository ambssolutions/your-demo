# AMBS house method

Drawn from teamkarl, mikia, ambs-website, deltaair-website, chandigarh-dental and the Team K demo in this repo.

## 1. Structure
- No build step. Static HTML on Vercel. Preview with `python3 -m http.server`.
- Concept galleries (teamkarl): `index.html` gallery + `designs/NN-slug/index.html` + `designs/NN-slug/thumb.webp` + shared `assets/` (e.g. `concepts.js`). Two-digit, kebab-case slugs.
- Gallery `vercel.json`: friendly rewrites (`/classic` → `/designs/01-classic-harcourts/index.html`), `X-Robots-Tag: noindex` on everything, week-long cache on images, short cache on JS. Gallery also has `<meta name="robots" content="noindex">`.
- Client sites (mikia): `cleanUrls: true`, security headers (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`), `?v=` cache busting, `sitemap.xml`, `robots.txt`, `404.html`.
- README: one-line purpose, page list, "Things to finish before launch". A `CONTENT-NEEDED.md` table (Need | Goes in) lists what the client must supply.

## 2. Gallery conventions
- Cards: "Concept NN", `Type · Style`, a type tag + a motion tag ("Subtle motion", "Animated", "Highly animated", "Interactive"), 1-2 sentence description, whole card clickable.
- Optional "★ Recommended" badge with a one-line "Why".
- Filter pills with `aria-pressed`: All, Recommended, My shortlist (count), then each type. Row scrolls sideways on mobile.
- Shortlist star per card, saved in localStorage, synced across tabs via the `storage` event; floating tray when non-empty; share link carries the shortlist.
- Every concept page loads a shared floating switcher (prev · "NN Name ▾" menu · next · star) so reviewers can move between concepts without returning to the gallery.
- Thumbnails 16:10 webp, `object-position: top`, eager for the first 3, lazy for the rest.

## 3. Page anatomy (MiKia, the closest match for Thomas)
1. Hero: mono eyebrow, word-split h1, lede, CTA pair, 3 trust badges, numbered disciplines strip ("01 Surveying … 06 Project Management").
2. Ticker of disciplines.
3. Services: "Six disciplines. One integrated team."
4. Process: 4 sticky stacked stages (Understand the site → Design & consent → Deliver on site → Complete & hand over). Use CSS `position: sticky`, not scroll-jacking.
5. Projects (Residential | Commercial split), photo mosaic "In the field".
6. Why (4 points), Mission / Vision / Values.
7. Proof: testimonials, accreditations, FAQ teaser (4 `<details>`), "All questions" link.
8. Contact: "Let's talk about your site." Address → Google Maps, book a meeting, enquiry, phone, email.
9. Footer: logo, tagline, Services + Explore columns, legal line, stock-image disclaimer, "Proudly designed by AMBS Solutions".
- Subpages: page hero with breadcrumbs (Home / Page), full-sentence h1 ending in a full stop, lede. Every subpage ends with a CTA band.
- Nav: skip link, logo with width/height, `.menu-btn` (`aria-expanded`, `aria-controls`, 44px), nav links + pill CTA, header gains a solid/blurred state on scroll, menu closes on link click, `scroll-padding-top` for the sticky header.
- Mobile quick bar: fixed bottom "Call" bar using `env(safe-area-inset-bottom)`.

## 4. Tokens and type
- Short semantic tokens: `--ink --paper --sand --line --muted --accent --accent-text --serif --sans --mono --pad`.
- `.wrap` 1180-1440px max with `--pad: clamp(20px,5.5vw,80px)`.
- h2 `clamp(36px,4.4vw,56px)`, line-height 1.05, letter-spacing -.025em. Mono eyebrows 12px, uppercase, `.18em` tracking. Numbered labels ("STAGE 01", "01 / 06").
- Pill buttons `border-radius: 999px; min-height: 56px; padding: 0 28px`. Cards 16-22px radius. Long soft negative-spread shadows.
- Focus: `outline: 2px solid var(--accent); outline-offset: 3px`.
- Dark mode (when offered): `html[data-theme=dark]` overriding tokens only, set before first paint from a project-prefixed key (e.g. `tc-theme`).
- Optional SVG feTurbulence grain at `.05` opacity.

## 5. Motion
- Base layer is vanilla: IntersectionObserver adds `.in` to `.rv` (`threshold .12`, `rootMargin 0 0 -40px 0`), stagger via `--rd`.
- Word-split hero h1 with `aria-label` holding the full text.
- Counters: rAF over ~1400ms, ease `1-(1-p)^3`, `toLocaleString('en-NZ')`.
- GSAP 3.12.5 + ScrollTrigger (cdnjs) for showpiece concepts. Lenis 1.1.13 only for `pointer: fine` and no reduced motion, synced to ScrollTrigger via `gsap.ticker`.
- Reduced motion respected everywhere. Never an unconditional `animation: none`. Low-power check (`deviceMemory <= 2`, `pointer: coarse`) disables heavy effects.

## 6. SEO and meta
- `lang="en-NZ"`, `viewport-fit=cover`, title "Brand | What, Auckland" (subpages "Page | Brand").
- Meta description, canonical, Open Graph (+ `og:locale en_NZ`), Twitter card, theme-color.
- JSON-LD `ProfessionalService` with addresses and phones; `BreadcrumbList` on subpages; `FAQPage` where there is an FAQ.

## 7. Forms, accessibility, copy
- `<form novalidate>` + JS validation, honeypot field, `<p role="status" aria-live="polite">` for results, `(optional)` markers, `autocomplete` on every field. Email regex `/^[^@\s]+@[^@\s]+\.[^@\s]+$/`.
- Send: `FORM_ENDPOINT` JSON POST if set, otherwise a pre-filled `mailto:`. Note under the form: "We use your details only to reply to your enquiry."
- Contact details as a `<dl>`; "What to tell us" list (site, idea, timing, budget: "A guess is fine.").
- Accessibility: skip link, labelled navs, `aria-expanded`/`aria-pressed`, decorative layers `aria-hidden`, descriptive alt text, 44px tap targets.
- Phones: display "09 836 1804", link `tel:+6498361804`.
- Copy: NZ English, short plain sentences, full-sentence headings with a full stop. No em dashes, no exclamation marks, no hype words (seamless, unlock, revolutionise, leverage). Never invent stats, testimonials or awards; hide missing content until supplied.
- Footer disclaimer: "Some images on this website may be stock images or illustrative renders."

## 8. Images
- Responsive webp sets (`-800/-1600/-2400`) with `srcset`/`sizes`, explicit width and height, `loading="lazy"`, `decoding="async"`; hero image `fetchpriority="high"`.
- Heavy extras load near the viewport only, with a fallback.
