from pathlib import Path

file = Path("index.html")

if not file.exists():
    raise SystemExit("ERROR: index.html not found. Enter your website folder first.")

html = file.read_text(encoding="utf-8")

if "GMM-EXPANDED-CATALOGUE" in html:
    print("The expanded catalogue is already installed.")
    raise SystemExit

products = [
    ("Floral Summer Dress", "Clothes", "₦18,000", "photo-1496747611176-843222e1e57c"),
    ("Ladies Casual Top", "Clothes", "₦8,000", "photo-1551163943-3f6a855d1153"),
    ("Women's Fashion Outfit", "Clothes", "₦15,000", "photo-1483985988355-763728e1935b"),
    ("Elegant Ladies Dress", "Clothes", "₦22,000", "photo-1539109136881-3be0616acf4b"),
    ("Ladies Two-Piece Outfit", "Clothes", "₦20,000", "photo-1529139574466-a303027c1d8b"),
    ("Fashion Skirt", "Clothes", "₦12,000", "photo-1583496661160-fb5886a0aaaa"),
    ("Classic Handbag", "Bags", "₦15,000", "photo-1548036328-c9fa89d128fa"),
    ("Ladies Shoulder Bag", "Bags", "₦18,000", "photo-1584917865442-de89df76afd3"),
    ("Mini Fashion Bag", "Bags", "₦12,000", "photo-1590874103328-eac38a683ce7"),
    ("Elegant Ladies Heels", "Shoes", "₦20,000", "photo-1543163521-1bf539c55dd2"),
    ("Ladies Casual Sneakers", "Shoes", "₦18,000", "photo-1542291026-7eec264c27ff"),
    ("Ladies Fashion Flats", "Shoes", "₦10,000", "photo-1560343090-f0409e92791a"),
    ("Stylish Women's Sandals", "Shoes", "₦12,000", "photo-1562273138-f46be4ebdf33"),
    ("Ladies Fashion Accessories", "Accessories", "₦5,000", "photo-1611652022419-a9419f74343d"),
    ("Fashion Sunglasses", "Accessories", "₦4,000", "photo-1511499767150-a48a237f0083"),
]

cards = []
for name, category, price, photo in products:
    image = f"https://images.unsplash.com/{photo}?auto=format&fit=crop&w=800&q=85"
    message = f"Hello Girlies Mini Mart! I am interested in {name}. I saw the approximate reference price of {price}. Can we negotiate the price? Please confirm availability."
    from urllib.parse import quote
    link = "https://wa.me/2348169719745?text=" + quote(message)

    cards.append(f"""
      <article class="gmm-extra-card">
        <img src="{image}" alt="{name}" loading="lazy">
        <div class="gmm-extra-info">
          <span class="gmm-extra-category">{category}</span>
          <h3>{name}</h3>
          <p class="gmm-extra-price">Approx. {price}</p>
          <a href="{link}" target="_blank" rel="noopener">Negotiate on WhatsApp</a>
        </div>
      </article>
    """)

section = """
<!-- GMM-EXPANDED-CATALOGUE -->
<style>
#gmm-expanded-catalogue {
  padding: 55px 5%;
  background: #fff7fb;
  font-family: inherit;
}
#gmm-expanded-catalogue .gmm-extra-heading {
  text-align: center;
  margin-bottom: 28px;
}
#gmm-expanded-catalogue .gmm-extra-heading h2 {
  color: #c02670;
  font-size: clamp(25px, 4vw, 38px);
  margin-bottom: 10px;
}
#gmm-expanded-catalogue .gmm-extra-heading p {
  color: #65515c;
  line-height: 1.7;
}
#gmm-expanded-catalogue .gmm-extra-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 20px;
  max-width: 1200px;
  margin: auto;
}
.gmm-extra-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 5px 20px #6b234014;
  transition: transform .25s ease, box-shadow .25s ease;
}
.gmm-extra-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px #6b234025;
}
.gmm-extra-card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  display: block;
}
.gmm-extra-info { padding: 15px; }
.gmm-extra-category {
  color: #c02670;
  font-size: 12px;
  font-weight: bold;
  text-transform: uppercase;
}
.gmm-extra-info h3 {
  font-size: 16px;
  margin: 8px 0;
  color: #292129;
}
.gmm-extra-price {
  color: #bd246b;
  font-size: 17px;
  font-weight: bold;
}
.gmm-extra-info a {
  display: block;
  background: #25d366;
  color: #fff;
  text-align: center;
  padding: 11px 8px;
  border-radius: 9px;
  text-decoration: none;
  font-weight: bold;
  margin-top: 12px;
}
.gmm-extra-info a:hover { background: #1eae55; }
.gmm-price-note {
  max-width: 850px;
  margin: 28px auto 0;
  padding: 15px;
  border: 1px solid #f2c5dc;
  border-radius: 12px;
  color: #654557;
  background: white;
  text-align: center;
  line-height: 1.7;
  font-size: 13px;
}
@media(max-width:480px) {
  #gmm-expanded-catalogue { padding: 38px 4%; }
  #gmm-expanded-catalogue .gmm-extra-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 12px;
  }
  .gmm-extra-card img { height: 165px; }
  .gmm-extra-info { padding: 11px; }
  .gmm-extra-info h3 { font-size: 14px; }
}
</style>

<section id="gmm-expanded-catalogue">
  <div class="gmm-extra-heading">
    <h2>More Styles, More Choices 🎀</h2>
    <p>Explore more fashion inspiration at Girlies Mini Mart!</p>
  </div>
  <div class="gmm-extra-grid">
""" + "\n".join(cards) + """
  </div>
  <div class="gmm-price-note">
    <strong>PLEASE NOTE:</strong> These additional products are style inspiration
    with approximate market-reference prices. Prices may vary by quality,
    brand, size and seller. Availability is not guaranteed. Contact our seller
    on WhatsApp to confirm availability and negotiate your price.
  </div>
</section>
"""

if "</body>" not in html:
    raise SystemExit("ERROR: Could not find </body> in index.html.")

html = html.replace("</body>", section + "\n</body>", 1)
file.write_text(html, encoding="utf-8")
print("SUCCESS! Added 15 extra catalogue styles.")
print("Original products were left unchanged.")
print("WhatsApp negotiation buttons are included.")
