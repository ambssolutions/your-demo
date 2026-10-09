# Rules for every concept page

Each concept is ONE self-contained file: thomas-consultants/designs/NN-slug.html (inline CSS + JS).
It is a full homepage concept for Thomas Consultants using the content in ../BRIEF.md.
Goal: the client should be AMAZED. Premium, award-site quality (Awwwards / FWA level) motion, flow and craft.

## Required sections (order/treatment free per concept)
Nav (sticky, with mobile menu) · Hero · Services (all 6) · Why us / 25 years · Process (site assessment → consent → design → delivery) · Projects (at least 6) · Testimonials · Clients + accreditations · Contact CTA with both office phones · Footer.

## Motion: make it remarkable, and make each concept move differently
- Use GSAP 3.12.5 + ScrollTrigger from cdnjs:
  https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js
  https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js
  Optional smooth scroll: https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js
  No other external scripts. Fonts only from Google Fonts.
- Every concept needs: a choreographed hero intro (load sequence, split-text / mask reveals), scroll-driven storytelling (pinned or scrubbed sections), micro-interactions (magnetic buttons, hover states, cursor or tilt effects where they fit), animated counters, and at least one "wow" signature moment unique to that concept (e.g. SVG contour lines drawing in, survey grid assembling, horizontal pinned project reel, layered parallax terrain, morphing shapes, canvas particles).
- Smooth 60fps: animate transform/opacity/clip-path, not layout props.
- If GSAP fails to load, the page must still show all content (do not hide content by default in CSS unless JS adds a class like `html.js` first).
- Respect `prefers-reduced-motion: reduce`: skip heavy motion, show content statically.

## UI/UX quality
- Clear hierarchy, strong typography (pair Google Fonts deliberately), generous spacing, consistent design tokens in :root.
- Fully responsive down to 360px wide: no horizontal scroll, 16px gutters, touch-friendly targets, working mobile menu.
- Accessible: semantic landmarks, alt text, visible focus states, sufficient contrast, buttons are <a>/<button>.
- Phones as tel: links (tel:+6498361804, tel:+6498696070). CTAs link to #contact; contact section has a simple enquiry form (no backend: on submit show an inline thank-you).
- Photos: only the 3 URLs in the brief, always with a coloured background fallback. Everything else drawn with CSS / inline SVG / canvas.
- A small fixed badge bottom-left: "Concept NN · <Name>" (unobtrusive).
- <title>: "Thomas Consultants · Concept NN"
- Must look like its own distinct design language, not a reskin of the others.
- Inspired-by means the *style* only: never use another brand's name, logo, copy or assets on the page.

# Phase 2: make every concept a complete end-to-end website

Each concept becomes a full multi-page site in its own design language (same fonts, tokens, nav, footer, motion system).

## File layout (for concept NN-slug)
- Home lives at `designs/NN-slug/index.html` (moved from `designs/NN-slug.html` after phase 2)
- Inner pages in a folder: `designs/NN-slug/services.html`, `projects.html`, `about.html`, `contact.html`
- Optional extra: `designs/NN-slug/project.html` (one project case-study detail page, e.g. Scott Road, Hobsonville)
- Pages may share nothing on disk except what's copied (keep each page self-contained, inline CSS/JS; duplication is fine).
- Links: home → `NN-slug/services.html` etc; inner pages → `../NN-slug.html` for Home and plain `services.html` etc. between siblings. Home-page "Learn more"/"View all" links go to the matching inner page (anchors like `services.html#engineering` welcome).

