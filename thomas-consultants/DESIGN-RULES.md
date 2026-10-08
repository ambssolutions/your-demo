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
