from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found.")

html = p.read_text(encoding="utf-8")

if "</head>" not in html.lower():
    raise SystemExit("Could not find the HTML head section.")

# Remove old Open Graph tags so this update does not create duplicates.
html = re.sub(
    r'<meta[^>]+(?:property|name)=["\'](?:og:[^"\']+|twitter:[^"\']+)["\'][^>]*>',
    "",
    html,
    flags=re.I
)

html = re.sub(
    r'<title>.*?</title>',
    '<title>Girlies Mini Mart | Fashion, Bags, Shoes & More</title>',
    html,
    count=1,
    flags=re.I | re.S
)

tags = """
<!-- GIRLIES MINI MART WHATSAPP PREVIEW -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Girlies Mini Mart">
<meta property="og:title" content="Girlies Mini Mart | Fashion, Bags, Shoes & More">
<meta property="og:description" content="Discover stylish clothes, bags, shoes and accessories. Shop and negotiate directly on WhatsApp!">
<meta property="og:url" content="https://ezueraphchrisfavour-netizen.github.io/girlies-mini-mart/">
<meta property="og:image" content="https://ezueraphchrisfavour-netizen.github.io/girlies-mini-mart/assets/logo.png">
<meta property="og:image:alt" content="Girlies Mini Mart business logo">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Girlies Mini Mart">
<meta name="twitter:description" content="Fashion, bags, shoes and accessories.">
<meta name="twitter:image" content="https://ezueraphchrisfavour-netizen.github.io/girlies-mini-mart/assets/logo.png">
"""

html = re.sub(r"</head>", tags + "\n</head>", html, count=1, flags=re.I)
p.write_text(html, encoding="utf-8")

print("SUCCESS: WhatsApp and social preview metadata added!")
