from kit import *
# ===== batch 2, part K: e25-e30 =====
# ---- e25 pickle haircut
PICK = dict(color=GREEN, body='tall', voice='bm_lewis', tc=(30,110,50), glasses=True)
BARB = dict(color=PINK, body='pear', voice='bf_emma', tc=(200,40,120), hair=True, blush=True, bow=True)
e25 = dict(id='e25', title='Mr. Pickle Gets A Haircut', cast=dict(pick=PICK, barb=BARB), narr='am_michael', narr_speed=1.08, bpm=126, mscale=3, scenes=[
 dict(bg='restaurant', text="Mr. Pickle walked into the barber shop. He sat in the chair. The barber asked, what are we doing today?",
  stage=dict(pick=dict(at=(280,1450), s=0.95, mood='happy'), barb=dict(at=(800,1450), s=0.85, mood='happy')),
  ev=[('pop',0.15,'MR. PICKLE',540,720,1.5,100,0),('sfx','@walked','bell'),('prop','@barber','@end','✂️',(800,1000),(800,1000),200,{'wob':8}),('sfx','@asked','ding')]),
 dict(bg='restaurant', text="",
  stage=dict(pick=dict(at=(280,1450), s=0.95, mood='happy'), barb=dict(at=(800,1450), s=0.85, mood='confused')),
  ev=[('say',0.4,'pick',"Just a little off the top."),('say',None,'barb',"Sir. You are a pickle."),('say',None,'pick',"And I would like a little off the top."),('say',None,'barb',"There is nothing on top.")]),
 dict(bg='restaurant', text="She trimmed one bump. The pickle gasped. She trimmed another bump. The pickle cried. Soon, the pickle was a little pickle. Then a tiny pickle.", post=0.3,
  stage=dict(pick=dict(at=(280,1450), s=0.95, mood='shock'), barb=dict(at=(800,1450), s=0.85, mood='worry')),
  ev=[('sfx','@trimmed','whistle'),('act','@gasped',0.8,'pick','grow',0.85),('sfx','@gasped','scratch'),('mood','@cried','pick','cry'),('act','@tiny',1.5,'pick','grow',0.6),('sfx','@tiny','sad')]),
 dict(bg='restaurant', text="The barber looked in the mirror. Mr. Pickle said, perfect. Then he paid in quarters. And he rolled out. He left a very big tip. It was a dill.", post=1.0,
  stage=dict(pick=dict(at=(280,1450), s=0.6, mood='proud'), barb=dict(at=(800,1450), s=0.85, mood='confused')),
  ev=[('sfx','@perfect','tada'),('sfx','@quarters','cash'),('prop','@tip','@end','🥒',(540,1000),(540,1000),200,{'wob':6}),('sfx','@dill','trombone')]),
])
# ---- e26 alarm clock
CLK = dict(color=RED, body='round', voice='am_fenrir', vpitch=1.2, tc=(190,40,40), blush=True)
SLEEPR = dict(color=BLUE, body='pear', voice='am_adam', tc=(40,80,200), hat='beanie', hatc=YEL, blush=True)
e26 = dict(id='e26', title='My Alarm Clock Has Trust Issues', cast=dict(clk=CLK, slp=SLEEPR), narr='bm_george', narr_speed=1.08, bpm=126, mscale=0, scenes=[
 dict(bg='bedroom', text="My alarm clock has trust issues. Every morning at six, it says, are you awake? I say, yes. It does not believe me.",
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='sleepy'), clk=dict(at=(800,1450), s=0.8, mood='worry')),
  ev=[('pop',0.15,'6:00 AM',540,720,1.6,120,0),('sfx','@six','buzz'),('sfx','@awake','buzz'),('mood','@yes','slp','neutral'),('sfx','@believe','scratch')]),
 dict(bg='bedroom', text="",
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='sleepy'), clk=dict(at=(800,1450), s=0.8, mood='angry')),
  ev=[('say',0.4,'clk',"You said you were awake five minutes ago."),('say',None,'slp',"I was. Mostly."),('say',None,'clk',"You were snoring."),('say',None,'slp',"Awake snoring.")]),
 dict(bg='bedroom', text="So the alarm clock started asking questions. What is the capital of France? What is seven times eight? Who is your favorite alarm clock? The right answer is me.", post=0.3,
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='confused'), clk=dict(at=(800,1450), s=0.8, mood='smug')),
  ev=[('sfx','@france','ding'),('sfx','@eight','ding'),('sfx','@favorite','ding'),('prop','@questions','@end','❓',(540,950),(540,950),260,{'wob':8}),('sfx','@me','giggle')]),
 dict(bg='bedroom', text="Now I get up at five fifty nine. Just to beat it. And the alarm clock says, wow. Impressive. And I say, no thanks. And I go back to sleep.", post=1.0,
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='smug'), clk=dict(at=(800,1450), s=0.8, mood='shock')),
  ev=[('sfx','@wow','tada'),('sfx','@sleep','snore'),('mood','@sleep','slp','sleepy')]),
])
# ---- e27 octopus shoes
OCT = dict(color=PUR, body='round', voice='am_puck', vpitch=1.1, tc=(90,50,170), blush=True)
e27 = dict(id='e27', title='Octopus Tries To Tie His Shoes', cast=dict(oct=OCT), narr='am_michael', narr_speed=1.08, bpm=128, mscale=2, scenes=[
 dict(bg='underwater', text="Oscar the octopus got new shoes. Eight of them. He was very excited. And he had one hour to put them on.",
  stage=dict(oct=dict(at=(540,1450), s=0.95, mood='happy')),
  ev=[('pop',0.15,'8 SHOES',540,720,1.6,120,0),('prop','@shoes','@end','👟',(300,1100),(300,1100),200,{'bob':8}),('prop','@shoes','@end','👟',(780,1100),(780,1100),200,{'bob':10}),('sfx','@excited','tada'),('sfx','@hour','tick')]),
 dict(bg='underwater', text="He tied the first shoe. Perfect. He tied the second. Perfect. By the fourth shoe, he was tangled in his own legs.",
  stage=dict(oct=dict(at=(540,1450), s=0.95, mood='happy')),
  ev=[('sfx','@first','pop'),('sfx','@second','pop'),('sfx','@fourth','scratch'),('mood','@tangled','oct','worry'),('act','@tangled',2.0,'oct','wobble',6)]),
 dict(bg='underwater', text="By the seventh shoe, he had tied himself to a chair. And a lamp. And a very confused crab. The crab said, can you help me?", post=0.3,
  stage=dict(oct=dict(at=(300,1450), s=0.9, mood='scared')),
  ev=[('prop','@chair','@end','🪑',(700,1250),(700,1250),240,{'wob':3}),('prop','@lamp','@end','💡',(900,1100),(900,1100),180,{'bob':4}),('prop','@crab','@end','🦀',(540,1500),(540,1500),200,{'bob':8}),('sfx','@crab','squawk')]),
 dict(bg='underwater', text="Then Oscar had an idea. He took off all the shoes. He walked barefoot. And he said, that was a very long hour. The crab agreed. The crab is still tied up.", post=1.0,
  stage=dict(oct=dict(at=(300,1450), s=0.9, mood='proud')),
  ev=[('sfx','@idea','ding'),('sfx','@long','trombone'),('sfx','@still','giggle')]),
])
# ---- e28 elf on the shelf january
ELF = dict(color=RED, body='small', voice='af_nova', vpitch=1.25, tc=(190,40,40), hat='party', hatc=RED, ears='cat', blush=True)
FAMD = dict(color=GREEN, body='tall', voice='am_onyx', tc=(30,110,50), glasses=True, hair=True)
e28 = dict(id='e28', title='The Elf On The Shelf Is Still Here In January', cast=dict(elf=ELF, dad=FAMD), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='bedroom', text="It was January twelfth. The Christmas tree was gone. The lights were gone. But the elf on the shelf was still there.",
  stage=dict(elf=dict(at=(540,1450), s=0.75, mood='worry')),
  ev=[('pop',0.15,'JANUARY 12',540,720,1.6,120,0),('sfx','@january','tick'),('mood','@gone','elf','sad'),('prop','@shelf','@end','📚',(540,1150),(540,1150),360,{})]),
 dict(bg='bedroom', text="He had nowhere to go. Nobody told him Christmas was over. He sat on the shelf. Watching. And watching. And watching.",
  stage=dict(elf=dict(at=(540,1450), s=0.75, mood='sad')),
  ev=[('look','@watching','elf',(1,0)),('look','@watching#2','elf',(-1,0)),('look','@watching#3','elf',(0,1)),('sfx','@nowhere','sad'),('prop','@over','@end','📅',(850,950),(850,950),240,{'wob':4})]),
 dict(bg='bedroom', text="The dad found him. He said, you are still here. The elf said, nobody told me it was over. The dad said, it has been two weeks. The elf said, I thought you were just being quiet.", post=0.3,
  stage=dict(dad=dict(at=(250,1450), s=0.9, mood='confused'), elf=dict(at=(800,1450), s=0.75, mood='worry')),
  ev=[('sfx','@found','ding'),('sfx','@weeks','buzz'),('mood','@quiet','elf','happy'),('sfx','@quiet','giggle')]),
 dict(bg='bedroom', text="So the dad gave him a plane ticket. And a very small suitcase. The elf flew all the way back to the North Pole. And he told Santa. Nobody was ever late for Christmas again.", post=1.0,
  stage=dict(dad=dict(at=(250,1450), s=0.9, mood='happy'), elf=dict(at=(800,1450), s=0.75, mood='happy', arms='cheer')),
  ev=[('prop','@plane','@end','✈️',(700,1050),(700,1050),240,{'bob':6}),('sfx','@plane','whoosh'),('sfx','@santa','tada'),('sfx','@again','cheer')]),
])
# ---- e29 socks superpower
HERO = dict(color=RED, body='pear', voice='am_adam', tc=(190,40,40), hat='cap', hatc=BLUE, blush=True)
VILL = dict(color=PUR, body='tall', voice='bm_fable', vpitch=0.85, tc=(90,50,170), hat='tophat', hatc=BLACK if 'BLACK' in globals() else (40,30,60), mustache=True)
e29 = dict(id='e29', title='My Superpower Is Finding The Other Sock', cast=dict(hero=HERO, vill=VILL), narr='am_michael', narr_speed=1.08, bpm=130, mscale=2, scenes=[
 dict(bg='city_night', text="Every hero has a power. Flying. Super strength. Invisibility. Mine is much better. I can always find the other sock.",
  stage=dict(hero=dict(at=(540,1450), s=0.95, mood='proud', arms='up')),
  ev=[('pop',0.15,'SOCK MAN',540,720,1.5,120,0),('prop','@flying','@end','🦸',(150,1000),(150,1000),180,{'bob':6}),('prop','@sock','@end','🧦',(540,950),(540,950),280,{'wob':6}),('sfx','@sock','tada')]),
 dict(bg='city_night', text="One day, a villain stole every single left sock in the city. He said, now they will never match! Ha ha ha!",
  stage=dict(vill=dict(at=(800,1450), s=0.95, mood='evil', arms='up'), hero=dict(at=(250,1450), s=0.8, mood='shock')),
  ev=[('prop','@sock','@end','🧦',(800,900),(800,900),260,{'bob':8}),('sfx','@stole','zap'),('sfx','@match','trombone'),('mood','@never','vill','evil')]),
 dict(bg='city_night', text="Sock Man closed his eyes. He focused. And he followed the feeling. It led him to a secret lair. Under a very big laundromat.", post=0.3,
  stage=dict(hero=dict(at=(250,1450), s=0.9, mood='worry')),
  ev=[('sfx','@focused','powerup'),('tint','@followed','@end',(120,60,200,40)),('move','@followed','@lair','hero',800,1450,'walk'),('prop','@laundromat','@end','🧺',(850,1150),(850,1150),420,{'bob':4}),('sfx','@lair','rumble')]),
 dict(bg='cave', text="Inside, there were a million left socks. Sock Man took them all. He found every pair. And the villain said, no! Not the matching! And he ran away crying. His socks were holes.", post=0.3,
  stage=dict(hero=dict(at=(250,1450), s=0.9, mood='proud', arms='cheer'), vill=dict(at=(800,1450), s=0.9, mood='cry')),
  ev=[('prop','@million','@end','🧦',(300,1000),(300,1000),200,{'bob':8}),('prop','@million','@end','🧦',(540,950),(540,950),200,{'bob':10}),('prop','@million','@end','🧦',(780,1000),(780,1000),200,{'bob':9}),('sfx','@pair','cheer'),('sfx','@holes','trombone')]),
 dict(bg='city_night', text="The city was saved. Every sock was matched. But I still cannot find my own right sock. Some things are just not meant to be.", post=1.0,
  stage=dict(hero=dict(at=(540,1450), s=0.95, mood='sad')),
  ev=[('sfx','@saved','cheer'),('sfx','@still','sad'),('sfx','@meant','trombone')]),
])
# ---- e30 cheese heist
MOUSE = dict(color=GRAY, body='small', voice='am_eric', vpitch=1.3, tc=(80,85,110), ears='cat', hat='cap', hatc=(40,40,60), blush=True)
CAT = dict(color=ORG, body='round', voice='bm_lewis', vpitch=0.8, tc=(180,70,20), ears='cat', blush=True)
e30 = dict(id='e30', title='The Great Cheese Heist', cast=dict(mouse=MOUSE, cat=CAT), narr='am_michael', narr_speed=1.08, bpm=130, mscale=3, scenes=[
 dict(bg='kitchen', text="Marty the mouse had one goal. The biggest block of cheese in the world. It was guarded by one very sleepy cat.",
  stage=dict(mouse=dict(at=(250,1450), s=0.7, mood='evil'), cat=dict(at=(800,1450), s=0.95, mood='sleepy')),
  ev=[('pop',0.15,'THE HEIST',540,720,1.6,120,0),('prop','@cheese','@end','🧀',(850,1100),(850,1100),360,{'wob':3}),('sfx','@goal','ding'),('sfx','@sleepy','snore')]),
 dict(bg='kitchen', text="Step one. Sneak past the cat. Marty tiptoed. The floor creaked. The cat opened one eye. Marty froze. The cat closed it again.",
  stage=dict(mouse=dict(at=(250,1450), s=0.7, mood='worry'), cat=dict(at=(800,1450), s=0.95, mood='sleepy')),
  ev=[('pop','@one','STEP 1',540,720,1.4,110,0),('move','@tiptoed','@froze','mouse',600,1450,'walk'),('sfx','@creaked','clank'),('mood','@opened','cat','angry'),('mood','@closed','cat','sleepy'),('sfx','@froze','scratch')]),
 dict(bg='kitchen', text="Step two. Get the cheese. It was too heavy. So Marty brought a tiny crane. And a tiny truck. And a tiny crew of mice in tiny hard hats.", post=0.3,
  stage=dict(mouse=dict(at=(250,1450), s=0.7, mood='proud')),
  ev=[('pop','@two','STEP 2',540,720,1.4,110,0),('prop','@crane','@end','🏗️',(700,1000),(700,1000),360,{'bob':3}),('prop','@truck','@end','🚚',(300,1400),(600,1400),240,{'bob':5}),('sfx','@crane','clank'),('sfx','@hats','giggle')]),
 dict(bg='kitchen', text="Step three. Escape. They carried the cheese out the door. The cat woke up. He said, nice try. And ate all the mice. Just kidding. He ate the cheese.", post=0.3,
  stage=dict(mouse=dict(at=(250,1450), s=0.7, mood='scared'), cat=dict(at=(800,1450), s=0.95, mood='evil')),
  ev=[('pop','@three','STEP 3',540,720,1.4,110,0),('sfx','@woke','alien'),('sfx','@kidding','trombone'),('sfx','@ate#2','gulp'),('mood','@cheese#2','cat','happy')]),
 dict(bg='kitchen', text="Marty sat on the floor and cried. Then the cat gave him a slice. And they became best friends. And that is why my kitchen is always missing cheese.", post=1.0,
  stage=dict(mouse=dict(at=(250,1450), s=0.7, mood='cry'), cat=dict(at=(800,1450), s=0.95, mood='happy', hold='🧀', arms='hold')),
  ev=[('sfx','@cried','sad'),('sfx','@slice','tada'),('mood','@friends','mouse','happy'),('sfx','@missing','giggle')]),
])
STORIES = [e25, e26, e27, e28, e29, e30]
