from PIL import Image, ImageDraw, ImageFont, ImageChops
import numpy as np, math, random
S = 1.5
W, H = 1080, 1920
INK = (43, 34, 51)
FONT = "/usr/share/fonts/truetype/google-fonts/ofl/anton/Anton-Regular.ttf"
_fc = {}
def font(sz):
    sz = max(4, int(sz))
    if sz not in _fc: _fc[sz] = ImageFont.truetype(FONT, sz)
    return _fc[sz]
def lerp(a, b, t): return a + (b - a) * t
def lerpc(c1, c2, t): return tuple(int(lerp(c1[i], c2[i], max(0, min(1, t)))) for i in range(3))
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def ease_out_back(t):
    t = clamp(t); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2
def ease_io(t):
    t = clamp(t); return t * t * (3 - 2 * t)

class Layer:
    def __init__(self, w, h, rgb=False, bg=None):
        self.im = Image.new('RGB' if rgb else 'RGBA', (int(w * S), int(h * S)), bg if bg else ((0, 0, 0) if rgb else (0, 0, 0, 0)))
        self.d = ImageDraw.Draw(self.im, 'RGBA')
    def ell(self, cx, cy, rx, ry, fill=None, ink=None, w=6):
        self.d.ellipse([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S], fill=fill, outline=ink, width=int(w * S) if ink else 0)
    def rect(self, x0, y0, x1, y1, fill=None, ink=None, w=6, r=0):
        box = [x0 * S, y0 * S, x1 * S, y1 * S]
        if r: self.d.rounded_rectangle(box, radius=r * S, fill=fill, outline=ink, width=int(w * S) if ink else 0)
        else: self.d.rectangle(box, fill=fill, outline=ink, width=int(w * S) if ink else 0)
    def poly(self, pts, fill=None, ink=None, w=6):
        p = [(x * S, y * S) for x, y in pts]
        self.d.polygon(p, fill=fill)
        if ink: self.d.line(p + [p[0]], fill=ink, width=int(w * S), joint='curve')
    def line(self, pts, fill=INK, w=6, round_ends=True):
        p = [(x * S, y * S) for x, y in pts]
        self.d.line(p, fill=fill, width=max(1, int(w * S)), joint='curve')
        if round_ends:
            for x, y in (p[0], p[-1]):
                r = w * S / 2; self.d.ellipse([x - r, y - r, x + r, y + r], fill=fill)
    def chord(self, cx, cy, rx, ry, a0, a1, fill=None, ink=None, w=6):
        self.d.chord([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S], a0, a1, fill=fill, outline=ink, width=int(w * S) if ink else 0)
    def arc(self, cx, cy, rx, ry, a0, a1, fill=INK, w=6):
        self.d.arc([(cx - rx) * S, (cy - ry) * S, (cx + rx) * S, (cy + ry) * S], a0, a1, fill=fill, width=int(w * S))
    def text(self, x, y, s, size, fill=(255, 255, 255), stroke=INK, sw=10, anchor='mm'):
        self.d.text((x * S, y * S), s, font=font(size * S), fill=fill, stroke_width=int(sw * S), stroke_fill=stroke, anchor=anchor)

def gradient(top, bot, h=H, w=W):
    ys = np.linspace(0, 1, int(h * S))[:, None, None]
    a = np.array(top, np.float32)[None, None, :]; b = np.array(bot, np.float32)[None, None, :]
    arr = (a + (b - a) * ys) * np.ones((1, int(w * S), 1), np.float32)
    return Image.fromarray(arr.astype(np.uint8), 'RGB')

def canvas_from(img):
    c = Layer(W, H, rgb=True); c.im = img.copy(); c.d = ImageDraw.Draw(c.im, 'RGBA'); return c

def paste(cv, spr, x, y, anchor, scale=1.0, rot=0.0, sx=1.0, sy=1.0):
    w, h = spr.size
    if scale != 1 or sx != 1 or sy != 1:
        nw, nh = max(1, int(w * scale * sx)), max(1, int(h * scale * sy))
        spr = spr.resize((nw, nh), Image.BILINEAR)
        ax, ay = anchor[0] * S * scale * sx, anchor[1] * S * scale * sy
    else:
        ax, ay = anchor[0] * S, anchor[1] * S
    w, h = spr.size
    if abs(rot) > 0.01:
        R = int(2 * max(ax, w - ax, ay, h - ay)) + 4
        pad = Image.new('RGBA', (R, R), (0, 0, 0, 0))
        pad.paste(spr, (int(R / 2 - ax), int(R / 2 - ay)))
        pad = pad.rotate(rot, resample=Image.BILINEAR)
        cv.im.paste(pad, (int(x * S - R / 2), int(y * S - R / 2)), pad)
    else:
        cv.im.paste(spr, (int(x * S - ax), int(y * S - ay)), spr)

