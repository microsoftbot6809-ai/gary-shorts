import sys, re, math, subprocess, time, os, importlib, json
from fractions import Fraction
import numpy as np
from scipy import signal
from scipy.io import wavfile
from kokoro_onnx import Kokoro
import sfx
from gfx import *
import toon
FPS = 30; SR = sfx.SR
K = Kokoro("models/kokoro-v1.0.int8.onnx", "models/voices-v1.0.bin")
SFX = {'toot': lambda: sfx.fart(0.28, 140, 100, 55, seed=1), 'pfft': lambda: sfx.fart(0.35, 260, 170, 60, seed=2, cutoff=2200),
 'fartlong': lambda: sfx.fart(1.1, 110, 70, 42, seed=3), 'blast': lambda: sfx.fart(1.9, 70, 38, 30, seed=5, wet=0.8, cutoff=900),
 'rumble': sfx.rumble, 'chomp': sfx.chomp, 'thump': sfx.thump, 'boom': sfx.boom, 'whoosh': sfx.whoosh, 'squawk': sfx.squawk,
 'clank': sfx.clank, 'sparkle': sfx.sparkle, 'ding': sfx.ding, 'gasp': sfx.gasp, 'trombone': sfx.trombone, 'boing': sfx.boing,
 'hiss': sfx.hiss, 'crash': sfx.crash, 'doorbell': sfx.doorbell, 'alien': sfx.alien, 'flame': sfx.flame, 'bonk': sfx.bonk,
 'pop': sfx.pop, 'zap': sfx.zap, 'splash': sfx.splash, 'scratch': sfx.scratch, 'cheer': sfx.cheer, 'phone': sfx.phone, 'snore': sfx.snore,
 'powerup': sfx.powerup, 'cash': sfx.cash, 'fall': sfx.fall, 'buzz': sfx.buzz, 'tada': sfx.tada, 'engine': sfx.engine, 'tick': sfx.tick,
 'sad': sfx.sad, 'giggle': sfx.giggle, 'kiss': sfx.kiss, 'whistle': sfx.whistle_up, 'gulp': sfx.gulp, 'bell': sfx.bell}

def say(text, voice, speed=1.0, pitch=1.0):
    x, sr = K.create(text, voice=voice, speed=speed, lang='en-us')
    x = x.astype(np.float32)
    idx = np.where(np.abs(x) > 0.02 * np.max(np.abs(x)))[0]
    x = x[max(0, idx[0] - 150): idx[-1] + 300]
    ratio = (Fraction(SR, sr) / Fraction(pitch).limit_denominator(100)).limit_denominator(400)
    x = signal.resample_poly(x, ratio.numerator, ratio.denominator).astype(np.float32)
    return x / (np.max(np.abs(x)) + 1e-9) * 0.9

def narrate(text, voice, speed, gap=0.16):
    if not text.strip(): return np.zeros(0, np.float32), []
    sents = re.split(r'(?<=[.!?])\s+', text.strip()); parts, spans, pos = [], [], 0.0
    for s in sents:
        a = say(s, voice, speed); spans.append((s, pos, pos + len(a) / SR)); parts.append(a)
        parts.append(np.zeros(int(gap * SR), np.float32)); pos += len(a) / SR + gap
    return np.concatenate(parts[:-1]), spans

def word_times(spans, ns):
    out = []
    for s, a, b in spans:
        toks = s.split(); base = [len(re.sub(r'\W', '', w)) + 1.5 for w in toks]; tot = sum(base); p = 0
        for w, bw in zip(toks, base):
            out.append((w, ns + a + (b - a) * p / tot, ns + a + (b - a) * (p + bw) / tot)); p += bw
    return out

def chunk_words(words, maxw=3):
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= maxw or w[0][-1] in '.!?,': chunks.append(dict(ts=cur[0][1], te=cur[-1][2], words=cur)); cur = []
    if cur: chunks.append(dict(ts=cur[0][1], te=cur[-1][2], words=cur))
    return chunks

