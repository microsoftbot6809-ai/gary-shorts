import math, random, re
import numpy as np
from gfx import *
import bgs
EMO = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
_ef = ImageFont.truetype(EMO, 109); _ec = {}
def emoji(ch):
    if ch not in _ec:
        im = Image.new('RGBA', (136, 128), (0, 0, 0, 0)); ImageDraw.Draw(im).text((68, 64), ch, font=_ef, embedded_color=True, anchor='mm')
        bb = im.getbbox(); _ec[ch] = im.crop(bb) if bb else im
    return _ec[ch]
def put_emoji(cv, ch, x, y, size, rot=0.0, flip=False, alpha=1.0):
    if size < 2 or alpha <= 0: return
    e = emoji(ch); k = size * S / 109.0
    im = e.resize((max(1, int(e.width * k)), max(1, int(e.height * k))), Image.BICUBIC)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if abs(rot) > 0.01: im = im.rotate(rot, resample=Image.BILINEAR, expand=True)
    if alpha < 1: im.putalpha(im.split()[3].point(lambda v: int(v * alpha)))
    cv.im.paste(im, (int(x * S - im.width / 2), int(y * S - im.height / 2)), im)

WHITE = (255, 255, 255)
MOODS = {
 'neutral': ('open', None, 'smile_s'), 'happy': ('arc', None, 'grin'), 'grin': ('open', 'up', 'grin'), 'shock': ('wide', 'up', 'oh'),
 'scream': ('wide', 'up', 'scream'), 'angry': ('open_s', 'angry', 'clench'), 'sad': ('open_d', 'worry', 'frown'), 'cry': ('open_d', 'worry', 'wail'),
 'smug': ('half', None, 'smug'), 'sick': ('open', 'worry', 'wavy'), 'sleepy': ('closed', None, 'oh_s'), 'dizzy': ('spiral', None, 'wavy'),
 'love': ('heart', None, 'grin'), 'scared': ('wide', 'worry', 'wavy'), 'evil': ('open_s', 'angry', 'grin'), 'dead': ('x', None, 'flat'),
 'proud': ('arc', 'up', 'smile'), 'confused': ('open', 'tilt', 'wavy_s'), 'wow': ('wide', 'up', 'grin'), 'yum': ('arc', None, 'tongue'), 'think': ('open', 'tilt', 'flat'),
}
BODY = {'blob': (150, 140, 0.0), 'tall': (118, 185, 0.08), 'pear': (150, 150, 0.30), 'box': (140, 140, -1), 'round': (165, 165, 0.0), 'small': (120, 115, 0.05)}
PW, PH, CX, CY = 640, 800, 320, 420

def _egg(rx, ry, tap, n=72):
    pts = []
    for i in range(n):
        th = i / n * 2 * math.pi; s = math.sin(th)
        pts.append((CX + rx * math.cos(th) * (1 + tap * s), CY + ry * s))
    return pts
def _mix(c, d, k): return tuple(int(c[i] * (1 - k) + d[i] * k) for i in range(3))

