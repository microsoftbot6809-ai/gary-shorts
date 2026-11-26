from gfx import *
GROUND = 1250
def new(top, bot): return canvas_from(gradient(top, bot))
def shade(c, k): return tuple(max(0, min(255, int(v * k))) for v in c[:3])
def cloud(L, x, y, s=1.0, col=(255, 255, 255, 235)):
    for dx, dy, r in [(-60, 10, 45), (-20, -15, 58), (30, -5, 52), (70, 12, 40), (0, 20, 50)]:
        L.d.ellipse([(x + (dx - r) * s) * S, (y + (dy - r) * s) * S, (x + (dx + r) * s) * S, (y + (dy + r) * s) * S], fill=col)
def tree(L, x, base, h, leaf=(70, 170, 80), trunk=(120, 80, 50)):
    L.rect(x - h * 0.06, base - h * 0.45, x + h * 0.06, base, fill=trunk, ink=INK, w=5)
    for dx, dy, r in [(0, -0.62, 0.34), (-0.2, -0.45, 0.26), (0.2, -0.45, 0.26)]:
        L.ell(x + dx * h, base + dy * h, r * h, r * h, fill=leaf, ink=INK, w=5)
def pine(L, x, base, h, col=(40, 120, 80), snow=False):
    L.rect(x - 14, base - 30, x + 14, base, fill=(110, 70, 45))
    for i in range(3):
        y1 = base - 30 - i * h * 0.27; w = h * (0.34 - i * 0.08)
        L.poly([(x - w, y1), (x + w, y1), (x, y1 - h * 0.42)], fill=col, ink=INK, w=5)
        if snow: L.poly([(x - w * 0.55, y1 - h * 0.17), (x + w * 0.55, y1 - h * 0.17), (x, y1 - h * 0.42)], fill=(250, 252, 255))
def bldg(L, x0, y0, x1, y1, col, win=(255, 230, 120), rs=7, lit=0.6, seed=1):
    rr = random.Random(seed)
    L.rect(x0, y0, x1, y1, fill=col, ink=INK, w=5)
    cols = max(1, int((x1 - x0) / 70)); rows = max(1, int((y1 - y0) / 90))
    for r in range(rows):
        for c in range(cols):
            wx = x0 + 18 + c * ((x1 - x0 - 36) / cols); wy = y0 + 24 + r * 90
            if wy + 50 < y1: L.rect(wx, wy, wx + 36, wy + 50, fill=win if rr.random() < lit else shade(col, 0.7), r=3)
def floor_lines(L, y0, col, n=8):
    for i in range(1, n):
        y = y0 + (H - y0) * (i / n) ** 1.4
        L.d.line([0, y * S, W * S, y * S], fill=col + (90,), width=int(4 * S))

def th_bedroom(L):
    L.rect(0, GROUND, W, H, fill=(184, 134, 96)); floor_lines(L, GROUND, (120, 80, 50))
    L.rect(0, GROUND - 14, W, GROUND + 10, fill=(240, 236, 250), ink=INK, w=4)
    L.rect(640, 330, 960, 700, fill=(20, 30, 80), ink=INK, w=10, r=14)
    stars(L, 0, seed=5, n=14, y0=350, y1=680, alpha=0.8); L.ell(870, 450, 45, 45, fill=(255, 250, 210))
    L.line([(800, 335), (800, 695)], fill=INK, w=8); L.line([(645, 515), (955, 515)], fill=INK, w=8)
    L.rect(90, 760, 520, 980, fill=(255, 210, 90), ink=INK, w=6, r=10); L.rect(110, 790, 500, 940, fill=(255, 120, 150), ink=INK, w=5, r=8)
    L.rect(60, 1080, 560, 1230, fill=(90, 120, 220), ink=INK, w=7, r=20); L.rect(60, 1040, 190, 1130, fill=(255, 255, 255), ink=INK, w=6, r=24)
    L.rect(60, 1230, 90, 1280, fill=(90, 60, 40)); L.rect(530, 1230, 560, 1280, fill=(90, 60, 40))