# ---------------------------------------------------------------- GARY
SKIN = (255, 207, 160); GREEN = (150, 205, 85); RED = (255, 115, 100); SHIRT = (70, 130, 230); HAIR = (95, 60, 40)
GAS_C = (150, 200, 70)

def helmet_layer(gas=0.0, phase=0.0, open_visor=False):
    sz = 620; L = Layer(sz, sz); c = sz / 2; r = 235
    if gas > 0:
        g = Layer(sz, sz)
        g.ell(c, c, r - 6, r - 6, fill=(GAS_C[0], GAS_C[1], GAS_C[2], int(215 * clamp(gas))))
        rr = random.Random(7)
        for i in range(10):
            a = rr.random() * 6.28 + phase * (0.6 + rr.random()); d = rr.random() * 150
            rad = (40 + rr.random() * 60) * (0.5 + gas)
            g.ell(c + math.cos(a) * d, c + math.sin(a) * d, rad, rad, fill=(190, 225, 90, int(150 * clamp(gas))), ink=(110, 160, 40, int(160 * clamp(gas))), w=4)
        m = Image.new('L', g.im.size, 0); ImageDraw.Draw(m).ellipse([(c - r + 4) * S, (c - r + 4) * S, (c + r - 4) * S, (c + r - 4) * S], fill=255)
        g.im.putalpha(ImageChops.multiply(g.im.split()[3], m))
        L.im = Image.alpha_composite(L.im, g.im)
    gl = Layer(sz, sz)
    gl.ell(c, c, r, r, fill=(200, 235, 255, 55))
    L.im = Image.alpha_composite(L.im, gl.im)
    d = ImageDraw.Draw(L.im, 'RGBA')
    d.ellipse([(c - r) * S, (c - r) * S, (c + r) * S, (c + r) * S], outline=(235, 245, 255, 255), width=int(10 * S))
    d.ellipse([(c - r - 5) * S, (c - r - 5) * S, (c + r + 5) * S, (c + r + 5) * S], outline=INK + (255,), width=int(5 * S))
    d.arc([(c - r + 30) * S, (c - r + 30) * S, (c + r - 30) * S, (c + r - 30) * S], 200, 260, fill=(255, 255, 255, 230), width=int(14 * S))
    d.arc([(c - r + 30) * S, (c - r + 30) * S, (c + r - 30) * S, (c + r - 30) * S], 270, 285, fill=(255, 255, 255, 200), width=int(14 * S))
    return L.im, (c, c)

