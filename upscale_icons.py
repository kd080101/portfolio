"""
Run this from inside your repo's assets/ folder:
    pip install pillow
    python upscale_icons.py

Upscales each icon to 400x400 using LANCZOS resampling so they
render crisp when scaled up by CSS (fixes pixelation).
Overwrites the files in place — commit + push after.
"""
from PIL import Image
import os

ICONS = [
    "assets/contacts.png",
    "assets/sale.png",
    "assets/purchase.png",
    "assets/invoice.png",
    "assets/stock.png",
    "assets/mrp.png",
    "assets/pos.png",
    "assets/website.png",
    "assets/hr.png",
    "assets/crm.png",
    "assets/dhise.webp",
    "assets/french_retro.png",
    "assets/green_rock.webp",
    "assets/iskcon.webp",
    "assets/kik_trading.webp",
    "assets/sasmar.webp",
]

TARGET_SIZE = (400, 400)

for name in ICONS:
    if not os.path.exists(name):
        print(f"skip (not found): {name}")
        continue
    im = Image.open(name).convert("RGBA")
    im2 = im.resize(TARGET_SIZE, Image.LANCZOS)
    im2.save(name, optimize=True)
    print(f"upscaled: {name} -> {TARGET_SIZE[0]}x{TARGET_SIZE[1]}")

print("done")
