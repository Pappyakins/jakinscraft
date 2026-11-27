#!/usr/bin/env python3
"""Builds the JakinsCraft single-page site -> index.html.

Swap these two values and re-run to update the whole site:
"""
WHATSAPP_NUMBER = "14378552210"   # Pappy's real WhatsApp number (digits only, with country code)
LOGO_PATH = "assets/logo.png?v=3"     # drop the real logo file here later; no code changes needed
IMG_E1 = "assets/machine-e1.jpg"    # eufyMake E1 UV printer -> UV printing / tumbler card
IMG_P1S = "assets/machine-p1s.jpg"  # Bambu Lab P1S -> Custom 3D Printing card
IMG_F2 = "assets/machine-f2.jpg"    # xTool F2 laser engraver -> Laser Engraving card
IMG_PENDANT = "assets/fb/nfc-pendant.jpg"    # Facebook listing photo -> NFC pendant card
IMG_KEYCHAIN = "assets/fb/nfc-keychain.jpg"  # Facebook listing photo -> QR keychain card
IMG_PLATE_CARD = "assets/fb/nfc-plate-card.jpg"  # Facebook listing photo -> Ontario plate NFC card
IMG_TUMBLER_FAITH = "assets/gallery/tumbler-man-of-faith.jpg"  # Custom "Man of Faith" tumbler -> gallery tile
IMG_HOODIE_AHEAD = "assets/gallery/hoodie-ahead-art.jpg"  # Custom "Ahead" hoodie -> gallery tile
IMG_CANVAS_CHILD = "assets/gallery/canvas-portrait-child.jpg"  # Canvas portrait, child in red traditional attire
IMG_CANVAS_GELE = "assets/gallery/canvas-portrait-gele.jpg"  # Canvas portrait, gele headwrap
IMG_CANVAS_PIZZA = "assets/gallery/canvas-portrait-pizza.jpg"  # Canvas portrait
IMG_CANVAS_BRAIDS = "assets/gallery/canvas-portrait-braids.jpg"  # Canvas portrait, braided hair
IMG_CANVAS_BOY = "assets/gallery/canvas-portrait-boy-beads.jpg"  # Canvas portrait, boy with coral beads
IMG_CANVAS_PAIR = "assets/gallery/canvas-portraits-pair.jpg"  # Two canvas portraits
IMG_HOODIE_BUNNY = "assets/gallery/hoodie-hiphop-bunny.jpg"  # Hip Hop bunny hoodie
IMG_TEE_MOMLIFE = "assets/gallery/tee-mom-life.jpg"  # Mom Life t-shirt
IMG_TEE_MONKEY = "assets/gallery/tee-monkey-dj.jpg"  # DJ monkey t-shirt
IMG_KEY_BOTB = "assets/gallery/keychain-botb-arena.jpg"  # BOTB Arena keychain
IMG_KEY_INSTA = "assets/gallery/keychains-instagram.jpg"  # Instagram QR keychains
IMG_PENS_TREM = "assets/gallery/pens-trem-engraved.jpg"  # Laser-engraved TREM bamboo pens
IMG_TUMBLER_SUMMER = "assets/gallery/tumbler-summer-vibes.jpg"  # Summer Vibes tumbler
IMG_E1_PRINTING = "assets/gallery/e1-printing-tumbler.jpg"  # Tumbler UV printing on the E1
IMG_GAL_PENDANT = "assets/fb/nfc-pendant.jpg"  # NFC pendant listing photo -> gallery tile
IMG_CANVAS_HAT = "assets/gallery/canvas-portrait-hat.jpg"  # New: framed canvas portrait, man in wide-brim hat -> gallery tile
IMG_CANVAS_GLASSES = "assets/gallery/canvas-portrait-glasses.jpg"  # New: unframed canvas portrait, man with glasses -> gallery tile
IMG_TREM_PAIR = "assets/gallery/canvas-portrait-trem-pair.jpg"  # New: framed TREM Children Church painted portraits, pair on display -> gallery tile
IMG_TREM_SUIT = "assets/gallery/canvas-portrait-trem-suit.jpg"  # New: framed TREM Children Church painted portrait, suit and striped tie -> gallery tile
IMG_TREM_FLORAL = "assets/gallery/canvas-portrait-trem-floral.jpg"  # New: framed TREM Children Church painted portrait, floral top -> gallery tile

import pathlib, urllib.parse

OUT = pathlib.Path(__file__).parent / "index.html"