def envelope(x):
    n = int(len(x) / SR * FPS) + 2; e = np.zeros(n, np.float32)
    h = SR // FPS
    for i in range(n):
        seg = x[i * h:(i + 1) * h]
        e[i] = np.sqrt(np.mean(seg ** 2)) if len(seg) else 0
    e = e / (np.percentile(e, 95) + 1e-6); e = np.clip(e * 1.1, 0, 1)
    return e

def prep(V):
    """resolve a story dict into renderable scenes with absolute timings; returns total duration"""
    cast = {k: dict(v) for k, v in V['cast'].items()}; V['cast'] = cast
    for i, (cid, spec) in enumerate(cast.items()): spec['_id'] = V['id'] + '/' + cid
    narr_v = V.get('narr', 'bm_george'); narr_s = V.get('narr_speed', 1.08)
    t_acc = 0.0
    for si, sc in enumerate(V['scenes']):
        sc.setdefault('pre', 0.35); sc.setdefault('post', 0.9); sc.setdefault('music', 0.6)
        narr, spans = narrate(sc.get('text', ''), narr_v, narr_s)
        sc['narr'] = narr; sc['ns'] = sc['pre']; sc['ne'] = sc['pre'] + len(narr) / SR
        sc['words'] = word_times(spans, sc['ns']); sc['chunks'] = chunk_words(sc['words'])
        wl = [(re.sub(r'\W', '', w[0]).lower(), w[1], w[2]) for w in sc['words']]
        def tm(T):
            if T is None or isinstance(T, (int, float)): return T
            m = re.match(r'@(\w+)(?:#(\d+))?([+-][\d.]+)?$', T)
            if not m: raise ValueError('bad time ' + str(T))
            w, nth, off = m.group(1).lower(), int(m.group(2) or 1), float(m.group(3) or 0)
            if w == 'end': return sc['ne'] + off
            if w == 'start': return sc['ns'] + off
            hits = [x for x in wl if x[0] == w]
            if len(hits) < nth: raise ValueError(f"scene {si}: word '{w}' not found in narration: {sc.get('text','')[:60]}")
            return hits[nth - 1][1] + off
        sc['actors'] = {}
        for aid, a in sc.get('stage', {}).items():
            spec = cast[a.get('c', aid)]
            sc['actors'][aid] = dict(spec=spec, x=a['at'][0], y=a['at'][1], scale=a.get('s', 0.6), flip=a.get('flip', False), mood=a.get('mood', 'neutral'),
                                     arms=a.get('arms', 'down'), hidden=a.get('hidden', False), phase=hash(aid) % 7, moves=[], acts=[], tl={})
            if a.get('hidden'): sc['actors'][aid]['tl']['vis'] = [(0, 0)]
            if a.get('hold'): sc['actors'][aid]['tl']['hold'] = [(0, a['hold'])]
        sc['props'] = []; sc['pops'] = []; sc['flashes'] = []; sc['tints'] = []; sc['zooms'] = []; sc['shakes'] = []; sc['says'] = {}; sc['sfx'] = []; sc['extra_audio'] = []
        cursor = sc['ne'] + 0.3; last = sc['ne']
        def tl(aid, name, t, v): sc['actors'][aid]['tl'].setdefault(name, []).append((t, v))
        for ev in sc.get('ev', []):
            k = ev[0]
            if k == 'mood': tl(ev[2], 'mood', tm(ev[1]), ev[3])
            elif k == 'look': tl(ev[2], 'look', tm(ev[1]), ev[3])
            elif k == 'arms': tl(ev[2], 'arms', tm(ev[1]), ev[3])
            elif k == 'hold': tl(ev[2], 'hold', tm(ev[1]), ev[3])
            elif k == 'flip': tl(ev[2], 'flip', tm(ev[1]), ev[3])
            elif k == 'show': t = tm(ev[1]); tl(ev[2], 'vis', t, 1); tl(ev[2], 'vis_t', t, t)
            elif k == 'hide': tl(ev[2], 'vis', tm(ev[1]), 0)
            elif k == 'move':
                sc['actors'][ev[3]]['moves'].append((tm(ev[1]), tm(ev[2]), ev[4], ev[5], ev[6] if len(ev) > 6 else 'walk'))
                last = max(last, tm(ev[2]))
            elif k == 'act':
                t0 = tm(ev[1]); sc['actors'][ev[3]]['acts'].append((t0, ev[2], ev[4], ev[5] if len(ev) > 5 else None)); last = max(last, t0 + (ev[2] if ev[4] not in ('fly', 'sink', 'float', 'fall', 'grow', 'flop', 'lean') else 0))
            elif k == 'prop':
                p = dict(e=ev[3], t0=tm(ev[1]), t1=tm(ev[2]), p0=ev[4], p1=ev[5], size=ev[6] if len(ev) > 6 else 200); p.update(ev[7] if len(ev) > 7 else {})
                if p.get('out') is not None: p['out'] = tm(p['out'])
                sc['props'].append(p); last = max(last, p['t1'])
            elif k == 'pop':
                sc['pops'].append(dict(t=tm(ev[1]), text=ev[2], x=ev[3], y=ev[4], dur=ev[5] if len(ev) > 5 else 1.1, size=ev[6] if len(ev) > 6 else 140, rot=ev[7] if len(ev) > 7 else -8, fill=ev[8] if len(ev) > 8 else (255, 226, 60)))
            elif k == 'sfx': sc['sfx'].append((tm(ev[1]), ev[2], ev[3] if len(ev) > 3 else 1.0))
            elif k == 'flash': sc['flashes'].append((tm(ev[1]), ev[2] if len(ev) > 2 else 0.35)); 
            elif k == 'tint': sc['tints'].append((tm(ev[1]), tm(ev[2]), ev[3]))
            elif k == 'shake': sc['shakes'].append((tm(ev[1]), ev[2], ev[3] if len(ev) > 3 else 14))
            elif k == 'zoom': sc['zooms'].append((tm(ev[1]), tm(ev[2]), ev[3], ev[4], ev[5] if len(ev) > 5 else W / 2, ev[6] if len(ev) > 6 else H / 2))
            elif k == 'say':
                aid = ev[2]; spec = sc['actors'][aid]['spec']; t0 = tm(ev[1]) if ev[1] is not None else cursor
                x = say(ev[3], spec.get('voice', 'am_puck'), spec.get('vspeed', 1.0), spec.get('vpitch', 1.0)) * spec.get('vgain', 1.0)
                t1 = t0 + len(x) / SR; sc['says'].setdefault(aid, []).append((t0, t1, envelope(x), ev[3])); sc['extra_audio'].append((t0, x))
                cursor = t1 + 0.2; last = max(last, t1)
            else: raise ValueError('unknown event ' + str(ev))
        for a in sc['actors'].values():
            a['moves'].sort(key=lambda m: m[0]); a['acts'].sort(key=lambda m: m[0])
            for lst in a['tl'].values(): lst.sort(key=lambda m: m[0])
        sc['dur'] = max(sc['ne'] + sc['post'], last + 0.8 if sc['sfx'] or sc['says'] else 0, last + 0.5)
        sc['dur'] = max(sc['dur'], max([s[0] + 0.5 for s in sc['sfx']], default=0), 1.6)
        sc['start'] = t_acc; t_acc += sc['dur']
    return t_acc

