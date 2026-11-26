import sys, subprocess, json, os
from PIL import Image
def info(p):
    d = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size','-of','json',p]))['format']
    return float(d['duration']), int(d['size'])
def sheet(vid):
    p = f'out/{vid}.mp4'; dur, size = info(p); n = 8; ims = []
    for i in range(n):
        t = dur * (i + 0.5) / n
        subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',f'{t:.2f}','-i',p,'-frames:v','1','-vf','scale=180:320',f'out/_q{i}.png'], check=True)
        ims.append(Image.open(f'out/_q{i}.png'))
    s = Image.new('RGB', (180*n, 320)); [s.paste(im, (i*180, 0)) for i, im in enumerate(ims)]
    s.save(f'out/qa_{vid}.png')
    vol = subprocess.run(['ffmpeg','-i',p,'-af','volumedetect','-f','null','-'], capture_output=True, text=True).stderr
    mv = [l for l in vol.splitlines() if 'max_volume' in l or 'mean_volume' in l]
    print(vid, round(dur,1), 's', round(size/1e6,1), 'MB', [m.split(']')[-1].strip() for m in mv])
for v in sys.argv[1:]: sheet(v)