def draw_char(spec, mood='neutral', mo=0.0, look=(0, 0), arms='down', arm_t=0.0, legs_t=0.0, blink=False, sweat=False, spin=0.0, held=False):
    L = Layer(PW, PH)
    col = spec.get('color', (120, 200, 120)); body = spec.get('body', 'blob'); rx, ry, tap = BODY[body]
    rx *= spec.get('w', 1.0); ry *= spec.get('h', 1.0)
    eyes, brow, mouth = MOODS.get(mood, MOODS['neutral'])
    if mood == 'sick': col = _mix(col, (150, 200, 90), 0.45)
    if mood in ('angry',): col = _mix(col, (255, 110, 100), 0.18)
    dark = _mix(col, (0, 0, 0), 0.18); belly = _mix(col, WHITE, 0.55); shoe = spec.get('shoe', (60, 50, 70))
    top = CY - ry
    ears = spec.get('ears')
    if ears == 'cat':
        for s in (-1, 1): L.poly([(CX + s * rx * 0.85, CY - ry * 0.45), (CX + s * rx * 0.75, top - 70), (CX + s * rx * 0.18, top + 8)], fill=col, ink=INK, w=6); L.poly([(CX + s * rx * 0.72, top - 8), (CX + s * rx * 0.68, top - 44), (CX + s * rx * 0.36, top + 4)], fill=(255, 170, 190))
    elif ears == 'bunny':
        for s in (-1, 1): L.ell(CX + s * rx * 0.38, top - 70, 38, 105, fill=col, ink=INK, w=6); L.ell(CX + s * rx * 0.38, top - 62, 17, 78, fill=(255, 170, 190))
    elif ears == 'bear':
        for s in (-1, 1): L.ell(CX + s * rx * 0.68, top + 22, 50, 50, fill=col, ink=INK, w=6); L.ell(CX + s * rx * 0.68, top + 26, 26, 26, fill=(255, 190, 170))
    elif ears == 'dog':
        for s in (-1, 1): L.ell(CX + s * (rx + 6), CY - ry * 0.35, 40, 85, fill=dark, ink=INK, w=6)
    if spec.get('horns'):
        for s in (-1, 1): L.poly([(CX + s * rx * 0.55, top + 20), (CX + s * rx * 0.85, top - 70), (CX + s * rx * 0.25, top + 4)], fill=(250, 240, 220), ink=INK, w=6)
    if spec.get('antenna'):
        L.line([(CX, top + 6), (CX + 10, top - 85)], fill=INK, w=9); L.ell(CX + 10, top - 95, 24, 24, fill=(255, 90, 90), ink=INK, w=6)
    # legs
    for s in (-1, 1):
        off = math.sin(legs_t + (0 if s < 0 else math.pi)) * 30
        L.rect(CX + s * rx * 0.42 - 26 + off * 0.3, CY + ry - 26, CX + s * rx * 0.42 + 26 + off * 0.3, CY + ry + 50, fill=dark, ink=INK, w=6, r=18)
        L.ell(CX + s * rx * 0.42 + off + s * 8, CY + ry + 58, 52, 26, fill=shoe, ink=INK, w=6)
    # arms
    def arm(pts):
        L.line(pts, fill=INK, w=46); L.line(pts, fill=col, w=33); hx, hy = pts[-1]; L.ell(hx, hy, 29, 29, fill=col, ink=INK, w=6)
    shx = rx - 14; w_ = math.sin(arm_t)
    for s in (-1, 1):
        sh = (CX + s * shx, CY + 10)
        if arms == 'down': arm([sh, (CX + s * (rx + 20), CY + 80), (CX + s * (rx + 26), CY + 140)])
        elif arms == 'up': arm([sh, (CX + s * (rx + 50), CY - 70), (CX + s * (rx + 75 + 10 * w_), CY - 190 - 8 * w_)])
        elif arms == 'wave':
            if s > 0: arm([sh, (CX + s * (rx + 55), CY - 40), (CX + s * (rx + 70 + 25 * w_), CY - 150)])
            else: arm([sh, (CX + s * (rx + 20), CY + 80), (CX + s * (rx + 26), CY + 140)])
        elif arms == 'point':
            if s > 0: arm([sh, (CX + rx + 70, CY - 10), (CX + rx + 150, CY - 30)])
            else: arm([sh, (CX + s * (rx + 20), CY + 80), (CX + s * (rx + 26), CY + 140)])
        elif arms == 'hold': arm([sh, (CX + s * (rx - 20), CY + 100), (CX + s * 45, CY + 85)])
        elif arms == 'shrug': arm([sh, (CX + s * (rx + 40), CY + 20), (CX + s * (rx + 45), CY - 70 + 6 * w_)])
        elif arms == 'hips': arm([sh, (CX + s * (rx + 45), CY + 60), (CX + s * (rx * 0.62), CY + 100)])
        elif arms == 'cheer': arm([sh, (CX + s * (rx + 60), CY - 90), (CX + s * (rx + 40 + 20 * w_ * s), CY - 215 - 14 * abs(w_))])
        elif arms == 'face': arm([sh, (CX + s * (rx - 10), CY - 40), (CX + s * 62, CY - ry * 0.12)])
        elif arms == 'belly': arm([sh, (CX + s * (rx - 25), CY + 60), (CX + s * 58, CY + 70)])
        elif arms == 'run': arm([sh, (CX + s * (rx + 30), CY + 30 + 40 * math.sin(arm_t * 2 * s)), (CX + s * (rx + 10), CY + 90 + 60 * math.sin(arm_t * 2 * s))])
    # body
    if tap < 0: L.rect(CX - rx, CY - ry, CX + rx, CY + ry, fill=col, ink=INK, w=7, r=70)
    else: L.poly(_egg(rx, ry, tap), fill=col, ink=INK, w=7)
    if spec.get('belly', True): L.ell(CX, CY + ry * 0.42, rx * 0.52, ry * 0.4, fill=belly)
    if spec.get('stripes'):
        for k in range(3): L.line([(CX - rx * 0.78, CY - ry * 0.3 + k * 40), (CX - rx * 0.5, CY - ry * 0.3 + k * 40 + 6)], fill=dark, w=11)
    # face
    ex = rx * 0.40; ey = CY - ry * 0.16; er = min(44, rx * 0.30); eh = er * 1.2
    for s in (-1, 1):
        x = CX + s * ex
        if eyes in ('open', 'open_s', 'open_d', 'wide', 'half', 'spiral', 'heart'):
            rr = er * (1.18 if eyes == 'wide' else 1.0); hh = eh * (1.18 if eyes == 'wide' else (0.78 if eyes == 'open_s' else 1.0))
            L.ell(x, ey, rr, hh, fill=WHITE, ink=INK, w=6)
            if eyes == 'spiral':
                pts = [(x + math.cos(k * 0.34 + spin) * (1 + k * 0.5), ey + math.sin(k * 0.34 + spin) * (1 + k * 0.5)) for k in range(58)]; L.line(pts, fill=INK, w=5)
            elif eyes == 'heart':
                for hx in (-9, 9): L.ell(x + hx * 1.2, ey - 7, 12, 12, fill=(240, 60, 90))
                L.poly([(x - 21, ey - 2), (x + 21, ey - 2), (x, ey + 26)], fill=(240, 60, 90))
            else:
                p = 0.55 if eyes == 'wide' else 1.0; dy = 12 if eyes == 'open_d' else 0
                px, py = x + look[0] * 14, ey + look[1] * 14 + dy
                L.ell(px, py, 20 * p + 2, 23 * p + 2, fill=INK); L.ell(px - 6, py - 8, 6, 6, fill=WHITE)
            if eyes == 'half': L.rect(x - rr - 3, ey - hh - 4, x + rr + 3, ey - hh * 0.05, fill=col); L.line([(x - rr, ey - hh * 0.05), (x + rr, ey - hh * 0.05)], w=6, round_ends=False)
            if blink: L.ell(x, ey, rr + 4, hh + 4, fill=col); L.line([(x - rr, ey), (x + rr, ey)], w=7)
        elif eyes == 'arc': L.arc(x, ey + 12, er * 0.9, er * 0.8, 200, 340, w=9)
        elif eyes == 'closed': L.line([(x - er * 0.9, ey + 4), (x + er * 0.9, ey + 4)], w=8)
        elif eyes == 'x': L.line([(x - 22, ey - 22), (x + 22, ey + 22)], w=9); L.line([(x + 22, ey - 22), (x - 22, ey + 22)], w=9)
    if brow:
        by = ey - eh - 30
        for s in (-1, 1):
            x = CX + s * ex
            if brow == 'angry': pts = [(x - s * 40, by - 20), (x + s * 34, by + 16)]
            elif brow == 'worry': pts = [(x - s * 38, by + 16), (x + s * 34, by - 18)]
            elif brow == 'tilt': pts = [(x - 36, by + (4 if s < 0 else -14)), (x + 36, by + (-8 if s < 0 else 4))]
            else: pts = [(x - 36, by - 16), (x + 36, by - 16)]
            L.line(pts, fill=INK, w=12)
    mx, my = CX, CY + ry * 0.30
    if mo > 0.05 and mouth not in ('scream',):
        hh = 12 + 52 * mo; ww = 30 + 20 * mo
        L.ell(mx, my + hh * 0.4, ww, hh, fill=INK); L.ell(mx, my + hh * 0.4 + hh * 0.55, ww * 0.6, hh * 0.38, fill=(235, 100, 110))
    elif mouth == 'smile_s': L.arc(mx, my - 6, 36, 26, 20, 160, w=8)
    elif mouth == 'smile': L.arc(mx, my - 10, 50, 36, 15, 165, w=9)
    elif mouth == 'grin':
        L.chord(mx, my - 18, 58, 54, 0, 180, fill=INK); L.rect(mx - 44, my - 16, mx + 44, my - 2, fill=WHITE); L.ell(mx, my + 20, 24, 12, fill=(235, 100, 110)); L.arc(mx, my - 18, 58, 54, 0, 180, w=6)
    elif mouth == 'oh': L.ell(mx, my + 12, 24, 32, fill=INK)
    elif mouth == 'oh_s': L.ell(mx, my + 10, 14, 16, fill=INK)
    elif mouth == 'scream': L.ell(mx, my + 20, 50, 74 if mo < 0.05 else 60 + 30 * mo, fill=INK); L.ell(mx, my + 62, 32, 24, fill=(235, 100, 110))
    elif mouth == 'frown': L.arc(mx, my + 34, 36, 28, 200, 340, w=8)
    elif mouth == 'wail': L.ell(mx, my + 18, 38, 48, fill=INK); L.ell(mx, my + 52, 24, 16, fill=(235, 100, 110))
    elif mouth == 'smug': L.line([(mx - 40, my), (mx + 4, my + 10), (mx + 42, my - 18)], w=8)
    elif mouth == 'clench':
        L.rect(mx - 54, my - 12, mx + 54, my + 28, fill=WHITE, ink=INK, w=6, r=10)
        for k in range(-2, 3): L.line([(mx + k * 20, my - 10), (mx + k * 20, my + 26)], w=4, round_ends=False)
    elif mouth in ('wavy', 'wavy_s'):
        a = 10 if mouth == 'wavy' else 5; pts = [(mx - 46 + i * 7.7, my + 8 + math.sin(i * 1.4 + spin) * a) for i in range(13)]; L.line(pts, w=8)
    elif mouth == 'flat': L.line([(mx - 34, my + 8), (mx + 34, my + 8)], w=8)
    elif mouth == 'tongue':
        L.arc(mx, my - 10, 50, 36, 15, 165, w=9); L.ell(mx + 18, my + 24, 18, 24, fill=(240, 110, 120), ink=INK, w=5)
    if spec.get('blush'):
        for s in (-1, 1): L.ell(CX + s * (ex + 22), my - 16, 26, 15, fill=(255, 120, 140, 130))
    if spec.get('mustache'): L.poly([(mx - 70, my - 22), (mx, my - 34), (mx + 70, my - 22), (mx + 40, my - 2), (mx, my - 14), (mx - 40, my - 2)], fill=spec.get('mustachec', (90, 60, 40)), ink=INK, w=4)
    if spec.get('glasses'):
        for s in (-1, 1): L.ell(CX + s * ex, ey, er + 12, eh + 10, ink=INK, w=8, fill=(180, 220, 255, 70))
        L.line([(CX - ex + er + 10, ey), (CX + ex - er - 10, ey)], w=7)
    if spec.get('tie'): 
        L.poly([(CX, CY + ry * 0.62), (CX - 44, CY + ry * 0.52), (CX - 44, CY + ry * 0.76)], fill=(230, 60, 80), ink=INK, w=5); L.poly([(CX, CY + ry * 0.62), (CX + 44, CY + ry * 0.52), (CX + 44, CY + ry * 0.76)], fill=(230, 60, 80), ink=INK, w=5); L.ell(CX, CY + ry * 0.62, 13, 13, fill=(190, 30, 55), ink=INK, w=4)
    if sweat:
        sx, sy = CX + rx * 0.7, CY - ry * 0.5; L.poly([(sx, sy - 46), (sx - 19, sy), (sx + 19, sy)], fill=(120, 200, 255)); L.ell(sx, sy + 2, 19, 19, fill=(120, 200, 255))
    if mood == 'cry':
        for s in (-1, 1): L.rect(CX + s * ex - 6, ey + eh, CX + s * ex + 6, CY + ry * 0.22, fill=(120, 200, 255, 220), r=6)
    elif mood == 'sad':
        L.poly([(CX + ex + 12, ey + eh - 4), (CX + ex + 2, ey + eh + 34), (CX + ex + 24, ey + eh + 34)], fill=(120, 200, 255, 230))
    if spec.get('hair'):
        for dx, h in ((-34, 48), (0, 66), (34, 42)): L.line([(CX + dx, top + 10), (CX + dx * 1.3 + 8, top - h * 0.55), (CX + dx * 1.5 + 18, top - h)], fill=spec.get('hairc', (95, 60, 40)), w=14)
    # hats
    hat = spec.get('hat'); hc = spec.get('hatc', (230, 70, 70)); ty = top + 14
    if hat == 'cap':
        L.chord(CX, ty + 10, rx * 0.78, 110, 180, 360, fill=hc, ink=INK, w=6); L.rect(CX - 10, ty + 2, CX + rx * 1.05, ty + 24, fill=_mix(hc, (0, 0, 0), 0.2), ink=INK, w=6, r=10)
    elif hat == 'tophat':
        L.rect(CX - rx * 0.78, ty - 14, CX + rx * 0.78, ty + 16, fill=(40, 40, 50), ink=INK, w=6, r=8); L.rect(CX - rx * 0.52, ty - 130, CX + rx * 0.52, ty - 6, fill=(40, 40, 50), ink=INK, w=6, r=8); L.rect(CX - rx * 0.52, ty - 50, CX + rx * 0.52, ty - 22, fill=hc)
    elif hat == 'crown':
        L.poly([(CX - rx * 0.6, ty + 10), (CX - rx * 0.6, ty - 70), (CX - rx * 0.3, ty - 30), (CX, ty - 90), (CX + rx * 0.3, ty - 30), (CX + rx * 0.6, ty - 70), (CX + rx * 0.6, ty + 10)], fill=(255, 215, 60), ink=INK, w=6)
        for dx in (-0.6, 0, 0.6): L.ell(CX + dx * rx, ty - (70 if dx else 90) - 8, 11, 11, fill=(230, 60, 80), ink=INK, w=3)
    elif hat == 'chef':
        L.rect(CX - rx * 0.5, ty - 20, CX + rx * 0.5, ty + 14, fill=WHITE, ink=INK, w=6, r=6)
        for dx in (-0.4, 0, 0.4): L.ell(CX + dx * rx, ty - 62, 46, 52, fill=WHITE, ink=INK, w=6)
        L.rect(CX - rx * 0.5, ty - 24, CX + rx * 0.5, ty + 14, fill=WHITE, ink=INK, w=6, r=6)
    elif hat == 'party':
        L.poly([(CX - 70, ty + 12), (CX + 70, ty + 12), (CX + 8, ty - 150)], fill=hc, ink=INK, w=6); L.ell(CX + 8, ty - 152, 18, 18, fill=(255, 230, 90), ink=INK, w=4)
        for k in range(3): L.line([(CX - 40 + k * 38, ty - 4 - k * 6), (CX - 8 + k * 24, ty - 70 - k * 20)], fill=(255, 255, 255), w=8)
    elif hat == 'beanie':
        L.chord(CX, ty + 20, rx * 0.8, 105, 180, 360, fill=hc, ink=INK, w=6); L.rect(CX - rx * 0.8, ty + 10, CX + rx * 0.8, ty + 40, fill=_mix(hc, WHITE, 0.35), ink=INK, w=6, r=12); L.ell(CX, ty - 92, 26, 26, fill=WHITE, ink=INK, w=5)
    elif hat == 'helmet':
        L.chord(CX, ty + 30, rx * 0.95, 130, 180, 360, fill=(170, 175, 190), ink=INK, w=6); L.rect(CX - rx * 0.95, ty + 22, CX + rx * 0.95, ty + 44, fill=(130, 135, 150), ink=INK, w=6, r=8)
    elif hat == 'wizard':
        L.poly([(CX - rx * 0.7, ty + 12), (CX + rx * 0.7, ty + 12), (CX + 30, ty - 190)], fill=(110, 70, 190), ink=INK, w=6); L.ell(CX, ty + 12, rx * 0.95, 20, fill=(90, 55, 165), ink=INK, w=6)
        L.ell(CX - 10, ty - 50, 12, 12, fill=(255, 230, 90)); L.ell(CX + 24, ty - 110, 9, 9, fill=(255, 230, 90))
    elif hat == 'cowboy':
        L.ell(CX, ty + 12, rx * 1.1, 26, fill=(160, 110, 60), ink=INK, w=6); L.rect(CX - rx * 0.5, ty - 80, CX + rx * 0.5, ty + 10, fill=(175, 125, 70), ink=INK, w=6, r=24)
    elif hat == 'headband':
        L.rect(CX - rx * 0.86, ty + 24, CX + rx * 0.86, ty + 52, fill=hc, ink=INK, w=5, r=12)
    if spec.get('bow'): 
        L.poly([(CX + rx * 0.4, top + 10), (CX + rx * 0.4 + 52, top - 22), (CX + rx * 0.4 + 52, top + 42)], fill=(255, 110, 170), ink=INK, w=4); L.poly([(CX + rx * 0.4, top + 10), (CX + rx * 0.4 - 52, top - 22), (CX + rx * 0.4 - 52, top + 42)], fill=(255, 110, 170), ink=INK, w=4); L.ell(CX + rx * 0.4, top + 10, 14, 14, fill=(230, 70, 140), ink=INK, w=4)
    return L.im, (CX, CY), (CY + ry + 84)

