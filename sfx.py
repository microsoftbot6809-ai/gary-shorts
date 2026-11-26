import numpy as np
from scipy import signal
SR = 44100
PI2 = 2 * np.pi

def lp(x, fc, order=4):
    return signal.sosfilt(signal.butter(order, fc, 'low', fs=SR, output='sos'), x)
def hp(x, fc, order=4):
    return signal.sosfilt(signal.butter(order, fc, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi, order=3):
    return signal.sosfilt(signal.butter(order, [lo, hi], 'band', fs=SR, output='sos'), x)
def tt(d): return np.arange(int(d * SR)) / SR
def norm(x, g=1.0):
    m = np.max(np.abs(x)) + 1e-9
    return (x / m * g).astype(np.float32)
def env_ad(n, a=0.01, r=None, power=1.5):
    t = np.arange(n) / SR
    d = n / SR
    r = r if r else d - a
    return np.minimum(t / max(a, 1e-4), 1.0) * np.clip(1 - (t - a) / max(r, 1e-4), 0, 1) ** power

def fart(dur=0.4, f0=120, f1=90, flutter=50, seed=0, wet=0.5, cutoff=1500, rise=False):
    rng = np.random.default_rng(seed)
    n = int(dur * SR); t = np.arange(n) / SR
    jit = lp(rng.standard_normal(n), 25, 2); jit /= (np.max(np.abs(jit)) + 1e-9)
    contour = np.linspace(f0, f1, n)
    if rise: contour = np.concatenate([np.linspace(f0, f1, n // 3), np.linspace(f1, f0 * 0.8, n - n // 3)])
    f = contour * (1 + 0.12 * jit + 0.05 * np.sin(PI2 * 4.5 * t))
    ph = PI2 * np.cumsum(f) / SR
    saw = 2 * ((ph / PI2) % 1) - 1
    fl_f = flutter * (1 + 0.35 * jit)
    fl = 0.5 + 0.5 * np.sin(PI2 * np.cumsum(fl_f) / SR)
    noise = rng.standard_normal(n)
    sig = saw * (0.35 + 0.65 * fl ** 2) + wet * 0.5 * lp(noise, 2500) * fl
    sig = lp(sig, cutoff)
    e = np.minimum(t / 0.012, 1) * np.clip(1 - np.maximum(t - dur * 0.55, 0) / (dur * 0.45), 0, 1) ** 0.7
    e *= (1 + 0.15 * np.sin(PI2 * 9 * t))
    return norm(sig * e, 0.9)

def rumble(dur=1.2, seed=1):
    rng = np.random.default_rng(seed); n = int(dur * SR); t = tt(dur)
    g = lp(rng.standard_normal(n), 120, 3)
    gur = 0.5 + 0.5 * np.sin(PI2 * (6 + 5 * t / dur) * t)
    sig = g * gur * 3 + 0.6 * np.sin(PI2 * 48 * t) * gur
    return norm(lp(sig, 300) * env_ad(n, 0.15, power=0.6), 0.8)

def chomp(seed=0):
    rng = np.random.default_rng(seed); n = int(0.14 * SR)
    x = bp(rng.standard_normal(n), 500, 2500) * env_ad(n, 0.003, power=3)
    x += 0.8 * np.sin(PI2 * 110 * tt(0.14)) * env_ad(n, 0.002, power=4)
    return norm(x, 0.7)

def whoosh(dur=0.7, lo=300, hi=3500, seed=0):
    rng = np.random.default_rng(seed); n = int(dur * SR)
    x = rng.standard_normal(n)
    out = np.zeros(n); chunks = 24
    for i in range(chunks):
        a, b = i * n // chunks, (i + 1) * n // chunks
        c = lo * (hi / lo) ** (i / chunks)
        seg = bp(np.concatenate([np.zeros(200), x[a:b], np.zeros(200)]), c * 0.7, min(c * 1.4, SR / 2 - 100), 2)[200:-200]
        out[a:b] = seg
    return norm(out * np.sin(np.pi * np.arange(n) / n) ** 1.5, 0.7)

def boing(dur=0.5):
    t = tt(dur); f = 250 + 500 * np.sin(np.pi * t / dur) ** 2 + 25 * np.sin(PI2 * 30 * t)
    return norm(np.sin(PI2 * np.cumsum(f) / SR) * env_ad(len(t), 0.005, power=1.2), 0.6)

def clank():
    t = tt(0.7); x = 0
    for fr, a in [(620, 1), (1190, 0.7), (1730, 0.5), (2410, 0.3)]:
        x = x + a * np.sin(PI2 * fr * t) * np.exp(-t * (8 + fr / 300))
    x = x + 0.5 * np.random.default_rng(3).standard_normal(len(t)) * np.exp(-t * 90)
    return norm(x, 0.8)

def squawk():
    t = tt(0.35); f = 900 - 350 * t / 0.35 + 60 * np.sin(PI2 * 28 * t)
    ph = PI2 * np.cumsum(f) / SR
    x = (2 * ((ph / PI2) % 1) - 1) * 0.6 + np.sin(ph * 2) * 0.3
    return norm(bp(x, 400, 3500) * env_ad(len(t), 0.01, power=1.2), 0.6)

def gasp():
    rng = np.random.default_rng(5); n = int(0.35 * SR); t = np.arange(n) / SR
    x = bp(rng.standard_normal(n), 600, 3500) * np.minimum(t / 0.2, 1) * np.clip(1 - (t - 0.2) / 0.15, 0, 1)
    return norm(x, 0.5)

def ding():
    t = tt(0.9); return norm((np.sin(PI2 * 1320 * t) + 0.4 * np.sin(PI2 * 2640 * t)) * np.exp(-t * 5), 0.5)

def sparkle():
    out = np.zeros(int(0.9 * SR))
    for i, f in enumerate([1568, 1975, 2349, 2637, 3136]):
        t = tt(0.4); s = np.sin(PI2 * f * t) * np.exp(-t * 9)
        o = int(i * 0.07 * SR); out[o:o + len(s)] += s
    return norm(out, 0.4)

def boom():
    rng = np.random.default_rng(9); dur = 1.6; n = int(dur * SR); t = tt(dur)
    x = lp(rng.standard_normal(n), 400, 3) * np.exp(-t * 3.2) * 2 + np.sin(PI2 * np.cumsum(60 * np.exp(-t * 1.5) + 25) / SR) * np.exp(-t * 2.2)
    return norm(x, 0.95)

def thump():
    t = tt(0.3); return norm(np.sin(PI2 * np.cumsum(120 * np.exp(-t * 14) + 40) / SR) * np.exp(-t * 9), 0.8)

def trombone():
    notes = [(233, .5), (220, .5), (208, .5), (196, 1.3)]
    out = []
    for i, (f, d) in enumerate(notes):
        t = tt(d); fv = f * (1 + (0.02 * np.sin(PI2 * 6 * t) if i == 3 else 0)) * (1 - 0.06 * (t / d) ** 2 * (i == 3))
        ph = PI2 * np.cumsum(fv) / SR
        s = lp(2 * ((ph / PI2) % 1) - 1, 1100) * env_ad(len(t), 0.03, power=0.6)
        out.append(s)
    return norm(np.concatenate(out), 0.6)

# ---- new for part 2
def hiss(dur=1.2, seed=21):
    rng = np.random.default_rng(seed); n = int(dur * SR)
    x = hp(rng.standard_normal(n), 3000, 3) * env_ad(n, 0.02, power=1.0)
    return norm(x, 0.55)

def crash(seed=31):
    rng = np.random.default_rng(seed); dur = 1.1; n = int(dur * SR); t = tt(dur)
    x = bp(rng.standard_normal(n), 200, 4000) * np.exp(-t * 6) * 1.5
    for k in range(9):
        o = int(rng.random() * 0.5 * SR); m = int(0.08 * SR)
        x[o:o + m] += hp(rng.standard_normal(m), 1500, 2) * env_ad(m, 0.002, power=2) * rng.uniform(0.3, 0.9)
    x += np.sin(PI2 * np.cumsum(90 * np.exp(-t * 10) + 35) / SR) * np.exp(-t * 7) * 1.4
    return norm(x, 0.95)

def doorbell():
    out = np.zeros(int(1.6 * SR))
    for o, f in ((0.0, 659.25), (0.55, 523.25)):
        t = tt(0.9); s = (np.sin(PI2 * f * t) + 0.35 * np.sin(PI2 * f * 2.01 * t)) * np.exp(-t * 3.2)
        i = int(o * SR); out[i:i + len(s)] += s
    return norm(out, 0.55)

def alien(seed=0):
    t = tt(0.9)
    f = 700 + 350 * np.sin(PI2 * 5 * t) + 400 * np.sin(PI2 * 11 * t) * np.exp(-t * 2)
    s = np.sin(PI2 * np.cumsum(f) / SR) * (0.6 + 0.4 * np.sin(PI2 * 22 * t))
    return norm(s * env_ad(len(t), 0.03, power=0.8), 0.45)

def flame(dur=1.8, seed=41):
    rng = np.random.default_rng(seed); n = int(dur * SR); t = tt(dur)
    x = lp(rng.standard_normal(n), 1800, 2) * (0.6 + 0.4 * np.sin(PI2 * 17 * t + 3 * lp(rng.standard_normal(n), 30, 1)))
    return norm(x * env_ad(n, 0.1, power=0.5), 0.7)

def bonk():
    t = tt(0.35); f = 420 * np.exp(-t * 7) + 140
    return norm(np.sin(PI2 * np.cumsum(f) / SR) * np.exp(-t * 11) + 0.4 * np.sin(PI2 * 1200 * t) * np.exp(-t * 25), 0.8)

def music(dur, bpm=128):
    n = int((dur + 1) * SR); out = np.zeros(n)
    beat = 60 / bpm
    bass = [65.41, 98.0, 110.0, 87.31]
    mel = [523.25, 587.33, 659.25, 783.99, 880.0]
    rng = np.random.default_rng(8)
    pat = [rng.integers(0, 5, 8) for _ in range(4)]
    bar = 4 * beat; nb = int(dur / bar) + 2
    for b in range(nb):
        root = bass[b % 4]
        for k in range(8):
            ts = b * bar + k * beat / 2
            fr = root * (2 if k % 2 else 1)
            d = beat * 0.45; t = tt(d)
            s = np.sign(np.sin(PI2 * fr * t)) * np.exp(-t * 6)
            o = int(ts * SR)
            if o + len(s) < n: out[o:o + len(s)] += 0.5 * s
            if k % 2 == 0 and (k // 2 + b) % 3 != 2:
                fm = mel[pat[b % 4][k]]; t2 = tt(beat * 0.4)
                s2 = (2 / np.pi) * np.arcsin(np.sin(PI2 * fm * t2)) * np.exp(-t2 * 5)
                if o + len(s2) < n: out[o:o + len(s2)] += 0.35 * s2
    return norm(lp(out, 3500), 1.0)[:n]

# ---- toon extras
def pop():
    t = tt(0.16); return norm(np.sin(PI2 * np.cumsum(900 * np.exp(-t * 18) + 200) / SR) * np.exp(-t * 22), 0.7)
def zap():
    t = tt(0.5); f = 2200 * np.exp(-t * 5) + 200 + 400 * np.sin(PI2 * 60 * t)
    return norm(np.sign(np.sin(np.cumsum(PI2 * f) / SR)) * env_ad(len(t), 0.003, power=1.0) * 0.6, 0.6)
def splash():
    rng = np.random.default_rng(12); n = int(0.9 * SR); t = np.arange(n) / SR
    x = bp(rng.standard_normal(n), 300, 5000) * np.exp(-t * 5) * (0.6 + 0.4 * np.sin(PI2 * 25 * t))
    return norm(x, 0.8)
def scratch():
    rng = np.random.default_rng(14); n = int(0.5 * SR); t = np.arange(n) / SR
    f = 900 + 2500 * np.sin(PI2 * 3 * t) ** 2
    x = (2 * ((np.cumsum(f) / SR) % 1) - 1) * 0.5 + 0.5 * rng.standard_normal(n) * 0.3
    return norm(bp(x, 500, 5000) * np.minimum(t / 0.01, 1) * np.clip(1 - (t - 0.35) / 0.15, 0, 1), 0.6)
def cheer():
    rng = np.random.default_rng(16); n = int(1.6 * SR); t = np.arange(n) / SR
    x = bp(rng.standard_normal(n), 500, 3500) * (0.5 + 0.5 * np.sin(PI2 * 7 * t + lp(rng.standard_normal(n), 8, 1) * 6)) * np.minimum(t / 0.2, 1) * np.clip(1 - (t - 1.0) / 0.6, 0, 1)
    return norm(x, 0.6)
def phone():
    out = np.zeros(int(1.2 * SR))
    for k in range(6):
        t = tt(0.1); s = (np.sin(PI2 * 1400 * t) + np.sin(PI2 * 1700 * t)) * 0.5 * env_ad(len(t), 0.005, power=0.5); o = int(k * 0.15 * SR); out[o:o + len(s)] += s
    return norm(out, 0.5)
def snore():
    rng = np.random.default_rng(18); n = int(1.6 * SR); t = np.arange(n) / SR
    ins = lp(rng.standard_normal(n), 700, 2) * np.clip(np.sin(np.pi * t / 0.8), 0, 1) * (t < 0.8)
    exh = lp(rng.standard_normal(n), 400, 2) * np.clip(np.sin(np.pi * (t - 0.8) / 0.8), 0, 1) * (t >= 0.8) * (1 + 0.5 * np.sin(PI2 * 25 * t))
    return norm(ins + exh, 0.45)
def powerup():
    t = tt(0.7); f = 300 * 2 ** (t / 0.7 * 2.5); return norm(np.sign(np.sin(np.cumsum(PI2 * f) / SR)) * env_ad(len(t), 0.01, power=0.7) * 0.5, 0.5)
def cash():
    out = np.zeros(int(0.8 * SR))
    for o, f in ((0, 1568), (0.09, 2093)):
        t = tt(0.6); s = (np.sin(PI2 * f * t) + 0.3 * np.sin(PI2 * f * 3 * t)) * np.exp(-t * 7); i = int(o * SR); out[i:i + len(s)] += s
    return norm(out, 0.5)
def fall():
    t = tt(1.0); f = 1800 * np.exp(-t * 2.2) + 150; return norm(np.sin(PI2 * np.cumsum(f) / SR) * np.minimum(t / 0.02, 1) * np.clip(1 - (t - 0.85) / 0.15, 0, 1), 0.5)
def buzz():
    t = tt(0.5); return norm(np.sign(np.sin(PI2 * 110 * t)) * np.minimum(t / 0.01, 1) * np.clip(1 - (t - 0.4) / 0.1, 0, 1), 0.55)
def tada():
    out = np.zeros(int(1.4 * SR))
    for o, f in ((0, 523.25), (0.12, 659.25), (0.24, 783.99), (0.4, 1046.5)):
        t = tt(0.9 if o > 0.3 else 0.2); s = (np.sin(PI2 * f * t) + 0.4 * np.sin(PI2 * 2 * f * t)) * env_ad(len(t), 0.01, power=1.2); i = int(o * SR); out[i:i + len(s)] += s
    return norm(out, 0.6)
def engine():
    t = tt(1.4); f = 55 + 70 * np.minimum(t / 1.0, 1) + 6 * np.sin(PI2 * 17 * t)
    return norm(lp(np.sign(np.sin(np.cumsum(PI2 * f) / SR)), 900, 2) * env_ad(len(t), 0.05, power=0.6), 0.6)
def tick():
    t = tt(0.05); return norm(np.sin(PI2 * 1800 * t) * np.exp(-t * 90), 0.5)
def sad():
    out = []
    for f, d in ((392, .45), (370, .45), (349, .45), (330, 1.0)):
        t = tt(d); fv = f * (1 + 0.015 * np.sin(PI2 * 5.5 * t) * (d > 0.9)); out.append(lp(2 * ((np.cumsum(PI2 * fv) / SR / PI2) % 1) - 1, 1500) * env_ad(len(t), 0.03, power=0.6))
    return norm(np.concatenate(out), 0.5)
def giggle():
    out = np.zeros(int(0.9 * SR))
    for k in range(5):
        t = tt(0.1); s = np.sin(PI2 * np.cumsum(520 + 200 * (k % 2) + 80 * t) / SR) * env_ad(len(t), 0.01, power=1.0); o = int(k * 0.14 * SR); out[o:o + len(s)] += s
    return norm(out, 0.45)
def kiss():
    t = tt(0.2); return norm(np.sin(PI2 * np.cumsum(700 + 900 * (t / 0.2)) / SR) * env_ad(len(t), 0.005, power=2), 0.5)
def whistle_up():
    t = tt(0.6); f = 900 + 1200 * t / 0.6; return norm(np.sin(PI2 * np.cumsum(f) / SR) * env_ad(len(t), 0.03, power=0.8), 0.4)
def gulp():
    t = tt(0.25); return norm(np.sin(PI2 * np.cumsum(260 - 150 * t / 0.25) / SR) * np.exp(-t * 14) + 0.3 * np.sin(PI2 * 90 * t) * np.exp(-t * 20), 0.7)
def bell():
    t = tt(1.2); return norm((np.sin(PI2 * 880 * t) + 0.5 * np.sin(PI2 * 2210 * t)) * np.exp(-t * 3.5), 0.5)
def music_v(dur, bpm=128, seed=8, scale=0):
    # variant of music() with different melody pool / bass per scale index
    n = int((dur + 1) * SR); out = np.zeros(n); beat = 60 / bpm
    basses = [[65.41, 98.0, 110.0, 87.31], [73.42, 55.0, 87.31, 98.0], [82.41, 61.74, 110.0, 98.0], [55.0, 65.41, 73.42, 49.0]]
    mels = [[523.25, 587.33, 659.25, 783.99, 880.0], [440.0, 523.25, 587.33, 659.25, 783.99], [493.88, 587.33, 659.25, 739.99, 880.0], [392.0, 440.0, 523.25, 587.33, 659.25]]
    bass = basses[scale % 4]; mel = mels[scale % 4]
    rng = np.random.default_rng(seed); pat = [rng.integers(0, 5, 8) for _ in range(4)]
    bar = 4 * beat; nb = int(dur / bar) + 2
    for b in range(nb):
        root = bass[b % 4]
        for k in range(8):
            ts = b * bar + k * beat / 2; fr = root * (2 if k % 2 else 1); d = beat * 0.45; t = tt(d)
            s = np.sign(np.sin(PI2 * fr * t)) * np.exp(-t * 6); o = int(ts * SR)
            if o + len(s) < n: out[o:o + len(s)] += 0.5 * s
            if k % 2 == 0 and (k // 2 + b) % 3 != 2:
                fm = mel[pat[b % 4][k]]; t2 = tt(beat * 0.4); s2 = (2 / np.pi) * np.arcsin(np.sin(PI2 * fm * t2)) * np.exp(-t2 * 5)
                if o + len(s2) < n: out[o:o + len(s2)] += 0.35 * s2
    return norm(lp(out, 3500), 1.0)[:n]
