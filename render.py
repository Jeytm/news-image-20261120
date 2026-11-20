#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news poster (1024x1024 PNG).

Original artwork: six verified stories of Friday 20 November 2026,
drawn with Pillow primitives. No external assets, no network.
Run: python3 render.py  -> writes entry.png next to this file.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
BG = (12, 22, 38)          # deep ink navy
CARD = (21, 42, 66)        # slate blue panel
CARD_EDGE = (36, 59, 87)   # panel border
INK = (245, 242, 232)      # warm white
SUB = (185, 196, 208)      # soft grey for sublines
GOLD = (217, 164, 65)      # masthead gold
TICK_BG = (9, 17, 32)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


F_KICKER = font(BOLD, 62)
F_DATE = font(BOLD, 30)
F_TAG = font(BOLD, 19)
F_HEAD = font(BOLD, 29)
F_SUB = font(REG, 20)
F_TICK = font(BOLD, 16)

# (tag, accent, headline lines, subline lines, icon)
STORIES = [
    ("WASHINGTON — TEHRAN", (224, 82, 82),
     ["TRUMP PUTS IRAN", "DECISION OFF TO 2027"],
     ["\u201cWe\u2019ll see what happens after Jan 1,\u201d",
      "Trump says as the standoff drags on."],
     "mic"),
    ("THE HAGUE", (46, 158, 143),
     ["COURT: MYANMAR", "COMMITTED GENOCIDE"],
     ["ICJ rules 9\u20136 on the Rohingya; ~10,000",
      "killed in 2017. Reparations ordered."],
     "scales"),
    ("INDIA", (74, 144, 217),
     ["CYCLONE AKVAN", "NEARS LANDFALL"],
     ["Due ashore by noon on the Andhra\u2013",
      "Odisha coast; 100,000+ evacuated."],
     "spiral"),
    ("KYIV", (224, 138, 46),
     ["DRONE RAID DAMAGES", "TWO EMBASSIES"],
     ["One killed, five hurt; Austrian and",
      "Dutch missions damaged, cathedral too."],
     "embassy"),
    ("LOS SANTOS — HOLLYWOOD", (180, 90, 196),
     ["GTA VI: $1.84BN", "IN A SINGLE DAY"],
     ["19.05m copies sold, Sensor Tower says \u2014",
      "past The Odyssey\u2019s $1.805bn box office."],
     "pad"),
    ("WELLINGTON", (76, 175, 109),
     ["NICHOLLS RESCUES", "NEW ZEALAND"],
     ["113 not out lifts the hosts from 70/5",
      "to 243/5 on day one against India."],
     "bat"),
]

TICKER = ("SEOUL: HAN DUCK-SOO RETRIAL ORDERED  \u2022  "
          "MODI HOSTS WILLIAM & KATE  \u2022  "
          "APEC LEADERS IN SHENZHEN")


