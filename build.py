#!/usr/bin/env python3
"""Builds the JakinsCraft single-page site -> index.html.

Swap these two values and re-run to update the whole site:
"""
WHATSAPP_NUMBER = "14165550000"   # PLACEHOLDER - Pappy's real WhatsApp number goes here (digits only, with country code)
LOGO_PATH = "assets/logo.png"     # drop the real logo file here later; no code changes needed
IMG_E1 = "assets/machine-e1.jpg"    # eufyMake E1 UV printer -> UV printing / tumbler card
IMG_P1S = "assets/machine-p1s.jpg"  # Bambu Lab P1S -> Custom 3D Printing card
IMG_F2 = "assets/machine-f2.jpg"    # xTool F2 laser engraver -> Laser Engraving card

import pathlib, urllib.parse

OUT = pathlib.Path(__file__).parent / "index.html"

def wa(text: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text=" + urllib.parse.quote(text)

orders = {
    "pendant": wa("Hi JakinsCraft! I'd like to order a Custom NFC & QR Code Business Logo Pendant. (1/$20, 2/$35, 5/$75)"),
    "tumbler": wa("Hi JakinsCraft! I'd like to order a custom-printed 30oz tumbler."),
    "keychain": wa("Hi JakinsCraft! I'd like to order a custom QR keychain."),
    "3dprint": wa("Hi JakinsCraft! I'm interested in custom 3D printing. Here's what I need:"),
    "laser": wa("Hi JakinsCraft! I'm interested in laser engraving. Here's what I need:"),
    "bulk": wa("Hi JakinsCraft! I'm interested in a bulk / corporate order. Let's talk."),
    "quote": None,  # built live in JS
}

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>JakinsCraft — Custom UV-Printed Gear | Toronto</title>
<meta name="description" content="JakinsCraft: custom NFC & QR business logo pendants, UV-printed 30oz tumblers and QR keychains. Designed in Toronto.">
<link rel="icon" href="%%LOGO_PATH%%">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#0c0c0e; --panel:#141417; --panel2:#1a1a1e;
  --gold:#d4af37; --gold-soft:#e8c96a; --gold-dim:rgba(212,175,55,.16);
  --text:#f5f1e8; --muted:#a9a49a; --line:rgba(212,175,55,.22);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased}
h1,h2,h3,.serif{font-family:'Playfair Display',Georgia,serif}
a{color:inherit}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
section{padding:64px 0}
.eyebrow{color:var(--gold);text-transform:uppercase;letter-spacing:.22em;font-size:.75rem;font-weight:600;margin-bottom:12px}
h2.sec{font-size:clamp(1.7rem,5vw,2.4rem);margin-bottom:8px}
.sub{color:var(--muted);max-width:640px;margin-bottom:32px}
/* nav */
nav{position:sticky;top:0;z-index:50;background:rgba(12,12,14,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;justify-content:space-between;padding:12px 20px;max-width:1080px;margin:0 auto}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:700}
.brand img{width:38px;height:38px;border-radius:10px}
.brand span{font-family:'Playfair Display',serif;font-size:1.25rem;letter-spacing:.02em}
.brand span em{color:var(--gold);font-style:normal}
.nav-links{display:flex;gap:18px;font-size:.9rem}
.nav-links a{text-decoration:none;color:var(--muted)}
.nav-links a:hover{color:var(--gold)}
@media(max-width:640px){.nav-links{display:none}}
/* hero */
.hero{position:relative;text-align:center;padding:96px 0 80px;overflow:hidden}
.hero::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 70% 55% at 50% 30%,rgba(212,175,55,.14),transparent 70%);pointer-events:none}
.hero img.logo{width:120px;height:120px;border-radius:28px;box-shadow:0 12px 40px rgba(212,175,55,.25);margin-bottom:24px;position:relative}
.hero h1{font-size:clamp(2.6rem,9vw,4.5rem);line-height:1.05;letter-spacing:.01em;position:relative}
.hero h1 em{color:var(--gold);font-style:normal}
.tag{color:var(--muted);font-size:clamp(1rem,3.5vw,1.2rem);max-width:600px;margin:18px auto 32px;position:relative}
.cta-row{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;position:relative}
.btn{display:inline-block;padding:14px 30px;border-radius:999px;font-weight:600;text-decoration:none;font-size:1rem;transition:transform .15s ease,box-shadow .15s ease;border:1px solid transparent}
.btn:active{transform:scale(.97)}
.btn-gold{background:linear-gradient(135deg,var(--gold-soft),var(--gold));color:#141414;box-shadow:0 8px 28px rgba(212,175,55,.35)}
.btn-ghost{border-color:var(--line);color:var(--text);background:rgba(255,255,255,.02)}
.btn-ghost:hover{border-color:var(--gold)}
.badges{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:36px;position:relative}
.badge{font-size:.8rem;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:6px 14px;background:rgba(212,175,55,.05)}
/* products */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}
.card{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:20px;padding:28px;display:flex;flex-direction:column;transition:transform .18s ease,box-shadow .18s ease}
.card:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(0,0,0,.5),0 0 0 1px rgba(212,175,55,.35)}
.card .icon{font-size:2.2rem;margin-bottom:14px}
.card .machine-photo{display:block;width:calc(100% + 56px);height:190px;object-fit:cover;margin:-28px -28px 18px;border-radius:20px 20px 0 0;border-bottom:1px solid var(--line);background:#0e0e10}
.card h3{font-size:1.45rem;margin-bottom:10px}
.card h3 em{color:var(--gold);font-style:normal}
.card p{color:var(--muted);font-size:.95rem;flex:1;margin-bottom:18px}
.price{font-weight:700;color:var(--gold-soft);margin-bottom:18px;font-size:1.02rem}
.price small{display:block;color:var(--muted);font-weight:400;font-size:.85rem;margin-top:2px}
.btn-wa{display:block;text-align:center;background:#1f2c24;border:1px solid #2f7d4f;color:#7bf0a4;padding:13px;border-radius:14px;font-weight:600;text-decoration:none;font-size:.95rem}
.btn-wa:hover{background:#243829}
/* quote */
#quote .panel{background:linear-gradient(180deg,var(--panel2),var(--panel));border:1px solid var(--line);border-radius:24px;padding:32px;max-width:640px;margin:0 auto}
.field{margin-bottom:18px}
.field label{display:block;font-size:.85rem;font-weight:600;color:var(--gold-soft);margin-bottom:8px;letter-spacing:.04em}
.field input,.field select,.field textarea{width:100%;background:#0e0e10;border:1px solid var(--line);border-radius:12px;color:var(--text);padding:13px 14px;font-size:1rem;font-family:inherit}
.field input:focus,.field select:focus,.field textarea:focus{outline:none;border-color:var(--gold);box-shadow:0 0 0 3px rgba(212,175,55,.15)}
.field textarea{min-height:110px;resize:vertical}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:520px){.row2{grid-template-columns:1fr}}
.hint{font-size:.82rem;color:var(--muted);margin-top:14px;text-align:center}
/* bulk */
.bulk-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:20px;margin-bottom:32px}
.bulk-card{background:rgba(212,175,55,.05);border:1px solid var(--line);border-radius:18px;padding:24px}
.bulk-card h3{font-size:1.2rem;margin-bottom:8px;color:var(--gold-soft)}
.bulk-card p{color:var(--muted);font-size:.93rem}
.center{text-align:center}
/* gallery */
.gal{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px}
.tile{aspect-ratio:1/1;border-radius:18px;border:1px dashed rgba(212,175,55,.45);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:var(--muted);font-size:.85rem;text-align:center;padding:16px;background:rgba(255,255,255,.015)}
.tile .t-icon{font-size:1.8rem;opacity:.7}
.tile b{color:var(--gold-soft);font-weight:600}
/* footer */
footer{border-top:1px solid var(--line);padding:36px 0;text-align:center;color:var(--muted);font-size:.9rem}
footer .fbrand{font-family:'Playfair Display',serif;font-size:1.3rem;color:var(--text);margin-bottom:6px}
footer .fbrand em{color:var(--gold);font-style:normal}
footer .powered{margin-top:10px;font-size:.85rem}
footer .powered b{color:var(--gold)}
.gold-rule{width:64px;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:0 auto 28px}
</style>
</head>
<body>

<nav>
  <div class="nav-in">
    <a class="brand" href="#top"><img src="%%LOGO_PATH%%" alt="JakinsCraft logo"><span>Jakins<em>Craft</em></span></a>
    <div class="nav-links">
      <a href="#products">Products</a><a href="#quote">Get a Quote</a><a href="#bulk">Bulk Orders</a><a href="#gallery">Gallery</a>
    </div>
  </div>
</nav>

<header class="hero" id="top">
  <div class="wrap">
    <img class="logo" src="%%LOGO_PATH%%" alt="JakinsCraft logo">
    <h1>Jakins<em>Craft</em></h1>
    <p class="tag">Custom UV-printed gear from Toronto — NFC &amp; QR business pendants, printed tumblers and keychains, made to carry your brand everywhere.</p>
    <div class="cta-row">
      <a class="btn btn-gold" href="#products">Shop Products</a>
      <a class="btn btn-ghost" href="#quote">Get a Custom Quote</a>
    </div>
    <div class="badges">
      <span class="badge">Toronto, Canada</span>
      <span class="badge">Full-colour UV printing</span>
      <span class="badge">NFC + QR smart products</span>
    </div>
  </div>
</header>

<section id="products">
  <div class="wrap">
    <div class="eyebrow">Products</div>
    <h2 class="sec">Made to order, made to last</h2>
    <p class="sub">Every piece is printed in full colour with commercial UV printing. Send your logo, pick your product, done.</p>
    <div class="gold-rule" style="margin:0 0 28px"></div>
    <div class="cards">
      <div class="card">
        <div class="icon">📿</div>
        <h3>NFC &amp; QR <em>Business Pendant</em></h3>
        <p>Your business logo on a sleek pendant with a built-in NFC chip and QR code. One tap or scan shares your digital business card — name, number, links, everything.</p>
        <div class="price">1 / $20 &nbsp;·&nbsp; 2 / $35 &nbsp;·&nbsp; 5 / $75<small>Bulk pricing on request</small></div>
        <a class="btn-wa" href="%%WA_PENDANT%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <img class="machine-photo" src="%%IMG_E1%%" alt="eufyMake E1 UV printer" loading="lazy">
        <h3>Custom 30oz <em>Tumbler</em></h3>
        <p>Your design wrapped around a 30oz insulated tumbler, UV-printed in vivid full colour. Keeps drinks hot or cold for hours — and keeps your brand in hand all day.</p>
        <div class="price">Custom quote<small>Tell us your design &amp; quantity</small></div>
        <a class="btn-wa" href="%%WA_TUMBLER%%">Order on WhatsApp</a>
      </div>
      <div class="card">
        <div class="icon">🔑</div>
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
        <p>Precision engraving with our xTool F2 — crisp logos and text on wood, metal, acrylic, leather, tumblers and more. Perfect for gifts, signage, and branded gear.</p>
        <div class="price">Custom quote<small>Tell us your design &amp; quantity</small></div>
        <a class="btn-wa" href="%%WA_LASER%%">Order on WhatsApp</a>
      </div>
    </div>
  </div>
</section>

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
            <option>Custom 30oz Tumbler</option>
            <option>Custom QR Keychain</option>
            <option>Custom 3D Printing</option>
            <option>Laser Engraving</option>
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
        <textarea id="q-design" placeholder="e.g. My real-estate logo in navy and gold, QR linking to my listings page…"></textarea>
      </div>
      <a class="btn btn-gold" id="q-send" href="#" style="display:block;text-align:center">Send Order via WhatsApp</a>
      <p class="hint">No account, no checkout — your order opens right in WhatsApp.</p>
    </div>
  </div>
</section>

<section id="bulk">
  <div class="wrap">
    <div class="eyebrow">Bulk &amp; Corporate</div>
    <h2 class="sec">Put your brand in every hand</h2>
    <p class="sub">Branded pendants and keychains are walking business cards. We handle bulk runs for teams and businesses across the GTA.</p>
    <div class="gold-rule" style="margin:0 0 28px"></div>
    <div class="bulk-grid">
      <div class="bulk-card"><h3>🏠 Realtors</h3><p>Hand clients a pendant that opens your listings, contact card and reviews with one tap. memorable at every open house.</p></div>
      <div class="bulk-card"><h3>💈 Salons &amp; Barbershops</h3><p>QR keychains linking to your booking page — clients rebook in one scan, and your logo travels on their keys.</p></div>
      <div class="bulk-card"><h3>🍽️ Restaurants &amp; Cafés</h3><p>Table-ready QR pieces for menus, Wi-Fi and reviews. Branded, scannable, and easy to reprint for new locations.</p></div>
    </div>
    <div class="center"><a class="btn btn-gold" href="%%WA_BULK%%">Discuss a Bulk Order on WhatsApp</a></div>
  </div>
</section>

<section id="gallery">
  <div class="wrap">
    <div class="eyebrow">Gallery</div>
    <h2 class="sec">Fresh from the printer</h2>
    <p class="sub">Real customer pieces landing here soon.</p>
    <div class="gold-rule" style="margin:0 0 28px"></div>
    <div class="gal">
      <div class="tile"><span class="t-icon">📿</span><b>Pendant</b><span>Your design here</span></div>
      <div class="tile"><span class="t-icon">🥤</span><b>Tumbler</b><span>Your design here</span></div>
      <div class="tile"><span class="t-icon">🔑</span><b>Keychain</b><span>Your design here</span></div>
      <div class="tile"><span class="t-icon">📿</span><b>Pendant</b><span>Your design here</span></div>
      <div class="tile"><span class="t-icon">🥤</span><b>Tumbler</b><span>Your design here</span></div>
      <div class="tile"><span class="t-icon">🔑</span><b>Keychain</b><span>Your design here</span></div>
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

out = (HTML
       .replace("%%LOGO_PATH%%", LOGO_PATH)
       .replace("%%IMG_E1%%", IMG_E1)
       .replace("%%IMG_P1S%%", IMG_P1S)
       .replace("%%IMG_F2%%", IMG_F2)
       .replace("%%WHATSAPP_NUMBER%%", WHATSAPP_NUMBER)
       .replace("%%WA_PENDANT%%", orders["pendant"])
       .replace("%%WA_TUMBLER%%", orders["tumbler"])
       .replace("%%WA_KEYCHAIN%%", orders["keychain"])
       .replace("%%WA_3DPRINT%%", orders["3dprint"])
       .replace("%%WA_LASER%%", orders["laser"])
       .replace("%%WA_BULK%%", orders["bulk"]))

OUT.write_text(out, encoding="utf-8")
print(f"wrote {OUT} ({len(out)} bytes)")