def gary(mouth='neutral', open_=0.0, look=(0, 0), belly=1.0, skin=SKIN, arms='down', arm_t=0.0, helmet=False, gas=0.0,
         lid=0.0, squint=False, spiral=None, wind=0.0, legs_t=0.0, brow=None, sweat=False, gphase=0.0):
    PW, PH = 760, 900; cx, cy = 380, 430
    L = Layer(PW, PH)
    rx = 168 * belly; ry = 190 * (1 + (belly - 1) * 0.6)
    skin_d = tuple(int(v * 0.88) for v in skin)
    for sgn in (-1, 1):
        off = math.sin(legs_t + (0 if sgn < 0 else 2.2)) * 28
        L.rect(cx + sgn * 75 - 28 + off * 0.3, cy + ry - 30, cx + sgn * 75 + 28 + off * 0.3, cy + ry + 55, fill=skin_d, ink=INK, w=6, r=20)
        L.ell(cx + sgn * 85 + off, cy + ry + 62, 56, 27, fill=(120, 70, 50), ink=INK, w=6)
    def arm(sgn, pts):
        L.line(pts, fill=INK, w=50)
        L.line(pts, fill=skin, w=36)
        hx, hy = pts[-1]; L.ell(hx, hy, 31, 31, fill=skin, ink=INK, w=6)
    sh = lambda sgn: (cx + sgn * (rx - 18), cy + 20)
    w_ = math.sin(arm_t)
    if arms == 'down':
        for s in (-1, 1): arm(s, [sh(s), (cx + s * (rx + 22), cy + 90), (cx + s * (rx + 30), cy + 150)])
    elif arms == 'up':
        for s in (-1, 1): arm(s, [sh(s), (cx + s * (rx + 55), cy - 60), (cx + s * (rx + 85 + 12 * w_), cy - 190 - 10 * w_)])
    elif arms == 'behind':
        for s in (-1, 1): arm(s, [sh(s), (cx + s * (rx + 85), cy - 70), (cx + s * 62, cy - 175)])
    elif arms == 'type':
        for s in (-1, 1): arm(s, [sh(s), (cx + s * (rx - 10), cy + 120), (cx + s * (60 + 15 * math.sin(arm_t + s)), cy + 175 + 8 * math.sin(arm_t * 2 + s))])
    elif arms == 'hold':
        for s in (-1, 1): arm(s, [sh(s), (cx + s * (rx - 25), cy + 110), (cx + s * 55, cy + 120)])
    L.ell(cx, cy, rx, ry, fill=skin, ink=INK, w=7)
    L.chord(cx, cy, rx - 3, ry - 3, 8, 172, fill=SHIRT)
    for k in range(3):
        yy = cy + ry * (0.35 + 0.22 * k)
        half = rx * math.sqrt(max(0, 1 - ((yy - cy) / ry) ** 2)) - 8
        L.line([(cx - half, yy), (cx + half, yy)], fill=(245, 245, 255), w=9, round_ends=False)
    L.ell(cx, cy, rx, ry, ink=INK, w=7)
    for i, dx in enumerate((-34, 0, 34)):
        bx, by = cx + dx * 1.2, cy - ry + 8
        ex = bx + (dx * 0.8 + [-12, 6, 18][i]) * (1 + wind * 0.8)
        ey = by - [48, 70, 44][i] * (1 - wind * 0.55)
        L.line([(bx, by), ((bx + ex) / 2 + 6, (by + ey) / 2 - 4), (ex, ey)], fill=HAIR, w=15)
    ey0 = cy - ry * 0.34
    for s in (-1, 1):
        ex = cx + s * 62
        if squint:
            L.line([(ex - s * 28, ey0 - 28), (ex + s * 22, ey0), (ex - s * 28, ey0 + 28)], fill=INK, w=11)
            continue
        L.ell(ex, ey0, 50, 60, fill=(255, 255, 255), ink=INK, w=6)
        if spiral is not None:
            pts = []
            for k in range(60):
                th = k * 0.32 + spiral; rr = 1.0 + k * 0.62
                pts.append((ex + math.cos(th) * rr, ey0 + math.sin(th) * rr))
            L.line(pts, fill=INK, w=5)
        else:
            px, py = ex + look[0] * 16, ey0 + look[1] * 16
            L.ell(px, py, 22, 25, fill=INK)
            L.ell(px - 7, py - 9, 7, 7, fill=(255, 255, 255))
        if lid > 0:
            top = ey0 - 60; bot = top + 2 * 60 * lid
            L.rect(ex - 53, top - 4, ex + 53, bot, fill=skin)
            L.line([(ex - 50, bot), (ex + 50, bot)], fill=INK, w=7, round_ends=False)
    if brow:
        by = ey0 - 82
        for s in (-1, 1):
            ex = cx + s * 62
            if brow == 'angry': pts = [(ex - s * 45, by - 22), (ex + s * 40, by + 14)]
            elif brow == 'worry': pts = [(ex - s * 45, by + 14), (ex + s * 40, by - 20)]
            else: pts = [(ex - 40, by - 12), (ex + 40, by - 12)]
            L.line(pts, fill=HAIR, w=15)
    mx, my = cx, cy + 48
    if mouth == 'neutral':
        L.arc(mx, my - 12, 34, 24, 20, 160, w=7)
    elif mouth == 'grin':
        L.chord(mx, my - 25, 70, 62, 0, 180, fill=INK)
        L.rect(mx - 52, my - 22, mx + 52, my - 4, fill=(255, 255, 255))
        L.ell(mx, my + 22, 28, 14, fill=(235, 100, 110))
        L.arc(mx, my - 25, 70, 62, 0, 180, w=7)
    elif mouth == 'open':
        hh = 14 + 60 * open_; ww = 36 + 26 * open_
        L.ell(mx, my + hh * 0.3, ww, hh, fill=INK)
        L.ell(mx, my + hh * 0.3 + hh * 0.5, ww * 0.6, hh * 0.4, fill=(235, 100, 110))
    elif mouth == 'scream':
        L.ell(mx, my + 25, 58, 82, fill=INK, ink=INK, w=6)
        L.ell(mx, my + 78, 38, 28, fill=(235, 100, 110))
    elif mouth == 'smug':
        L.line([(mx - 46, my + 2), (mx + 6, my + 12), (mx + 48, my - 20)], fill=INK, w=8)
        L.line([(mx + 48, my - 20), (mx + 56, my - 34)], fill=INK, w=6)
    elif mouth == 'clench':
        L.rect(mx - 66, my - 18, mx + 66, my + 34, fill=(255, 255, 255), ink=INK, w=7, r=14)
        for k in range(-3, 4): L.line([(mx + k * 18, my - 16), (mx + k * 18, my + 32)], fill=INK, w=4, round_ends=False)
        L.line([(mx - 64, my + 8), (mx + 64, my + 8)], fill=INK, w=4, round_ends=False)
    elif mouth == 'sick':
        pts = [(mx - 52 + i * 8.7, my + 8 + math.sin(i * 1.3 + gphase) * 12) for i in range(13)]
        L.line(pts, fill=INK, w=8)
    elif mouth == 'oh':
        L.ell(mx, my + 12, 28, 36, fill=INK)
    if sweat:
        sx, sy = cx + rx * 0.72, cy - ry * 0.55
        L.poly([(sx, sy - 48), (sx - 20, sy), (sx + 20, sy)], fill=(120, 200, 255), ink=None)
        L.ell(sx, sy + 2, 20, 20, fill=(120, 200, 255))
    spr = L.im
    if helmet:
        hl, _ = helmet_layer(gas, gphase)
        spr = spr.copy()
        spr.alpha_composite(hl, (int((cx - 310) * S), int((cy - 350) * S)))
    return spr, (cx, cy)

