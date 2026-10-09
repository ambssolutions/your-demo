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

# Phase 5: real brand + "stop looking AI-generated" (client feedback: "why not the original logo?", "is it looking AI generated?")

## A. Real logo and brand colours (mandatory, every page)
- Logo files: `thomas-consultants/assets/logo/` (from pages: `../../assets/logo/...`)
  - `thomas-consultants.svg`: full colour (green swirl #77A22F + teal text #052C31), for light backgrounds
  - `thomas-consultants-white.svg`: white text + green swirl, for dark backgrounds/headers over photos
  - `thomas-consultants-mono-dark.svg`: all teal, for very light/green backgrounds where the swirl would clash
  - `mark.svg`: swirl only, for favicon and tight spaces
- Header: replace ANY text wordmark / invented icon with `<img src="../../assets/logo/....svg" alt="Thomas Consultants" width="152" height="40">` (height 34-44px desktop, 30-34px mobile; width auto from 190x50 ratio). Use the white version when the header sits over a photo or dark section, and swap to colour when the header becomes solid light on scroll (two <img> toggled by class is fine). Footer: logo too. Favicon: `<link rel="icon" type="image/svg+xml" href="../../assets/logo/mark.svg">`.
- Brand colours: official green **#77A22F**, official ink/teal **#052C31**. Replace #6DAB3C/#5F9434 etc with the official green (lighter/darker tints derived from it are fine). Each concept may keep its personality palette, but the brand green and ink must appear correctly (logo, primary buttons or key accents).

## B. Remove copied and AI-template copy (mandatory)
- REMOVE all MiKia lines (another client's copy): "Six disciplines. One integrated team.", "We make it easy. You see it through.", "From the first survey peg to the finished street/last planting/new street", "Let's talk about your site.", "Easy to work with. Committed to your goals.", "Quick answers.", "From raw land to a place people…". Write your own.
- Do NOT use "From raw land to <word> people love." in any concept. Rotating accent-word headlines are allowed ONLY in 01 Terrain and 09 Kinetic.
- Prefer the client's own language: "Creating Better Spaces Together", "Quality civil engineering, resource consents and planning", "Land development & subdivision consultants", "from site assessments to final delivery", and the real project text.
- Cut AI-template tells: no more than ONE mono/uppercase eyebrow style label per section and none on every card; no "STAGE 01 / SHEET S-01 / REV A / CH 0.250" decoration unless it carries real meaning (Blueprint may keep a little); limit pill tags to 2 per card; no fake UI widgets with invented data; no generic stat row "25 years · 6 disciplines · 3 offices" in the hero (use it once, lower down, at most); no invented figures.
- Vary rhythm: not every section needs heading + subheading + 3 cards. Use some long-form paragraphs, a real quote, a big real number, a single large photo with a caption.

## C. Real project content (mandatory)
- `thomas-consultants/assets/content/projects-source.json` holds the real text from the client's 40 project pages (title, site, overview, goal, process, outcome). Use it for project cards and every `project.html?p=` case study (2-4 short paragraphs + the real facts: site address, client, what Thomas did, outcome). Light editing for length is fine; do not invent facts.
- Use concrete real facts on home pages where they fit, e.g. Thom Street: engineering design + construction monitoring for 82 terrace houses and apartments for Kāinga Ora, about 300 tenants, 11,046 m² site, completed November 2020; Taurus Crescent: engineering, surveying and planning for 21 homes in Beach Haven; Churchill Park lookout: concept design for Auckland Council and the Ōrakei Local Board, 360° views over a former golf course.
- Keep the photo mapping from Phase 4.

## D. Make each concept structurally distinct (mandatory)
The ten concepts currently share one section order. Restructure each home page around its own idea (keep all pages, nav, forms, JSON-LD, perf budget):
- **01 Terrain**: cinematic long scroll that tells ONE project start to finish (Thom Street: survey → design → consent → construction → handover), then the services and a short project list. Headline may rotate words.
- **02 Flow**: product-style "Where do you want to start?" chooser at the top (Subdivide my land / Get a resource consent / Survey my site / Design a public space) leading to the right service; clean feature sections; headline built on "Quality civil engineering, resource consents and planning."
- **03 Blueprint**: the drawing register IS the home page: a large project register table/list with real sites, clients, disciplines, years where known; each row expands to a photo + facts. Headline idea: "Every good development starts with a good survey." (or similar, your words).
- **04 Field Notes**: magazine issue: one lead feature article (Churchill Park lookout, real text + pull quote), then 2 secondary features, then a short "contents" of services. Serif, generous whitespace.
- **05 Midnight**: capability and assurance: accreditations (ISO 45001, IANZ, Toitū), health and safety, council approvals process; projects as a dark gallery. Distinct headline.
- **06 Swiss**: index of real numbers and facts (82 homes, 21 dwellings, 11,046 m², 25 years) set in giant type, services as a numbered index; minimal photography in a strict grid.
- **07 Aotearoa**: land, water and ecology first: streams, reserves, native planting, contamination testing; sustainability commitment with real projects (Kauri Glen, Withers Reserve, rural subdivision stormwater).
- **08 Bento**: homeowner and small developer focus ("Thinking of subdividing your section?"): friendly guide tiles, cross-lease to freehold explainer, the quiz, simple steps, real FAQ.
- **09 Kinetic**: bold big-energy: the team and culture (people photos), huge real numbers, project reel. Rotating words allowed.
- **10 Infrastructure**: for councils, government and large developers: sectors, clients (Kāinga Ora, Auckland Council, Auckland Transport, Watercare), prequalification and accreditations, office map, projects grouped by client.

## Verify
`node thomas-consultants/tests/e2e.mjs NN` 40/40 and `node thomas-consultants/tests/perf.mjs NN` all pages within budget. Grep your pages for the banned MiKia lines and for "people love" before finishing. Then regenerate thumbnails: `node thomas-consultants/tools/thumbs.mjs NN-slug`.

# Phase 6: laptop screens (client feedback: "not laptop screen friendly, text overlapping", "design 2 cards stacking when transparent", "swiss grid is not good", "design 7 not laptop friendly")

Test viewports (all must look intentional, nothing overlapping or cut): **1280x720, 1366x768, 1440x900, 1536x864**, plus 390x844 mobile.
Audit: `node thomas-consultants/tests/laptop.mjs NN` must report **0 layout issues**. Also scroll each page with the mouse wheel at 1280x720 and look at screenshots yourself (tests/out/laptop/ has top-of-page shots).

## Rules
1. **Hero fits the screen.** On a 720px-tall laptop the whole hero (eyebrow, H1, lede, CTAs) must be visible above the fold with breathing room. Size display type with BOTH width and height, e.g. `font-size: clamp(2.4rem, min(6.2vw, 9.5vh), 6.5rem)`; tighten line-height; cap hero height to `min(100svh, …)`; never let hero text sit under the fixed header or run off the bottom.
2. **Stacked/sticky cards:** every stacked card must have a **fully opaque background** (no rgba/alpha, no backdrop blur as the only background). No opacity or reveal (.rv) fade on a sticky card or its children: content inside stacked cards is always opacity 1 (animate only transform if anything). The card must fit: `max-height: calc(100svh - <sticky top> - 24px)`; if content can't fit, reduce padding/type with vh-aware clamp. When `(max-height: 760px)` and the stack would still be cramped, turn the stack into normal flow (position: static, no overlap).
3. **No accidental overlap:** cursor-follow previews must not cover the text they belong to (offset them or show beside); giant footer/display text must fit the viewport width (use vw-based clamp, `overflow-wrap:anywhere` not acceptable for words, reduce size instead); big counters/numbers must not overlap their labels or neighbouring headings; animated counters reserve width (tabular-nums / min-width) so layouts don't jump.
4. **Pinned/horizontal sections** (project reels, journals, pinned heroes): check at 720px height that titles and captions are fully visible; reduce card height using vh units.
5. **Reveal animations** must never leave text semi-transparent over other content; anything that overlaps another layer must be opaque before it overlaps.
6. Keep everything else from Phases 2–5 (perf budget, e2e 64/64, real logo/content, copy rules).

## Concept-specific
- **02 Flow:** fix the stacked process cards: opaque, no fade, fit 720px height, as above.
- **06 Swiss Grid:** client says "not good". Redesign the home (and carry the system to inner pages): a proper International Typographic Style layout that is rich, not sparse: asymmetric 12-col grid with strong photography blocks next to the numbers (each real number paired with its project photo and caption), tighter vertical rhythm (no near-empty screens), a confident red-free palette of white, ink #052C31 and brand green #77A22F, Archivo/Inter Tight type with a clear scale, the services index without overlapping previews (preview image in a fixed right column instead), and a footer whose large type fits. It should look like a polished Swiss design studio site, not a wireframe.
- **07 Aotearoa:** client says "not laptop friendly": the pinned ridgeline hero, the koru section and stacked sections must all fit 1280x720 and 1366x768 per the rules above.

# Phase 7: stop looking like a template (client asked again: "are they looking like AI generated websites?")

Honest review: real logo, photos, projects and quotes help a lot, but the concepts still share one template skeleton. Fix the skeleton, not just the paint.

Audit: `node thomas-consultants/tests/tells.mjs NN` must pass for your concept (and the cross-concept section must not list your concept). It checks:
- **Accent-word headings** (one word/phrase in a different colour or italic inside an H1/H2): max 1 per page (the hero). 01 Terrain and 09 Kinetic may use up to 3 (their rotating/kinetic device).
- **Short headings ending in a full stop** ("Recent work.", "What we do.", "Three offices. One team."): max 2 per page. Most section headings should be plain labels or real facts without a full stop ("Projects", "Kāinga Ora housing at Thom Street", "Offices").
- **Eyebrow labels** (small uppercase letter-spaced label above a heading): max 2 per page. 03 Blueprint and 06 Swiss are exempt because their numbering is the design system, but keep it purposeful.
- **The generic 4-step process** (Understand the site / Design & consent / Deliver on site / Complete & hand over) may appear on at most ONE home page in the whole set. Assignments below say who keeps it.
- **No section heading repeated across concepts** (3+ words, project names excepted).

## What to change (every concept)
1. **Hero composition is the concept's own.** Not the formula "tiny uppercase label → big headline with one green word → grey paragraph → green pill button + outline pill button". Pick a composition that fits the concept (e.g. a register table, a magazine cover, a split index, a full-bleed photo with a caption block, a chooser). One primary action is enough; the second can be a text link.
2. **Each concept has its own surface language** (buttons, cards, dividers, corners). Not every concept gets 16-24px rounded cards with soft shadows and pill buttons. Allowed: square corners + hairlines, paper/editorial rules, drawing frames, dense tables, flat colour blocks, etc. "Rounded sheet slides up over the previous section" transitions: at most one concept (01 Terrain keeps it).
3. **Process:** only 08 Bento keeps a 4-stage explainer on its home page (as homeowner steps, in its own words). Everyone else: drop it from the home page or replace it with something specific and real (e.g. 02: Thom Street timeline with real milestones; 05: an approvals/consents list naming the real consents (s223, s224c, engineering plan approval, building consent) and who issues them; 10: a stage table "Stage / What we deliver / Who signs it off"). On services pages, rename and reshape it in the concept's own way; do not reuse the same four step titles everywhere.
4. **About pages are not the same list.** Currently every about page is "Our story / Values / Why choose us / Community & sustainability / Clients & accreditations / Testimonials / Offices". Each concept picks the 3-5 sections that suit it and gives them its own form and wording (e.g. 04 a long-form interview/essay, 06 a fact index, 09 people-first team grid, 10 a capability statement).
5. **Copy cadence.** Avoid AI rhythm: "X. One Y." pairs, triplets, "from A to B" taglines, "Built over 25 years, one project at a time", "What we hold ourselves to", "Better spaces for the people who use them", "Tell us about your land", "Sit down with a planner. It costs nothing." Write like a consultancy writes: plain, specific, factual, real names, real numbers. NZ English, no em dashes, no invented facts.
6. **Quotes:** use at most 2 testimonials per page, presented in the concept's own way.
7. **Footers:** each concept its own footer layout; only 01 keeps the giant faded wordmark.
8. Keep everything that already passes: real logo, photos, real content, perf budget (`tests/perf.mjs`), laptop audit 0 issues (`tests/laptop.mjs`), e2e 64/64, mobile.

## Concept direction
- **01 Terrain:** keep the Thom Street cinematic story and the rotating hero. Cut eyebrow/full-stop habit on about/services; fewer pill buttons (text links with arrows). Keeps the rounded sheet transition and giant footer wordmark.
- **02 Flow (heavy):** keep the "Where do you want to start?" chooser hero (it is distinctive). Replace the stacked 01-04 process with a Stripe-like horizontal Thom Street timeline (brief, design, consents, construction, titles, opened Nov 2020) drawn with thin lines. Remove rounded sheet sections and soft-shadow cards; use crisp white panels, thin borders, small diagrams. Headings plain.
- **03 Blueprint:** already strong. Remove the process block from home (register + one drawing-sheet section is enough), plain headings, footer as a drawing title block.
- **04 Field Notes:** already strong. Fewer italic accent headings (the cover headline only), section labels as running heads/page numbers rather than eyebrows, about page as a long-form essay.
- **05 Midnight (heavy):** Linear/Vercel feel. Replace the stacked process + ISO cards with: an approvals list (consent / issued by / when in the project) in a dense dark table, a changelog-style dated project log, accreditations as a compact row. No green-word headlines, no rounded light section in a dark site.
- **06 Swiss:** already redesigned. Remove the process block from home, keep numbered index system, plain headings.
- **07 Aotearoa:** too many eyebrows (12 on home). Use trail-marker/signage or map-legend devices sparingly, plain headings, drop the process block from home, fewer sections.
- **08 Bento (heavy):** keeps the homeowner 4-step explainer (one bento tile group, own words: "Check / Survey / Design and consent / Titles"). Remove "Clients say it best.", "In good company." style headings; tiles carry content, not section headers; one testimonial tile, one accreditations tile.
- **09 Kinetic:** reduce accent headings to 3, eyebrows to 2 per page (the "01 / 06" counters on services are fine as large kinetic numbers, not as eyebrow labels), remove the process block from home.
- **10 Infrastructure (heavy):** Arup/AECOM: sober, square corners, no pill buttons, no green-word headlines. Home: sectors index, projects grouped by client, prequalification table, stage table (Stage / Deliverable / Sign-off authority), offices. Services and about as capability statements.
