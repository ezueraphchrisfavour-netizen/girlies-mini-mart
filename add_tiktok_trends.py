from pathlib import Path
from urllib.parse import quote

p = Path("index.html")

if not p.exists():
    raise SystemExit("index.html not found. Check your website folder.")

html = p.read_text(encoding="utf-8")

if "GMM-TIKTOK-TRENDS" in html:
    print("TikTok Trends collection is already installed.")
    raise SystemExit

products = [
    ("Blue Baggy Jeans", "Jeans", "₦22,000", "photo-1542272604-787c3835535d"),
    ("Black Baggy Jeans", "Jeans", "₦23,000", "photo-1541099649105-f69ad21f3246"),
    ("Grey Wide-Leg Jeans", "Jeans", "₦21,000", "photo-1548883354-94bcfe321cbb"),
    ("Ladies Cargo Baggy Jeans", "Jeans", "₦25,000", "photo-1551488831-00ddcb6c6bd3"),
    ("Oversized Streetwear Style", "Fashion", "₦18,000", "photo-1529139574466-a303027c1d8b"),
    ("Large Handle Water Tumbler", "Water Bottles", "₦15,000", "photo-1602143407151-7111542de6e8"),
    ("Cute Straw Water Bottle", "Water Bottles", "₦8,000", "photo-1608270586620-248524c67de9"),
    ("40oz Travel Tumbler", "Water Bottles", "₦19,000", "photo-1577937927133-66ef06acdf18"),
    ("Insulated Stainless Steel Flask", "Water Bottles", "₦18,000", "photo-1602143407151-7111542de6e8"),
    ("Large Capacity Water Cup", "Water Bottles", "₦10,000", "photo-1608270586620-248524c67de9"),
]

cards = []

for name, category, price, photo in products:
    image = f"https://images.unsplash.com/{photo}?auto=format&fit=crop&w=800&q=85"
    message = (
        f"Hello Girlies Mini Mart! I am interested in {name}. "
        f"I saw the approximate reference price of {price}. "
        "Is it available? Can we negotiate?"
    )
    whatsapp = "https://wa.me/2348169719745?text=" + quote(message)

    cards.append(f"""
      <article class="gmm-trend-card">
        <img src="{image}" alt="{name}" loading="lazy">
        <div class="gmm-trend-info">
          <span>{category}</span>
          <h3>{name}</h3>
          <p>Approx. {price}</p>
          <a href="{whatsapp}" target="_blank" rel="noopener">
            Negotiate on WhatsApp
          </a>
        </div>
      </article>
    """)

section = """
<!-- GMM-TIKTOK-TRENDS -->
<style>
#gmm-tiktok-trends {
  padding: 55px 5%;
  background: #fff0f7;
}
#gmm-tiktok-trends .gmm-trend-heading {
  text-align: center;
  margin-bottom: 30px;
}
#gmm-tiktok-trends h2 {
  color: #c02670;
  font-size: clamp(25px, 4vw, 37px);
}
#gmm-tiktok-trends .gmm-trend-heading p {
  color: #715665;
  line-height: 1.7;
}
.gmm-trend-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 19px;
  max-width: 1200px;
  margin: auto;
}
.gmm-trend-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 5px 18px #8c245018;
  transition: transform .25s ease;
}
.gmm-trend-card:hover {
  transform: translateY(-5px);
}
.gmm-trend-card img {
  display: block;
  width: 100%;
  height: 220px;
  object-fit: cover;
}
.gmm-trend-info {
  padding: 15px;
}
.gmm-trend-info span {
  color: #c02670;
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
}
.gmm-trend-info h3 {
  color: #292129;
  font-size: 16px;
}
.gmm-trend-info p {
  color: #bd246b;
  font-size: 17px;
  font-weight: bold;
}
.gmm-trend-info a {
  display: block;
  background: #25d366;
  color: white;
  text-align: center;
  padding: 11px 7px;
  border-radius: 9px;
  text-decoration: none;
  font-weight: bold;
  font-size: 13px;
}
.gmm-trend-note {
  max-width: 850px;
  margin: 25px auto 0;
  padding: 15px;
  border-radius: 12px;
  background: white;
  color: #715665;
  text-align: center;
  line-height: 1.7;
  font-size: 13px;
}
@media(max-width:480px) {
  #gmm-tiktok-trends { padding: 38px 4%; }
  .gmm-trend-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
  }
  .gmm-trend-card img { height: 165px; }
  .gmm-trend-info { padding: 11px; }
  .gmm-trend-info h3 { font-size: 14px; }
}
</style>

<section id="gmm-tiktok-trends">
  <div class="gmm-trend-heading">
    <h2>🔥 TikTok Trending Collection</h2>
    <p>Baggy jeans, cute tumblers and trendy everyday essentials!</p>
  </div>
  <div class="gmm-trend-grid">
""" + "\n".join(cards) + """
  </div>
  <div class="gmm-trend-note">
    <strong>Price information:</strong> Prices are approximate Nigerian
    market-reference estimates, not confirmed store prices. Photos are
    illustrative examples and may not show the exact item supplied.
    Confirm stock, colour, size and final price with the seller on WhatsApp.
  </div>
</section>
"""

if "</body>" not in html:
    raise SystemExit("Could not find </body> in index.html.")

html = html.replace("</body>", section + "\n</body>", 1)
p.write_text(html, encoding="utf-8")

print("SUCCESS! Added 10 TikTok trend product cards.")
print("Original products and existing catalogue were preserved.")