## Page content (from BRIEF.md)
- services.html: all 6 services with their sub-services listed, process steps, FAQ accordion (4-5 Qs, e.g. "Do I need a resource consent?", "How long does a subdivision take?", "What is a cross-lease to freehold conversion?", "Do you work outside Auckland?"), CTA.
- projects.html: all 9 projects with working category filter buttons (Engineering, Planning, Landscape, Surveying, Environmental, Residential/Commercial) and animated filtering; each card links to project.html (or #).
- about.html: 25-year story, values (sustainability, transparent communication, on-time on-budget), "Why choose us", accreditations, client list, community & sustainability commitment, testimonials, offices.
- contact.html: both offices with phones (tel: links), Christchurch satellite office, full enquiry form with validation (name, email, phone, service select, message; inline errors; success state, no backend), "Complimentary Planner Meeting" booking block, social links, client portal link (https://portal.thomasconsultants.co.nz).
- Nav on every page: Home, Services, Projects, About, Contact + CTA button; active page highlighted; mobile menu works on every page.

## End-to-end requirements
- Every internal link resolves to an existing file (no 404s), every anchor target exists.
- Page transitions: add a tasteful transition between pages consistent with the concept (e.g. overlay wipe on link click then navigate; reveal on load). Must not break back/forward (handle `pageshow` with persisted to remove overlay).
- Same motion quality on inner pages as on home (hero reveal, scroll reveals, micro-interactions).
- No console errors, no horizontal overflow at 390px and 1440px on any page.

# Phase 3: apply the AMBS house method (read ../AMBS-METHOD.md)

Apply to every page of your concepts (keep each concept's own visual language and signature motion):
- `<html lang="en-NZ">`, meta description, Open Graph tags, theme-color, JSON-LD `ProfessionalService` (both offices + phones) on home, `BreadcrumbList` on inner pages, `FAQPage` on services.html FAQ.
- Title: home "Thomas Consultants | Land Development Consultants, Auckland · Concept NN", inner "Services | Thomas Consultants · Concept NN".
- Skip link to `#main`; menu button with `aria-expanded` + `aria-controls`, 44px; menu closes on link click; `scroll-padding-top` for sticky header.
- Inner page heroes: breadcrumbs (Home / Page), full-sentence h1 ending in a full stop (e.g. "Six disciplines. One integrated team."), short lede. Every inner page ends with a CTA band.
- Mobile (<=760px): fixed bottom quick bar with "Call 09 836 1804" + "Book a meeting", using env(safe-area-inset-bottom); pad the footer so it isn't covered.
- Process uses the four stages: Understand the site → Design & consent → Deliver on site → Complete & hand over.
- Forms: `novalidate`, JS validation, hidden honeypot field (`name="company_website"`, tabindex -1, aria-hidden wrapper), `<p role="status" aria-live="polite">`, "(optional)" markers, `autocomplete` on fields; success text "Thank you. We have your enquiry and will be in touch soon."; note under form "We use your details only to reply to your enquiry."
- Contact details as a `<dl>`; add "What to tell us": your site, your idea, timing, budget ("A guess is fine.").
- Counters ease with 1-(1-p)^3. Lenis only when `matchMedia('(pointer:fine)')` and no reduced motion. No unconditional `animation:none`.
- Images: width/height attributes, `loading="lazy" decoding="async"` (hero: `fetchpriority="high"`, not lazy).
- Copy: NZ English, short plain sentences. NO em dashes (—) anywhere in visible copy, no exclamation marks (except inside verbatim client testimonials), no hype words (seamless, unlock, revolutionise, leverage, cutting-edge). Do not invent stats, awards or testimonials beyond BRIEF.md (25 years, 6 disciplines, 3 offices, project count are fine).
- Footer: Services + Explore columns, legal line "© 2026 Thomas Consultants Ltd", "Some images may be stock images or illustrative renders.", "Proudly designed by AMBS Solutions".
- REMOVE the "Concept NN" bottom-left badge: the gallery will inject a shared concept switcher (`../assets/concepts.js` style) at the end; just leave `<html data-concept="NN-slug">` on every page.

# Phase 4: rebuild to MiKia standard (client feedback: "not optimised", "not impressive")

Benchmark: https://mikia-consulting.vercel.app (AMBS's own land-development site). Open it, study it, and match its level of craft in your concept's own design language. Do not copy MiKia's brand (red/serif look, logo, copy); copy its *quality and patterns*.

## What makes MiKia impressive (apply these)
1. **Cinematic full-bleed photo hero**: real photography (or a slow crossfading slideshow of 3 photos with Ken Burns), dark gradient for legibility, a SHORT punchy serif/display headline with one animated or italic accent word that rotates (e.g. "From raw land to *homes* / *parks* / *streets* people love."). The long "Your Trusted Partner for End-to-End Land Development Support" becomes the eyebrow or lede, not the H1. Big pill CTAs, full-width on mobile. Progress bar on the slideshow.
2. **Discipline showcase**: "Six disciplines. One integrated team." as an interactive carousel/tabs with story progress bars, autoplay with pause, each discipline with a real photo + 3-4 ticked points.
3. **Process**: 4 stages as sticky stacking cards (CSS position:sticky), each a different tone, with a photo or icon, big stage number.
4. **Projects**: real photos on EVERY project card; hover zoom; Residential | Commercial | Public spaces split panels with photos.
5. **"In the field" photo carousel/mosaic** with captions and prev/next.
6. **People**: use the team photos (engineer-smiling, engineer-scaffold, team-plans, site-visit, park-team) in Why/About so it feels human.
7. **Rounded section sheets** that overlap the previous section (border-radius 32-40px top, negative margin), alternating light/dark for rhythm. No large empty areas: every section has a visual anchor (photo, illustration, data).
8. **Warm contact block**: "Let's talk about your site." with a prominent Book a meeting card, phone, email.
9. Mobile is the primary experience: check every section at 390px. Hero fills the screen, text never cramped, no awkward empty gaps, swipeable carousels, sticky quick bar.

## Photography (mandatory)
- Use ONLY the self-hosted library `thomas-consultants/assets/img/` (from pages: `../../assets/img/NAME-800.webp` etc). Manifest with alt text, sizes and source project: `assets/img/photos.json`. Each photo has `NAME-800.webp` and usually `NAME-1600.webp` (or a native width listed in `widths`).
- Every <img>: `srcset` with the available widths, a correct `sizes`, `width`/`height`, `alt` from the manifest, `loading="lazy" decoding="async"` except the LCP hero image (`fetchpriority="high"`, no lazy, plus `<link rel="preload" as="image" imagesrcset=... imagesizes=...>` in <head>).
- Remove ALL hotlinked thomasconsultants.co.nz images.
- Project ↔ photo mapping (use real names and matching photos):
  - McMillan and Lockwood, Kāinga Ora: aerial-apartments, apartments-street
  - 2 Cracroft Road / 618-620 Great South Road, Kāinga Ora: apartments-colour, aerial-apartment-block
  - Churchill Park Lookout (landscape architecture): lookout-seat, park-seating, park-team
  - Observation Green (landscape architecture): play-space
  - Open Space, Fearon Park (project management): plaza-path
  - Taurus Crescent, Kāinga Ora (engineering, surveying): aerial-subdivision, aerial-street
  - Thom Street, New Lynn (engineering design, construction monitoring): apartments-bright, street-new
  - Tasman Avenue, Mt Albert (engineering, surveying): house-dusk, house-modern
  - Signature Homes & Kāinga Ora (engineering, planning): aerial-harbour, homes-fenced
  - Kaimai Avenue, Massey terraced housing: townhouses-new, aerial-townhouses
  - Elliott Reserve playground, Glenfield (project management): playground
  - Kauri Glen Reserve, Northcote (ecological assessment): bush
  - Withers Reserve (environmental): boardwalk
  - Rural subdivision (stormwater, ecology): stream, swale, swale-path
  - Henderson High School Heart Space (landscape architecture): render-park
  - Scott Road, Hobsonville (resource consent): plan-engineering
- Service photos: surveying → surveyor-road / aerial-subdivision; planning → team-plans / plan-engineering; engineering → engineer-scaffold / roadworks / new-road; landscape → lookout-seat / playground-aerial; environmental → stream / bush / soil-test; project management → site-visit / earthworks-sunset.
- `surveyor-road`, `team-meeting`, `fern-canopy`, `playground-aerial`, `office`, `plans-desk`, `site-visit`, `engineer-*`, `team-plans` come from the client's general site imagery (fine to use).

## Performance budget (mandatory, measured)
Test: Playwright, 390x844 mobile, 4x CPU throttle, ~1.6 Mbps, 150 ms latency.
- LCP < 2.5 s, CLS < 0.05, Total Blocking Time < 300 ms, HTML < 150 KB per page, total page weight on first load < 1.2 MB.
- Fonts: at most 2 families, only the weights used, `display=swap`, preconnect.
- JS: GSAP + ScrollTrigger with `defer`; init after `DOMContentLoaded`. Lenis only for `(pointer:fine)` and no reduced motion. No layout reads inside scroll handlers; use ScrollTrigger or rAF. Pause canvas/WebGL/rAF loops when off-screen (IntersectionObserver) and when `document.hidden`; cap canvas DPR at 1.5; on `(pointer:coarse)` or `navigator.hardwareConcurrency<=4` use a lighter variant (fewer particles, no per-frame SVG rebuild).
- No huge inline SVG/data (generate procedurally in JS if needed). Big decorative SVGs: keep path counts low.
- `content-visibility:auto; contain-intrinsic-size:auto 800px` on below-the-fold sections that have no pinned ScrollTrigger inside.
- Animate only transform/opacity/clip-path. Reserve space for images (aspect-ratio) to keep CLS ~0.
- Keep all Phase 2/3 requirements (pages, nav, forms, JSON-LD, copy rules, data-concept, concepts.js script tag).

Verify with `node thomas-consultants/tests/e2e.mjs NN` (must pass 40/40) and `node thomas-consultants/tests/perf.mjs NN` (must meet the budget on every page).
