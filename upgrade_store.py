from pathlib import Path

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found. Check your website folder.")

html = p.read_text(encoding="utf-8")

if "GMM-PRO-UPGRADE" in html:
    print("This upgrade is already installed.")
    raise SystemExit

upgrade = r"""
<!-- GMM-PRO-UPGRADE -->
<style>
#gmm-special-offer {
  margin: 35px auto;
  padding: 30px 18px;
  max-width: 1100px;
  border-radius: 20px;
  text-align: center;
  color: white;
  background: linear-gradient(120deg,#c02670,#f18ab8,#a91d61);
}
#gmm-special-offer h2 {font-size:27px;margin:0 0 10px}
#gmm-special-offer p {line-height:1.7;margin:0}
#gmm-reviews {
  padding:55px 5%;
  background:#fff7fb;
  text-align:center;
}
#gmm-reviews h2 {color:#c02670;font-size:30px}
.gmm-review-grid {
  display:grid;
  grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
  gap:18px;
  max-width:1000px;
  margin:25px auto;
}
.gmm-review {
  background:white;
  border:1px solid #f3d4e3;
  border-radius:15px;
  padding:22px;
  text-align:left;
  box-shadow:0 5px 18px #a91d6110;
}
.gmm-stars {color:#e6a400;font-size:20px;letter-spacing:2px}
.gmm-review p {color:#594752;line-height:1.7}
.gmm-review small {color:#a02663;font-weight:bold}
.gmm-review-note {
  font-size:12px;
  color:#765d6b;
  margin-top:15px;
}
#gmm-whatsapp-float {
  position:fixed;
  right:18px;
  bottom:22px;
  z-index:9998;
  background:#25d366;
  color:white;
  padding:13px 17px;
  border-radius:50px;
  text-decoration:none;
  font-weight:bold;
  box-shadow:0 5px 18px #0003;
}
#gmm-top-button {
  display:none;
  position:fixed;
  left:18px;
  bottom:22px;
  z-index:9998;
  border:0;
  background:#c02670;
  color:white;
  width:45px;
  height:45px;
  border-radius:50%;
  font-size:23px;
  cursor:pointer;
  box-shadow:0 5px 18px #0003;
}
@media(max-width:480px) {
  #gmm-special-offer h2 {font-size:22px}
  #gmm-reviews {padding:40px 4%}
}
</style>

<section id="gmm-special-offer">
  <h2>🎀 Special Shopping Deals 🎀</h2>
  <p>Discover your favourite fashion styles at Girlies Mini Mart.</p>
  <p>Contact our seller on WhatsApp to ask about current offers,
  availability and possible price negotiations!</p>
</section>

<section id="gmm-reviews">
  <h2>What Our Customers Say ⭐</h2>
  <p>We would love to hear about your shopping experience.</p>

  <div class="gmm-review-grid">
    <article class="gmm-review">
      <div class="gmm-stars">★★★★★</div>
      <p>Share your experience shopping with Girlies Mini Mart here.</p>
      <small>Customer review placeholder</small>
    </article>
    <article class="gmm-review">
      <div class="gmm-stars">★★★★★</div>
      <p>Tell us what you liked about your product and service.</p>
      <small>Customer review placeholder</small>
    </article>
    <article class="gmm-review">
      <div class="gmm-stars">★★★★★</div>
      <p>Your feedback helps us improve our products and service.</p>
      <small>Customer review placeholder</small>
    </article>
  </div>
  <p class="gmm-review-note">
    These are sample placeholders, not actual customer testimonials.
  </p>
  <a href="https://wa.me/2348169719745?text=Hello%20Girlies%20Mini%20Mart%2C%20I%20would%20like%20to%20share%20my%20shopping%20feedback."
     style="display:inline-block;background:#c02670;color:white;padding:12px 20px;border-radius:9px;text-decoration:none;font-weight:bold">
    Send Your Feedback
  </a>
</section>

<a id="gmm-whatsapp-float"
   href="https://wa.me/2348169719745?text=Hello%20Girlies%20Mini%20Mart%21%20I%20want%20to%20make%20an%20enquiry."
   target="_blank" rel="noopener">WhatsApp Us</a>

<button id="gmm-top-button" aria-label="Back to top"
 onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>

<script>
(function(){
 const btn=document.getElementById('gmm-top-button');
 if(!btn)return;
 window.addEventListener('scroll',function(){
   btn.style.display=window.scrollY>350?'block':'none';
 });
})();
</script>
<!-- END GMM-PRO-UPGRADE -->
"""

if "</body>" not in html:
    raise SystemExit("Could not find </body> in index.html.")

html = html.replace("</body>", upgrade + "\n</body>", 1)
p.write_text(html, encoding="utf-8")
print("SUCCESS! Girlies Mini Mart professional upgrade installed.")