_sc = {}
def char_sprite(spec, key, **kw):
    k = (spec['_id'], key)
    if k not in _sc:
        if len(_sc) > 90: _sc.clear()
        _sc[k] = draw_char(spec, **kw)
    return _sc[k]

# ------------------------------------------------------------------ scene state
def val_at(tl, t, default=None):
    v = default
    for (tt, x) in tl:
        if tt <= t: v = x
        else: break
    return v

def actor_state(sc, aid, t):
    a = sc['actors'][aid]; x, y = a['x'], a['y']; moving = False; hopy = 0.0; vis = 1.0
    for (t0, t1, x1, y1, style) in a['moves']:
        if t >= t1: x, y = x1, y1
        elif t > t0:
            u = ease_io((t - t0) / max(1e-3, t1 - t0)); xs, ys = x, y
            x, y = lerp(xs, x1, u), lerp(ys, y1, u)
            if style == 'walk': moving = True; hopy = abs(math.sin((t - t0) * 9.0)) * 14
            elif style == 'hop': hopy = 180 * 4 * u * (1 - u) * 0.0 + abs(math.sin(u * math.pi * 3)) * 70
            elif style == 'run': moving = True; hopy = abs(math.sin((t - t0) * 14.0)) * 22
            break
        else: break
    dx = dy = rot = 0.0; sx = sy = 1.0; extra_scale = 1.0
    for (t0, dur, name, p) in a['acts']:
        if t < t0: continue
        u = (t - t0) / max(1e-3, dur); uc = clamp(u)
        if name == 'jump': h = p or 170; dy -= h * 4 * uc * (1 - uc) if u <= 1 else 0; sy *= 1 + 0.14 * math.sin(uc * math.pi) if u <= 1 else 1; sx *= 1 - 0.08 * math.sin(uc * math.pi) if u <= 1 else 1
        elif name == 'bounce':
            n = p or 3
            if u <= 1: dy -= abs(math.sin(uc * math.pi * n)) * 120
        elif name == 'shake':
            if u <= 1: dx += math.sin(t * 70) * (p or 14) * (1 - 0.4 * uc)
        elif name == 'tremble':
            if u <= 1: dx += math.sin(t * 90) * (p or 5); dy += math.cos(t * 83) * (p or 5) * 0.5
        elif name == 'spin':
            rot += 360 * (p or 1) * ease_io(uc)
        elif name == 'wobble':
            if u <= 1: rot += math.sin(t * 13) * (p or 9)
        elif name == 'grow': extra_scale *= lerp(1, p or 1.5, ease_out_back(uc) if (p or 1.5) > 1 else ease_io(uc))
        elif name == 'pulse':
            if u <= 1: extra_scale *= 1 + (p or 0.12) * math.sin(uc * math.pi * 6)
        elif name == 'fall': rot += (p or 90) * ease_io(uc); dy += 70 * ease_io(uc)
        elif name == 'fly': dy -= 2600 * uc * uc; rot += 900 * uc; dx += 300 * uc * (p or 1)
        elif name == 'sink': dy += (p or 300) * ease_io(uc)
        elif name == 'float': dy -= (p or 200) * ease_io(uc) + math.sin(t * 3) * 10 * uc
        elif name == 'stretch':
            if u <= 1: sy *= 1 + (p or 0.3) * math.sin(uc * math.pi); sx *= 1 - (p or 0.3) * 0.5 * math.sin(uc * math.pi)
        elif name == 'lean': rot += (p or 12) * ease_io(uc)
        elif name == 'flop': rot += (p or 90) * ease_io(uc)
    return dict(x=x + dx, y=y + dy - hopy, rot=rot, sx=sx, sy=sy, es=extra_scale, moving=moving)