def mix(V, total, path):
    n = int((total + 1.5) * SR); voice = np.zeros(n, np.float32); fx = np.zeros(n, np.float32)
    def put(buf, x, t):
        o = int(t * SR); e = min(n, o + len(x))
        if 0 <= o < n: buf[o:e] += x[:e - o]
    cache = {}
    for sc in V['scenes']:
        put(voice, sc['narr'], sc['start'] + sc['ns'])
        for (t, x) in sc['extra_audio']: put(voice, x, sc['start'] + t)
        for (t, name, g) in sc['sfx']:
            if name not in cache: cache[name] = SFX[name]()
            put(fx, cache[name] * g * 0.6, sc['start'] + t)
    mus = sfx.music_v(total + 1.5, V.get('bpm', 124), V.get('mseed', 8), V.get('mscale', 0))[:n]
    env = np.zeros(n, np.float32)
    for sc in V['scenes']: env[int(sc['start'] * SR): int((sc['start'] + sc['dur']) * SR)] = sc['music']
    env = sfx.lp(env, 1.5, 2).astype(np.float32); env[:int(0.4 * SR)] *= np.linspace(0, 1, int(0.4 * SR))
    fade = int(1.0 * SR); env[int(total * SR) - fade:int(total * SR)] *= np.linspace(1, 0, fade); env[int(total * SR):] = 0
    out = voice + fx + mus * env * 0.11
    out = np.tanh(out * 1.1) / np.tanh(1.1); wavfile.write(path, SR, (out * 30000).astype(np.int16))

