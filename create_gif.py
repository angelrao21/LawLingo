from PIL import Image, ImageDraw, ImageFont
import math
import os

# ============================================================
# LAW LINGO — ANIMATED GITHUB README HERO
# ============================================================

WIDTH = 1200
HEIGHT = 600
FRAMES = 60
DURATION = 100

OUTPUT = "lawlingo-hero.gif"

# ------------------------------------------------------------
# Fonts
# ------------------------------------------------------------

def get_font(size, bold=False):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",

        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    ]

    for path in paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)

    return ImageFont.load_default()


FONT_BIG = get_font(58, True)
FONT_TITLE = get_font(34, True)
FONT_NORMAL = get_font(22)
FONT_SMALL = get_font(17)
FONT_TINY = get_font(14)

# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def center_text(draw, text, y, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    x = (WIDTH - (box[2] - box[0])) // 2
    draw.text((x, y), text, font=font, fill=fill)


def rounded_box(draw, xy, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(
        xy,
        radius=radius,
        fill=fill,
        outline=outline,
        width=width
    )


def draw_scale(draw, cx, cy, scale=1.0):
    # Pole
    draw.line(
        (cx, cy - 70 * scale, cx, cy + 45 * scale),
        fill="#F3C969",
        width=max(2, int(5 * scale))
    )

    # Top bar
    draw.line(
        (
            cx - 75 * scale,
            cy - 65 * scale,
            cx + 75 * scale,
            cy - 65 * scale
        ),
        fill="#F3C969",
        width=max(2, int(5 * scale))
    )

    # Center triangle
    draw.polygon([
        (cx, cy - 85 * scale),
        (cx - 14 * scale, cy - 65 * scale),
        (cx + 14 * scale, cy - 65 * scale)
    ], fill="#F3C969")

    # Left strings
    lx = cx - 55 * scale
    rx = cx + 55 * scale

    draw.line(
        (lx, cy - 65 * scale, lx - 20 * scale, cy - 25 * scale),
        fill="#F3C969",
        width=max(1, int(3 * scale))
    )

    draw.line(
        (lx, cy - 65 * scale, lx + 20 * scale, cy - 25 * scale),
        fill="#F3C969",
        width=max(1, int(3 * scale))
    )

    # Right strings
    draw.line(
        (rx, cy - 65 * scale, rx - 20 * scale, cy - 25 * scale),
        fill="#F3C969",
        width=max(1, int(3 * scale))
    )

    draw.line(
        (rx, cy - 65 * scale, rx + 20 * scale, cy - 25 * scale),
        fill="#F3C969",
        width=max(1, int(3 * scale))
    )

    # Pans
    draw.arc(
        (
            lx - 30 * scale,
            cy - 25 * scale,
            lx + 30 * scale,
            cy + 15 * scale
        ),
        0,
        180,
        fill="#F3C969",
        width=max(1, int(3 * scale))
    )

    draw.arc(
        (
            rx - 30 * scale,
            cy - 25 * scale,
            rx + 30 * scale,
            cy + 15 * scale
        ),
        0,
        180,
        fill="#F3C969",
        width=max(1, int(3 * scale))
    )

    # Base
    draw.rectangle(
        (
            cx - 40 * scale,
            cy + 45 * scale,
            cx + 40 * scale,
            cy + 52 * scale
        ),
        fill="#F3C969"
    )


def draw_court(draw):
    # Court building
    building_x = 355
    building_y = 205
    building_w = 490

    # Main building
    rounded_box(
        draw,
        (
            building_x,
            building_y,
            building_x + building_w,
            420
        ),
        12,
        "#F3E4C3"
    )

    # Dome
    draw.ellipse(
        (475, 95, 725, 280),
        fill="#E9D4A9"
    )

    # Dome shadow/base
    draw.rectangle(
        (475, 180, 725, 245),
        fill="#D8BE91"
    )

    # Pillars
    for x in range(400, 820, 70):
        draw.rectangle(
            (x, 235, x + 28, 420),
            fill="#FFF5DD"
        )

    # Pillar tops
    for x in range(395, 825, 70):
        draw.rectangle(
            (x, 225, x + 38, 242),
            fill="#C9AB78"
        )

    # Central entrance
    draw.rectangle(
        (570, 310, 630, 420),
        fill="#8C6546"
    )

    # Door
    draw.rectangle(
        (582, 325, 618, 420),
        fill="#5D4030"
    )

    # Steps
    draw.rectangle(
        (530, 420, 670, 435),
        fill="#C9AB78"
    )

    draw.rectangle(
        (545, 435, 655, 448),
        fill="#B69769"
    )

    # Indian flag
    draw.line(
        (765, 255, 765, 360),
        fill="#6B5138",
        width=4
    )

    draw.rectangle(
        (765, 260, 820, 275),
        fill="#E88967"
    )

    draw.rectangle(
        (765, 275, 820, 290),
        fill="#FFF3D0"
    )

    draw.rectangle(
        (765, 290, 820, 305),
        fill="#7AAE73"
    )

    # Ground
    draw.rectangle(
        (0, 445, WIDTH, HEIGHT),
        fill="#E8D6B7"
    )


def draw_document(draw, x, y, progress):
    # Shadow
    rounded_box(
        draw,
        (x + 8, y + 8, x + 175, y + 225),
        12,
        "#B89C78"
    )

    # Paper
    rounded_box(
        draw,
        (x, y, x + 165, y + 215),
        12,
        "#FFFDF5"
    )

    # PDF label
    rounded_box(
        draw,
        (x + 15, y + 15, x + 70, y + 45),
        6,
        "#C95F4D"
    )

    draw.text(
        (x + 25, y + 18),
        "PDF",
        font=FONT_SMALL,
        fill="white"
    )

    # Document title
    draw.text(
        (x + 18, y + 62),
        "JUDGMENT",
        font=FONT_SMALL,
        fill="#172A46"
    )

    # Text lines
    for i in range(7):
        length = 115 if i % 2 == 0 else 95

        draw.rounded_rectangle(
            (
                x + 20,
                y + 95 + i * 15,
                x + 20 + length,
                y + 100 + i * 15
            ),
            radius=2,
            fill="#C8BCA7"
        )

    # Scanning line
    scan_y = y + 80 + int(progress * 110)

    draw.line(
        (x + 10, scan_y, x + 155, scan_y),
        fill="#E0A94F",
        width=3
    )


def draw_pipeline_card(draw, x, y, title, subtitle, active):
    fill = "#FFF8E9" if not active else "#F7E3B2"
    outline = "#D7B35A" if active else "#D6C5A5"

    rounded_box(
        draw,
        (x, y, x + 175, y + 110),
        18,
        fill,
        outline,
        2
    )

    center_x = x + 87

    # Icon circle
    draw.ellipse(
        (
            center_x - 23,
            y + 15,
            center_x + 23,
            y + 61
        ),
        fill="#172A46"
    )

    if title == "PDF":
        draw.text(
            (center_x - 17, y + 26),
            "P",
            font=FONT_SMALL,
            fill="#F3C969"
        )

    elif title == "NLP":
        draw.text(
            (center_x - 18, y + 25),
            "N",
            font=FONT_SMALL,
            fill="#F3C969"
        )

    elif title == "SEARCH":
        draw.ellipse(
            (
                center_x - 12,
                y + 23,
                center_x + 8,
                y + 43
            ),
            outline="#F3C969",
            width=3
        )

        draw.line(
            (center_x + 7, y + 42, center_x + 17, y + 51),
            fill="#F3C969",
            width=3
        )

    elif title == "RAG":
        draw.text(
            (center_x - 17, y + 26),
            "AI",
            font=FONT_TINY,
            fill="#F3C969"
        )

    elif title == "✓":
        draw.text(
            (center_x - 12, y + 24),
            "✓",
            font=FONT_TITLE,
            fill="#F3C969"
        )

    center_text_local(
        draw,
        title,
        x,
        x + 175,
        y + 67,
        FONT_SMALL,
        "#172A46"
    )

    center_text_local(
        draw,
        subtitle,
        x,
        x + 175,
        y + 88,
        FONT_TINY,
        "#665C50"
    )


def center_text_local(draw, text, left, right, y, font, fill):
    box = draw.textbbox((0, 0), text, font=font)
    width = box[2] - box[0]

    x = left + ((right - left) - width) / 2

    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill
    )


