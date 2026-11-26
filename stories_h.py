from kit import *
# ===== batch 2, part H: e07-e12 =====
# ---- e07 Fluffy for president
FLUF = dict(color=(255,215,160), body='blob', voice='af_nova', vpitch=1.4, tc=(160,100,40), ears='cat', blush=True)
SUIT = dict(color=GRAY, body='box', voice='am_onyx', tc=(60,60,80), tie=True, glasses=True, hair=True)
e07 = dict(id='e07', title='Fluffy The Hamster Runs For President', cast=dict(fluf=FLUF, suit=SUIT), narr='am_michael', narr_speed=1.08, bpm=126, mscale=2, scenes=[
 dict(bg='stage', text="Fluffy the hamster decided to run for president. Her promise was simple. More seeds. For everyone.",
  stage=dict(fluf=dict(at=(540,1450), s=0.8, mood='proud', arms='up')),
  ev=[('pop',0.15,'VOTE FLUFFY',540,720,1.5,100,0),('prop','@seeds','@end','🌰',(300,1000),(300,1000),200,{'bob':8}),('prop','@seeds','@end','🌰',(780,1000),(780,1000),200,{'bob':8}),('sfx','@promise','tada')]),
 dict(bg='stage', text="Her opponent was a man in a very expensive suit. He had a very long speech. Fluffy had a very short speech.",
  stage=dict(suit=dict(at=(250,1450), s=0.95, mood='smug', arms='hips'), fluf=dict(at=(820,1450), s=0.8, mood='neutral')),
  ev=[('sfx','@long','trombone'),('mood','@short','fluf','happy'),('sfx','@expensive','cash')]),
 dict(bg='stage', text="",
  stage=dict(suit=dict(at=(250,1450), s=0.95, mood='smug'), fluf=dict(at=(820,1450), s=0.8, mood='happy')),
  ev=[('say',0.4,'suit',"I will lower taxes, fix roads, and build a bridge."),('say',None,'fluf',"Seeds."),('sfx','@end','cheer'),('say',None,'suit',"...That is not a plan."),('say',None,'fluf',"SEEDS.")]),
 dict(bg='stage', text="The crowd went crazy. The suit man was confused. He had never seen anyone win with one word. Fluffy won by ninety nine percent. The other one percent was a goat.", post=0.3,
  stage=dict(suit=dict(at=(250,1450), s=0.95, mood='shock'), fluf=dict(at=(820,1450), s=0.8, mood='proud', arms='cheer')),
  ev=[('sfx','@crazy','cheer'),('prop','@percent','@end','🗳️',(540,950),(540,950),300,{'wob':5}),('pop','@ninety','99%',540,740,1.8,140,0),('prop','@goat','@end','🐐',(540,1250),(540,1250),240,{'bob':6})]),
 dict(bg='stage', text="Fluffy's first law was that all meetings must have snacks. Nothing has ever gone better.", post=1.0,
  stage=dict(fluf=dict(at=(540,1450), s=0.85, mood='proud', hold='🌰', arms='hold')),
  ev=[('sfx','@snacks','gulp'),('sfx','@better','tada')]),
])
# ---- e08 pizza pete moon
PETE = dict(color=ORG, body='tall', hat='cap', hatc=RED, voice='am_puck', tc=(200,70,20), blush=True)
MOONMAN = dict(color=(225,235,255), body='round', voice='bm_fable', vpitch=0.9, tc=(60,70,160), antenna=True, blush=True)
e08 = dict(id='e08', title='Pizza Pete Delivers To The Moon', cast=dict(pete=PETE, moon=MOONMAN), narr='am_michael', narr_speed=1.08, bpm=124, mscale=3, scenes=[
 dict(bg='street', text="Pizza Pete got a new order. The address was, the moon. Pete said, that is a long drive.",
  stage=dict(pete=dict(at=(540,1450), s=0.95, mood='confused', hold='🍕', arms='hold')),
  ev=[('pop',0.15,'NEW ORDER',540,720,1.4,100,0),('sfx','@order','phone'),('prop','@moon','@end','🌕',(850,700),(850,700),300,{'bob':4}),('sfx','@drive','engine')]),
 dict(bg='space', text="He strapped the pizza to a rocket. He pressed the big green button. Three, two, one, blast off!",
  stage=dict(pete=dict(at=(540,1450), s=0.8, mood='scared', arms='up')),
  ev=[('prop','@rocket','@end','🚀',(540,1400),(540,-300),400,{'lin':True}),('sfx','@three','tick'),('sfx','@two','tick'),('sfx','@one','tick'),('sfx','@blast','blast'),('shake','@blast',1.5,14),('act','@blast',2.5,'pete','float',700)]),
 dict(bg='space', text="Pete landed on the moon. A little moon man walked up. He said, you are four minutes late. That is a bad review.",
  stage=dict(pete=dict(at=(260,1450), s=0.85, mood='shock', hold='🍕', arms='hold'), moon=dict(at=(800,1450), s=0.85, mood='angry', hidden=True)),
  ev=[('show','@little','moon'),('sfx','@landed','thump'),('mood','@late','pete','sad'),('sfx','@review','buzz'),('pop','@review','1 STAR',540,740,1.6,120,0)]),
 dict(bg='space', text="Pete said, the roads are very empty up here. The moon man took one bite. He said, this is cheese. Pete said, no, that is the moon.", post=0.3,
  stage=dict(pete=dict(at=(260,1450), s=0.85, mood='happy'), moon=dict(at=(800,1450), s=0.85, mood='confused', hold='🍕', arms='hold')),
  ev=[('sfx','@bite','gulp'),('mood','@cheese','moon','happy'),('prop','@moon#2','@end','🧀',(540,980),(540,980),260,{'wob':5}),('sfx','@cheese','giggle')]),
 dict(bg='space', text="Then Pete ate the moon. And he got a five star review. And the moon man got a very fat moon.", post=1.0,
  stage=dict(pete=dict(at=(540,1450), s=0.9, mood='proud')),
  ev=[('sfx','@ate','gulp'),('sfx','@five','tada'),('pop','@five','5 STARS',540,740,1.6,120,0)]),
])
# ---- e09 back to school brain
TEA = dict(color=GREEN, body='tall', voice='bf_emma', tc=(30,110,50), glasses=True, hair=True)
KID9 = dict(color=BLUE, body='small', voice='am_puck', vpitch=1.1, tc=(40,80,200), hat='cap', hatc=RED, blush=True)
e09 = dict(id='e09', title='Back To School: Everyone Forgot Everything', cast=dict(tea=TEA, kid=KID9), narr='bm_george', narr_speed=1.08, bpm=126, mscale=2, scenes=[
 dict(bg='school', text="The first day back after winter break. The teacher asked one simple question. What is two plus two?",
  stage=dict(tea=dict(at=(780,1450), s=0.95, mood='happy'), kid=dict(at=(260,1450), s=0.75, mood='confused')),
  ev=[('pop',0.15,'FIRST DAY BACK',540,720,1.5,90,0),('prop','@two#2','@end','➕',(540,950),(540,950),260,{'wob':4}),('sfx','@question','ding')]),
 dict(bg='school', text="The whole class stared. Nobody knew. Not even the smart kid. A tumbleweed rolled through the room.",
  stage=dict(kid=dict(at=(540,1450), s=0.85, mood='shock')),
  ev=[('act','@stared',2.5,'kid','tremble',3),('sfx','@nobody','sad'),('prop','@tumbleweed','@end','🌾',(1000,1450),(-100,1450),200,{'lin':True,'spin':300}),('sfx','@tumbleweed','whistle')]),
 dict(bg='school', text="The kid raised his hand. He said, is it a fish? The teacher said, no. He said, is it Tuesday? The teacher said, it is Monday. He said, I knew it was a day.", post=0.3,
  stage=dict(tea=dict(at=(780,1450), s=0.95, mood='confused'), kid=dict(at=(260,1450), s=0.75, mood='proud', arms='up')),
  ev=[('sfx','@fish','giggle'),('prop','@fish','@end','🐟',(260,1050),(260,1050),200,{'wob':8}),('sfx','@tuesday','buzz'),('mood','@knew','kid','smug'),('sfx','@day','trombone')]),
 dict(bg='school', text="The teacher sighed. She said, class, we will start with the alphabet. And the kid said, A. B. Wait. Which one comes next?", post=1.0,
  stage=dict(tea=dict(at=(780,1450), s=0.95, mood='sad'), kid=dict(at=(260,1450), s=0.75, mood='confused')),
  ev=[('sfx','@sighed','sad'),('prop','@alphabet','@end','🔤',(540,950),(540,950),280,{'wob':4}),('sfx','@wait','scratch')]),
])
# ---- e10 boris time machine
BORIS = dict(color=BLUE, body='pear', voice='am_adam', tc=(40,80,200), hat='cap', hatc=RED, blush=True)
DINO = dict(color=GREEN, body='blob', voice='am_fenrir', vpitch=0.8, tc=(30,110,50), horns=True)
e10 = dict(id='e10', title='Boris Built A Burp-Powered Time Machine', cast=dict(boris=BORIS, dino=DINO), narr='am_michael', narr_speed=1.08, bpm=128, mscale=3, scenes=[
 dict(bg='bedroom', text="Boris built a time machine. It had one problem. It only runs on burps. So he drank twelve sodas.",
  stage=dict(boris=dict(at=(540,1450), s=0.95, mood='grin', hold='🥤', arms='hold')),
  ev=[('pop',0.15,'TIME MACHINE',540,720,1.5,90,0),('prop','@time','@end','⏰',(850,900),(850,900),260,{'wob':4}),('sfx','@burps','rumble'),('sfx','@twelve','gulp'),('sfx','@sodas','gulp'),('act','@twelve',1.5,'boris','grow',1.3)]),
 dict(bg='bedroom', text="He pressed the button. BURRRP! The machine glowed. Then the whole room spun. And Boris landed in a swamp.", post=0.3,
  stage=dict(boris=dict(at=(540,1450), s=1.0, mood='scream')),
  ev=[('sfx','@burrrp','blast'),('flash','@burrrp',0.3),('shake','@burrrp',1.5,16),('tint','@spun','@end',(120,60,200,70)),('act','@spun',1.2,'boris','pulse',0.2),('sfx','@spun','whoosh'),('sfx','@swamp','splash')]),
 dict(bg='forest', text="It was the time of the dinosaurs. And a big dinosaur was looking at Boris. Boris waved. The dinosaur licked his lips.",
  stage=dict(boris=dict(at=(260,1450), s=0.8, mood='scared'), dino=dict(at=(800,1420), s=1.1, mood='evil', hidden=True)),
  ev=[('show','@dinosaurs','dino'),('prop','@dinosaurs','@end','🦖',(900,1000),(900,1000),300,{'back':True}),('sfx','@dinosaur','alien'),('mood','@waved','boris','worry'),('sfx','@licked','gulp')]),
 dict(bg='forest', text="Boris had one last soda. He burped right in the dinosaur's face. The dinosaur fainted. All dinosaurs did. Every single one.", post=0.3,
  stage=dict(boris=dict(at=(260,1450), s=0.85, mood='grin'), dino=dict(at=(800,1420), s=1.0, mood='dead')),
  ev=[('sfx','@burped','blast'),('flash','@burped',0.3),('prop','@burped','@end','💨',(300,1250),(800,1250),380,{'fade':True}),('act','@fainted',0.8,'dino','sink',200),('sfx','@fainted','thump'),('sfx','@single','trombone')]),
 dict(bg='bedroom', text="Boris got home. He read in a book that the dinosaurs went extinct. He just smiled. And never drank soda again. Just kidding. He drank six.", post=1.0,
  stage=dict(boris=dict(at=(540,1450), s=0.95, mood='smug', hold='🥤', arms='hold')),
  ev=[('sfx','@smiled','giggle'),('sfx','@kidding','tada'),('sfx','@six','gulp')]),
])
# ---- e11 fridge disco
FRIDGE = dict(color=(215,225,240), body='box', voice='bm_lewis', tc=(60,70,100), glasses=False)
MILK = dict(color=WHT, body='small', voice='af_nova', vpitch=1.3, tc=(100,100,150), blush=True)
SLEEPY = dict(color=PINK, body='pear', voice='bf_emma', tc=(200,40,120), hair=True, blush=True)
e11 = dict(id='e11', title='What Your Fridge Does When The Door Is Closed', cast=dict(girl=SLEEPY, milk=MILK), narr='bm_george', narr_speed=1.08, bpm=130, mscale=2, scenes=[
 dict(bg='kitchen', text="Every night, I get a snack from the fridge. And every night, I wonder. Is the light really off when I close the door?",
  stage=dict(girl=dict(at=(540,1450), s=0.95, mood='confused', arms='hold')),
  ev=[('pop',0.15,'THE FRIDGE LIGHT',540,720,1.5,90,0),('prop','@fridge','@end','🧊',(850,1100),(850,1100),420,{}),('look','@wonder','girl',(1,0)),('sfx','@door','thump')]),
 dict(bg='kitchen', text="Last night, I tested it. I opened the door very slowly. And I saw it. A full disco party.",
  stage=dict(girl=dict(at=(250,1450), s=0.9, mood='shock')),
  ev=[('sfx','@slowly','whistle'),('tint','@saw','@end+0.5',(160,60,200,50)),('prop','@disco','@end','🪩',(700,500),(700,500),300,{'spin':80}),('sfx','@disco','cheer'),('prop','@party','@end','🎵',(400,850),(400,750),200,{'bob':14}),('prop','@party','@end','🎶',(900,900),(900,820),200,{'bob':10})]),
 dict(bg='kitchen', text="The milk was on the turntables. The eggs were doing a conga line. And the cheese was dancing by itself. It was very good.", post=0.3,
  stage=dict(milk=dict(at=(780,1450), s=0.85, mood='happy', arms='cheer')),
  ev=[('prop','@eggs','@end','🥚',(150,1300),(450,1300),170,{'bob':10}),('prop','@eggs','@end','🥚',(300,1300),(600,1300),170,{'bob':10}),('prop','@cheese','@end','🧀',(300,1000),(300,1000),220,{'wob':14}),('sfx','@conga','cheer'),('sfx','@good','tada')]),
 dict(bg='kitchen', text="Then they all froze. The milk said, shh. She is looking. I smiled and closed the door. And I heard the music turn right back on.", post=1.0,
  stage=dict(girl=dict(at=(250,1450), s=0.9, mood='smug'), milk=dict(at=(780,1450), s=0.85, mood='worry')),
  ev=[('sfx','@froze','scratch'),('sfx','@closed','thump'),('mood','@smiled','girl','happy'),('sfx','@music','cheer')]),
])
# ---- e12 penny pigeon pizza
PEN = dict(color=GRAY, body='round', voice='af_bella', vpitch=1.15, tc=(80,85,110), ears='cat', blush=False)
CHEF = dict(color=RED, body='pear', voice='bm_lewis', tc=(190,40,40), hat='party', hatc=WHT, mustache=True)
e12 = dict(id='e12', title='Penny The Pigeon Steals A Whole Pizza (Part 1)', cast=dict(pen=PEN, chef=CHEF), narr='am_michael', narr_speed=1.08, bpm=126, mscale=3, scenes=[
 dict(bg='street', text="This is Penny. Penny is a pigeon. And today, Penny wants a whole pizza. Not a crumb. A whole one.",
  stage=dict(pen=dict(at=(540,1450), s=0.85, mood='evil', arms='hips')),
  ev=[('pop',0.15,'PENNY WANTS PIZZA',540,720,1.5,85,0),('prop','@pizza','@end','🍕',(850,1000),(850,1000),260,{'bob':8}),('sfx','@pizza','ding'),('mood','@crumb','pen','smug')]),
 dict(bg='restaurant', text="The pizza shop was right there. A chef pulled a fresh pizza out of the oven. It was still steaming. Penny licked her beak.",
  stage=dict(pen=dict(at=(250,1450), s=0.8, mood='evil'), chef=dict(at=(800,1450), s=0.9, mood='proud', hold='🍕', arms='hold')),
  ev=[('sfx','@pulled','bell'),('prop','@steaming','@end','♨️',(800,1050),(800,950),200,{'fade':True,'bob':6}),('sfx','@licked','gulp')]),
 dict(bg='restaurant', text="She flew in fast. She grabbed the pizza with both claws. And the chef screamed. Hey! That is for a customer!", post=0.3,
  stage=dict(pen=dict(at=(250,1450), s=0.8, mood='grin'), chef=dict(at=(800,1450), s=0.9, mood='scream')),
  ev=[('sfx','@flew','whoosh'),('move','@flew','@grabbed','pen',700,1450,'run'),('prop','@grabbed','@end','🍕',(700,1300),(700,1300),260,{}),('sfx','@grabbed','pop'),('pop','@screamed','HEY!',540,740,1.5,150,-5),('sfx','@screamed','squawk')]),
 dict(bg='street', text="Penny ran down the street with the pizza. Wait. Pigeons fly. The chef chased her anyway. All across the whole city.", post=0.3,
  stage=dict(pen=dict(at=(250,1450), s=0.8, mood='grin'), chef=dict(at=(100,1450), s=0.8, mood='angry')),
  ev=[('move','@ran',"@city",'pen',900,1450,'run'),('move','@chased','@city','chef',700,1450,'run'),('sfx','@ran','engine',0.5),('sfx','@chef','squawk'),('pop','@wait','FLY, PENNY!',540,740,1.4,110,0)]),
 dict(bg='street', text="Penny landed on a roof. She opened the box. It was a pineapple pizza. Penny said, ew. And threw it away. To be continued.", post=0.8,
  stage=dict(pen=dict(at=(540,1450), s=0.9, mood='sick')),
  ev=[('prop','@roof','@end','🏠',(540,1100),(540,1100),500,{'back':True}),('prop','@pineapple','@end','🍍',(540,1050),(540,1050),220,{'wob':5}),('sfx','@ew','buzz'),('pop','@end+0.2','PART 2 TOMORROW',540,700,1.6,100,0)]),
])
STORIES = [e07, e08, e09, e10, e11, e12]