def wa(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text=" + urllib.parse.quote(text)

orders = {
    "pendant": wa("Hi JakinsCraft! I'd like to order a Custom NFC & QR Code Business Logo Pendant. (1/$20, 2/$35, 5/$75)"),
    "plate_card": wa("Hi JakinsCraft! I'd like to order an Ontario Licence Plate NFC Card. ($20)"),
    "tumbler": wa("Hi JakinsCraft! I'd like to order custom UV printing."),
    "keychain": wa("Hi JakinsCraft! I'd like to order a custom QR keychain."),
    "3dprint": wa("Hi JakinsCraft! I'm interested in custom 3D printing. Here's what I need:"),
    "laser": wa("Hi JakinsCraft! I'm interested in laser engraving. Here's what I need:"),
    "crystal": wa("Hi JakinsCraft! I'm interested in a 3D crystal or relief keepsake. Here's what I need:"),
    "zodiac": wa("Hi JakinsCraft! I'm interested in a zodiac birthday gift. Here's what I need:"),
    "music": wa("Hi JakinsCraft! I'm interested in a music photo frame. Here's what I need:"),
    "wordtiles": wa("Hi JakinsCraft! I'm interested in a family word tile display. Here's what I need:"),
    "babyblocks": wa("Hi JakinsCraft! I'm interested in a baby photo block. Here's what I need:"),
    "bulk": wa("Hi JakinsCraft! I'm interested in a bulk / corporate order. Let's talk."),
    "quote": None,  # built live in JS
}

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JakinsCraft — Custom UV-Printed Gear | Toronto</title>
<meta name="description" content="JakinsCraft: custom NFC & QR business logo pendants, UV-printed 30oz tumblers, QR keychains, and laser engraving and cutting. Designed in Toronto.">
<link rel="icon" href="%%LOGO_PATH%%">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0c0c0e; --panel:#141417; --panel2:#1a1a1e;
  --accent:#a855f7; --accent-soft:#c084fc; --accent-dim:rgba(168,85,247,.16);
  --text:#f3f0fa; --muted:#a8a3b8; --line:rgba(168,85,247,.22);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
h1,h2,h3,.serif{font-family:'Playfair Display',Georgia,serif}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
section{padding:64px 0}
.eyebrow{color:var(--accent);text-transform:uppercase;letter-spacing:.22em;font-size:.75rem;font-weight:600;margin-bottom:12px}
h2.sec{font-size:clamp(1.7rem,5vw,2.4rem);margin-bottom:8px}
.sub{color:var(--muted);max-width:640px;margin-bottom:32px}
/* nav */
nav{position:sticky;top:0;z-index:50;background:rgba(12,12,14,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;max-width:1080px;margin:0 auto}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:700}
.brand img{width:38px;height:38px;border-radius:10px}
.brand span{font-family:'Playfair Display',serif;font-size:1.25rem;letter-spacing:.02em}
.brand span em{color:var(--accent);font-style:normal}
.nav-links{display:flex;gap:18px;font-size:.9rem}
.nav-links a{text-decoration:none;color:var(--muted)}
.nav-links a:hover{color:var(--accent)}
@media(max-width:640px){.nav-links{display:none}}
/* hero */
.hero{position:relative;text-align:center;padding:96px 0 80px;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 70% 55% at 50% 30%,rgba(168,85,247,.14),transparent 70%);pointer-events:none}
.hero img.logo{width:120px;height:120px;border-radius:28px;box-shadow:0 12px 40px rgba(168,85,247,.25);margin-bottom:24px;position:relative}
.hero h1{font-size:clamp(2.6rem,9vw,4.5rem);line-height:1.05;letter-spacing:.01em;position:relative}
.hero h1 em{color:var(--accent);font-style:normal}
.tag{color:var(--muted);font-size:clamp(1rem,3.5vw,1.2rem);max-width:600px;margin:18px auto 32px;position:relative}
.cta-row{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;position:relative}
.btn{display:inline-block;padding:14px 30px;border-radius:999px;font-weight:600;text-decoration:none;font-size:1rem;transition:transform .15s ease,box-shadow .15s ease;border:1px solid transparent}
.btn:active{transform:scale(.97)}
.btn-accent{background:linear-gradient(135deg,var(--accent-soft),var(--accent));color:#ffffff;box-shadow:0 8px 28px rgba(168,85,247,.35)}
.btn-ghost{border-color:var(--line);color:var(--text);background:rgba(255,255,255,.02)}
.btn-ghost:hover{border-color:var(--accent)}
.badges{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:36px;position:relative}
.badge{font-size:.8rem;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:6px 14px;background:rgba(168,85,247,.05)}
/* products */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}
.card{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:20px;padding:28px;display:flex;flex-direction:column;transition:transform .18s ease,box-shadow .18s ease}
.card:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(0,0,0,.5),0 0 0 1px rgba(168,85,247,.35)}
.card .icon{font-size:2.2rem;margin-bottom:14px}
.card .machine-photo{display:block;width:calc(100% + 56px);height:190px;object-fit:cover;margin:-28px -28px 18px;border-radius:20px 20px 0 0;border-bottom:1px solid var(--line);background:#0e0e10}
.card h3{font-size:1.45rem;margin-bottom:10px}
.card h3 em{color:var(--accent);font-style:normal}
.card p{color:var(--muted);font-size:.95rem;flex:1;margin-bottom:18px}
.price{font-weight:700;color:var(--accent-soft);margin-bottom:18px;font-size:1.02rem}
.price small{display:block;color:var(--muted);font-weight:400;font-size:.85rem;margin-top:2px}
.btn-wa{display:block;text-align:center;background:#1f2c24;border:1px solid #2f7d4f;color:#7bf0a4;padding:13px;border-radius:14px;font-weight:600;text-decoration:none;font-size:.95rem}
.btn-wa:hover{background:#243829}
/* quote */
#quote .panel{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:24px;padding:32px;max-width:640px;margin:0 auto}
.field{margin-bottom:18px}
.field label{display:block;font-size:.85rem;font-weight:600;color:var(--accent-soft);margin-bottom:8px;letter-spacing:.04em}
.field input,.field select,.field textarea{width:100%;background:#0e0e10;border:1px solid var(--line);border-radius:12px;color:var(--text);padding:13px 14px;font-size:1rem;font-family:inherit}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(168,85,247,.15)}
.field textarea{min-height:110px;resize:vertical}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:520px){.row2{grid-template-columns:1fr}}
.hint{font-size:.82rem;color:var(--muted);margin-top:14px;text-align:center}
/* bulk */
.bulk-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin-bottom:32px}
.bulk-card{background:rgba(168,85,247,.05);border:1px solid var(--line);border-radius:18px;padding:24px}
.bulk-card h3{font-size:1.2rem;margin-bottom:8px;color:var(--accent-soft)}
.bulk-card p{color:var(--muted);font-size:.93rem}
.center{text-align:center}
/* gallery */
.gal{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px}
.tile{aspect-ratio:1/1;border-radius:18px;border:1px dashed rgba(168,85,247,.45);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:var(--muted);font-size:.85rem;text-align:center;padding:16px;background:rgba(255,255,255,.015)}
.tile .t-icon{font-size:1.8rem;opacity:.7}
.tile b{color:var(--accent-soft);font-weight:600}
.tile.tile-photo{padding:0;overflow:hidden;border-style:solid}
.tile.tile-photo img{width:100%;height:100%;object-fit:cover;display:block}
/* laser work */
.work-group{font-size:1.35rem;margin:36px 0 6px;color:var(--text)}
.work-note{color:var(--muted);font-size:.93rem;margin-bottom:18px}
.work-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
.work-tile{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:16px;overflow:hidden}
.work-tile img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;background:#0e0e10}
.work-tile.wide{grid-column:1/-1}
.work-tile.wide img{aspect-ratio:21/9}
.work-cap{padding:12px 14px 14px}
.work-cap b{display:block;font-size:.95rem;font-weight:600;margin-bottom:2px}
.work-cap span{color:var(--accent-soft);font-size:.8rem}
.work-price{color:var(--accent-soft);font-weight:700;font-size:1rem;margin-top:6px}
/* footer */
footer{border-top:1px solid var(--line);padding:36px 0;text-align:center;color:var(--muted);font-size:.9rem}
footer .fbrand{font-family:'Playfair Display',serif;font-size:1.3rem;color:var(--text);margin-bottom:6px}
footer .fbrand em{color:var(--accent);font-style:normal}
footer .powered{margin-top:10px;font-size:.85rem}
footer .powered b{color:var(--accent)}
.accent-rule{width:64px;height:2px;background:linear-gradient(90deg,transparent,var(--accent),transparent);margin:0 auto 28px}
</style>
</head>
<body>

<nav>
  <div class="nav-in">
    <a class="brand" href="#top"><img src="%%LOGO_PATH%%" alt="JakinsCraft logo"><span>Jakins<em>Craft</em></span></a>
    <div class="nav-links">
      <a href="#products">Products</a><a href="#laser-work">Laser Work</a><a href="#crystal-3d">3D Crystal &amp; Relief</a><a href="#zodiac">Zodiac Birthday Gifts</a><a href="#music-frames">Music Frames</a><a href="#word-tiles">Word Tiles</a><a href="#baby-blocks">Baby Photo Blocks</a><a href="#quote">Get a Quote</a><a href="#bulk">Bulk Orders</a><a href="#gallery">Gallery</a>
    </div>
  </div>
</nav>

<header class="hero" id="top">
  <div class="wrap">
    <img class="logo" src="%%LOGO_PATH%%" alt="JakinsCraft logo">
    <h1>Jakins<em>Craft</em></h1>
    <p class="tag">Custom UV-printed gear from Toronto — NFC &amp; QR business pendants, printed tumblers and keychains, made to carry your brand everywhere.</p>
    <div class="cta-row">
      <a class="btn btn-accent" href="#products">Shop Products</a>
      <a class="btn btn-ghost" href="#quote">Get a Custom Quote</a>
    </div>
    <div class="badges">
      <span class="badge">Toronto, Canada</span>
      <span class="badge">Full-colour UV printing</span>
      <span class="badge">NFC + QR smart products</span>
      <span class="badge">Laser engraving &amp; cutting</span>
    </div>
  </div>
</header>

<section id="products">
  <div class="wrap">
    <div class="eyebrow">Products</div>
    <h2 class="sec">Made to order, made to last</h2>
    <p class="sub">Every piece is printed in full colour with commercial UV printing. Send your logo, pick your product, done.</p>
    <div class="accent-rule" style="margin:0 0 28px"></div>
    <div class="cards">
      <div class="card">
        <img class="machine-photo" src="%%IMG_PENDANT%%" alt="Custom NFC business logo pendant" loading="lazy">
        <h3>NFC &amp; QR <em>Business Pendant</em></h3>
        <p>Your business logo on a sleek pendant with a built-in NFC chip and QR code. One tap or scan shares your digital business card — name, number, links, everything.</p>
        <div class="price">1 / $20 &nbsp;·&nbsp; 2 / $35 &nbsp;·&nbsp; 5 / $75<small>Bulk pricing on request</small></div>
        <a class="btn-wa" href="%%WA_PENDANT%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <img class="machine-photo" src="%%IMG_PLATE_CARD%%" alt="Ontario licence plate NFC card" loading="lazy">
        <h3>Ontario Plate <em>NFC Card</em></h3>
        <p>Your insurance slip, one tap away. A custom Ontario plate card with an NFC tag sealed inside, tap it with any phone and your proof of insurance opens instantly, no app, no login.</p>
        <div class="price">$20<small>Custom plate, programmed tag included</small></div>
        <a class="btn-wa" href="%%WA_PLATE_CARD%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <img class="machine-photo" src="%%IMG_E1%%" alt="eufyMake E1 UV printer" loading="lazy">
        <h3>Custom <em>UV Printing</em></h3>
        <p>Your design UV-printed in vivid full colour — 30oz tumblers, blanks, signage and more. Crisp, durable prints that keep your brand in hand all day.</p>
        <div class="price">Custom quote<small>Tell us your design &amp; quantity</small></div>
        <a class="btn-wa" href="%%WA_TUMBLER%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <img class="machine-photo" src="%%IMG_KEYCHAIN%%" alt="Custom NFC QR keychains" loading="lazy">
        <h3>Custom QR <em>Keychain</em></h3>
        <p>Your logo, your link, your QR — on a durable keychain people actually scan. Perfect for menus, Wi-Fi codes, socials, or your business page.</p>
        <div class="price">Custom quote<small>Tell us your design &amp; quantity</small></div>
        <a class="btn-wa" href="%%WA_KEYCHAIN%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <img class="machine-photo" src="%%IMG_P1S%%" alt="Bambu Lab P1S 3D printer" loading="lazy">
        <h3>Custom <em>3D Printing</em></h3>
        <p>Printed on our Bambu Lab — custom parts, prototypes, decor, replacement bits, and one-off creations. Send a file or just describe the idea and we'll make it real.</p>
        <div class="price">Custom quote<small>Tell us your design &amp; quantity</small></div>
        <a class="btn-wa" href="%%WA_3DPRINT%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <img class="machine-photo" src="%%IMG_F2%%" alt="xTool F2 laser engraver" loading="lazy">
        <h3>Laser <em>Engraving</em></h3>
        <p>Precision engraving and cutting with our xTool X1 (55W CO2 + 20W diode galvo) and xTool F2 — crisp logos and text on wood, metal, acrylic, leather, glass, tumblers and more. Perfect for gifts, signage, and branded gear.</p>
        <div class="price">Custom quote<small>Tell us your design &amp; quantity</small></div>
        <a class="btn-wa" href="%%WA_LASER%%">Order on WhatsApp</a>
      </div>
    </div>
  </div>
</section>

%%LASER_WORK%%

%%CRYSTAL_3D%%

%%ZODIAC%%

%%MUSIC_FRAMES%%

%%WORD_TILES%%

%%BABY_BLOCKS%%

<section id="quote">
  <div class="wrap">
    <div class="eyebrow" style="text-align:center">Custom Quote</div>
    <h2 class="sec" style="text-align:center">Build your order</h2>
    <p class="sub" style="text-align:center;margin-left:auto;margin-right:auto">Fill this in and we'll open WhatsApp with your order typed out — just hit send.</p>
    <div class="panel">
      <div class="field">
        <label for="q-name">Your name</label>
        <input id="q-name" type="text" placeholder="e.g. Jane Doe" autocomplete="name">
      </div>
      <div class="row2">
        <div class="field">
          <label for="q-product">Product</label>
          <select id="q-product">
            <option>NFC &amp; QR Business Pendant</option>
            <option>Ontario Plate NFC Card</option>
            <option>Custom UV Printing</option>
            <option>Custom QR Keychain</option>
            <option>Custom 3D Printing</option>
            <option>Laser Engraving</option>
            <option>Laser Cutting (X1)</option>
            <option>Bulk / Corporate Order</option>
          </select>
        </div>
        <div class="field">
          <label for="q-qty">Quantity</label>
          <input id="q-qty" type="number" min="1" value="1">
        </div>
      </div>
      <div class="field">
        <label for="q-design">Describe your design</label>
        <textarea id="q-design" placeholder="e.g. My real-estate logo in navy and purple, QR linking to my listings page…"></textarea>
      </div>
      <a class="btn btn-accent" id="q-send" href="#" style="display:block;text-align:center">Send Order via WhatsApp</a>
      <p class="hint">No account, no checkout — your order opens right in WhatsApp.</p>
    </div>
  </div>
</section>

<section id="bulk">
  <div class="wrap">
    <div class="eyebrow">Bulk &amp; Corporate</div>
    <h2 class="sec">Put your brand in every hand</h2>
    <p class="sub">Branded pendants and keychains are walking business cards. We handle bulk runs for teams and businesses across the GTA.</p>
    <div class="accent-rule" style="margin:0 0 28px"></div>
    <div class="bulk-grid">
      <div class="bulk-card"><h3>🏠 Realtors</h3><p>Hand clients a pendant that opens your listings, contact card and reviews with one tap. memorable at every open house.</p></div>
      <div class="bulk-card"><h3>💈 Salons &amp; Barbershops</h3><p>QR keychains linking to your booking page — clients rebook in one scan, and your logo travels on their keys.</p></div>
      <div class="bulk-card"><h3>🍽️ Restaurants &amp; Cafés</h3><p>Table-ready QR pieces for menus, Wi-Fi and reviews. Branded, scannable, and easy to reprint for new locations.</p></div>
    </div>
    <div class="center"><a class="btn btn-accent" href="%%WA_BULK%%">Discuss a Bulk Order on WhatsApp</a></div>
  </div>
</section>

<section id="gallery">
  <div class="wrap">
    <div class="eyebrow">Gallery</div>
    <h2 class="sec">Fresh from the printer</h2>
    <p class="sub">Real work, fresh from the printer.</p>
    <div class="accent-rule" style="margin:0 0 28px"></div>
    <div class="gal">
      <div class="tile tile-photo"><img src="%%IMG_TREM_PAIR%%" alt="Framed painted portrait prints — pair on display, TREM Children Church" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_TREM_SUIT%%" alt="Framed painted portrait print — suit and striped tie, TREM Children Church" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_TREM_FLORAL%%" alt="Framed painted portrait print — floral top, TREM Children Church" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_HAT%%" alt="Custom canvas portrait print — man in a wide-brim hat and glasses, framed" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_GLASSES%%" alt="Custom canvas portrait print — man with glasses and beard on canvas" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_GAL_PENDANT%%" alt="Custom NFC & QR code business logo pendant" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_TUMBLER_FAITH%%" alt="Custom printed tumbler — A Man of Faith" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_HOODIE_AHEAD%%" alt="Custom printed hoodie — Ahead Art Gallery" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_CHILD%%" alt="Custom canvas portrait print — child in traditional attire" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_GELE%%" alt="Custom canvas portrait print — gele headwrap" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_PIZZA%%" alt="Custom canvas portrait print" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_BRAIDS%%" alt="Custom canvas portrait print — braided hair" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_BOY%%" alt="Custom canvas portrait print — coral beads" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_CANVAS_PAIR%%" alt="Custom canvas portrait prints" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_HOODIE_BUNNY%%" alt="Custom printed hoodie — Hip Hop bunny" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_TEE_MOMLIFE%%" alt="Custom printed t-shirt — Mom Life" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_TEE_MONKEY%%" alt="Custom printed t-shirt — DJ monkey" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_KEY_BOTB%%" alt="Custom printed keychain — BOTB Arena" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_KEY_INSTA%%" alt="Custom Instagram QR keychains" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_PENS_TREM%%" alt="Laser-engraved bamboo pens — TREM" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_TUMBLER_SUMMER%%" alt="Custom UV-printed tumbler — Summer Vibes" loading="lazy"></div>
      <div class="tile tile-photo"><img src="%%IMG_E1_PRINTING%%" alt="Tumbler being UV printed on the eufyMake E1" loading="lazy"></div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="fbrand">Jakins<em>Craft</em></div>
    <div>Custom UV-printed gear · Toronto, Canada</div>
    <div class="powered">Powered by <b>@jakinsCraft</b></div>
  </div>
</footer>

<script>
const WA_NUMBER = "%%WHATSAPP_NUMBER%%";
document.getElementById("q-send").addEventListener("click", function (e) {
  e.preventDefault();
  const name = document.getElementById("q-name").value.trim();
  const product = document.getElementById("q-product").value;
  const qty = document.getElementById("q-qty").value || "1";
  const design = document.getElementById("q-design").value.trim() || "(no description yet)";
  const msg = "Hi JakinsCraft! I'd like a quote/place an order:\n"
    + "• Name: " + (name || "(not given)") + "\n"
    + "• Product: " + product + "\n"
    + "• Quantity: " + qty + "\n"
    + "• Design: " + design;
  window.open("https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(msg), "_blank");
});
document.getElementById("q-send").addEventListener("auxclick", function (e) { e.preventDefault(); });
</script>
</body>
</html>
"""

# --- Laser Work section (xTool X1 + F2 samples) ---
# Photos are xTool's own samples of what each machine does, kept in
# assets/samples/. Each tile is (image, title, laser tag, price), or
# (image, title, laser tag, price, wide) for the two full F2 panels.
# Prices are CAD starting prices from a Nov 26, 2026 market survey
# (Toronto shops, Etsy Canada, US laser shops): set at or above the
# Toronto market midpoint, blanks run a few dollars, so margins are
# strong. Final quote depends on size and design.
X1_NOW = [
    ("assets/samples/x1-wood-dollhouse.jpg", "Wooden dollhouse", "55W CO2 · Powerful cutting", "From $85"),
    ("assets/samples/x1-wood-mountain.jpg", "Layered mountain wood art", "55W CO2 · Powerful cutting", "From $65"),
    ("assets/samples/x1-acrylic-motorcycle.jpg", "Clear acrylic motorcycle model", "55W CO2 · Clear acrylic cutting", "From $55"),
    ("assets/samples/x1-acrylic-wedding.jpg", "Olivia and James wedding sign", "55W CO2 · Cutting and engraving", "From $65"),
    ("assets/samples/x1-glass-award.jpg", "The Legacy Award glass plaque", "55W CO2 · Surface engraving", "From $55"),
    ("assets/samples/x1-mm-leather.jpg", "Leather cap patch", "CO2 / Diode", "From $12"),
    ("assets/samples/x1-mm-stone.jpg", "Slate coasters", "Diode", "From $12 each"),
    ("assets/samples/x1-mm-silicone.jpg", "Silicone phone cases", "Diode", "From $25"),
    ("assets/samples/x1-mm-denim.jpg", "Denim jeans", "CO2 / Diode", "From $30"),
    ("assets/samples/x1-mm-paper.jpg", "Paper anniversary card", "CO2 / Diode", "From $15"),
    ("assets/samples/x1-mm-rubber.jpg", "Rubber stamps", "Diode", "From $20"),
    ("assets/samples/x1-door-sign.jpg", "Wooden door sign", "xTool X1", "From $45"),
    ("assets/samples/x1-tumbler.jpg", "Personalized tumbler", "xTool X1", "From $35"),
    ("assets/samples/x1-glass-ornament.jpg", "Glass ornament", "xTool X1", "From $20"),
]
X1_ADDON = [
    ("assets/samples/x1-wood-cat.jpg", "Framed cat portrait", "5W UV · High-detail engraving", "From $75"),
    ("assets/samples/x1-wood-relief.jpg", "Wood relief carving", "5W UV · Char-free relief", "From $95"),
    ("assets/samples/x1-acrylic-anderson.jpg", "Green acrylic Anderson card", "5W UV · Fine engraving", "From $25"),
    ("assets/samples/x1-acrylic-earrings.jpg", "Acrylic earrings", "55W CO2 + 5W UV", "From $25"),
    ("assets/samples/x1-glass-wine.jpg", "Wine glass, rotary engraving", "5W UV · Fine rotary engraving", "From $30"),
    ("assets/samples/x1-glass-tajmahal.jpg", "Taj Mahal crystal block", "5W UV · Inner engraving", "From $85"),
    ("assets/samples/x1-glass-cameo.jpg", "Glass cameo pendant", "5W UV · Relief and cutting", "From $30"),
    ("assets/samples/x1-metal-sf-plaque.jpg", "San Francisco gold plaque", "60W MOPA · Metal embossing", "From $95"),
    ("assets/samples/x1-metal-zebra.jpg", "Colour zebra art", "60W MOPA · Metal colour engraving", "From $85"),
    ("assets/samples/x1-metal-tags.jpg", "Alpencore metal tags", "30W Fiber · Batch metal marking", "From $10 each"),
    ("assets/samples/x1-metal-mountain.jpg", "Oval metal mountain", "60W MOPA · Thin metal cutting", "From $65"),
    ("assets/samples/x1-mm-ceramic.jpg", "Ceramic Starry Night plate", "UV / Fiber / MOPA", "From $45"),
    ("assets/samples/x1-mm-plastic.jpg", "Plastic AirPods case", "UV / MOPA", "From $25"),
    ("assets/samples/x1-mm-pearl.jpg", "Mother-of-pearl pendant", "5W UV", "From $45"),
    ("assets/samples/x1-mm-pcb.jpg", "PCB circuit board", "UV / MOPA / Fiber", "From $40"),
]
F2_WORK = [
    ("assets/samples/f2-ir.jpg", "5W infrared: colour metal tags, tumblers, rings, knives, pendants", "5W IR · Metals and plastics", "From $10", True),
    ("assets/samples/f2-diode.jpg", "15W diode: slate, denim, wood, glass, leather, paper, acrylic", "15W Diode · Everyday materials", "From $12", True),
]

def _work_tiles(items):
    parts = []
    for it in items:
        img, title, tag, price = it[0], it[1], it[2], it[3]
        wide = " wide" if len(it) > 4 and it[4] else ""
        parts.append(
            '<div class="work-tile' + wide + '"><img src="' + img + '" alt="' + title + '" loading="lazy">'
            '<div class="work-cap"><b>' + title + '</b><span>' + tag + '</span>'
            '<div class="work-price">' + price + '</div></div></div>'
        )
    return "\n      ".join(parts)

LASER_WORK = """
<section id="laser-work">
  <div class="wrap">
    <div class="eyebrow">Laser Work</div>
    <h2 class="sec">What the X1 and F2 can make</h2>
    <p class="sub">Our new xTool X1 (55W CO2 + 20W diode galvo) joins the xTool F2 (5W infrared + 15W diode). Between them they cut and engrave wood, metal, glass, acrylic, leather, slate, denim, paper and more. The photos below are xTool's own samples of what each machine does, real JakinsCraft pieces coming soon as we make them. Prices are starting prices in Canadian dollars, the final quote depends on size and design.</p>
    <h3 class="work-group">Made with the X1's CO2 and diode lasers</h3>
    <p class="work-note">Cut and engraved with the 55W CO2 and 20W diode galvo lasers.</p>
    <div class="work-grid">
      """ + _work_tiles(X1_NOW) + """
    </div>
    <h3 class="work-group">Made with the X1's UV, MOPA and Fiber lasers</h3>
    <p class="work-note">UV for crystal and glass, MOPA and Fiber for metal colour, embossing and marking.</p>
    <div class="work-grid">
      """ + _work_tiles(X1_ADDON) + """
    </div>
    <h3 class="work-group">Made with the F2</h3>
    <p class="work-note">5W infrared for premium metals and plastics, 15W diode for wood, acrylic, leather and more, on the go or in the shop.</p>
    <div class="work-grid">
      """ + _work_tiles(F2_WORK) + """
    </div>
    <div class="center" style="margin-top:28px"><a class="btn btn-accent" href="%%WA_LASER%%">Ask About a Laser Project on WhatsApp</a></div>
  </div>
</section>
"""

# --- 3D Crystal & Relief section (Atomm AI 3D Model Generator) ---
# A photo becomes a 3D model two ways: 3D Photo mode gives a depth map
# for 2.5D relief carving (wood, acrylic, slate), 3D Modeling mode gives
# a mesh for inner engraving in crystal. Relief runs on the X1's 55W CO2
# + 20W diode galvo, inner engraving in crystal on the UV laser. Per
# Pappy Nov 26, 2026, all products are listed as available, assume he
# has the kit it takes to make them. Photos are xTool/Atomm samples of the
# technique, in assets/crystal/; tiles without a real photo yet use the
# "Photo coming soon" tile. Prices are CAD starting prices from a Nov 26,
# 2026 market survey (Etsy Canada 3D crystal and wood relief listings):
# set at or above the market midpoint. Final quote depends on size/design.
RELIEF_NOW = [
    ("assets/crystal/crystal-coming-soon.jpg", "Portrait relief plaque, wood", "2.5D relief · CO2 / Diode", "From $115"),
    ("assets/crystal/relief-pet-dog.jpg", "Pet portrait relief, wood", "2.5D relief · CO2 / Diode", "From $95"),
    ("assets/crystal/crystal-coming-soon.jpg", "Family portrait relief plaque", "2.5D relief · CO2 / Diode", "From $125"),
    ("assets/crystal/crystal-coming-soon.jpg", "Memorial relief plaque", "2.5D relief · CO2 / Diode", "From $110"),
    ("assets/crystal/relief-stone-eye.jpg", "Stone relief art plaque", "2.5D relief · CO2 / Diode", "From $85"),
    ("assets/crystal/relief-wildlife-giraffe.jpg", "Wildlife relief plaque, stone", "2.5D relief · CO2 / Diode", "From $85"),
    ("assets/crystal/relief-slate-eye.jpg", "Slate relief plaque", "2.5D relief · CO2 / Diode", "From $55"),
    ("assets/crystal/crystal-coming-soon.jpg", "Acrylic edge-lit relief panel", "2.5D relief · CO2 / Diode", "From $65"),
    ("assets/crystal/relief-animal-giraffe.jpg", "Animal portrait relief, stone", "2.5D relief · CO2 / Diode", "From $85"),
    ("assets/crystal/crystal-coming-soon.jpg", "3D house ornament, reindeer", "Laser-cut · CO2 / Diode", "From $20"),
]
CRYSTAL_UV = [
    ("assets/crystal/crystal-portrait-block.jpg", "Crystal photo block, portrait", "5W UV · Inner engraving", "From $65"),
    ("assets/crystal/crystal-wedding-block.jpg", "Couple portrait crystal block", "5W UV · Inner engraving", "From $75"),
    ("assets/crystal/crystal-coming-soon.jpg", "Crystal photo block with music code", "5W UV · Inner engraving", "From $75"),
    ("assets/crystal/crystal-jellyfish-cube.jpg", "Crystal art cube", "5W UV · Inner engraving", "From $70"),
    ("assets/crystal/crystal-coming-soon.jpg", "Crystal keychain, name pendant", "5W UV · Inner engraving", "From $25"),
    ("assets/crystal/crystal-led-family.jpg", "LED night light, portrait block", "5W UV · Inner engraving", "From $85"),
    ("assets/crystal/crystal-coming-soon.jpg", "Heart keepsake, portrait", "5W UV · Inner engraving", "From $55"),
    ("assets/crystal/crystal-pug-cube.jpg", "Pet memorial crystal cube", "5W UV · Inner engraving", "From $65"),
    ("assets/crystal/crystal-galaxy-ball.jpg", "Crystal ball, galaxy", "5W UV · Inner engraving", "From $75"),
    ("assets/crystal/crystal-eiffel-block.jpg", "Landmark crystal block", "5W UV · Inner engraving", "From $65"),
    ("assets/crystal/crystal-city-block.jpg", "Cityscape crystal block", "5W UV · Inner engraving", "From $60"),
]

CRYSTAL_3D = """
<section id="crystal-3d">
  <div class="wrap">
    <div class="eyebrow">3D Crystal &amp; Relief</div>
    <h2 class="sec">Your photo, carved in 3D</h2>
    <p class="sub">Send us a photo and AI turns it into a 3D model: a 2.5D relief carved into wood, acrylic or slate, a true 3D portrait floating inside crystal, or a laser-cut 3D ornament. Relief work runs on our X1 (55W CO2 + 20W diode galvo), crystal inner engraving on our UV laser. The photos below are xTool and Atomm samples of the technique, real JakinsCraft pieces coming soon as we make them. Prices are starting prices in Canadian dollars, the final quote depends on size and design.</p>
    <h3 class="work-group">2.5D relief, crystal inner engraving &amp; laser-cut</h3>
    <p class="work-note">Carved and cut with the 55W CO2 and 20W diode galvo lasers, 256 levels of grey for real depth on relief pieces. Crystal pieces are engraved inside clear K9 crystal with the UV laser, nothing printed on top and nothing wears off.</p>
    <div class="work-grid">
      """ + _work_tiles(RELIEF_NOW + CRYSTAL_UV) + """
    </div>
    <div class="center" style="margin-top:28px"><a class="btn btn-accent" href="%%WA_CRYSTAL%%">Ask About a 3D Keepsake on WhatsApp</a></div>
  </div>
</section>
"""

# --- Zodiac Birthday Gifts section (Atomm Zodiac Signs generator) ---
# All 12 signs as personalized birthday gifts: the recipient's sign, name
# and birth date engraved on the piece. Relief plaques run on the X1's
# 55W CO2 + 20W diode galvo, crystal inner engraving on the UV laser.
# Per Pappy Nov 26, 2026, all products are listed as available, assume
# he has the kit it takes to make them. No Atomm sample photos were
# fetchable for
# zodiac (the generator page is an interactive designer with no
# extractable images), so the 12 sign tiles are JakinsCraft-made sign
# tiles (gold glyph on the site's dark purple, sign name and dates), and
# the UV forms use the honest "Photo coming soon" tile. Prices are CAD
# starting prices from a Nov 26, 2026 market survey (Etsy Canada zodiac
# gifts: laser-cut metal wall art ~$60, engraved acrylic plaque ~$66,
# bas relief ~$40, 3D engraved crystal keepsake ~$88, constellation LED
# night light ~$41-52, zodiac necklace ~$21-43): set at or above the
# market midpoint. Final quote depends on size/design.
ZODIAC_NOW = [
    ("assets/zodiac/zodiac-aries.jpg", "Aries relief plaque, personalized", "2.5D relief · Mar 21 - Apr 19", "From $65"),
    ("assets/zodiac/zodiac-taurus.jpg", "Taurus relief plaque, personalized", "2.5D relief · Apr 20 - May 20", "From $65"),
    ("assets/zodiac/zodiac-gemini.jpg", "Gemini relief plaque, personalized", "2.5D relief · May 21 - Jun 20", "From $65"),
    ("assets/zodiac/zodiac-cancer.jpg", "Cancer relief plaque, personalized", "2.5D relief · Jun 21 - Jul 22", "From $65"),
    ("assets/zodiac/zodiac-leo.jpg", "Leo relief plaque, personalized", "2.5D relief · Jul 23 - Aug 22", "From $65"),
    ("assets/zodiac/zodiac-virgo.jpg", "Virgo relief plaque, personalized", "2.5D relief · Aug 23 - Sep 22", "From $65"),
    ("assets/zodiac/zodiac-libra.jpg", "Libra relief plaque, personalized", "2.5D relief · Sep 23 - Oct 22", "From $65"),
    ("assets/zodiac/zodiac-scorpio.jpg", "Scorpio relief plaque, personalized", "2.5D relief · Oct 23 - Nov 21", "From $65"),
    ("assets/zodiac/zodiac-sagittarius.jpg", "Sagittarius relief plaque, personalized", "2.5D relief · Nov 22 - Dec 21", "From $65"),
    ("assets/zodiac/zodiac-capricorn.jpg", "Capricorn relief plaque, personalized", "2.5D relief · Dec 22 - Jan 19", "From $65"),
    ("assets/zodiac/zodiac-aquarius.jpg", "Aquarius relief plaque, personalized", "2.5D relief · Jan 20 - Feb 18", "From $65"),
    ("assets/zodiac/zodiac-pisces.jpg", "Pisces relief plaque, personalized", "2.5D relief · Feb 19 - Mar 20", "From $65"),
]
ZODIAC_UV = [
    ("assets/crystal/crystal-coming-soon.jpg", "Zodiac crystal block, personalized", "5W UV · Inner engraving", "From $75"),
    ("assets/crystal/crystal-coming-soon.jpg", "Zodiac LED night light, crystal", "5W UV · Inner engraving", "From $85"),
    ("assets/crystal/crystal-coming-soon.jpg", "Zodiac crystal pendant", "5W UV · Inner engraving", "From $30"),
    ("assets/crystal/crystal-coming-soon.jpg", "Zodiac constellation crystal ball", "5W UV · Inner engraving", "From $75"),
]

ZODIAC = """
<section id="zodiac">
  <div class="wrap">
    <div class="eyebrow">Zodiac Birthday Gifts</div>
    <h2 class="sec">Their sign, made personal</h2>
    <p class="sub">A birthday gift with their star sign on it, personalized with their name and birth date. Pick their sign, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius or Pisces, and we engrave it as a 2.5D relief plaque in wood, acrylic or slate, or as a portrait floating inside crystal. Relief plaques run on our X1 (55W CO2 + 20W diode galvo), crystal pieces on our UV laser. The sign tiles below are our own designs, real JakinsCraft pieces coming soon as we make them. Prices are starting prices in Canadian dollars, the final quote depends on size and design.</p>
    <h3 class="work-group">Zodiac relief plaques &amp; crystal</h3>
    <p class="work-note">One plaque per sign, carved with the 55W CO2 and 20W diode galvo lasers, personalized with a name and birth date. Crystal pieces are engraved inside clear K9 crystal with the UV laser, nothing printed on top and nothing wears off.</p>
    <div class="work-grid">
      """ + _work_tiles(ZODIAC_NOW + ZODIAC_UV) + """
    </div>
    <div class="center" style="margin-top:28px"><a class="btn btn-accent" href="%%WA_ZODIAC%%">Ask About a Zodiac Gift on WhatsApp</a></div>
  </div>
</section>
"""

# --- Music Photo Frames section (Atomm Music Photo Frame generator) ---
# A personalized music-player photo frame, laser-cut in three layers: a
# front with a photo window, a spacer with a photo pocket open at the top,
# and a back with a finger notch, plus an optional stand and an applied or
# engraved heart. The buyer supplies their photo, song title, artist,
# play time and their OWN Spotify code (the tool does not create codes;
# the buyer makes one free in the Spotify app). All laser-cut on the X1's
# 55W CO2 + 20W diode galvo, available now. NOTE: the 3D Crystal &
# Relief section already has a "Crystal photo block with music code"
# in the crystal section, that is a
# different product (crystal inner engraving), do not duplicate or remove
# it. No Atomm sample photos were fetchable for this tool (the page is a
# community generator with no extractable images), so all tiles use the
# honest "Photo coming soon" tile. Prices are CAD starting prices from a
# Nov 26, 2026 market survey (Etsy Canada personalized music plaques and
# photo frames: acrylic song plaques CA$24-46, wooden-stand plaques
# CA$34-60, LED night light plaques CA$19-37): set at or above the
# market midpoint. Final quote depends on size/design.
MUSIC_NOW = [
    ("assets/crystal/crystal-coming-soon.jpg", "Music photo frame, 5x7 in", "Laser-cut · CO2 / Diode", "From $45"),
    ("assets/crystal/crystal-coming-soon.jpg", "Music photo frame, 8x10 in", "Laser-cut · CO2 / Diode", "From $55"),
    ("assets/crystal/crystal-coming-soon.jpg", "Music photo frame with display stand", "Laser-cut · CO2 / Diode", "From $55"),
    ("assets/crystal/crystal-coming-soon.jpg", "Music photo frame with engraved heart", "Laser-cut · CO2 / Diode", "From $50"),
]

MUSIC_FRAMES = """
<section id="music-frames">
  <div class="wrap">
    <div class="eyebrow">Music Photo Frames</div>
    <h2 class="sec">Your song, in a frame</h2>
    <p class="sub">Your favourite photo and your song, built into a layered laser-cut frame: a front with a photo window, a spacer with a photo pocket, and a back with a finger notch, so the photo slides in and out. We engrave the song title, artist and play time, and your scannable Spotify code, so a phone scan plays the song. You supply your own Spotify code, made free in the Spotify app, and your photo. Available now on our X1 (55W CO2 + 20W diode galvo), in wood or acrylic. Prices are starting prices in Canadian dollars, the final quote depends on size and design.</p>
    <h3 class="work-group">Available now — laser-cut music frames</h3>
    <p class="work-note">Cut and engraved with the 55W CO2 and 20W diode galvo lasers, three layers for real 3D depth.</p>
    <div class="work-grid">
      """ + _work_tiles(MUSIC_NOW) + """
    </div>
    <div class="center" style="margin-top:28px"><a class="btn btn-accent" href="%%WA_MUSIC%%">Ask About a Music Frame on WhatsApp</a></div>
  </div>
</section>
"""
# --- Family Word Tiles section (Atomm Family Word Tile Studio) ---
# Family names and meaningful words arranged into a connected crossword
# layout, matching letters intersect and share one tile. Up to 20 words,
# max 24 letters each, English A-Z only. Tile size and spacing, square or
# rounded corners, letter styles Classic Bold, Traditional Serif or
# Typewriter, Scrabble-style point numbers on or off. Laser-cut and
# engraved on the X1's 55W CO2 + 20W diode galvo (wood, plywood, MDF,
# acrylic), or UV-printed as 300 DPI PNG artwork on the eufyMake E1
# (acrylic, wood, metal and other flat substrates). Per Pappy Nov 26,
# 2026, all products are listed as available, assume he has the kit it
# takes to make them, no availability split. A backing board, frame or
# stand is extra unless the listing says it is included; the tool does
# not supply backing-board cut files, frames or stands. The one real
# photo is Atomm's own Family Word Tile Studio sample (assets/word-
# tiles/family-word-tile-studio.jpg); the rest use the honest "Photo
# coming soon" tile. Prices are CAD starting prices from a Nov 26, 2026
# market survey (Etsy Canada physical wooden family crossword /
# Scrabble tile signs: CA$25-102, wooden wall pieces CA$52-82, shadow
# box versions to CA$102): set at or above the market midpoint. Final
# quote depends on size/design.
WORD_TILES = [
    ("assets/word-tiles/family-word-tile-studio.jpg", "Family word tile wall display, small, up to 10 words", "Laser-cut · CO2 / Diode", "From $65"),
    ("assets/crystal/crystal-coming-soon.jpg", "Family word tile wall display, medium, up to 15 words", "Laser-cut · CO2 / Diode", "From $85"),
    ("assets/crystal/crystal-coming-soon.jpg", "Family word tile wall display, large, up to 20 words", "Laser-cut · CO2 / Diode", "From $115"),
    ("assets/crystal/crystal-coming-soon.jpg", "Wedding keepsake word tile set", "Laser-cut · CO2 / Diode", "From $95"),
    ("assets/crystal/crystal-coming-soon.jpg", "Tabletop word tile sign", "Laser-cut · CO2 / Diode", "From $55"),
    ("assets/crystal/crystal-coming-soon.jpg", "UV-printed word tile set, acrylic panel", "UV print · eufyMake E1", "From $75"),
]

WORD_TILES_HTML = """
<section id="word-tiles">
  <div class="wrap">
    <div class="eyebrow">Family Word Tiles</div>
    <h2 class="sec">Your family, in tiles</h2>
    <p class="sub">Your family names and the words that mean something, arranged into one connected crossword layout, where matching letters cross and share a tile. We laser-cut and engrave each tile in wood, plywood, MDF or acrylic on our X1 (55W CO2 + 20W diode galvo), or UV-print the whole layout onto an acrylic panel on our eufyMake E1. You pick the words, the tile size, the letter style, and point numbers on or off. A backing board, frame or stand is extra unless the listing says it is included. The photo below is Atomm's own sample of the design, real JakinsCraft pieces coming soon as we make them. Prices are starting prices in Canadian dollars, the final quote depends on size and design.</p>
    <h3 class="work-group">Family word tile displays</h3>
    <p class="work-note">Up to 20 words per layout, every word included, letters in Classic Bold, Traditional Serif or Typewriter, with Scrabble-style point numbers on or off.</p>
    <div class="work-grid">
      """ + _work_tiles(WORD_TILES) + """
    </div>
    <div class="center" style="margin-top:28px"><a class="btn btn-accent" href="%%WA_WORDTILES%%">Ask About a Word Tile Display on WhatsApp</a></div>
  </div>
</section>
"""
# --- Baby Photo Blocks section (Atomm photo block generator) ---
# A laser-cut baby photo block that stands on a shelf, previewed in 3D
# before making it. Baby's photo, name and birth details (date, time,
# weight, length, hospital) on the block, 7 shapes: rectangle, arch,
# oval, round, scalloped, cloud or heart. The block has a tab or
# notches for its stand; the stand is a slot base with an engraved
# line in front or two slot-on feet. Optional raised name layer cut
# from gold, silver or rose gold mirror acrylic and glued on the
# front. Two finishes: UV print, full color, mirrored on the back of
# clear acrylic with a white layer behind it, or printed straight
# onto white acrylic or wood, on the eufyMake E1; or laser engrave,
# the photo turned to greys and engraved into birch, walnut, black
# or clear acrylic on the X1's 55W CO2 + 20W diode galvo, no printer
# needed. 12 templates, 3 layouts (name card, details panel, text
# over the photo), 8 color themes, 8 artworks (bunting, balloons,
# rainbow, moon and stars, leafy sprigs), 12 fonts. Per Pappy Nov 26,
# 2026, all products are listed as available, assume he has the kit
# it takes to make them, no availability split. The one real photo is
# Atomm's own photo-block sample (assets/baby-blocks/baby-photo-
# block-sample.jpg); the rest use the honest "Photo coming soon"
# tile. Prices are CAD starting prices from a Nov 26, 2026 market
# survey (Etsy Canada personalized baby birth blocks CA$26-56,
# birth announcement plaques CA$32-72, framed stats plaques to
# CA$72): set at or above the market midpoint. Final quote depends
# on size/design. Buyer supplies the baby photo and birth details.
BABY_BLOCKS = [
    ("assets/baby-blocks/baby-photo-block-sample.jpg", "Baby photo block, UV-printed, clear acrylic", "UV print · eufyMake E1", "From $65"),
    ("assets/crystal/crystal-coming-soon.jpg", "Baby photo block, laser-engraved, wood or acrylic", "Laser engrave · CO2 / Diode", "From $55"),
    ("assets/crystal/crystal-coming-soon.jpg", "Baby photo block with raised mirror name", "Mirror acrylic name · Laser-cut", "From $75"),
    ("assets/crystal/crystal-coming-soon.jpg", "Baby photo block set, twins or siblings, two blocks", "UV print or laser engrave", "From $95"),
]

BABY_BLOCKS_HTML = """
<section id="baby-blocks">
  <div class="wrap">
    <div class="eyebrow">Baby Photo Blocks</div>
    <h2 class="sec">Welcome, little one</h2>
    <p class="sub">Your baby's photo, name and birth details on a block that stands on the shelf, in one of 7 shapes: rectangle, arch, oval, round, scalloped, cloud or heart. We UV-print it in full color on clear acrylic on our eufyMake E1, or laser-engrave it in greys into birch, walnut, black or clear acrylic on our X1 (55W CO2 + 20W diode galvo). Every block comes with its stand, a slot base with an engraved line in front or two slot-on feet, and an optional raised name in gold, silver or rose gold mirror acrylic. You supply the photo and the birth details, name, date, time, weight, length and hospital, and pick from 12 templates, 3 layouts, 8 color themes, 8 artworks and 12 fonts. The photo below is Atomm's own sample of the design, real JakinsCraft pieces coming soon as we make them. Prices are starting prices in Canadian dollars, the final quote depends on size and design.</p>
    <h3 class="work-group">Baby photo blocks</h3>
    <p class="work-note">Stand included with every block. Raised name layer in mirror acrylic, 2-3 mm thick.</p>
    <div class="work-grid">
      """ + _work_tiles(BABY_BLOCKS) + """
    </div>
    <div class="center" style="margin-top:28px"><a class="btn btn-accent" href="%%WA_BABYBLOCKS%%">Ask About a Baby Photo Block on WhatsApp</a></div>
  </div>
</section>
"""
out = (HTML
       .replace("%%LOGO_PATH%%", LOGO_PATH)
       .replace("%%IMG_E1%%", IMG_E1)
       .replace("%%IMG_P1S%%", IMG_P1S)
       .replace("%%IMG_F2%%", IMG_F2)
       .replace("%%IMG_PENDANT%%", IMG_PENDANT)
       .replace("%%IMG_KEYCHAIN%%", IMG_KEYCHAIN)
       .replace("%%IMG_PLATE_CARD%%", IMG_PLATE_CARD)
       .replace("%%IMG_TUMBLER_FAITH%%", IMG_TUMBLER_FAITH)
       .replace("%%IMG_HOODIE_AHEAD%%", IMG_HOODIE_AHEAD)
       .replace("%%IMG_CANVAS_CHILD%%", IMG_CANVAS_CHILD)
       .replace("%%IMG_CANVAS_GELE%%", IMG_CANVAS_GELE)
       .replace("%%IMG_CANVAS_PIZZA%%", IMG_CANVAS_PIZZA)
       .replace("%%IMG_CANVAS_BRAIDS%%", IMG_CANVAS_BRAIDS)
       .replace("%%IMG_CANVAS_BOY%%", IMG_CANVAS_BOY)
       .replace("%%IMG_CANVAS_PAIR%%", IMG_CANVAS_PAIR)
       .replace("%%IMG_HOODIE_BUNNY%%", IMG_HOODIE_BUNNY)
       .replace("%%IMG_TEE_MOMLIFE%%", IMG_TEE_MOMLIFE)
       .replace("%%IMG_TEE_MONKEY%%", IMG_TEE_MONKEY)
       .replace("%%IMG_KEY_BOTB%%", IMG_KEY_BOTB)
       .replace("%%IMG_KEY_INSTA%%", IMG_KEY_INSTA)
       .replace("%%IMG_PENS_TREM%%", IMG_PENS_TREM)
       .replace("%%IMG_TUMBLER_SUMMER%%", IMG_TUMBLER_SUMMER)
       .replace("%%IMG_E1_PRINTING%%", IMG_E1_PRINTING)
       .replace("%%IMG_GAL_PENDANT%%", IMG_GAL_PENDANT)
       .replace("%%IMG_CANVAS_HAT%%", IMG_CANVAS_HAT)
       .replace("%%IMG_CANVAS_GLASSES%%", IMG_CANVAS_GLASSES)
       .replace("%%IMG_TREM_PAIR%%", IMG_TREM_PAIR)
       .replace("%%IMG_TREM_SUIT%%", IMG_TREM_SUIT)
       .replace("%%IMG_TREM_FLORAL%%", IMG_TREM_FLORAL)
       .replace("%%WHATSAPP_NUMBER%%", WHATSAPP_NUMBER)
       .replace("%%WA_PENDANT%%", orders["pendant"])
       .replace("%%WA_TUMBLER%%", orders["tumbler"])
       .replace("%%WA_KEYCHAIN%%", orders["keychain"])
       .replace("%%WA_PLATE_CARD%%", orders["plate_card"])
       .replace("%%WA_3DPRINT%%", orders["3dprint"])
       .replace("%%LASER_WORK%%", LASER_WORK)
       .replace("%%CRYSTAL_3D%%", CRYSTAL_3D)
       .replace("%%ZODIAC%%", ZODIAC)
       .replace("%%MUSIC_FRAMES%%", MUSIC_FRAMES)
       .replace("%%WORD_TILES%%", WORD_TILES_HTML)
       .replace("%%BABY_BLOCKS%%", BABY_BLOCKS_HTML)
       .replace("%%WA_LASER%%", orders["laser"])
       .replace("%%WA_CRYSTAL%%", orders["crystal"])
       .replace("%%WA_ZODIAC%%", orders["zodiac"])
       .replace("%%WA_MUSIC%%", orders["music"])
       .replace("%%WA_WORDTILES%%", orders["wordtiles"])
       .replace("%%WA_BABYBLOCKS%%", orders["babyblocks"])
       .replace("%%WA_BULK%%", orders["bulk"]))

OUT.write_text(out, encoding="utf-8")
print(f"wrote {OUT} ({len(out)} bytes)")