def draw_actor(cv, sc, aid, t):
    a = sc['actors'][aid]; spec = a['spec']
    vis = val_at(a['tl'].get('vis', []), t, 0 if a.get('hidden') else 1)
    if not vis: return None
    t_show = val_at(a['tl'].get('vis_t', []), t, -9)
    pop = ease_out_back(clamp((t - t_show) / 0.28)) if t_show > -5 else 1.0
    if pop < 0.02: return None
    st = actor_state(sc, aid, t)
    mood = val_at(a['tl'].get('mood', []), t, a.get('mood', 'neutral'))
    look = val_at(a['tl'].get('look', []), t, (0, 0)); arms = val_at(a['tl'].get('arms', []), t, a.get('arms', 'down'))
    held = val_at(a['tl'].get('hold', []), t, None); flip = val_at(a['tl'].get('flip', []), t, a.get('flip', False))
    spk = None
    for (s0, s1, env, text) in sc['says'].get(aid, []):
        if s0 <= t < s1: spk = (s0, env); break
    mo = 0.0
    if spk:
        i = int((t - spk[0]) * 30); env = spk[1]; mo = float(env[min(i, len(env) - 1)])
    ph = a['phase']; blink = ((t + ph) % 3.4) < 0.12
    legs_t = t * 12 if st['moving'] else 0.0
    arm_t = t * 7 + ph
    if st['moving'] and arms == 'down': arms = 'run' if False else 'down'
    sweat = mood in ('scared', 'sick', 'worry') and (t * 2) % 2 < 1.4
    spin = t * 6
    key = (mood, int(mo * 6), (round(look[0], 1), round(look[1], 1)), arms, int(arm_t * 1.3) % 9 if arms in ('up', 'wave', 'cheer', 'shrug', 'run') else 0, int(legs_t * 1.2) % 8 if legs_t else -1, blink, sweat, int(spin * 2) % 12 if mood in ('dizzy', 'sick', 'scared', 'confused') else 0)
    spr, (cx, cy), feet = char_sprite(spec, key, mood=mood, mo=int(mo * 6) / 6.0, look=look, arms=arms, arm_t=int(arm_t * 1.3) % 9 * 0.7 if arms in ('up', 'wave', 'cheer', 'shrug', 'run') else 0.0, legs_t=legs_t, blink=blink, sweat=sweat, spin=spin)
    sc_ = a['scale'] * 1.4 * st['es'] * pop
    flipped = bool(flip)
    if flipped: spr = spr.transpose(Image.FLIP_LEFT_RIGHT); cxs = spr.width - cx * S
    else: cxs = cx * S
    breath = 1 + 0.018 * math.sin(t * 3 + ph)
    sx, sy = st['sx'] * (2 - breath), st['sy'] * breath
    off_y = (feet - cy) * sc_ * sy  # feet below center
    px, py = st['x'], st['y'] - off_y
    # shadow
    air = max(0, (a['y'] - st['y']))
    shw = 150 * sc_ * (1 - clamp(air / 600) * 0.5)
    cv.d.ellipse([(st['x'] - shw) * S, (a['y'] + 14 - 24 * sc_) * S, (st['x'] + shw) * S, (a['y'] + 14 + 24 * sc_) * S], fill=(0, 0, 0, 55)) if abs(a['y'] - st['y']) < 800 else None
    paste(cv, spr, px, py, (cxs / S, cy), scale=sc_, rot=-st['rot'], sx=sx, sy=sy)
    if held:
        side = -1 if flipped else 1
        put_emoji(cv, held, px + side * 40 * sc_, py + 95 * sc_, 150 * sc_ * (spec.get('held', 1.0)), rot=0)
    return dict(x=px, y=py, top=py - (cy + 40) * sc_ * 1.0, s=sc_)

