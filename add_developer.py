from pathlib import Path

p = Path("index.html")
html = p.read_text()

if "nicegoldmon-developer" in html:
    print("Developer credit already exists.")
    raise SystemExit

css = """
/* NICEGOLDMON DEVELOPER SIGNATURE */
.nicegoldmon-developer {
  background: linear-gradient(135deg,#17121d,#352034);
  color: white;
  text-align: center;
  padding: 35px 15px;
  margin-top: 40px;
  border-top: 3px solid #f35baa;
}
.nicegoldmon-developer .dev-label {
  font-size: 11px;
  letter-spacing: 3px;
  color: #f6b5d9;
  font-weight: 700;
}
.nicegoldmon-developer .dev-name {
  font-size: clamp(25px,6vw,38px);
  font-weight: 900;
  letter-spacing: 3px;
  margin: 12px 0;
  background: linear-gradient(90deg,#ff8bc9,#fff,#ff55a9);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.nicegoldmon-developer .dev-tagline {
  color: #e8cddd;
  font-size: 13px;
}
.nicegoldmon-developer .dev-copyright {
  color: #a99aaa;
  font-size: 11px;
  margin-top: 18px;
}
"""

footer = """
<footer class="nicegoldmon-developer">
  <div class="dev-label">WEBSITE DESIGNED & DEVELOPED BY</div>
  <div class="dev-name">NICEGOLDMON</div>
  <div class="dev-tagline">
    Creative Web Developer • Digital Solutions
  </div>
  <div class="dev-copyright">
    © 2026 Girlies Mini Mart. All Rights Reserved.
  </div>
</footer>
"""

if "</body>" not in html:
    raise SystemExit("Could not find closing body tag.")

if "</style>" in html:
    html = html.replace("</style>", css + "\n</style>", 1)
else:
    html = html.replace("</head>", "<style>" + css + "</style></head>", 1)

html = html.replace("</body>", footer + "\n</body>", 1)

p.write_text(html)
print("NICEGOLDMON developer signature added successfully!")