# ---------------------------------------------------------------- effects
def puffs(cv, events, t, color=GAS_C):
    for ev in events:
        age = t - ev['t0']
        if age < 0 or age > ev['life'] + 0.3: continue
        rr = random.Random(ev.get('seed', 1))
        for i in range(ev.get('n', 7)):
            ox, oy, rs, dl, dx, dy = rr.uniform(-1, 1), rr.uniform(-1, 1), rr.random(), rr.random() * 0.25, rr.uniform(-1, 1), rr.uniform(-1, 1)
            a = age - dl
            if a < 0 or a > ev['life']: continue
            u = a / ev['life']
            x = ev['x'] + ev.get('vx', 0) * a + ox * ev.get('spread', 40) + dx * ev.get('drift', 60) * u
            y = ev['y'] + ev.get('vy', 0) * a + oy * ev.get('spread', 40) * 0.5 + dy * ev.get('drift', 60) * u * 0.5
            rad = ev['size'] * (0.45 + rs * 0.55) * (0.35 + 1.0 * math.sqrt(u))
            al = int(215 * (1 - u) ** 1.1)
            col = lerpc(ev.get('color', color), (205, 215, 95) if ev.get('color') is None else (255, 255, 255), rs)
            cv.d.ellipse([(x - rad) * S, (y - rad) * S, (x + rad) * S, (y + rad) * S], fill=col + (al,), outline=(95, 140, 40, int(al * 0.9)) if ev.get('color') is None else (60, 40, 40, int(al * 0.6)), width=int(4 * S))

def popup(cv, text, x, y, t, t0, dur, size=150, rot=-8, fill=(255, 226, 60)):
    a = t - t0
    if a < 0 or a > dur: return
    k = ease_out_back(a / 0.2) * (1 if a < dur - 0.15 else clamp((dur - a) / 0.15))
    if k <= 0.02: return
    f = font(size * S * k)
    w = int(f.getlength(text) + 80 * S); h = int(size * S * 1.5 * max(k, 0.3))
    lay = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.text((w / 2, h / 2), text, font=f, fill=fill, stroke_width=int(12 * S * k), stroke_fill=INK, anchor='mm')
    lay = lay.rotate(rot, resample=Image.BILINEAR, expand=True)
    cv.im.paste(lay, (int(x * S - lay.width / 2), int(y * S - lay.height / 2)), lay)

