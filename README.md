# JakinsCraft

Public marketing site for the JakinsCraft custom UV-printing business (Toronto).
Live at https://pappyakins.github.io/jakinscraft/

## Structure

- `index.html` — the whole site (generated; served by GitHub Pages)
- `build.py` — builds `index.html`. **Edit the two constants at the top, then re-run:**
  - `WHATSAPP_NUMBER` — WhatsApp number used by every order/quote link (digits only, with country code)
  - `LOGO_PATH` — logo image path (default `assets/logo.png`)
- `assets/logo.png` — logo file. Drop the real logo here (same filename) and it appears everywhere — no code changes needed.

## Sections

Hero · Products (NFC/QR pendant, 30oz tumbler, QR keychain — each with WhatsApp order button) ·
Custom quote form (builds a pre-filled WhatsApp message, no backend) ·
Bulk & corporate pitch · Gallery placeholders · Footer.

No build step, no backend, no accounts — pure static site.