# ------------------------------------------------------------
# Create animation
# ------------------------------------------------------------

frames = []

for frame in range(FRAMES):

    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#172A46"
    )

    draw = ImageDraw.Draw(img)

    # --------------------------------------------------------
    # Background
    # --------------------------------------------------------

    draw.rectangle(
        (0, 0, WIDTH, HEIGHT),
        fill="#172A46"
    )

    # Warm glow
    for r in range(350, 50, -20):
        alpha = int(255 * (1 - r / 400))

    # Stars / floating particles
    for i in range(14):
        x = (i * 97 + frame * 2) % WIDTH
        y = 45 + (i * 31) % 160

        size = 2 + (i % 3)

        draw.ellipse(
            (x, y, x + size, y + size),
            fill="#F3C969"
        )

    # --------------------------------------------------------
    # Courtroom
    # --------------------------------------------------------

    draw_court(draw)

    # Dark overlay at top
    draw.rectangle(
        (0, 0, WIDTH, 165),
        fill="#172A46"
    )

    # --------------------------------------------------------
    # LawLingo title
    # --------------------------------------------------------

    center_text(
        draw,
        "⚖  LawLingo",
        30,
        FONT_BIG,
        "#F7D98A"
    )

    center_text(
        draw,
        "Understand. Retrieve. Reason.",
        105,
        FONT_TITLE,
        "#FFF8E8"
    )

    center_text(
        draw,
        "AI-powered legal document intelligence",
        148,
        FONT_SMALL,
        "#D9C9A8"
    )

    # --------------------------------------------------------
    # Scales
    # --------------------------------------------------------

    draw_scale(
        draw,
        185,
        290,
        0.9
    )

    draw_scale(
        draw,
        1015,
        290,
        0.9
    )

    # --------------------------------------------------------
    # Document
    # --------------------------------------------------------

    doc_x = 80

    # Document slides in during first part
    if frame < 15:
        doc_x = 80 + int(frame * 8)

    draw_document(
        draw,
        doc_x,
        275,
        (frame % 30) / 30
    )

    # --------------------------------------------------------
    # Laptop / AI answer
    # --------------------------------------------------------

    laptop_x = 950
    laptop_y = 335

    # Laptop screen
    rounded_box(
        draw,
        (
            laptop_x,
            laptop_y,
            laptop_x + 190,
            laptop_y + 120
        ),
        10,
        "#0D1B2E",
        "#D7B35A",
        3
    )

    draw.text(
        (laptop_x + 18, laptop_y + 15),
        "LawLingo AI",
        font=FONT_SMALL,
        fill="#F3C969"
    )

    draw.text(
        (laptop_x + 18, laptop_y + 45),
        "Answer found ✓",
        font=FONT_SMALL,
        fill="#DDE8E0"
    )

    draw.text(
        (laptop_x + 18, laptop_y + 75),
        "[Source: Judgment]",
        font=FONT_TINY,
        fill="#AFC0D0"
    )

    # Laptop base
    draw.polygon([
        (laptop_x - 20, laptop_y + 120),
        (laptop_x + 210, laptop_y + 120),
        (laptop_x + 180, laptop_y + 140),
        (laptop_x + 10, laptop_y + 140)
    ], fill="#BFA97C")

    # --------------------------------------------------------
    # Pipeline
    # --------------------------------------------------------

    pipeline_y = 475

    cards = [
        ("PDF", "Documents"),
        ("NLP", "Understand"),
        ("SEARCH", "Retrieve"),
        ("RAG", "Reason"),
        ("✓", "Verify")
    ]

    start_x = 235
    gap = 190

    active_index = (frame // 12) % len(cards)

    for i, (title, subtitle) in enumerate(cards):

        x = start_x + i * gap

        draw_pipeline_card(
            draw,
            x,
            pipeline_y,
            title,
            subtitle,
            i == active_index
        )

        # Arrow
        if i < len(cards) - 1:

            arrow_x = x + 180

            draw.line(
                (
                    arrow_x,
                    pipeline_y + 55,
                    arrow_x + 25,
                    pipeline_y + 55
                ),
                fill="#F3C969",
                width=3
            )

            draw.polygon([
                (arrow_x + 25, pipeline_y + 55),
                (arrow_x + 15, pipeline_y + 48),
                (arrow_x + 15, pipeline_y + 62)
            ], fill="#F3C969")

    # --------------------------------------------------------
    # Bottom tagline
    # --------------------------------------------------------

    center_text(
        draw,
        "Making Legal Knowledge More Accessible",
        595 - 45,
        FONT_SMALL,
        "#FFF8E8"
    )

    frames.append(img)


# ------------------------------------------------------------
# Save GIF
# ------------------------------------------------------------

frames[0].save(
    OUTPUT,
    save_all=True,
    append_images=frames[1:],
    duration=DURATION,
    loop=0,
    optimize=True
)

print()
print("==========================================")
print("      LawLingo GIF created successfully!")
print("==========================================")
print()
print(f"File: {OUTPUT}")
print(f"Frames: {FRAMES}")
print(f"Size: {WIDTH} x {HEIGHT}")
print()