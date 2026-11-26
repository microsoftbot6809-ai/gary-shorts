# Cartoon engine guide (channel: oranj joos)

Python PIL, 1080x1920 @ 30fps, piped to ffmpeg. Kokoro TTS voices. Run `bash setup.sh` once per fresh session (installs deps, downloads models).
Work from inside this folder (`engine/`).

## Commands
- `python3 lint.py stories_X`      -> checks every '@word' anchor exists in the scene text and every actor is on stage. Must print nothing.
- `python3 build.py stories_X check eNN` -> TTS + timing only. `preview` -> a still PNG. `render` -> `out/<id>.mp4` (~1-2 min per video).
- `python3 qa.py <id> ...` -> `out/qa_<id>.png` contact sheet + loudness. Look at it (Read tool) before publishing. Loudness mean ~ -16 dB is normal.
A story module defines dicts and ends with `STORIES = [e25, e26, ...]`. Copy the structure of `stories_k.py` (the best example; also see stories_e.py).

## Story dict
```
VID = dict(id='f01', title='...', cast=dict(sam=SAM, dog=DOG), narr='bm_george', narr_speed=1.08, bpm=126, mscale=0, scenes=[ ... ])
```
- Characters: `dict(color=RED, body='tall', voice='am_puck', tc=(r,g,b) caption/tint color, + options)`.
  - body: round, tall, small, pear, box, blob
  - options: blush, glasses, mustache, hair, bow, tie, antenna, horns, hat (cap beanie party tophat chef headband crown helmet wizard cowboy; with hatc=COLOR), ears (cat dog bear), vpitch (0.8-1.4), vspeed
  - person(color, ...) from kit.py makes a skin-toned person. Colors in kit.py: RED BLUE GREEN YEL PINK ORG PUR TEAL BRN GRAY WHT.
  - voices that work: am_onyx am_puck am_adam am_fenrir am_michael am_eric am_echo am_liam bm_lewis bm_fable bm_daniel bm_george af_nova af_bella af_nicole af_jessica af_sarah af_kore bf_emma bf_lily bf_isabella
- bg themes: bedroom kitchen street park school beach forest space city_night office snow desert cave underwater stage castle market sky farm restaurant gym void
- moods: happy proud worry confused shock scream scared evil angry smug sad neutral grin sleepy think yum sick cry dead wow love dizzy

## Scene dict
```
dict(bg='kitchen', text="Narration. One sentence at a time.", pre=0.35, post=0.9,
     stage=dict(sam=dict(at=(270,1450), s=0.9, mood='happy', arms='down', flip=False, hidden=False)),
     ev=[ ...events... ])
```
- Feet at y~1330-1480. x positions 270 (left) 540 (center) 810 (right). Scale s 0.6-1.0 (smaller for more actors).
- `text` is narrated by the narrator voice. Use `text=""` plus `('say', None, 'actor', "line")` events for a dialogue scene (each `say` follows the previous line automatically; first one gets a time like 0.4).
- Captions are generated from the narration automatically.
- Anchors: times can be seconds, or '@word' (first occurrence in the scene text, case-insensitive, punctuation stripped), '@word#2' (2nd occurrence), '@word+0.3' (offset), '@end', '@start'. Every anchored word MUST appear in that scene's `text` (lint checks it). Dialogue `say` lines are not anchor targets.

## Events (tuples)
- ('mood', T, actor, 'sad')   ('look', T, actor, v) ('arms', T, actor, v) ('hold', T, actor, v) ('flip', T, actor, True) ('show'|'hide', T, actor)
- ('move', T0, T1, actor, x, y [, 'walk'])
- ('act', T, dur, actor, kind [, value])   kinds: jump tremble wobble grow(value = target scale multiplier; <1 shrinks) pulse fly sink float lean
- ('prop', T0, T1, emoji, (x0,y0), (x1,y1), size, {opts})   opts: wob, bob, out=T, attach=actor ... e.g. ('prop','@pizza','@end','🍕',(540,1000),(540,1000),220,{'wob':6})
- ('pop', T, 'BIG TEXT', x, y, dur, size, rot [, fill])   a sticker word on screen. Use one near the start as a hook: ('pop',0.15,'JANUARY 12',540,720,1.6,120,0)
- ('sfx', T, name [, volume])   names: alien bell blast boing bonk boom buzz cash cheer chomp clank crash ding doorbell engine fall fartlong flame gasp giggle gulp hiss kiss phone pfft pop powerup rumble sad scratch snore sparkle splash squawk tada thump tick toot trombone whistle whoosh zap
  (ONLY these names; anything else crashes the render with KeyError. 'whistle_up' is NOT valid.)
- ('flash', T [, strength]) ('shake', T, dur [, amount]) ('tint', T0, T1, (r,g,b,a)) ('zoom', T0, T1, zoom0, zoom1 [, cx, cy])

## Format that works (keep doing this)
- 25-48 s total, 4-5 scenes. Hook in the first 1-2 seconds (a pop sticker + a weird/funny first line). Escalate each scene. Last line = the punchline or a callback. End on the joke; no outro.
- One clear joke per video, simple words (the TTS reads them), short sentences. No real people, brands, or copyrighted characters. Family friendly.
- 2-3 part mini-series (Part 1/2/3, ending Part 1 and 2 on a cliffhanger) keep viewers returning: do one series every ~10 videos.
- Sound effects on most beats (sfx anchored to key words) and a small prop emoji or two per scene.
- Characters recur: Sam, Boris, Fluffy the hamster, Pizza Pete, Penny the pigeon, Gary, Grandma, Mr. Pickle, etc. (see the stories_*.py files for the cast + voices; reuse them).
