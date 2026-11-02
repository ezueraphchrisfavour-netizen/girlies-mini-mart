GIRLIES MINI MART — TERMUX QUICK START

1. Extract this ZIP into your Termux home folder.
2. Open Termux and run:

   pkg update -y
   pkg install python unzip -y
   termux-setup-storage

3. If the ZIP is in your Android Download folder, run:

   cd ~/storage/downloads
   unzip girlies-mini-mart-termux.zip -d ~/girlies-mini-mart

   (If you saved it somewhere else, adjust the ZIP path.)

4. Start the website:

   cd ~/girlies-mini-mart
   python -m http.server 8080

5. Open Chrome and visit:

   http://127.0.0.1:8080

Keep Termux running while viewing the local website.

PRODUCTS:
The catalogue contains the 7 products and prices supplied by the owner.
No extra stock or prices have been invented.
The Brazil Top is marked as a promotional price.
WhatsApp order number is configured as 2348169719745.

TO EDIT PRODUCTS:
Open index.html and find `const products = [`.
Edit product names, prices, categories, notes, or image filenames there.
Put any new product image in the assets folder and reference it as assets/filename.jpg.

NOTE:
This is a local website preview. It is not yet published online.
