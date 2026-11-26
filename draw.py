#!/usr/bin/env python3
"""Draw entry.png for news-image-20261125.

Build-machine only (Pillow). Produces a dense 1024x1024 board for
Wednesday 25 November 2026: 34 dated stories across 8 regions.
The grading program is main.py, which only copies the finished PNG.
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "entry.png")
W = H = 1024

PAPER = (248, 243, 234)
INK = (24, 24, 24)
MUTED = (96, 96, 96)
LINE = (24, 24, 24)
PANEL = (238, 231, 217)
WHITE = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

REGIONS = {
    "MIDDLE EAST": (176, 58, 46),
    "EUROPE": (36, 86, 166),
    "ASIA": (190, 120, 20),
    "AMERICAS": (30, 132, 73),
    "AFRICA": (150, 84, 20),
    "PACIFIC": (14, 124, 123),
    "MARKETS": (90, 70, 160),
    "TECH & SPACE": (106, 58, 138),
}

STORIES = [
    ("MIDDLE EAST", "Hormuz tankers hit mines, catch fire", "IRGC says two vessels burned on an unauthorised route."),
    ("MIDDLE EAST", "Houthis target Jazan and Jeddah ports", "Saudi coalition reports minor Jazan damage."),
    ("MIDDLE EAST", "Saudi coalition strikes Hodeidah", "Strikes also reported in Saada and Amran."),
    ("MIDDLE EAST", "Israeli strikes kill 11 in Gaza", "Hospital sources say two girls were among the dead."),
    ("MIDDLE EAST", "Hamas security chief killed", "Mohammad Abuelouf and family reported killed."),
    ("EUROPE", "Russian strike kills two near Odesa", "Kyiv apartment fire injures two people."),
    ("EUROPE", "UK gives £240m Ukraine air-defence aid", "Missiles and launchers due from mid-December."),
    ("EUROPE", "Hungary and Ukraine seek fresh start", "Magyar and Zelenskyy meet in Uzhhorod."),
    ("EUROPE", "Pope warns over COP31 failure", "Leo XIV cites more frequent extreme climate events."),
    ("EUROPE", "London and Brussels draw economies closer", "Burnham calls Brexit a failure; no rejoining now."),
    ("ASIA", "Shenzhou-24 carries Pakistan's first astronaut", "Muhammad Zeeshan Ali joins Tiangong crew."),
    ("ASIA", "Bangladesh garment wage rises 36%", "Minimum pay rises to $139 after protests."),
    ("ASIA", "India unveils $1.62bn Nepal package", "Aid follows floods as ties reset."),
    ("ASIA", "Malaysia to return refugees to Myanmar", "Thousands face return, briefing reports say."),
    ("ASIA", "Indonesia gold-mine flood traps 17", "Nine dead after illegal mine floods."),
    ("ASIA", "Hong Kong fire survivors seek answers", "One year on, accountability still questioned."),
    ("ASIA", "China hits back over Huawei conviction", "Beijing accuses US of suppressing Chinese firms."),
    ("AMERICAS", "US unveils broad new tariffs", "China, EU, Brazil targeted; Brazil aircraft 10%."),
    ("AMERICAS", "Venezuela reveals $237.5bn debt", "Figure disclosed ahead of restructuring."),
    ("AMERICAS", "Colombia supermarket hostages rescued", "Standoff followed failed cash-truck robbery."),
    ("AMERICAS", "WHO chief urges end to Cuba fuel blockade", "Call comes amid Caribbean health pressure."),
    ("AFRICA", "Sudan RSF drones kill 19 in Blue Nile", "Rights group reports 20 wounded."),
    ("AFRICA", "South Africa court ends Ramaphosa case", "Phala Phala panel report set aside."),
    ("AFRICA", "Cairo tanker fire kills 31", "Health ministry reports 21 injured."),
    ("AFRICA", "$1.576bn plan targets Congo Ebola", "11,613 cases and 5,678 deaths cited."),
    ("AFRICA", "Nigeria troops rescue five in Kaduna", "Two suspected terrorists arrested."),
    ("PACIFIC", "Australia-Solomons treaty bars foreign bases", "Canberra named primary security partner."),
    ("PACIFIC", "French forces seize 3.3 tonnes of meth", "Drugs found near French Polynesia."),
    ("PACIFIC", "Pacific steps up El Niño drought response", "Three governments act as water crisis deepens."),
    ("MARKETS", "Dow rises 0.33% to 50,182.95", "Nasdaq falls 0.62% as AI selloff fades."),
    ("MARKETS", "Oil jumps on Hormuz and Houthi attacks", "Brent +3.51% to $94.61; WTI +1.99%."),
    ("MARKETS", "Kospi slides 6.16%", "Steepest fall among tracked indices."),
    ("TECH & SPACE", "CIA and ODNI cyber breach reported", "Some unclassified information compromised."),
    ("TECH & SPACE", "UN chief warns AI is reshaping warfare", "Guterres urges autonomous-weapons safeguards."),
]


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, font, max_w, max_lines):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
            if len(lines) == max_lines:
                break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    # If text was cut, mark the last line.
    joined = " ".join(lines)
    if len(joined) < len(text) and lines:
        last = lines[-1]
        while last and d.textlength(last + "…", font=font) > max_w:
            last = last[:-1].rstrip()
        lines[-1] = last + "…"
    return lines


def ship_icon(d, x, y):
    d.polygon([(x, y + 22), (x + 54, y + 22), (x + 46, y + 34), (x + 8, y + 34)], fill=(31, 56, 100))
    d.rectangle([x + 18, y + 8, x + 40, y + 22], fill=(210, 205, 180))
    d.polygon([(x + 44, y), (x + 52, y + 14), (x + 45, y + 20), (x + 38, y + 13)], fill=(232, 120, 32))


def rocket_icon(d, x, y):
    d.ellipse([x + 16, y, x + 38, y + 34], fill=(36, 86, 166))
    d.polygon([(x + 16, y + 24), (x + 4, y + 38), (x + 20, y + 34)], fill=(178, 34, 34))
    d.polygon([(x + 38, y + 24), (x + 50, y + 38), (x + 34, y + 34)], fill=(178, 34, 34))
    d.ellipse([x + 23, y + 9, x + 31, y + 17], fill=(220, 240, 250))


def tag_icon(d, x, y):
    d.rounded_rectangle([x + 4, y + 8, x + 50, y + 34], radius=6, fill=(30, 132, 73))
    d.ellipse([x + 10, y + 14, x + 18, y + 22], fill=PAPER)
    d.text((x + 23, y + 11), "%", font=F(SANS_B, 20), fill=WHITE)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28

    d.text((M, 20), "THE WORLD IN ONE DAY", font=F(SANS_B, 20), fill=MUTED)
    d.text((W - M - d.textlength("WEDNESDAY", font=F(SANS_B, 20)), 20), "WEDNESDAY", font=F(SANS_B, 20), fill=MUTED)
    d.text((M, 44), "25 NOVEMBER 2026", font=F(SERIF_B, 46), fill=INK)
    d.text((M, 96), "34 dated stories · 8 regions · date-checked", font=F(SANS_B, 17), fill=INK)
    d.line([M, 122, W - M, 122], fill=LINE, width=3)
    d.line([M, 128, W - M, 128], fill=LINE, width=1)

    # Lead strip
    lead_y = 138
    chips = [
        (ship_icon, "HORMUZ MINES"),
        (rocket_icon, "SHENZHOU-24"),
        (tag_icon, "US TARIFFS"),
    ]
    chip_w = (W - 2 * M - 16) // 3
    for i, (icon, label) in enumerate(chips):
        x = M + i * (chip_w + 8)
        d.rounded_rectangle([x, lead_y, x + chip_w, lead_y + 46], radius=8, fill=PANEL)
        icon(d, x + 12, lead_y + 6)
        d.text((x + 78, lead_y + 14), label, font=F(SANS_B, 17), fill=INK)

    # Story grid: 3 columns x 12 rows (34 stories + 2 note cells)
    gx, gy = M, 190
    gw, gh = W - 2 * M, 772
    cols, rows, gap = 3, 12, 5
    cw = (gw - gap * (cols - 1)) // cols
    ch = (gh - gap * (rows - 1)) // rows
    tag_f = F(SANS_B, 9)
    head_f = F(SANS_B, 13)
    det_f = F(SANS, 10)

    for idx, (region, head, det) in enumerate(STORIES):
        r, c = divmod(idx, cols)
        x = gx + c * (cw + gap)
        y = gy + r * (ch + gap)
        color = REGIONS[region]
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=6, outline=(205, 198, 182), width=1, fill=(252, 249, 243))
        d.rectangle([x, y + 6, x + 5, y + ch - 6], fill=color)
        tx = x + 12
        tw = cw - 20
        d.text((tx, y + 4), region, font=tag_f, fill=color)
        yy = y + 16
        for ln in wrap(d, head, head_f, tw, 2):
            d.text((tx, yy), ln, font=head_f, fill=INK)
            yy += 14
        for ln in wrap(d, det, det_f, tw, 1):
            d.text((tx, yy + 1), ln, font=det_f, fill=MUTED)

    # Two note cells complete the grid.
    notes = [
        ("DATE CHECK", "All items reported Wed 25 Nov 2026."),
        ("SOURCES", "Reuters · AP · Al Jazeera · SCMP · RNZ"),
    ]
    for j, (k, v) in enumerate(notes):
        idx = len(STORIES) + j
        r, c = divmod(idx, cols)
        x = gx + c * (cw + gap)
        y = gy + r * (ch + gap)
        d.rounded_rectangle([x, y, x + cw, y + ch], radius=6, fill=PANEL)
        d.text((x + 12, y + 8), k, font=F(SANS_B, 11), fill=INK)
        yy = y + 26
        for ln in wrap(d, v, F(SANS, 11), cw - 24, 2):
            d.text((x + 12, yy), ln, font=F(SANS, 11), fill=MUTED)
            yy += 14

    # Timeline strip
    ty = gy + gh + 10
    d.line([M, ty, W - M, ty], fill=LINE, width=2)
    timeline = "Hormuz mines  →  Canberra treaty  →  Dhaka wage rise  →  Gaza dawn strikes  →  Wall Street close"
    d.text((M, ty + 8), timeline, font=F(SANS_B, 13), fill=INK)
    d.text((M, ty + 30), "One image · Wednesday 25 November 2026 · claims dated to the day", font=F(SANS, 11), fill=MUTED)

    img.save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
