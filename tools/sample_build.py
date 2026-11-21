import os, subprocess, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = "/mnt/user-data/uploads/PPT Mockups/_claude_work/social"
OUT = "/root/social/out"
os.makedirs(OUT, exist_ok=True)
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
DARK = (46, 59, 62)
CREAM = (246, 239, 227)
RED = (179, 38, 46)
YEL = (242, 201, 76)

def font(p, s): return ImageFont.truetype(p, s)
def src(n): return Image.open(f"{S}/{n}.jpg").convert("RGB")

def wrap(draw, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def ctext(draw, y, text, f, fill, W, maxw=None, gap=1.12):
    lines = wrap(draw, text, f, maxw or W - 120)
    h = f.size * gap
    for i, l in enumerate(lines):
        draw.text((W / 2, y + i * h), l, font=f, fill=fill, anchor="ma")
    return y + len(lines) * h

def logo(size, bg=DARK, fg=CREAM):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse((0, 0, size - 1, size - 1), fill=bg)
    f = font(FB, int(size * 0.22))
    for i, w in enumerate(["PET", "PEEVE", "TEES"]):
        d.text((size / 2, size * (0.29 + i * 0.22)), w, font=f, fill=fg, anchor="mm")
    return im

def cover(im, W, H, zoom=1.0, cx=0.5, cy=0.5):
    w, h = im.size
    s = max(W / w, H / h) * zoom
    nw, nh = int(w * s), int(h * s)
    r = im.resize((nw, nh), Image.LANCZOS)
    x = int((nw - W) * cx); y = int((nh - H) * cy)
    return r.crop((x, y, x + W, y + H))

def pill(draw, cx, y, text, f, bg, fg, padx=34, pady=16):
    tw = draw.textlength(text, font=f)
    h = f.size + pady * 2
    draw.rounded_rectangle((cx - tw / 2 - padx, y, cx + tw / 2 + padx, y + h), radius=h / 2, fill=bg)
    draw.text((cx, y + h / 2), text, font=f, fill=fg, anchor="mm")
    return y + h

# ---------------- Post 2: carousel (Put Down Your Phone) ----------------
def carousel():
    W, H = 1080, 1350
    files = []
    # slide 1: title
    im = Image.new("RGB", (W, H), (255, 255, 255)); d = ImageDraw.Draw(im)
    pill(d, W / 2, 80, "PET PEEVE OF THE DAY", font(FB, 34), DARK, CREAM)
    ctext(d, 190, "Put down your phone.", font(FB, 84), DARK, W, maxw=1000)
    shirt = src("d7_white_7"); shirt = shirt.resize((960, 960), Image.LANCZOS)
    im.paste(shirt, (60, 330))
    ctext(d, 1265, "Swipe for more  >>", font(FM, 38), DARK, W)
    files.append(im)
    # slide 2: design close-up
    im = cover(src("d7_steel-blue_13"), W, H, zoom=1.0); files.append(im)
    # slide 3: model
    im = cover(src("d7_steel-blue_6"), W, H, zoom=1.05, cy=0.35); d = ImageDraw.Draw(im)
    pill(d, W / 2, H - 150, "Steel Blue · Unisex S–5XL", font(FB, 36), DARK, CREAM)
    files.append(im)
    # slide 4: couple
    im = cover(src("d7_white_0"), W, H, zoom=1.0); files.append(im)
    # slide 5: end card
    im = Image.new("RGB", (W, H), DARK); d = ImageDraw.Draw(im)
    lg = logo(380, bg=CREAM, fg=DARK); im.paste(lg, (W // 2 - 190, 230), lg)
    y = ctext(d, 700, "Say it without saying it.", font(FB, 72), CREAM, W)
    y = ctext(d, y + 40, "9 colors · Free US shipping", font(FM, 44), YEL, W)
    pill(d, W / 2, y + 90, "petpeevetees.com  ·  link in bio", font(FB, 40), RED, CREAM)
    files.append(im)
    out = []
    for i, im in enumerate(files, 1):
        p = f"{OUT}/post2_phone_{i}.jpg"; im.save(p, quality=92); out.append(p)
    return out

# ---------------- Post 3: which bugs you more ----------------
def poll():
    W, H = 1080, 1350
    im = Image.new("RGB", (W, H), DARK); d = ImageDraw.Draw(im)
    ctext(d, 90, "WHICH BUGS YOU MORE?", font(FB, 70), CREAM, W, maxw=1040)
    a = src("d4_yellow_13").resize((480, 480), Image.LANCZOS)
    b = src("d16_light-blue_13").resize((480, 480), Image.LANCZOS)
    for x, img in ((40, a), (560, b)):
        m = Image.new("L", img.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, 479, 479), 36, fill=255)
        im.paste(img, (x, 330), m)
    fA = font(FB, 120)
    for cx, letter, col in ((280, "A", YEL), (800, "B", (168, 196, 232))):
        d.ellipse((cx - 75, 230, cx + 75, 380), fill=col)
        d.text((cx, 305), letter, font=font(FB, 96), fill=DARK, anchor="mm")
    fl = font(FB, 46)
    for cx, txt in ((280, "Drivers who never use a turn signal"), (800, "Coworkers who microwave fish at work")):
        for i, l in enumerate(wrap(d, txt, fl, 460)):
            d.text((cx, 850 + i * fl.size * 1.12), l, font=fl, fill=CREAM, anchor="ma")
    d.line((540, 860, 540, 1040), fill=(90, 105, 108), width=3)
    pill(d, W / 2, 1130, "Comment A or B  ·  both tees at petpeevetees.com", font(FB, 36), RED, CREAM)
    p = f"{OUT}/post3_poll.jpg"; im.save(p, quality=92); return [p]

# ---------------- Post 1: video (Chew With Your Mouth Closed) ----------------
def ease(t): return 1 - (1 - max(0, min(1, t))) ** 3

def video():
    W, H, FPS = 1080, 1920, 30
    art = src("d3_white_13"); model = src("d3_light-blue_6"); flat = src("d3_light-blue_7")
    fr = f"{OUT}/frames"; os.makedirs(fr, exist_ok=True)
    for f in os.listdir(fr): os.remove(f"{fr}/{f}")
    lg = logo(360, bg=CREAM, fg=DARK)
    scenes = [(0, 3.2), (3.2, 5.2), (5.2, 8.4), (8.4, 11.2), (11.2, 14.0)]
    total = int(14.0 * FPS)
    big = font(FB, 112); med = font(FB, 64); sm = font(FM, 44)
    hook = ["Pet peeve", "of the week:"]
    line2 = "People who chew with their mouth open."
    for n in range(total):
        t = n / FPS
        if t < 3.2:
            im = Image.new("RGB", (W, H), DARK); d = ImageDraw.Draw(im)
            y = 560
            for i, l in enumerate(hook):
                a = ease((t - i * 0.25) / 0.4)
                d.text((W / 2, y + i * 130 + (1 - a) * 60), l, font=big, fill=tuple(int(c * a + DARK[k] * (1 - a)) for k, c in enumerate(YEL)), anchor="ma")
            a = ease((t - 0.9) / 0.5)
            lines = wrap(d, line2, med, W - 160)
            for i, l in enumerate(lines):
                d.text((W / 2, 900 + i * 82 + (1 - a) * 40), l, font=med, fill=tuple(int(c * a + DARK[k] * (1 - a)) for k, c in enumerate(CREAM)), anchor="ma")
        elif t < 5.2:
            tt = t - 3.2
            im = Image.new("RGB", (W, H), RED); d = ImageDraw.Draw(im)
            a = ease(tt / 0.35)
            s = 0.8 + 0.2 * a
            f = font(FB, int(150 * s))
            d.text((W / 2, 760), "*chomp*", font=f, fill=CREAM, anchor="mm")
            d.text((W / 2, 960), "*smack*", font=font(FB, int(120 * ease((tt - 0.4) / 0.35) + 1)), fill=CREAM, anchor="mm")
            if tt > 1.0:
                d.text((W / 2, 1180), "We all hear it.", font=med, fill=YEL, anchor="mm")
        elif t < 8.4:
            tt = (t - 5.2) / 3.2
            im = cover(art, W, H, zoom=1.0 + 0.12 * tt)
            d = ImageDraw.Draw(im)
            a = ease((t - 5.4) / 0.4)
            if a > 0: pill(d, W / 2, 1600 + (1 - a) * 60, "So we put it on a shirt.", font(FB, 52), DARK, CREAM)
        elif t < 11.2:
            tt = (t - 8.4) / 2.8
            im = cover(model, W, H, zoom=1.15, cx=0.5, cy=0.15 + 0.2 * tt)
            d = ImageDraw.Draw(im)
            a = ease((t - 8.6) / 0.4)
            if a > 0: pill(d, W / 2, 1560 + (1 - a) * 60, "Say it without saying it.", font(FB, 56), DARK, CREAM)
        else:
            tt = t - 11.2
            im = Image.new("RGB", (W, H), DARK); d = ImageDraw.Draw(im)
            a = ease(tt / 0.5)
            im.paste(lg, (W // 2 - 180, int(420 + (1 - a) * 80)), lg)
            ctext(d, 900, "Chew With Your Mouth Closed tee", med, CREAM, W)
            ctext(d, 1100, "6 colors · Unisex S–5XL", sm, YEL, W)
            if tt > 0.6: pill(d, W / 2, 1300, "Shop: petpeevetees.com", font(FB, 56), RED, CREAM)
            if tt > 1.0: ctext(d, 1460, "link in bio", sm, CREAM, W)
        im.save(f"{fr}/{n:04d}.jpg", quality=90)
    p = f"{OUT}/post1_chew.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{fr}/%04d.jpg",
                    "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", p], check=True)
    # cover frame
    Image.open(f"{fr}/0060.jpg").save(f"{OUT}/post1_cover.jpg")
    return [p]

if __name__ == "__main__":
    import sys
    which = sys.argv[1:] or ["1", "2", "3"]
    if "2" in which: print(carousel())
    if "3" in which: print(poll())
    if "1" in which: print(video())
