# shared constants for story scripts
L_, C_, R_ = 270, 540, 810
Y0, Y1, Y2 = 1480, 1400, 1330   # feet lines: front, middle, back
RED=(235,80,80); BLUE=(90,140,235); GREEN=(110,200,120); YEL=(250,205,70); PINK=(250,140,180); ORG=(250,150,70); PUR=(160,110,225); TEAL=(80,200,200); BRN=(170,120,80); GRAY=(160,165,185); WHT=(245,245,250); SKIN=(255,207,160); SKIN2=(190,130,90); SKIN3=(235,180,130)
def person(color, **kw):
    d = dict(color=SKIN, body='tall', belly=False, **kw); d['shirt'] = color; return d
