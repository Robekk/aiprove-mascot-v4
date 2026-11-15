#!/usr/bin/env python3
"""Mascot pose 5 for AiProve aiprove-mascot: 'The Night Guard'. Composites
the Clerk-Bot pose-1 crop onto a dark navy card with stars, a big gold
shield bearing '#1', and his guard speech line."""
import random
from PIL import Image, ImageDraw, ImageFont

SHEET = "/home/hatch/workspace/aiprove/art/mascot.png"
FONT = "/home/hatch/workspace/makefun/fonts/PatrickHand-Regular.ttf"
W, H = 1600, 1150
random.seed(55)

img = Image.new("RGB", (W, H), (18, 22, 44))
d = ImageDraw.Draw(img, "RGBA")
for _ in range(260):
    x, y = random.uniform(0, W), random.uniform(0, 300)
    b = random.randint(90, 200)
    d.ellipse([x, y, x + 3, y + 3], fill=(b, b, b + 30))

sheet = Image.open(SHEET).convert("RGB")
bot = sheet.crop((58, 258, 648, 1008))  # 590 x 750
img.paste(bot, (80, 250))
d = ImageDraw.Draw(img, "RGBA")

fT = ImageFont.truetype(FONT, 64)
fS = ImageFont.truetype(FONT, 36)
d.text((W // 2, 78), "CLERK-BOT — POSE 5: THE NIGHT GUARD", font=fT, fill=(240, 205, 110), anchor="mm")
d.line([(90, 140), (W - 90, 140)], fill=(240, 205, 110), width=4)

# gold shield with #1
sx, sy = 1130, 560
shield = [(sx, sy - 260), (sx + 210, sy - 190), (sx + 210, sy + 60),
          (sx + 160, sy + 240), (sx, sy + 330), (sx - 160, sy + 240),
          (sx - 210, sy + 60), (sx - 210, sy - 190)]
d.polygon(shield, fill=(52, 44, 18), outline=(240, 205, 110), width=8)
fN = ImageFont.truetype(FONT, 190)
fW = ImageFont.truetype(FONT, 44)
d.text((sx, sy - 30), "#1", font=fN, fill=(240, 205, 110), anchor="mm")
d.text((sx, sy + 130), "HELD, NOT", font=fW, fill=(235, 235, 245), anchor="mm")
d.text((sx, sy + 182), "BORROWED", font=fW, fill=(235, 235, 245), anchor="mm")

# speech bubble
fQ = ImageFont.truetype(FONT, 40)
d.rounded_rectangle([760, 830, 1520, 950], radius=20, fill=(255, 255, 255), outline=(240, 205, 110), width=4)
d.text((1140, 872), '"New bounty? Reopened round?', font=fQ, fill=(30, 40, 34), anchor="mm")
d.text((1140, 916), 'The guard sees it first."', font=fQ, fill=(30, 40, 34), anchor="mm")

# ground line
d.line([(60, 1010), (W - 60, 1010)], fill=(240, 205, 110), width=3)
fF = ImageFont.truetype(FONT, 32)
d.text((W // 2, 1062), "on watch every 30 minutes — season 1", font=fF, fill=(200, 205, 220), anchor="mm")

img.save("/home/hatch/workspace/aiprove/round6/clerkbot-night-guard.png")
print("saved mascot5")