def th_kitchen(L):
    L.rect(0, 0, W, 1000, fill=(255, 236, 190))
    for i in range(0, W, 120):
        L.d.line([i * S, 0, i * S, 1000 * S], fill=(230, 205, 150, 255), width=int(4 * S))
    for j in range(0, 1000, 120):
        L.d.line([0, j * S, W * S, j * S], fill=(230, 205, 150, 255), width=int(4 * S))
    L.rect(0, GROUND - 260, W, GROUND, fill=(140, 100, 70), ink=INK, w=6); L.rect(0, GROUND - 280, W, GROUND - 250, fill=(235, 235, 240), ink=INK, w=6)
    L.rect(0, GROUND, W, H, fill=(220, 200, 170)); floor_lines(L, GROUND, (150, 120, 90))
    L.rect(70, 330, 400, 900, fill=(240, 245, 250), ink=INK, w=8, r=24); L.line([(70, 600), (400, 600)], fill=INK, w=7); L.rect(350, 420, 372, 540, fill=(160, 170, 185), r=8); L.rect(350, 650, 372, 800, fill=(160, 170, 185), r=8)
    L.rect(600, 300, 960, 640, fill=(150, 215, 255), ink=INK, w=10, r=12); cloud(L, 760, 420, 0.9)
def th_street(L):
    L.im = gradient((255, 190, 140), (255, 235, 200)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    cols = [(120, 140, 200), (200, 120, 130), (240, 190, 100), (110, 170, 150), (170, 130, 200)]
    x = -40; i = 0
    while x < W:
        w = 180 + (i * 53) % 120; h = 520 + (i * 97) % 380
        bldg(L, x, GROUND - 80 - h, x + w, GROUND - 80, cols[i % 5], seed=i); x += w + 8; i += 1
    L.rect(0, GROUND - 80, W, GROUND + 30, fill=(200, 200, 205), ink=INK, w=6); L.rect(0, GROUND + 30, W, H, fill=(80, 85, 95))
    for k in range(0, W, 220): L.rect(k, 1650, k + 120, 1672, fill=(250, 220, 90))
def th_park(L):
    L.rect(0, GROUND - 250, W, GROUND, fill=(110, 200, 110))
    L.ell(300, GROUND - 100, 700, 220, fill=(90, 185, 100)); L.ell(900, GROUND - 80, 600, 200, fill=(105, 195, 105))
    L.rect(0, GROUND - 120, W, H, fill=(95, 190, 95))
    L.poly([(430, GROUND - 120), (650, GROUND - 120), (900, H), (120, H)], fill=(235, 215, 170))
    for x, h in [(110, 520), (960, 600), (300, 380), (780, 400)]: tree(L, x, GROUND - 30, h, leaf=(60 + x % 40, 165, 75))
    rr = random.Random(4)
    for i in range(30): L.ell(rr.uniform(0, W), rr.uniform(GROUND, H), 9, 9, fill=rr.choice([(255, 120, 150), (255, 230, 90), (255, 255, 255)]))
def th_school(L):
    L.rect(0, 0, W, GROUND, fill=(215, 225, 190)); L.rect(0, GROUND - 40, W, GROUND, fill=(150, 160, 130))
    L.rect(0, GROUND, W, H, fill=(205, 190, 160)); floor_lines(L, GROUND, (150, 135, 110))
    for i in range(5):
        x = 20 + i * 210; L.rect(x, 380, x + 190, GROUND - 60, fill=(80, 130, 190) if i % 2 == 0 else (200, 90, 80), ink=INK, w=6)
        L.rect(x + 40, 440, x + 150, 480, fill=shade((80, 80, 90), 1), r=6); L.ell(x + 150, 700, 10, 10, fill=(240, 240, 240))
    L.ell(540, 250, 95, 95, fill=(255, 255, 255), ink=INK, w=9); L.line([(540, 250), (540, 185)], w=8); L.line([(540, 250), (590, 270)], w=8)
def th_beach(L):
    L.rect(0, GROUND - 330, W, GROUND - 100, fill=(60, 170, 220)); L.rect(0, GROUND - 330, W, GROUND - 300, fill=(120, 210, 240))
    L.rect(0, GROUND - 120, W, H, fill=(245, 220, 160)); L.d.line([0, (GROUND - 120) * S, W * S, (GROUND - 120) * S], fill=(255, 255, 255, 255), width=int(14 * S))
    L.ell(840, 270, 120, 120, fill=(255, 225, 80), ink=(255, 190, 50), w=10)
    L.line([(160, GROUND + 250), (200, GROUND - 330)], fill=(120, 70, 40), w=22)
    for a in range(-2, 3): L.poly([(190, GROUND - 330), (190 + a * 130, GROUND - 400 + abs(a) * 40), (190 + a * 130 + 60, GROUND - 350 + abs(a) * 40)], fill=(60, 160, 80), ink=INK, w=4)
def th_forest(L):
    L.im = gradient((20, 50, 60), (40, 90, 70)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    for i, x in enumerate(range(-50, W + 80, 130)): pine(L, x + (i * 37) % 60, GROUND - 120, 700 + (i * 71) % 250, col=(25 + i % 3 * 8, 85 + i % 4 * 10, 70))
    L.rect(0, GROUND - 120, W, H, fill=(45, 105, 70)); L.poly([(470, GROUND - 120), (610, GROUND - 120), (900, H), (180, H)], fill=(120, 95, 65))
def th_space(L):
    L.im = gradient((8, 6, 30), (40, 20, 70)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    L.ell(820, 430, 150, 150, fill=(230, 120, 90), ink=INK, w=6); L.ell(780, 400, 40, 30, fill=(210, 95, 70)); L.ell(870, 480, 28, 22, fill=(210, 95, 70))
    L.ell(190, 1000, 90, 90, fill=(110, 170, 240), ink=INK, w=6); L.ell(480, 1380, 700, 240, fill=(120, 120, 150), ink=INK, w=8)
    for x, y, r in [(300, 1330, 40), (650, 1400, 55), (900, 1330, 30)]: L.ell(x, y, r, r * 0.6, fill=(95, 95, 125))
def th_city_night(L):
    L.im = gradient((12, 14, 50), (80, 50, 110)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    L.ell(850, 330, 80, 80, fill=(255, 250, 215))
    x = -30; i = 0
    while x < W:
        w = 150 + (i * 61) % 110; h = 400 + (i * 113) % 560
        bldg(L, x, GROUND - h, x + w, GROUND + 40, (30 + i % 3 * 12, 30 + i % 4 * 6, 70 + i % 3 * 14), win=(255, 225, 120), lit=0.5, seed=i + 3); x += w + 6; i += 1
    L.rect(0, GROUND + 40, W, H, fill=(40, 40, 60))
def th_office(L):
    L.rect(0, 0, W, GROUND, fill=(220, 228, 240)); L.rect(0, GROUND, W, H, fill=(110, 120, 140)); floor_lines(L, GROUND, (80, 90, 110))
    L.rect(80, 300, 520, 800, fill=(150, 205, 250), ink=INK, w=10, r=8); L.line([(300, 300), (300, 800)], fill=INK, w=8)
    for k in range(3): bldg(L, 110 + k * 130, 560 - k * 40, 190 + k * 130, 800, (140, 160, 190), seed=k)
    L.rect(600, 420, 1000, 620, fill=(255, 255, 255), ink=INK, w=8, r=10); L.line([(640, 480), (900, 480)], fill=(200, 60, 60), w=8); L.line([(640, 540), (850, 540)], fill=(60, 90, 200), w=8)
    L.rect(0, GROUND - 40, W, GROUND + 10, fill=(160, 120, 90), ink=INK, w=6)
def th_snow(L):
    L.im = gradient((170, 200, 240), (235, 245, 255)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    L.ell(300, GROUND - 60, 800, 300, fill=(225, 235, 250), ink=(190, 205, 230), w=5); L.ell(900, GROUND - 40, 700, 260, fill=(215, 228, 248))
    for x, h in [(90, 560), (960, 650), (260, 380), (820, 420)]: pine(L, x, GROUND - 60, h, snow=True)
    L.rect(0, GROUND - 90, W, H, fill=(245, 250, 255)); floor_lines(L, GROUND, (200, 215, 240), 6)
def th_desert(L):
    L.im = gradient((255, 170, 100), (255, 225, 160)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    L.ell(540, 520, 190, 190, fill=(255, 245, 190), ink=(255, 200, 100), w=12)
    L.ell(200, GROUND - 40, 600, 260, fill=(235, 185, 115), ink=INK, w=5); L.ell(860, GROUND - 20, 700, 240, fill=(225, 170, 100))
    L.rect(0, GROUND - 100, W, H, fill=(240, 195, 125))
    for x, h in [(130, 360), (920, 300)]:
        L.rect(x - 28, GROUND - 100 - h, x + 28, GROUND - 60, fill=(80, 160, 90), ink=INK, w=6, r=26)
        L.rect(x - 100, GROUND - h * 0.7, x - 40, GROUND - h * 0.7 + 40, fill=(80, 160, 90), ink=INK, w=6, r=20); L.rect(x - 100, GROUND - h * 0.7 - 70, x - 66, GROUND - h * 0.7 + 30, fill=(80, 160, 90), ink=INK, w=6, r=16)
def th_cave(L):
    L.im = gradient((50, 35, 55), (95, 70, 85)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    for i in range(9):
        x = 60 + i * 120 + (i % 2) * 30; L.poly([(x - 55, 0), (x + 55, 0), (x, 240 + (i * 83) % 200)], fill=(70, 50, 70), ink=INK, w=5)
    L.rect(0, GROUND - 40, W, H, fill=(85, 65, 75)); floor_lines(L, GROUND, (60, 45, 55), 6)
    for x, y, c in [(170, GROUND - 40, (90, 220, 255)), (900, GROUND - 40, (255, 120, 220)), (780, GROUND - 40, (120, 255, 170))]:
        L.poly([(x - 40, y), (x - 15, y - 160), (x + 15, y - 190), (x + 45, y)], fill=c, ink=INK, w=5)
def th_underwater(L):
    L.im = gradient((70, 190, 240), (10, 70, 150)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    L.rect(0, GROUND, W, H, fill=(225, 205, 150)); L.ell(300, GROUND, 700, 90, fill=(235, 215, 160)); L.ell(900, GROUND + 20, 500, 80, fill=(215, 195, 140))
    for x in (90, 180, 930, 1010):
        pts = [(x + math.sin(k * 0.8) * 24, GROUND + 20 - k * 40) for k in range(9)]
        L.line(pts, fill=(60, 180, 110), w=22)
    for x, y, c in [(210, GROUND + 70, (255, 120, 150)), (820, GROUND + 90, (255, 170, 80))]:
        for a in range(5): L.ell(x + a * 28 - 56, y - abs(a - 2) * 10, 22, 36, fill=c, ink=INK, w=4)
def th_stage(L):
    L.im = gradient((60, 20, 80), (30, 10, 50)); L.d = ImageDraw.Draw(L.im, 'RGBA')
    for side in (0, 1):
        for k in range(6):
            x0 = (0 if side == 0 else W - 190) + k * 32 * (1 if side == 0 else 1)
            L.poly([(x0, 0), (x0 + 36, 0), (x0 + 30, GROUND - 60), (x0 - 6, GROUND - 60)], fill=(170 - k * 10, 20, 50), ink=None)
    L.rect(0, GROUND - 60, W, H, fill=(160, 110, 70)); floor_lines(L, GROUND - 60, (110, 70, 40), 8)
    L.rect(0, GROUND - 60, W, GROUND - 30, fill=(110, 70, 40))
def th_castle(L):
    L.rect(0, 0, W, GROUND, fill=(150, 150, 165)); 
    for j in range(0, GROUND, 110):
        for i in range(-1, 10): L.rect(i * 130 + (j // 110 % 2) * 65, j, i * 130 + 130 + (j // 110 % 2) * 65, j + 110, ink=(115, 115, 130), w=4)
    L.rect(0, GROUND, W, H, fill=(110, 100, 105)); floor_lines(L, GROUND, (80, 72, 78))
    for x in (150, 930):
        L.rect(x - 14, 470, x + 14, 620, fill=(90, 60, 40)); L.ell(x, 440, 38, 58, fill=(255, 170, 50), ink=(255, 110, 30), w=5)
    L.poly([(380, 330), (700, 330), (700, 760), (540, 690), (380, 760)], fill=(190, 40, 60), ink=INK, w=7)
def th_market(L):
    L.rect(0, 0, W, GROUND, fill=(245, 240, 225)); L.rect(0, GROUND, W, H, fill=(190, 195, 205)); floor_lines(L, GROUND, (150, 155, 165))
    rr = random.Random(9)
    for r in range(3):
        L.rect(0, 380 + r * 260, W, 400 + r * 260, fill=(150, 150, 160), ink=INK, w=4)
        for i in range(14): L.rect(i * 80 + 8, 300 + r * 260, i * 80 + 66, 380 + r * 260, fill=(rr.randint(90, 255), rr.randint(90, 255), rr.randint(90, 255)), ink=INK, w=4, r=6)
def th_sky(L):
    L.im = gradient((90, 170, 255), (200, 235, 255)); L.d = ImageDraw.Draw(L.im, 'RGBA')
def th_farm(L):
    L.rect(0, GROUND - 200, W, H, fill=(130, 200, 100)); L.ell(540, GROUND - 160, 900, 200, fill=(115, 190, 95))
    L.rect(560, 560, 960, 1000, fill=(200, 60, 60), ink=INK, w=8); L.poly([(540, 570), (760, 400), (980, 570)], fill=(160, 40, 50), ink=INK, w=8)
    L.rect(690, 760, 830, 1000, fill=(250, 240, 230), ink=INK, w=6); L.line([(690, 760), (830, 1000)], w=6); L.line([(830, 760), (690, 1000)], w=6)
    for x in range(20, 520, 90): L.rect(x, GROUND - 170, x + 22, GROUND - 40, fill=(250, 245, 235), ink=INK, w=4)
    L.rect(0, GROUND - 130, 540, GROUND - 105, fill=(250, 245, 235), ink=INK, w=4); L.rect(0, GROUND - 70, 540, GROUND - 45, fill=(250, 245, 235), ink=INK, w=4)
    L.rect(0, GROUND - 20, W, H, fill=(120, 195, 95)); floor_lines(L, GROUND, (95, 165, 75), 6)
def th_restaurant(L):
    L.rect(0, 0, W, GROUND, fill=(140, 40, 50)); L.rect(0, GROUND - 160, W, GROUND, fill=(110, 30, 40))
    L.rect(0, GROUND, W, H, fill=(235, 220, 190))
    for i in range(0, W, 140):
        for j in range(GROUND, H, 140):
            if ((i // 140) + (j - GROUND) // 140) % 2 == 0: L.rect(i, j, i + 140, j + 140, fill=(70, 50, 50))
    for x in (230, 540, 850):
        L.d.line([x * S, 0, x * S, 330 * S], fill=INK + (255,), width=int(5 * S)); L.poly([(x - 80, 430), (x + 80, 430), (x + 35, 330), (x - 35, 330)], fill=(255, 200, 80), ink=INK, w=6)
def th_gym(L):
    L.rect(0, 0, W, GROUND, fill=(230, 215, 190)); L.rect(0, GROUND, W, H, fill=(200, 140, 90)); floor_lines(L, GROUND, (140, 90, 55))
    for i in range(0, W, 180): L.rect(i, 230, i + 90, GROUND - 20, fill=(215, 195, 165), ink=None)
    L.rect(120, 420, 960, 440, fill=(120, 120, 130), ink=INK, w=4)
    for x in (300, 780): L.rect(x - 28, 400, x + 28, 480, fill=(40, 40, 50), ink=INK, w=5, r=8)
def th_void(L): pass

THEMES = {k[3:]: v for k, v in globals().items() if k.startswith('th_')}
_cache = {}
def get_bg(theme):
    key = theme if isinstance(theme, str) else tuple(theme[0]) + tuple(theme[1])
    if key not in _cache:
        if isinstance(theme, str):
            L = new((200, 220, 255), (230, 240, 255)); THEMES[theme](L)
        else:
            L = new(theme[0], theme[1])
        _cache[key] = L.im
    return _cache[key]
def bg_dyn(cv, theme, t):
    name = theme if isinstance(theme, str) else 'void'
    if name in ('park', 'beach', 'sky', 'farm', 'desert'):
        for i, (x0, y0, sp, s) in enumerate([(100, 330, 14, 1.0), (700, 500, 9, 1.3), (420, 210, 19, 0.8)]):
            cloud(cv, (x0 + t * sp) % (W + 400) - 200, y0 + (30 if name == 'sky' else 0), s)
    if name == 'sky':
        for i, (x0, y0, sp, s) in enumerate([(300, 1100, 24, 1.4), (800, 1500, 17, 1.8)]): cloud(cv, (x0 + t * sp) % (W + 500) - 250, y0, s)
    if name in ('space', 'city_night'): stars(cv, t, seed=11, n=70, y0=0, y1=800 if name == 'city_night' else 1250)
    if name == 'snow':
        rr = random.Random(3)
        for i in range(80):
            x0, sp, r, ph = rr.uniform(0, W), rr.uniform(120, 260), rr.uniform(4, 11), rr.uniform(0, 6)
            x = (x0 + math.sin(t * 1.5 + ph) * 40) % W; y = (rr.uniform(0, H) + t * sp) % H
            cv.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=(255, 255, 255, 230))
    if name == 'underwater':
        rr = random.Random(5)
        for i in range(30):
            x0, sp, r, ph = rr.uniform(0, W), rr.uniform(90, 220), rr.uniform(6, 22), rr.uniform(0, 6)
            x = x0 + math.sin(t * 2 + ph) * 25; y = H - ((rr.uniform(0, H) + t * sp) % H)
            cv.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=(255, 255, 255, 60), outline=(255, 255, 255, 190), width=int(3 * S))
    if name == 'forest':
        rr = random.Random(6)
        for i in range(24):
            x = rr.uniform(0, W) + math.sin(t * 0.8 + i) * 60; y = rr.uniform(500, 1500) + math.cos(t * 0.7 + i * 2) * 50
            a = int(140 + 110 * math.sin(t * 3 + i * 1.7)); r = 7
            cv.d.ellipse([(x - r * 2) * S, (y - r * 2) * S, (x + r * 2) * S, (y + r * 2) * S], fill=(255, 250, 120, max(0, a) // 3))
            cv.d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S], fill=(255, 250, 150, max(0, a)))
    if name == 'stage':
        for k, (x0, ph) in enumerate([(300, 0.0), (780, 1.7)]):
            sx = x0 + math.sin(t * 1.4 + ph) * 220
            cv.d.polygon([(sx * S, 0), ((sx - 70) * S, 0), ((x0 - 260 + (sx - x0) * 0.5) * S, 1500 * S), ((x0 + 260 + (sx - x0) * 0.5) * S, 1500 * S)], fill=(255, 255, 220, 36))