def bubble(cv, text, x, y, t, t0, dur, size=80, tail=(0, 60), rot=0, color=(200, 30, 40)):
    a = t - t0
    if a < 0 or a > dur: return
    k = ease_out_back(a / 0.18)
    f = font(size * S); tw = f.getlength(text) / S; bw, bh = tw + 70, size + 50
    w, h = int((bw + 120) * S * k) + 4, int((bh + 120) * S * k) + 4
    if w < 8: return
    lay = Layer(bw + 120, bh + 120)
    cx, cy = (bw + 120) / 2, (bh + 120) / 2 - 15
    tb = tail[0] * 0.75
    lay.poly([(cx + tb - 20, cy + bh / 2 - 6), (cx + tail[0], cy + bh / 2 + tail[1]), (cx + tb + 28, cy + bh / 2 - 6)], fill=(255, 255, 255), ink=INK, w=6)
    lay.rect(cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2, fill=(255, 255, 255), ink=INK, w=6, r=40)
    lay.rect(cx + tb - 17, cy + bh / 2 - 10, cx + tb + 25, cy + bh / 2 + 3, fill=(255, 255, 255))
    lay.text(cx, cy + 2, text, size, fill=color, stroke=(255, 255, 255), sw=0)
    im = lay.im.resize((w, h), Image.BILINEAR)
    if rot: im = im.rotate(rot, resample=Image.BILINEAR, expand=True)
    cv.im.paste(im, (int(x * S - im.width / 2), int(y * S - im.height / 2)), im)

def flash(cv, a):
    if a <= 0: return
    ov = Image.new('RGBA', cv.im.size, (255, 255, 255, int(255 * clamp(a))))
    cv.im.paste(ov, (0, 0), ov)

def ring(cv, x, y, t, t0, dur=0.6, maxr=900, w=40):
    a = t - t0
    if a < 0 or a > dur: return
    u = a / dur; r = maxr * (1 - (1 - u) ** 3); al = int(255 * (1 - u))
    cv.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], outline=(255, 255, 255, al), width=max(1, int(w * (1 - u) * S)))

def stars(cv, t, seed=3, n=90, y0=0, y1=H, alpha=1.0):
    rr = random.Random(seed)
    for i in range(n):
        x, y, s, ph = rr.uniform(0, W), rr.uniform(y0, y1), rr.uniform(2, 6), rr.uniform(0, 6)
        tw = 0.55 + 0.45 * math.sin(t * 3 + ph)
        al = int(255 * tw * alpha)
        cv.d.ellipse([(x - s) * S, (y - s) * S, (x + s) * S, (y + s) * S], fill=(255, 255, 240, al))
        if s > 4.5: cv.d.line([(x - s * 2.4) * S, y * S, (x + s * 2.4) * S, y * S], fill=(255, 255, 240, al // 2), width=int(2 * S))

def captions(cv, chunks, t):
    for ch in chunks:
        if ch['ts'] - 0.02 <= t < ch['te'] + 0.12:
            words = ch['words']; size = 118
            k = 0.82 + 0.18 * ease_out_back(clamp((t - ch['ts']) / 0.14)) if t >= ch['ts'] else 0.8
            f = font(size * S * k)
            gap = 28 * S * k
            widths = [f.getlength(w[0].upper()) for w in words]
            total = sum(widths) + gap * (len(words) - 1)
            if total > 960 * S:
                k *= 960 * S / total
                f = font(size * S * k); gap = 28 * S * k
                widths = [f.getlength(w[0].upper()) for w in words]
                total = sum(widths) + gap * (len(words) - 1)
            x = W * S / 2 - total / 2; y = 360 * S
            for (w, ws, we), wd in zip(words, widths):
                active = ws - 0.02 <= t < we
                col = (255, 226, 60) if active else (255, 255, 255)
                cv.d.text((x, y), w.upper(), font=f, fill=col, stroke_width=int(14 * S * k), stroke_fill=INK, anchor='lm')
                x += wd + gap
            return