def prop_state(p, t):
    u = clamp((t - p['t0']) / max(1e-3, p['t1'] - p['t0']))
    if t < p['t0']: return None
    if p.get('out') is not None and t > p['out']: return None
    ue = ease_io(u) if not p.get('lin') else u
    x = lerp(p['p0'][0], p['p1'][0], ue); y = lerp(p['p0'][1], p['p1'][1], ue)
    if p.get('arc'): y -= p['arc'] * 4 * u * (1 - u)
    size = lerp(p['size'], p.get('size1') or p['size'], ue)
    k = ease_out_back(clamp((t - p['t0']) / 0.2)) if p.get('pop', True) else 1
    rot = p.get('rot', 0) + p.get('spin', 0) * (t - p['t0'])
    if p.get('wob'): rot += math.sin(t * 10) * p['wob']
    if p.get('bob'): y += math.sin(t * 5) * p['bob']
    al = 1.0
    if p.get('fade'): al = 1 - clamp((u - 0.6) / 0.4)
    if p.get('out') is not None: al *= clamp((p['out'] - t) / 0.18)
    return x, y, size * k, rot, al

def render_scene(sc, V, t):
    base = bgs.get_bg(sc['bg']); cv = canvas_from(base)
    bgs.bg_dyn(cv, sc['bg'], t)
    for p in sc['props']:
        if p.get('back'):
            s = prop_state(p, t)
            if s: put_emoji(cv, p['e'], s[0], s[1], s[2], s[3], p.get('flip', False), s[4])
    order = sorted(sc['actors'], key=lambda k: sc['actors'][k]['y'])
    info = {}
    for aid in order:
        r = draw_actor(cv, sc, aid, t)
        if r: info[aid] = r
    for p in sc['props']:
        if not p.get('back'):
            if p.get('attach'):
                a = info.get(p['attach'])
                if not a or t < p['t0']: continue
                if p.get('out') is not None and t > p['out']: continue
                put_emoji(cv, p['e'], a['x'] + p.get('dx', 0), a['y'] + p.get('dy', 0), p['size'] * a['s'] ** 0.5, p.get('rot', 0) + p.get('spin', 0) * (t - p['t0']), p.get('flip', False))
                continue
            s = prop_state(p, t)
            if s: put_emoji(cv, p['e'], s[0], s[1], s[2], s[3], p.get('flip', False), s[4])
    for ev in sc['pops']:
        popup(cv, ev['text'], ev['x'], ev['y'], t, ev['t'], ev['dur'], size=ev['size'], rot=ev['rot'], fill=ev['fill'])
    for aid, lst in sc['says'].items():
        for (s0, s1, env, text) in lst:
            if s0 <= t < s1 and aid in info:
                a = info[aid]; spec = sc['actors'][aid]['spec']
                n = len(text); size = int(min(96, 940 / (0.47 * n + 1.5))); size = max(46, size)
                bw = min(1000, 0.47 * n * size + 90)
                bx = min(max(a['x'], bw / 2 + 24), W - bw / 2 - 24); by = max(a['y'] - (spec.get('hh', 250)) * a['s'] - 90, 520)
                bubble(cv, text, bx, by, t, s0, s1 - s0 + 0.0, size=size, tail=(int(max(-bw / 2 + 60, min(bw / 2 - 60, (a['x'] - bx) * 0.8))), 70), color=spec.get('tc', (200, 30, 40)))
    for fl in sc['flashes']:
        if fl[0] <= t < fl[0] + fl[1]: flash(cv, 1 - (t - fl[0]) / fl[1])
    for (t0, t1, col) in sc['tints']:
        if t0 <= t < t1:
            a = col[3] * min(1, (t - t0) / 0.25, (t1 - t) / 0.25) if len(col) > 3 else 80
            ov = Image.new('RGBA', cv.im.size, col[:3] + (int(a),)); cv.im.paste(ov, (0, 0), ov)
    cam = {}
    for (t0, t1, z0, z1, cx, cy) in sc['zooms']:
        if t0 <= t <= t1 + 0.0:
            u = ease_io((t - t0) / max(1e-3, t1 - t0)); cam['zoom'] = lerp(z0, z1, u); cam['cx'] = cx; cam['cy'] = cy
        elif t > t1 and 'zoom' not in cam: cam['zoom'] = z1; cam['cx'] = cx; cam['cy'] = cy
    for (t0, dur, amp) in sc['shakes']:
        if t0 <= t < t0 + dur: cam['shake'] = max(cam.get('shake', 0), amp * (1 - (t - t0) / dur) ** 0.6)
    return cv, cam