def render_frame(sc, V, t):
    cv, cam = toon.render_scene(sc, V, t)
    captions(cv, sc['chunks'], t)
    amp = cam.get('shake', 0); z = max(cam.get('zoom', 1.0), 1.0 + (0.012 + amp * 0.002 if amp else 0))
    dx, dy = (amp * S * math.sin(t * 97.0), amp * S * math.cos(t * 83.0)) if amp else (0, 0)
    bw, bh = W * S / z, H * S / z
    cx, cy = cam.get('cx', W / 2) * S + dx, cam.get('cy', H / 2) * S + dy
    x0 = min(max(cx - bw / 2, 0), W * S - bw); y0 = min(max(cy - bh / 2, 0), H * S - bh)
    return cv.im.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + bw, y0 + bh))

def preview(V, path):
    scs = V['scenes']; cols = 4; rows = len(scs)
    sheet = Image.new('RGB', (cols * 216, rows * 384), (0, 0, 0))
    for r, sc in enumerate(scs):
        for c, f in enumerate((0.15, 0.4, 0.65, 0.9)):
            sheet.paste(render_frame(sc, V, min(sc['dur'] * f, sc['dur'] - 0.01)).resize((216, 384)), (c * 216, r * 384))
    sheet.save(path)

def render(V, total, audio, out, crf=24):
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', audio,
           '-c:v', 'libx264', '-preset', 'medium', '-crf', str(crf), '-maxrate', '2400k', '-bufsize', '4800k', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '112k', '-movflags', '+faststart', '-shortest', out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE); t0 = time.time(); done = 0; tot = sum(int(round(sc['dur'] * FPS)) for sc in V['scenes'])
    for sc in V['scenes']:
        for i in range(int(round(sc['dur'] * FPS))):
            p.stdin.write(render_frame(sc, V, i / FPS).tobytes()); done += 1
            if done % 150 == 0: print(f"  {V['id']} {done}/{tot} {time.time()-t0:.0f}s", flush=True)
    p.stdin.close(); p.wait(); print('DONE', V['id'], round(time.time() - t0), flush=True)

if __name__ == '__main__':
    mod, cmd = sys.argv[1], sys.argv[2]; ids = sys.argv[3:]
    M = importlib.import_module(mod)
    os.makedirs('out', exist_ok=True)
    for V in M.STORIES:
        if ids and V['id'] not in ids: continue
        total = prep(V); print(V['id'], 'duration', round(total, 1), flush=True)
        if cmd == 'preview': preview(V, f"out/{V['id']}_prev.png")
        elif cmd == 'check': pass
        elif cmd == 'render':
            mix(V, total, f"out/{V['id']}.wav"); render(V, total, f"out/{V['id']}.wav", f"out/{V['id']}.mp4")
