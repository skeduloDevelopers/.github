import sys

from PIL import Image, ImageDraw

W, H = 1920, 1080
LEFT, TOP = 170, 140
RADIUS, BORDER = 40, 3
TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT = "#0144ff", "#4799ff", "#1861ff", "#6bc4ff"


def solid(colour):
    return Image.new("RGB", (W, H), colour)


def top_left_rounded(size, radius):
    big = Image.new("L", (size[0] * 4, size[1] * 4), 0)
    ImageDraw.Draw(big).rounded_rectangle((0, 0, big.width + radius * 8, big.height + radius * 8), radius * 4, fill=255)
    return big.resize(size, Image.LANCZOS)


if len(sys.argv) < 3:
    sys.exit("usage: make-card.py <screenshot.png> <output.png> [scale]")
src, out = sys.argv[1], sys.argv[2]
scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1.35

down = Image.linear_gradient("L").resize((W, H))
across = Image.linear_gradient("L").rotate(90).resize((W, H))
card = Image.composite(
    Image.composite(solid(BOTTOM_RIGHT), solid(BOTTOM_LEFT), across),
    Image.composite(solid(TOP_RIGHT), solid(TOP_LEFT), across),
    down,
)

shot = Image.open(src).convert("RGB")
shot = shot.resize((round(shot.width * scale), round(shot.height * scale)), Image.LANCZOS)
frame = Image.new("RGB", (W - LEFT, H - TOP), "white")
if shot.width < frame.width or shot.height < frame.height:
    sys.exit(f"screenshot covers {shot.size} at scale {scale}; it must cover {frame.size}. Raise the scale.")
shot = shot.crop((0, 0, frame.width - BORDER, frame.height - BORDER))
frame.paste(shot, (BORDER, BORDER), top_left_rounded(shot.size, RADIUS - BORDER))
card.paste(frame, (LEFT, TOP), top_left_rounded(frame.size, RADIUS))
card.save(out, optimize=True)
