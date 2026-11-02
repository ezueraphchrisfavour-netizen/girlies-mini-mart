from pathlib import Path

p = Path("index.html")
html = p.read_text()

if 'id="girlies-auto-slideshow"' in html:
    print("Slideshow is already installed.")
    raise SystemExit

css = """
/* GIRLIES MINI MART SLOW SLIDESHOW */
#gmm-slideshow {
  width: min(1100px, calc(100% - 28px));
  margin: 35px auto;
  position: relative;
  overflow: hidden;
  border-radius: 25px;
  background: #fff0f8;
  border: 1px solid #f4c9df;
  box-shadow: 0 12px 35px #d94b9018;
}
#gmm-slideshow .gmm-frame {
  display: none;
  opacity: 0;
  transition: opacity 2s ease;
}
#gmm-slideshow .gmm-frame.active {
  display: block;
  opacity: 1;
  animation: gmmFade 2s ease;
}
#gmm-slideshow img {
  display: block;
  width: 100%;
  height: clamp(240px, 55vw, 510px);
  object-fit: contain;
  background: #fff;
}
#gmm-slideshow .gmm-caption {
  padding: 16px;
  text-align: center;
  background: #fff;
}
#gmm-slideshow .gmm-caption b {
  display: block;
  font-family: Georgia, serif;
  font-size: 19px;
}
#gmm-slideshow .gmm-caption span {
  color: #c92d83;
  font-weight: 800;
}
#gmm-slideshow .gmm-dots {
  position: absolute;
  top: 14px;
  right: 14px;
  display: flex;
  gap: 7px;
  z-index: 2;
}
#gmm-slideshow .gmm-dot {
  width: 9px;
  height: 9px;
  padding: 0;
  border: 0;
  border-radius: 50px;
  background: #fff9;
}
#gmm-slideshow .gmm-dot.active {
  width: 25px;
  background: #ed4ca7;
}
.gmm-reveal {
  opacity: 0;
  transform: translateY(25px);
  transition: opacity 1.2s ease, transform 1.2s ease;
}
.gmm-reveal.gmm-shown {
  opacity: 1;
  transform: translateY(0);
}
@keyframes gmmFade {
  from { opacity: 0; }
  to { opacity: 1; }
}
@media(prefers-reduced-motion:reduce) {
  #gmm-slideshow *, .gmm-reveal { transition: none !important; }
}
"""

markup = """
<div id="gmm-slideshow" aria-label="Girlies Mini Mart product slideshow">
  <div class="gmm-dots"></div>
  <div class="gmm-frame active">
    <img src="assets/brown-bags-original.jpg" alt="Brown fashion bags">
    <div class="gmm-caption"><b>Beautiful Brown Bags</b><span>₦15,000</span></div>
  </div>
  <div class="gmm-frame">
    <img src="assets/zirconia-blue-set.jpg" alt="Blue zirconia jewellery">
    <div class="gmm-caption"><b>Blue Zirconia Set</b><span>₦8,000</span></div>
  </div>
  <div class="gmm-frame">
    <img src="assets/zirconia-green-set.jpg" alt="Green jewellery set">
    <div class="gmm-caption"><b>Green Zirconia Set</b><span>₦8,000</span></div>
  </div>
  <div class="gmm-frame">
    <img src="assets/brazil-top.jpg" alt="Brazil fashion top">
    <div class="gmm-caption"><b>Brazil Fashion Top</b><span>₦10,000 Promo</span></div>
  </div>
  <div class="gmm-frame">
    <img src="assets/black-girls-shoes.jpg" alt="Black girls shoes">
    <div class="gmm-caption"><b>Black Girls' Shoes</b><span>₦12,000</span></div>
  </div>
  <div class="gmm-frame">
    <img src="assets/rodo-loafers.jpg" alt="Rodo loafers">
    <div class="gmm-caption"><b>Rodo Shoes</b><span>₦29,000</span></div>
  </div>
  <div class="gmm-frame">
    <img src="assets/womens-bag.jpg" alt="Women's fashion bag">
    <div class="gmm-caption"><b>Women's Fashion Bag</b><span>₦15,000</span></div>
  </div>
</div>
"""

js = """
<script>
(() => {
  const box = document.getElementById('gmm-slideshow');
  if (!box) return;

  const slides = [...box.querySelectorAll('.gmm-frame')];
  const dotsBox = box.querySelector('.gmm-dots');
  let current = 0;

  slides.forEach((slide, i) => {
    const dot = document.createElement('button');
    dot.className = 'gmm-dot' + (i === 0 ? ' active' : '');
    dot.setAttribute('aria-label', 'Show product ' + (i + 1));
    dot.addEventListener('click', () => show(i));
    dotsBox.appendChild(dot);
  });

  function show(index) {
    slides[current].classList.remove('active');
    dotsBox.children[current].classList.remove('active');
    current = index;
    slides[current].classList.add('active');
    dotsBox.children[current].classList.add('active');
  }

  setInterval(() => show((current + 1) % slides.length), 5500);

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('gmm-shown');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.product, .showcase-card').forEach(card => {
    card.classList.add('gmm-reveal');
    observer.observe(card);
  });
})();
</script>
"""

if "</style>" not in html or "<main>" not in html or "</body>" not in html:
    raise SystemExit("Could not find the expected HTML sections. No changes made.")

html = html.replace("</style>", css + "\n</style>", 1)
html = html.replace("<main>", "<main>\n" + markup, 1)
html = html.replace("</body>", js + "\n</body>", 1)

p.write_text(html)
print("Girlies Mini Mart slideshow installed successfully!")
