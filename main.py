"""Entrypoint for the news-image-20261124 entry.

Renders "THE WORLD IN ONE DAY" — a dense, sourced newspaper front page
summing up Tuesday 24 November 2026 — deterministically with PIL and
writes it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
No network, no clock, fixed seed: two runs produce byte-identical PNGs.
The image is validated before it is written: PNG magic, 1 MiB cap,
1024x1024 canvas, and a second render must match byte for byte.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image, ImageDraw, ImageFont  # noqa: E402

import stories as S  # noqa: E402

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
W, H = 1024, 1024

CREAM = (247, 242, 231)
PAPER = (252, 250, 244)
INK = (20, 33, 61)
RED = (180, 35, 24)
GOLD = (192, 138, 43)
TEAL = (31, 111, 107)
GREY = (90, 90, 82)
LIGHT = (232, 226, 212)
BLUE = (43, 88, 140)
GREEN = (46, 110, 62)

FD = "/usr/share/fonts/truetype/noto"


def _f(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


def serif_black(s):
    return _f("NotoSerif-Black.ttf", s)


def serif_bold(s):
    return _f("NotoSerif-Bold.ttf", s)


def sans(s):
    return _f("NotoSans-Regular.ttf", s)


def sans_bold(s):
    return _f("NotoSans-Bold.ttf", s)


def sans_semi(s):
    return _f("NotoSans-SemiBold.ttf", s)


def wrap(d, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def cert_colors(cert):
    return {
        "CONFIRMED": (GREEN, (255, 255, 255)),
        "REPORTED": (BLUE, (255, 255, 255)),
        "CLAIM": (GOLD, (20, 33, 61)),
        "FORECAST": (GREY, (255, 255, 255)),
    }[cert]


def draw_cert(d, x, y, cert):
    bg, fg = cert_colors(cert)
    f = sans_bold(9)
    tw = d.textlength(cert, font=f)
    d.rounded_rectangle([x, y, x + tw + 10, y + 14], radius=2, fill=bg)
    d.text((x + 5, y + 2), cert, font=f, fill=fg)
    return tw + 10


def draw_source(d, x, y, source, cert):
    f = sans_bold(9)
    d.text((x, y + 2), "SOURCE: " + source, font=f, fill=GREY)
    w = d.textlength("SOURCE: " + source, font=f)
    draw_cert(d, x + w + 8, y, cert)


# ---- flat vector icons, drawn in code (one per drawn story) ----

def icon_chip(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.rectangle([x + s * 0.22, y + s * 0.22, x + s * 0.78, y + s * 0.78],
                outline=c2, width=3)
    d.rectangle([x + s * 0.38, y + s * 0.38, x + s * 0.62, y + s * 0.62],
                fill=c2)
    for i in range(3):
        px = x + s * (0.3 + i * 0.2)
        d.line([px, y, px, y + s * 0.22], fill=c2, width=3)
        d.line([px, y + s * 0.78, px, y + s], fill=c2, width=3)
        py = y + s * (0.3 + i * 0.2)
        d.line([x, py, x + s * 0.22, py], fill=c2, width=3)
        d.line([x + s * 0.78, py, x + s, py], fill=c2, width=3)


def icon_flame(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    cx, cy = x + s / 2, y + s * 0.55
    d.ellipse([cx - s * 0.26, cy - s * 0.3, cx + s * 0.26, cy + s * 0.3],
              fill=c2)
    d.polygon([(cx, y + s * 0.12), (cx + s * 0.2, cy + s * 0.1),
               (cx, cy + s * 0.32), (cx - s * 0.2, cy + s * 0.1)], fill=GOLD)


def icon_radar(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    cx, cy = x + s / 2, y + s / 2
    for r in (0.36, 0.24, 0.12):
        d.ellipse([cx - s * r, cy - s * r, cx + s * r, cy + s * r],
                  outline=c2, width=2)
    d.line([cx, cy, cx + s * 0.3, cy - s * 0.3], fill=c2, width=3)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=c2)


def icon_ship(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.polygon([(x + s * 0.15, y + s * 0.62), (x + s * 0.85, y + s * 0.62),
               (x + s * 0.72, y + s * 0.82), (x + s * 0.28, y + s * 0.82)],
              fill=c2)
    d.rectangle([x + s * 0.42, y + s * 0.25, x + s * 0.58, y + s * 0.62],
                fill=c2)
    d.line([x + s * 0.1, y + s * 0.88, x + s * 0.9, y + s * 0.88],
           fill=c2, width=2)


def icon_stars(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    cx, cy = x + s / 2, y + s / 2
    for k in range(8):
        import math
        a = math.pi * k / 4
        sx, sy = cx + s * 0.28 * math.cos(a), cy + s * 0.28 * math.sin(a)
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=c2)
    d.ellipse([cx - s * 0.08, cy - s * 0.08, cx + s * 0.08, cy + s * 0.08],
              fill=GOLD)


def icon_building(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.rectangle([x + s * 0.3, y + s * 0.2, x + s * 0.7, y + s * 0.85],
                fill=c2)
    for r in range(3):
        for c in range(2):
            d.rectangle([x + s * (0.36 + c * 0.14), y + s * (0.28 + r * 0.18),
                         x + s * (0.44 + c * 0.14), y + s * (0.36 + r * 0.18)],
                        fill=c1)


def icon_jet(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.polygon([(x + s * 0.15, y + s * 0.55), (x + s * 0.85, y + s * 0.45),
               (x + s * 0.7, y + s * 0.62), (x + s * 0.25, y + s * 0.68)],
              fill=c2)
    d.polygon([(x + s * 0.6, y + s * 0.45), (x + s * 0.75, y + s * 0.3),
               (x + s * 0.78, y + s * 0.48)], fill=c2)


def icon_chart(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    pts = [(x + s * 0.15, y + s * 0.7), (x + s * 0.35, y + s * 0.55),
           (x + s * 0.55, y + s * 0.62), (x + s * 0.85, y + s * 0.25)]
    d.line(pts, fill=c2, width=4, joint="curve")
    d.polygon([(x + s * 0.85, y + s * 0.25), (x + s * 0.72, y + s * 0.28),
               (x + s * 0.82, y + s * 0.4)], fill=c2)


def icon_cart(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.polygon([(x + s * 0.2, y + s * 0.3), (x + s * 0.8, y + s * 0.3),
               (x + s * 0.72, y + s * 0.65), (x + s * 0.28, y + s * 0.65)],
              fill=c2)
    d.ellipse([x + s * 0.3, y + s * 0.7, x + s * 0.4, y + s * 0.8], fill=c2)
    d.ellipse([x + s * 0.6, y + s * 0.7, x + s * 0.7, y + s * 0.8], fill=c2)


def icon_atom(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    cx, cy = x + s / 2, y + s / 2
    for k in range(3):
        import math
        a = math.pi * k / 3
        d.ellipse([cx - s * 0.32, cy - s * 0.14, cx + s * 0.32,
                   cy + s * 0.14], outline=c2, width=2)
        # rotate by drawing a second axis-ellipse is enough for a flat mark
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=GOLD)


def icon_shield(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.polygon([(x + s * 0.5, y + s * 0.15), (x + s * 0.8, y + s * 0.28),
               (x + s * 0.8, y + s * 0.55), (x + s * 0.5, y + s * 0.85),
               (x + s * 0.2, y + s * 0.55), (x + s * 0.2, y + s * 0.28)],
              fill=c2)
    d.line([x + s * 0.38, y + s * 0.5, x + s * 0.47, y + s * 0.6,
            x + s * 0.65, y + s * 0.38], fill=c1, width=3)


def icon_bank(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.polygon([(x + s * 0.12, y + s * 0.35), (x + s * 0.5, y + s * 0.15),
               (x + s * 0.88, y + s * 0.35)], fill=c2)
    for i in range(3):
        px = x + s * (0.25 + i * 0.22)
        d.rectangle([px, y + s * 0.42, px + s * 0.08, y + s * 0.72], fill=c2)
    d.rectangle([x + s * 0.15, y + s * 0.75, x + s * 0.85, y + s * 0.82],
                fill=c2)


def icon_globe(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    cx, cy = x + s / 2, y + s / 2
    d.ellipse([cx - s * 0.32, cy - s * 0.32, cx + s * 0.32, cy + s * 0.32],
              fill=c2)
    d.ellipse([cx - s * 0.32, cy - s * 0.32, cx + s * 0.32, cy + s * 0.32],
              outline=INK, width=2)
    d.line([cx - s * 0.32, cy, cx + s * 0.32, cy], fill=INK, width=2)
    d.ellipse([cx - s * 0.14, cy - s * 0.32, cx + s * 0.14, cy + s * 0.32],
              outline=INK, width=2)


def icon_satellite(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.rectangle([x + s * 0.38, y + s * 0.38, x + s * 0.62, y + s * 0.62],
                fill=c2)
    d.rectangle([x + s * 0.15, y + s * 0.42, x + s * 0.35, y + s * 0.58],
                fill=GOLD)
    d.rectangle([x + s * 0.65, y + s * 0.42, x + s * 0.85, y + s * 0.58],
                fill=GOLD)
    d.line([x + s * 0.62, y + s * 0.38, x + s * 0.8, y + s * 0.2],
           fill=c2, width=2)


def icon_smog(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.ellipse([x + s * 0.55, y + s * 0.18, x + s * 0.85, y + s * 0.48],
              fill=GOLD)
    for i, yy in enumerate((0.55, 0.68, 0.81)):
        d.rectangle([x + s * (0.15 + i * 0.05), y + s * yy,
                     x + s * (0.85 - i * 0.05), y + s * yy + 4], fill=c2)


def icon_cap(d, x, y, s, c1, c2):
    d.rectangle([x, y, x + s, y + s], fill=c1)
    d.polygon([(x + s * 0.12, y + s * 0.45), (x + s * 0.5, y + s * 0.25),
               (x + s * 0.88, y + s * 0.45), (x + s * 0.5, y + s * 0.62)],
              fill=c2)
    d.rectangle([x + s * 0.65, y + s * 0.5, x + s * 0.72, y + s * 0.75],
                fill=c2)


ICONS = {
    "chip": icon_chip, "flame": icon_flame, "radar": icon_radar,
    "ship": icon_ship, "stars": icon_stars, "building": icon_building,
    "jet": icon_jet, "chart": icon_chart, "cart": icon_cart,
    "atom": icon_atom, "shield": icon_shield, "bank": icon_bank,
    "globe": icon_globe, "satellite": icon_satellite, "smog": icon_smog,
    "cap": icon_cap,
}


def draw_icon(d, name, x, y, s):
    fn = ICONS.get(name)
    if fn:
        fn(d, x, y, s, LIGHT, INK)


# ---- layout ----

M = 28
CW = (W - 2 * M - 12) // 3  # card column width: 318


def draw_masthead(d):
    d.rectangle([0, 0, W, 100], fill=INK)
    d.text((M, 10), "THE WORLD IN ONE DAY", font=serif_black(40), fill=CREAM)
    d.text((M, 58), S.DATE_LINE, font=sans_bold(15), fill=GOLD)
    d.text((M, 80), S.ACCOUNTING, font=sans_bold(11), fill=(200, 205, 215))
    d.rectangle([0, 100, W, 104], fill=RED)


def draw_hero(d, x, y, w, h, hero):
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=INK, width=2)
    ix, iy, isz = x + 12, y + 12, 96
    draw_icon(d, hero["icon"], ix, iy, isz)
    tx = x + 120
    d.text((tx, y + 12), hero["kicker"], font=sans_bold(11), fill=RED)
    lines = wrap(d, hero["headline"], serif_black(24), w - 132)
    yy = y + 30
    for ln in lines[:2]:
        d.text((tx, yy), ln, font=serif_black(24), fill=INK)
        yy += 28
    deck = wrap(d, hero["deck"], sans(12), w - 24)
    yy = y + 92
    for ln in deck[:3]:
        d.text((x + 12, yy), ln, font=sans(12), fill=(40, 40, 36))
        yy += 16
    draw_source(d, x + 12, y + h - 22, hero["source"], hero["cert"])


def section_header(d, x, y, w, name):
    d.rectangle([x, y, x + w, y + 20], fill=INK)
    d.text((x + 8, y + 3), name, font=sans_bold(12), fill=CREAM)


SHORT_KICKER = {"WORLD": "WORLD", "MONEY & TECH": "MONEY",
                "SCIENCE & PLANET": "SCIENCE",
                "SOCIETY & CULTURE": "SOCIETY"}


def draw_card(d, x, y, w, h, sec, headline, deck, source, cert, icon):
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=(200, 192, 172))
    tx = x + 8
    if icon:
        draw_icon(d, icon, x + 8, y + 8, 46)
        tx = x + 62
        tw = w - 70
    else:
        tw = w - 16
    d.text((tx, y + 4), SHORT_KICKER.get(sec, sec), font=sans_bold(9),
           fill=RED)
    # source + certainty share the kicker line, right-aligned
    fsrc = sans_bold(8)
    sw = d.textlength("SOURCE: " + source, font=fsrc)
    bg, fg = cert_colors(cert)
    fcert = sans_bold(8)
    cw = d.textlength(cert, font=fcert) + 10
    sx = x + w - 8 - cw - 6 - sw
    d.text((sx, y + 5), "SOURCE: " + source, font=fsrc, fill=GREY)
    d.rounded_rectangle([x + w - 8 - cw, y + 3, x + w - 8, y + 15],
                        radius=2, fill=bg)
    d.text((x + w - 8 - cw + 5, y + 5), cert, font=fcert, fill=fg)
    lines = wrap(d, headline, serif_bold(13), tw)
    yy = y + 17
    for ln in lines[:2]:
        d.text((tx, yy), ln, font=serif_bold(13), fill=INK)
        yy += 15
    dline = wrap(d, deck, sans(10), w - 16)
    if dline:
        d.text((x + 8, y + 49), dline[0], font=sans(10), fill=(60, 60, 54))


def draw_timeline(d, y):
    d.rectangle([M, y, W - M, y + 52], fill=(238, 232, 216), outline=INK)
    d.text((M + 8, y + 4), "UTC TIMELINE \u2014 TUESDAY 24 NOVEMBER 2026",
           font=sans_bold(10), fill=INK)
    seg = (W - 2 * M - 16) / len(S.TIMELINE)
    for i, (t, label) in enumerate(S.TIMELINE):
        cx = M + 8 + seg * i
        d.text((cx, y + 16), t, font=sans_bold(9), fill=RED)
        d.line([cx + 20, y + 32, cx + 20, y + 48], fill=RED, width=2)
        d.ellipse([cx + 16, y + 28, cx + 24, y + 36], fill=RED)
        words = wrap(d, label, sans(8), seg - 8)
        ly = y + 40
        for ln in words[:1]:
            d.text((cx, ly), ln, font=sans(8), fill=INK)


def draw_sport(d, y):
    d.rectangle([M, y, W - M, y + 76], fill=PAPER, outline=INK, width=2)
    d.text((M + 8, y + 5), "SPORT", font=sans_bold(12), fill=RED)
    colw = (W - 2 * M - 16) // 4
    for i, (tag, head, deck, src, cert) in enumerate(S.SPORT):
        x = M + 8 + i * colw
        if i:
            d.line([x - 4, y + 24, x - 4, y + 70], fill=LIGHT, width=1)
        d.text((x, y + 22), tag, font=sans_bold(9), fill=TEAL)
        lines = wrap(d, head, serif_bold(12), colw - 12)
        yy = y + 36
        for ln in lines[:2]:
            d.text((x, yy), ln, font=serif_bold(12), fill=INK)
            yy += 14
        d.text((x, y + 64), src + " \u00b7 " + cert, font=sans_bold(8),
               fill=GREY)


def draw_numbers(d, y):
    d.rectangle([M, y, W - M, y + 56], fill=INK)
    d.text((M + 8, y + 4), "BY THE NUMBERS", font=sans_bold(11),
           fill=GOLD)
    colw = (W - 2 * M - 16) // 4
    for i, (num, label) in enumerate(S.NUMBERS):
        x = M + 8 + i * colw
        d.text((x, y + 20), num, font=serif_black(20), fill=CREAM)
        lines = wrap(d, label, sans(9), colw - 12)
        d.text((x, y + 43), lines[0] if lines else "", font=sans(9),
               fill=(200, 205, 215))


def draw_markets(d, y):
    d.rectangle([M, y, W - M, y + 50], fill=PAPER, outline=INK, width=1)
    d.text((M + 8, y + 4), "MARKETS & WEATHER", font=sans_bold(11),
           fill=RED)
    colw = (W - 2 * M - 16) // 3
    for i, (tag, line) in enumerate(S.MARKETS):
        x = M + 8 + i * colw
        d.text((x, y + 20), tag, font=sans_bold(9), fill=TEAL)
        lines = wrap(d, line, sans(10), colw - 12)
        if lines:
            d.text((x, y + 33), lines[0], font=sans(10), fill=INK)


def draw_wire(d, y):
    d.rectangle([M, y, W - M, y + 48], fill=(238, 232, 216))
    d.text((M + 8, y + 3), "LATE WIRE", font=sans_bold(11), fill=RED)
    colw = (W - 2 * M - 16) // 2
    for i, (head, cert) in enumerate(S.WIRE):
        col, row = i % 2, i // 2
        x = M + 8 + col * colw
        d.text((x, y + 16 + row * 11), "\u25aa " + head,
               font=sans_bold(10), fill=INK)


def draw_footer(d, y):
    d.text((M, y), S.FIELD_COUNTS + " \u00b7 Sources on every story"
           " \u00b7 All times UTC \u00b7 @kreutzx",
           font=sans_bold(9), fill=GREY)


def render():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    hy = 110
    hw = (W - 2 * M - 12) // 2
    draw_hero(d, M, hy, hw, 170, S.HEROES[0])
    draw_hero(d, M + hw + 12, hy, hw, 170, S.HEROES[1])
    draw_timeline(d, 286)
    # sections: 3 columns x 6 rows of cards
    sy = 340
    ch, gap = 64, 5
    for i, (sec, head, deck, src, cert, icon) in enumerate(S.SECTIONS):
        col, row = i % 3, i // 3
        x = M + col * (CW + 6)
        y = sy + row * (ch + gap)
        draw_card(d, x, y, CW, ch, sec, head, deck, src, cert, icon)
    ey = sy + 6 * (ch + gap) - gap
    draw_sport(d, ey + 6)
    draw_numbers(d, ey + 88)
    draw_markets(d, ey + 150)
    draw_wire(d, ey + 206)
    draw_footer(d, ey + 260)
    return img


def render_bytes():
    import io
    buf = io.BytesIO()
    render().save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def main():
    data = render_bytes()
    assert data[:8] == PNG_MAGIC, "rendered bytes are not a PNG"
    assert len(data) <= MAX_BYTES, f"image too large: {len(data)} bytes"
    assert render_bytes() == data, "rendering is not deterministic"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.png")
    with open(path, "wb") as fh:
        fh.write(data)
    print(f"wrote {path} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