def rounded_rect(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


def icon_mic(d, x, y, s, c):
    # Podium microphone: grille head, stem, base.
    d.rounded_rectangle([x + s * 0.30, y + s * 0.06, x + s * 0.70, y + s * 0.52],
                        radius=10, fill=c)
    for gy in (0.18, 0.30, 0.42):
        d.line([x + s * 0.32, y + s * gy, x + s * 0.68, y + s * gy], fill=BG, width=3)
    d.line([x + s * 0.50, y + s * 0.52, x + s * 0.50, y + s * 0.76], fill=c, width=5)
    d.line([x + s * 0.28, y + s * 0.84, x + s * 0.72, y + s * 0.84], fill=c, width=5)


def icon_scales(d, x, y, s, c):
    d.line([x + s * 0.50, y + s * 0.10, x + s * 0.50, y + s * 0.86], fill=c, width=5)
    d.line([x + s * 0.14, y + s * 0.22, x + s * 0.86, y + s * 0.22], fill=c, width=5)
    for cx in (0.22, 0.78):
        d.line([x + s * cx, y + s * 0.22, x + s * cx, y + s * 0.52], fill=c, width=4)
        d.polygon([(x + s * (cx - 0.16), y + s * 0.52),
                   (x + s * (cx + 0.16), y + s * 0.52),
                   (x + s * cx, y + s * 0.72)], fill=c)
    d.line([x + s * 0.30, y + s * 0.86, x + s * 0.70, y + s * 0.86], fill=c, width=5)


def icon_spiral(d, x, y, s, c):
    cx, cy = x + s * 0.50, y + s * 0.50
    for i, r in enumerate((8, 15, 22, 29)):
        d.arc([cx - r, cy - r, cx + r, cy + r], -40 + i * 55, 200 + i * 55, fill=c, width=5)


def icon_embassy(d, x, y, s, c):
    d.polygon([(x + s * 0.08, y + s * 0.34), (x + s * 0.50, y + s * 0.08),
               (x + s * 0.92, y + s * 0.34)], fill=c)
    for fx in (0.16, 0.44, 0.72):
        d.rectangle([x + s * fx, y + s * 0.40, x + s * (fx + 0.12), y + s * 0.78], fill=c)
    d.rectangle([x + s * 0.08, y + s * 0.78, x + s * 0.92, y + s * 0.88], fill=c)


def icon_pad(d, x, y, s, c):
    d.rounded_rectangle([x + s * 0.06, y + s * 0.26, x + s * 0.94, y + s * 0.80],
                        radius=14, fill=c)
    d.line([x + s * 0.24, y + s * 0.44, x + s * 0.24, y + s * 0.62], fill=BG, width=6)
    d.line([x + s * 0.15, y + s * 0.53, x + s * 0.33, y + s * 0.53], fill=BG, width=6)
    d.ellipse([x + s * 0.62, y + s * 0.44, x + s * 0.72, y + s * 0.54], fill=BG)
    d.ellipse([x + s * 0.76, y + s * 0.56, x + s * 0.86, y + s * 0.66], fill=BG)


def icon_bat(d, x, y, s, c):
    # Cricket bat: a wide blade + handle drawn as rotated rectangles (polygons).
    ang = math.radians(32)
    ux, uy = math.cos(ang), math.sin(ang)
    vx, vy = -uy, ux
    cx, cy = x + s * 0.40, y + s * 0.40
    L, Wd = s * 0.32, s * 0.13
    blade = [(cx + a * L * ux + b * Wd * vx, cy + a * L * uy + b * Wd * vy)
             for a, b in ((1, 1), (1, -1), (-1, -1), (-1, 1))]
    d.polygon(blade, fill=c)
    hx, hy = cx + L * ux, cy + L * uy
    Hl, Hw = s * 0.22, s * 0.05
    handle = [(hx + a * Hl * ux + b * Hw * vx, hy + a * Hl * uy + b * Hw * vy)
              for a, b in ((1, 1), (1, -1), (-1, -1), (-1, 1))]
    d.polygon(handle, fill=c)
    d.ellipse([x + s * 0.64, y + s * 0.60, x + s * 0.90, y + s * 0.86], fill=c)


ICONS = {"mic": icon_mic, "scales": icon_scales, "spiral": icon_spiral,
         "embassy": icon_embassy, "pad": icon_pad, "bat": icon_bat}


def draw_card(d, x, y, w, h, tag, accent, head, sub, icon):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD, outline=CARD_EDGE, width=1)
    d.rounded_rectangle([x, y, x + w, y + 6], radius=3, fill=accent)
    d.text((x + 18, y + 18), tag, font=F_TAG, fill=accent)
    ICONS[icon](d, x + w - 74, y + 14, 60, accent)
    hy = y + 48
    for line in head:
        d.text((x + 18, hy), line, font=F_HEAD, fill=INK)
        hy += 36
    sy = hy + 6
    for line in sub:
        d.text((x + 18, sy), line, font=F_SUB, fill=SUB)
        sy += 27


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Masthead
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=F_KICKER)
    d.text(((W - tw) / 2, 26), title, font=F_KICKER, fill=INK)
    date = "FRIDAY, 20 NOVEMBER 2026"
    dw = d.textlength(date, font=F_DATE)
    d.text(((W - dw) / 2, 102), date, font=F_DATE, fill=GOLD)
    d.line([28, 152, W - 28, 152], fill=GOLD, width=2)

    # Six story cards: 2 columns x 3 rows
    mx, my = 28, 176
    cw, ch, gx, gy = 474, 225, 20, 18
    for i, (tag, accent, head, sub, icon) in enumerate(STORIES):
        cx = mx + (i % 2) * (cw + gx)
        cy = my + (i // 2) * (ch + gy)
        draw_card(d, cx, cy, cw, ch, tag, accent, head, sub, icon)

    # Ticker
    d.line([28, 918, W - 28, 918], fill=GOLD, width=2)
    tkw = d.textlength(TICKER, font=F_TICK)
    d.text(((W - tkw) / 2, 932), TICKER, font=F_TICK, fill=(200, 176, 106))

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
