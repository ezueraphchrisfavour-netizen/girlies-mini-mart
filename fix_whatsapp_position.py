from pathlib import Path

p = Path("index.html")
html = p.read_text(encoding="utf-8")

fix = """
<style>
#gmm-whatsapp-float {
  right: 12px !important;
  bottom: auto !important;
  top: 110px !important;
  padding: 10px 13px !important;
  font-size: 13px !important;
  z-index: 9998;
}
@media(max-width:480px) {
  #gmm-whatsapp-float {
    top: 90px !important;
    right: 8px !important;
    padding: 8px 10px !important;
    font-size: 11px !important;
  }
}
</style>
"""

if "GMM-WHATSAPP-POSITION-FIX" not in html:
    fix = "<!-- GMM-WHATSAPP-POSITION-FIX -->\n" + fix
    html = html.replace("</body>", fix + "\n</body>", 1)
    p.write_text(html, encoding="utf-8")
    print("WhatsApp button repositioned!")
else:
    print("Position fix already installed.")
