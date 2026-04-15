"""
image_card.py — Clean card, no avatar, no divider lines
Layout: centered, score big, label, bar, username, footer
"""
import io, os
import aiohttp
from PIL import Image, ImageDraw, ImageFont, ImageFilter

CARD_W, CARD_H = 1200, 766

THEMES = {
    "True Believer":        {"accent": "#4fc3f7", "dark": "#050d14"},
    "Faithful but Curious": {"accent": "#ffa726", "dark": "#100800"},
    "On the Fence":         {"accent": "#b0bec5", "dark": "#0c0c0c"},
    "Closet Atheist":       {"accent": "#ce93d8", "dark": "#08000f"},
    "Proud Atheist":        {"accent": "#ef5350", "dark": "#110000"},
    "Full Antitheist":      {"accent": "#ff1744", "dark": "#0d0000"},
    "Asleep":               {"accent": "#78909c", "dark": "#080808"},
    "Waking Up":            {"accent": "#26c6da", "dark": "#001518"},
    "Aware":                {"accent": "#66bb6a", "dark": "#001500"},
    "Strategic":            {"accent": "#ab47bc", "dark": "#0a000f"},
    "Fully Unplugged":      {"accent": "#ff1744", "dark": "#0d0000"},
}

EMOJIS = {
    "True Believer":"🙏","Faithful but Curious":"🤔","On the Fence":"😐",
    "Closet Atheist":"👀","Proud Atheist":"😤","Full Antitheist":"🔥",
    "Asleep":"😴","Waking Up":"👁️","Aware":"🧠","Strategic":"♟️","Fully Unplugged":"🔴",
}

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def load_font(size, bold=False):
    paths = [
        f"/usr/share/fonts/truetype/dejavu/DejaVuSans{'-Bold' if bold else ''}.ttf",
        f"/usr/share/fonts/truetype/liberation/LiberationSans-{'Bold' if bold else 'Regular'}.ttf",
        f"/usr/share/fonts/truetype/freefont/FreeSans{'Bold' if bold else ''}.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for p in paths:
        if os.path.exists(p):
            try: return ImageFont.truetype(p, size)
            except: continue
    return ImageFont.load_default()

def tw(draw, text, font):
    return draw.textbbox((0,0), text, font=font)[2]

def dc(draw, y, text, font, color, x0=0, x1=CARD_W):
    x = x0 + (x1 - x0 - tw(draw, text, font)) // 2
    draw.text((x, y), text, font=font, fill=color)

async def generate_result_card(bot, user_id: int, username: str,
                                percentage: int, label: str,
                                subtitle: str = "Know Your Faith") -> io.BytesIO:

    theme      = THEMES.get(label, THEMES["Full Antitheist"])
    accent     = theme["accent"]
    dark       = theme["dark"]
    accent_rgb = hex_to_rgb(accent)
    dark_rgb   = hex_to_rgb(dark)
    bot_un     = os.getenv("BOT_USERNAME", "mirrorbot")

    # ── Background ────────────────────────────────────────────────────────────
    mode = "matrix" if label in ["Asleep","Waking Up","Aware","Strategic","Fully Unplugged"] else "faith"
    template_path = f"card_template_{mode}.png"
    if os.path.exists(template_path):
        try:
            img = Image.open(template_path).convert("RGB").resize((CARD_W, CARD_H), Image.LANCZOS)
        except:
            img = Image.new("RGB", (CARD_W, CARD_H), dark_rgb)
    else:
        img = Image.new("RGB", (CARD_W, CARD_H), dark_rgb)

    draw = ImageDraw.Draw(img)

    # ── Accent border bars ────────────────────────────────────────────────────
    draw.rectangle([0, 0, CARD_W, 10], fill=accent)
    draw.rectangle([0, CARD_H-10, CARD_W, CARD_H], fill=accent)
    draw.rectangle([0, 0, 10, CARD_H], fill=accent)
    draw.rectangle([CARD_W-10, 0, CARD_W, CARD_H], fill=accent)
    # Soft glow under top bar
    for i in range(1, 20):
        draw.rectangle([0, 10+i, CARD_W, 11+i],
                       fill=(*accent_rgb, max(0, 80 - i*4)))

    # ── Fonts ─────────────────────────────────────────────────────────────────
    f_micro = load_font(24)
    f_tiny  = load_font(30)
    f_small = load_font(38, bold=True)
    f_med   = load_font(50, bold=True)
    f_user  = load_font(44)
    f_score = load_font(220, bold=True)
    f_label = load_font(64, bold=True)

    # ── Header ────────────────────────────────────────────────────────────────
    dc(draw, 20, "MIRROR", f_small, accent)
    dc(draw, 70, subtitle.upper(), f_micro, "#555555")

    # ── Score (big glowing number) ────────────────────────────────────────────
    score_text = f"{percentage}%"
    score_y    = 130
    sx = (CARD_W - tw(draw, score_text, f_score)) // 2

    # Glow layers
    glow = Image.new("RGBA", img.size, (0,0,0,0))
    gd   = ImageDraw.Draw(glow)
    for off, a in [(22,8),(14,18),(7,35),(3,55)]:
        for ox in range(-off, off+1, 4):
            for oy in range(-off, off+1, 4):
                gd.text((sx+ox, score_y+oy), score_text, font=f_score,
                        fill=(*accent_rgb, a))
    img = Image.alpha_composite(
        img.convert("RGBA"),
        glow.filter(ImageFilter.GaussianBlur(12))
    ).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text((sx, score_y), score_text, font=f_score, fill=accent)

    # ── Label pill ────────────────────────────────────────────────────────────
    emoji_label = f"{EMOJIS.get(label, '')}  {label.upper()}"
    label_y = 460
    lx  = (CARD_W - tw(draw, emoji_label, f_label)) // 2
    bbox = draw.textbbox((lx, label_y), emoji_label, font=f_label)
    pad = 30
    draw.rounded_rectangle(
        [bbox[0]-pad, bbox[1]-14, bbox[2]+pad, bbox[3]+14],
        radius=18, fill=(*accent_rgb, 22), outline=accent, width=2
    )
    draw.text((lx, label_y), emoji_label, font=f_label, fill="#ffffff")

    # ── Username ──────────────────────────────────────────────────────────────
    display = f"@{username}" if username else "anonymous"
    dc(draw, 560, display, f_user, "#cccccc")

    # ── Progress bar ──────────────────────────────────────────────────────────
    pad_x = 160
    bar_x  = pad_x
    bar_x2 = CARD_W - pad_x
    bar_y  = 630
    bar_h  = 14
    bw     = bar_x2 - bar_x

    draw.rounded_rectangle([bar_x, bar_y, bar_x2, bar_y+bar_h],
                            radius=7, fill="#1c1c1c")
    fw = max(14, int(bw * percentage / 100))
    draw.rounded_rectangle([bar_x, bar_y, bar_x+fw, bar_y+bar_h],
                            radius=7, fill=accent)
    # Glow on fill
    for i in range(1, 5):
        draw.rounded_rectangle([bar_x, bar_y-i, bar_x+fw, bar_y+bar_h+i],
                                radius=7,
                                outline=(*accent_rgb, max(0, 36-i*8)),
                                width=1)

    # Percentage beside bar
    draw.text((bar_x+fw+12, bar_y-2), f"{percentage}%", font=f_tiny,
              fill=(*accent_rgb, 200))

    # ── Footer ────────────────────────────────────────────────────────────────
    dc(draw, 672, "HOW WELL DO YOU KNOW YOURSELF?", f_micro, "#3a3a3a")
    dc(draw, 700, f"t.me/{bot_un}", f_tiny, (*accent_rgb, 160))
    dc(draw, 734, "Mirror — Know Your Faith & the Matrix", f_micro, "#2e2e2e")

    buf = io.BytesIO()
    img.save(buf, format="PNG", quality=95)
    buf.seek(0)
    print(f"[Card] Done: {label} {percentage}% @{username}")
    return buf