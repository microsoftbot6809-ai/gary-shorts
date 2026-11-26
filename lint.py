import sys, re, importlib
bad = 0
def times(ev):
    k = ev[0]
    if k in ('mood','look','arms','hold','flip','show','hide'): yield ev[1]
    elif k in ('move','act','zoom'): yield ev[1]; yield ev[2] if k in ('move','zoom') else None
    elif k == 'prop':
        yield ev[1]; yield ev[2]
        if len(ev) > 7 and ev[7].get('out') is not None: yield ev[7]['out']
    elif k in ('pop','sfx','flash','shake','say'): yield ev[1]
    elif k == 'tint': yield ev[1]; yield ev[2]
for modname in sys.argv[1:]:
    M = importlib.import_module(modname)
    for V in M.STORIES:
        for si, sc in enumerate(V['scenes']):
            words = [re.sub(r'\W', '', w).lower() for w in sc.get('text', '').split()]
            stage = sc.get('stage', {})
            for ev in sc.get('ev', []):
                for T in times(ev):
                    if isinstance(T, str):
                        m = re.match(r'@(\w+)(?:#(\d+))?([+-][\d.]+)?$', T)
                        if not m: print(V['id'], si, 'bad time', T); bad += 1; continue
                        w, n = m.group(1).lower(), int(m.group(2) or 1)
                        if w in ('end', 'start'): continue
                        if words.count(w) < n: print(V['id'], si, f"anchor '{T}' not in text: {sc.get('text','')[:70]}"); bad += 1
                aid = {'mood':2,'look':2,'arms':2,'hold':2,'flip':2,'show':2,'hide':2,'move':3,'act':3,'say':2}.get(ev[0])
                if aid is not None and ev[aid] not in stage: print(V['id'], si, 'unknown actor', ev[aid], 'in', ev[0]); bad += 1
                if ev[0] == 'prop' and len(ev) > 7 and ev[7].get('attach') and ev[7]['attach'] not in stage: print(V['id'], si, 'bad attach'); bad += 1
            for a, d in stage.items():
                if d.get('c', a) not in V['cast']: print(V['id'], si, 'actor not in cast', a); bad += 1
            tot = len(words)
            print(V['id'], si, 'words', tot) if tot > 40 else None
print('BAD', bad)
