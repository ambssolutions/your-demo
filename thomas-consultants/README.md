# Thomas Consultants: website concepts

Ten complete website concepts for **Thomas Consultants Ltd** (land development, surveying, planning, engineering, landscape and environmental consultants, Auckland). Each concept is a full six-page site in its own design language, built from the content of thomasconsultants.co.nz.

Open `index.html` for the review gallery. Clients can preview each concept on desktop, tablet and mobile, shortlist favourites, compare up to three side by side, and send their preferred design.

No build step. To preview locally: `python3 -m http.server` from this folder, then open http://localhost:8000.

## Concepts

| # | Name | Inspired by | Motion | Short link |
|---|---|---|---|---|
| 01 | Terrain | Apple product pages | Highly animated | `/terrain` |
| 02 | Flow | Stripe | Animated | `/flow` |
| 03 | Blueprint ★ | Engineering drawings | Highly animated | `/blueprint` |
| 04 | Field Notes | Kinfolk / Aesop editorial | Subtle motion | `/field-notes` |
| 05 | Midnight | Linear / Vercel | Interactive | `/midnight` |
| 06 | Swiss Grid | Pentagram, Swiss style | Animated | `/swiss` |
| 07 | Aotearoa ★ | Patagonia, national parks | Highly animated | `/aotearoa` |
| 08 | Bento | Notion / Apple keynote | Interactive | `/bento` |
| 09 | Kinetic | Awwwards agency sites | Highly animated | `/kinetic` |
| 10 | Infrastructure ★ | Arup / AECOM | Interactive | `/infrastructure` |

★ = recommended in the gallery.

## Structure

```
index.html                  review gallery (shortlist, compare, send your pick)
designs/NN-slug/index.html  concept home
designs/NN-slug/services.html, projects.html, about.html, contact.html, project.html (?p=slug)
designs/NN-slug/thumb.webp  gallery thumbnail (thumb.jpg fallback)
assets/concepts.js          floating concept switcher on every page (prev / menu / next / shortlist)
vercel.json                 short links, noindex, cache headers
tests/e2e.mjs               end-to-end checks (gallery + every page at 1440px and 390px)
tools/thumbs.mjs            regenerate thumbnails
tools/restructure.py        one-off layout migration (kept for reference)
BRIEF.md, DESIGN-RULES.md, AMBS-METHOD.md   content brief and build rules
```

## Receiving the client's choice

At the top of the script in `index.html`:

- `FORM_ENDPOINT`: a form service URL that accepts JSON (e.g. Formspree). Choices are sent straight from the page.
- `SEND_TO`: fallback email address for the pre-filled email.

With neither set, "Send preference" opens the client's email app with the choice filled in, and they add the address. "Copy summary" and the share link (`?s=01,04&p=04`) also work.

## Testing

```
node tests/e2e.mjs            # everything
node tests/e2e.mjs gallery    # gallery only
node tests/e2e.mjs 03         # one concept
node tools/thumbs.mjs         # regenerate thumbnails
```

Checks: no console errors, no horizontal overflow, no broken links or anchors, mobile menu, contact form validation and success, gallery shortlist / compare / send / share link.

## Things to finish before launch (for the chosen concept)

- Confirm a form endpoint for enquiries (each contact form currently shows its thank-you without sending).
- Real project photos and case-study text (see `CONTENT-NEEDED.md`).
- Client copy check, especially FAQ answers and short supporting lines written for the concepts.
- Street addresses for the offices and the Christchurch contact details.
- Domain, canonical URLs, sitemap and robots (remove `noindex`).
