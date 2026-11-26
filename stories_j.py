from kit import *
# ===== batch 2, part J: e19-e24 =====
# ---- e19 dentist treasure
DOC = dict(color=TEAL, body='tall', voice='bm_lewis', tc=(20,120,120), glasses=True, hair=True, mustache=True)
PAT = dict(color=BLUE, body='pear', voice='am_adam', tc=(40,80,200), hat='cap', hatc=YEL, blush=True)
e19 = dict(id='e19', title='The Dentist Found Something In My Tooth', cast=dict(doc=DOC, pat=PAT), narr='am_michael', narr_speed=1.08, bpm=126, mscale=3, scenes=[
 dict(bg='office', text="I went to the dentist for a normal cleaning. He looked in my mouth. And he got very quiet.",
  stage=dict(pat=dict(at=(300,1450), s=0.85, mood='worry'), doc=dict(at=(800,1450), s=0.9, mood='shock')),
  ev=[('pop',0.15,'AT THE DENTIST',540,720,1.5,90,0),('sfx','@quiet','sad'),('prop','@cleaning','@end','🦷',(540,980),(540,980),260,{'wob':4})]),
 dict(bg='office', text="",
  stage=dict(pat=dict(at=(300,1450), s=0.85, mood='worry'), doc=dict(at=(800,1450), s=0.9, mood='shock')),
  ev=[('say',0.4,'doc',"Sir, how long have you had a door in your tooth?"),('say',None,'pat',"A what?"),('say',None,'doc',"There is a tiny door. With a doorbell."),('mood','@end','pat','shock')]),
 dict(bg='cave', text="The dentist pressed the bell. Ding dong. The door opened. Inside was a tiny cave. And a tiny pirate was sitting on a tiny treasure chest.",
  stage=dict(pat=dict(at=(300,1450), s=0.8, mood='scream'), doc=dict(at=(800,1450), s=0.85, mood='scared')),
  ev=[('sfx','@ding','bell'),('sfx','@dong','bell'),('prop','@treasure','@end','💰',(540,1100),(540,1100),300,{'bob':4}),('prop','@pirate','@end','🏴‍☠️',(540,850),(540,850),240,{'bob':6}),('sfx','@opened','clank')]),
 dict(bg='cave', text="The pirate said, I have lived here for ten years. Your toothpaste is great. And I have never found a single cavity. He gave the dentist a gold coin. And an invitation to the pirate party.", post=0.3,
  stage=dict(doc=dict(at=(800,1450), s=0.85, mood='happy')),
  ev=[('sfx','@years','giggle'),('sfx','@toothpaste','tada'),('prop','@coin','@end','🪙',(540,1000),(800,1200),180,{'spin':400}),('sfx','@coin','cash'),('prop','@party','@end','🎉',(300,900),(300,900),240,{'wob':6})]),
 dict(bg='office', text="Now I brush twice a day. And I floss. Because there is a pirate in my mouth. And he is very judgy.", post=1.0,
  stage=dict(pat=dict(at=(540,1450), s=0.9, mood='proud', hold='🪥', arms='hold')),
  ev=[('sfx','@floss','whistle'),('sfx','@judgy','giggle')]),
])
# ---- e20 two ghosts open house
G1 = dict(color=(225,235,255), body='round', voice='bm_fable', vpitch=0.9, tc=(60,70,160), blush=True)
G2 = dict(color=(255,215,235), body='pear', voice='bf_isabella', tc=(190,60,130), blush=True, bow=True)
FAM = dict(color=GREEN, body='tall', voice='am_onyx', tc=(30,110,50), glasses=True, hair=True)
e20 = dict(id='e20', title='The Ghosts Who Bought The Wrong House', cast=dict(g1=G1, g2=G2, fam=FAM), narr='bm_george', narr_speed=1.08, bpm=124, mscale=3, scenes=[
 dict(bg='castle', text="Two ghosts moved into a new house. It was perfect. It had creaky stairs. And a very scary basement.",
  stage=dict(g1=dict(at=(300,1450), s=0.9, mood='happy'), g2=dict(at=(780,1450), s=0.85, mood='happy')),
  ev=[('pop',0.15,'NEW HOUSE',540,720,1.5,100,0),('sfx','@creaky','clank'),('prop','@basement','@end','🏚️',(540,1000),(540,1000),500,{'back':True}),('sfx','@scary','alien')]),
 dict(bg='bedroom', text="But a living family moved in at the same time. A dad. A mom. And three kids. They were all very loud.",
  stage=dict(fam=dict(at=(250,1450), s=0.9, mood='happy', arms='cheer'), g1=dict(at=(800,1450), s=0.7, mood='worry', hidden=True)),
  ev=[('show','@moved','g1'),('sfx','@loud','cheer'),('sfx','@loud+0.3','cheer'),('mood','@loud','g1','sad')]),
 dict(bg='bedroom', text="The ghosts tried to scare them. They said, boo. The family said, aw, cute. They tried to move the furniture. The family said, thanks, we were going to do that.",
  stage=dict(g1=dict(at=(250,1450), s=0.8, mood='evil', arms='up'), fam=dict(at=(800,1450), s=0.85, mood='happy')),
  ev=[('pop','@boo','BOO!',540,740,1.5,150,-4),('sfx','@boo','alien'),('sfx','@cute','giggle'),('prop','@furniture','@end','🛋️',(260,1100),(560,1100),240,{'bob':6}),('sfx','@thanks','trombone')]),
 dict(bg='bedroom', text="So the ghosts gave up. They became the babysitters. They taught the kids ghost jokes. And they got a very nice rent discount. In ghost money.", post=0.3,
  stage=dict(g1=dict(at=(250,1450), s=0.8, mood='happy'), g2=dict(at=(540,1450), s=0.8, mood='happy'), fam=dict(at=(830,1450), s=0.85, mood='proud')),
  ev=[('sfx','@babysitters','tada'),('prop','@jokes','@end','😂',(540,900),(540,900),240,{'bob':8}),('sfx','@money','cash')]),
 dict(bg='bedroom', text="And every night at midnight, the whole family goes boo. Together. Because the ghosts told them to.", post=1.0,
  stage=dict(g1=dict(at=(250,1450), s=0.8, mood='proud'), fam=dict(at=(800,1450), s=0.85, mood='evil', arms='up')),
  ev=[('tint',0.1,'@end',(0,0,40,100)),('pop','@boo#1','BOO!',540,740,1.5,150,-4),('sfx','@together','alien')]),
])
# ---- e21 snail vs turtle
SNAIL = dict(color=YEL, body='blob', voice='af_nicole', vpitch=1.1, tc=(150,110,10), antenna=True, blush=True)
TURT = dict(color=GREEN, body='round', voice='bm_lewis', vpitch=0.85, tc=(30,110,50), glasses=True)
e21 = dict(id='e21', title="The World's Slowest Race: Snail Vs Turtle", cast=dict(snail=SNAIL, turt=TURT), narr='am_michael', narr_speed=1.08, bpm=124, mscale=2, scenes=[
 dict(bg='park', text="A snail and a turtle decided to race. First one to the finish line wins. The finish line was ten feet away.",
  stage=dict(snail=dict(at=(250,1450), s=0.75, mood='proud'), turt=dict(at=(430,1450), s=0.85, mood='smug')),
  ev=[('pop',0.15,'SLOWEST RACE',540,720,1.5,100,0),('prop','@finish','@end','🏁',(900,1250),(900,1250),300,{'bob':4}),('sfx','@race','tada')]),
 dict(bg='park', text="Three, two, one, go! Nobody moved. Then the snail moved one inch. The turtle gasped. Show off.",
  stage=dict(snail=dict(at=(250,1450), s=0.75, mood='happy'), turt=dict(at=(430,1450), s=0.85, mood='shock')),
  ev=[('sfx','@three','tick'),('sfx','@two','tick'),('sfx','@one','tick'),('sfx','@go','buzz'),('move','@moved','@end','snail',290,1450,'walk'),('sfx','@gasped','scratch'),('mood','@show','turt','angry')]),
 dict(bg='park', text="An hour passed. The turtle took a nap. The snail kept going. A bird flew by. A season changed. A tree grew. They were still racing.", post=0.3,
  stage=dict(snail=dict(at=(300,1450), s=0.75, mood='proud'), turt=dict(at=(430,1450), s=0.85, mood='sleepy')),
  ev=[('sfx','@hour','tick'),('prop','@bird','@end','🐦',(1000,500),(-100,500),160,{'lin':True}),('tint','@season','@end',(255,160,60,40)),('prop','@tree','@end','🌳',(800,1150),(800,1150),360,{'back':True}),('sfx','@tree','pop')]),
 dict(bg='park', text="Finally, they both crossed the line at the same time. It was a tie. The crowd was gone. The referee was gone. But the snail was very proud. And the turtle said, rematch tomorrow.", post=1.0,
  stage=dict(snail=dict(at=(850,1450), s=0.75, mood='proud', arms='cheer'), turt=dict(at=(600,1450), s=0.85, mood='happy')),
  ev=[('sfx','@tie','tada'),('prop','@line','@end','🏁',(540,1250),(540,1250),260,{'bob':4}),('sfx','@gone','whistle'),('sfx','@tomorrow','trombone')]),
])
# ---- e22-24 boy who couldn't stop growing
TOM = dict(color=SKIN3, body='small', voice='am_puck', vpitch=1.1, tc=(150,90,40), hat='cap', hatc=BLUE, blush=True)
MOMT = dict(color=PINK, body='tall', voice='bf_emma', tc=(200,40,120), hair=True, blush=True)
COACH = dict(color=RED, body='box', voice='am_onyx', tc=(190,40,40), mustache=True, hat='cap', hatc=RED)
CAST_T = dict(tom=TOM, mom=MOMT, coach=COACH)
e22 = dict(id='e22', title="The Boy Who Couldn't Stop Growing (Part 1)", cast=CAST_T, narr='am_michael', narr_speed=1.08, bpm=124, mscale=3, scenes=[
 dict(bg='bedroom', text="Tom woke up one morning. His feet were hanging off the bed. He had grown two feet. Overnight.",
  stage=dict(tom=dict(at=(540,1450), s=0.8, mood='shock')),
  ev=[('pop',0.15,'+2 FEET',540,720,1.6,120,0),('act','@feet',1.5,'tom','grow',1.5),('sfx','@feet','rumble'),('sfx','@overnight','whistle')]),
 dict(bg='kitchen', text="At breakfast, his mom said, honey, you look taller. Tom said, I know. By lunch, he hit his head on the ceiling. By dinner, he was in the attic.",
  stage=dict(mom=dict(at=(250,1450), s=0.85, mood='confused'), tom=dict(at=(800,1450), s=1.0, mood='worry')),
  ev=[('sfx','@ceiling','thump'),('act','@ceiling',0.6,'tom','jump',60),('act','@attic',2.0,'tom','grow',1.5),('pop','@ceiling','BONK',540,740,1.4,140,-5)]),
 dict(bg='bedroom', text="The next day, Tom was the size of the house. His head poked out of the roof. The neighbors took pictures. A bird built a nest on his hat.",
  stage=dict(tom=dict(at=(540,1450), s=1.1, mood='sad', arms='hold')),
  ev=[('act',0.2,3.0,'tom','grow',1.15),('prop','@neighbors','@end','📸',(150,900),(150,900),180,{'bob':8}),('prop','@neighbors','@end','📸',(930,950),(930,950),180,{'bob':9}),('sfx','@pictures','pop'),('prop','@bird','@end','🪹',(540,450),(540,450),200,{'bob':4}),('sfx','@nest','giggle')]),
 dict(bg='bedroom', text="Tom said, Mom, I think I am growing too fast. His mom said, it is okay. We will buy you bigger shirts. And the shirt company cried tears of joy. To be continued.", post=0.8,
  stage=dict(mom=dict(at=(250,1450), s=0.85, mood='happy'), tom=dict(at=(800,1450), s=1.1, mood='sad')),
  ev=[('sfx','@shirts','cash'),('prop','@shirts','@end','👕',(540,950),(540,950),260,{'wob':4}),('pop','@end+0.2','PART 2 TOMORROW',540,700,1.6,100,0)]),
])
e23 = dict(id='e23', title="The Boy Who Couldn't Stop Growing (Part 2)", cast=CAST_T, narr='am_michael', narr_speed=1.08, bpm=126, mscale=3, scenes=[
 dict(bg='gym', text="Tom was now ten feet tall. And a basketball coach was very interested. He said, young man, have you ever played basketball?",
  stage=dict(coach=dict(at=(250,1450), s=0.9, mood='happy', arms='point'), tom=dict(at=(800,1450), s=1.2, mood='confused')),
  ev=[('pop',0.15,'10 FEET TALL',540,720,1.5,100,0),('prop','@basketball','@end','🏀',(540,950),(540,950),220,{'bob':8}),('sfx','@interested','ding')]),
 dict(bg='gym', text="Tom did not even jump. He just stood there. And put the ball in the hoop. With his hand. Like putting a coin in a piggy bank.",
  stage=dict(tom=dict(at=(540,1450), s=1.2, mood='confused', arms='up')),
  ev=[('prop','@ball','@end','🏀',(540,700),(540,320),180,{}),('sfx','@hoop','pop'),('sfx','@coin','cash'),('prop','@hoop','@end','🥅',(540,300),(540,300),260,{'back':True})]),
 dict(bg='gym', text="The team won every game. One hundred to zero. The other team asked if Tom was allowed. The coach said, he is very allowed. And very tall.", post=0.3,
  stage=dict(coach=dict(at=(250,1450), s=0.9, mood='proud'), tom=dict(at=(800,1450), s=1.2, mood='happy')),
  ev=[('pop','@hundred','100 - 0',540,740,1.8,140,0),('sfx','@hundred','cheer'),('sfx','@asked','buzz'),('sfx','@tall','tada')]),
 dict(bg='gym', text="But there was one problem. Tom could not fit through the gym door. He had to be lifted in by crane. Every single game.", post=0.3,
  stage=dict(tom=dict(at=(540,1450), s=1.2, mood='worry')),
  ev=[('prop','@door','@end','🚪',(540,1100),(540,1100),360,{'back':True}),('prop','@crane','@end','🏗️',(850,800),(850,800),420,{'bob':4}),('sfx','@crane','clank'),('sfx','@single','trombone')]),
 dict(bg='gym', text="Tom did not mind. He loved basketball. But he had one big wish. He wanted to play hide and seek. To be continued.", post=0.8,
  stage=dict(tom=dict(at=(540,1450), s=1.2, mood='sad')),
  ev=[('prop','@seek','@end','🙈',(540,950),(540,950),260,{'wob':5}),('pop','@end+0.2','PART 3 TOMORROW',540,700,1.6,100,0)]),
])
e24 = dict(id='e24', title="The Boy Who Couldn't Stop Growing (Part 3)", cast=CAST_T, narr='am_michael', narr_speed=1.08, bpm=124, mscale=3, scenes=[
 dict(bg='park', text="Tom wanted to play hide and seek. But he was so big that nobody could lose him. He stood in the middle of the park.",
  stage=dict(tom=dict(at=(540,1450), s=1.2, mood='sad')),
  ev=[('pop',0.15,'HIDE AND SEEK',540,720,1.5,90,0),('prop','@park','@end','🌳',(150,1200),(150,1200),300,{'back':True}),('prop','@park','@end','🌳',(940,1200),(940,1200),300,{'back':True}),('sfx','@lose','sad')]),
 dict(bg='park', text="The kids counted to ten. Tom hid behind a tree. His legs stuck out. His body stuck out. His head stuck out above the tree. He was found in one second.",
  stage=dict(tom=dict(at=(540,1450), s=1.2, mood='worry')),
  ev=[('sfx','@ten','tick'),('prop','@tree','@end','🌳',(540,1150),(540,1150),360,{'back':True}),('pop','@found','FOUND!',540,740,1.5,150,-4),('sfx','@found','tada')]),
 dict(bg='park', text="Tom tried again. He hid behind a mountain. It was a very small mountain. He hid in a lake. The lake overflowed. He hid in the clouds. They found him by the shadow.", post=0.3,
  stage=dict(tom=dict(at=(540,1450), s=1.2, mood='sick')),
  ev=[('prop','@mountain','@end','🏔️',(300,1150),(300,1150),420,{'back':True}),('sfx','@lake','splash'),('sfx','@overflowed','splash'),('prop','@clouds','@end','☁️',(800,350),(800,350),300,{'bob':4}),('tint','@shadow','@end',(0,0,40,60))]),
 dict(bg='park', text="Then, a tiny girl came over. She said, I have an idea. You be the seeker. Tom said, but I will see everyone. She said, exactly. And that was the best game of hide and seek in history.", post=0.3,
  stage=dict(tom=dict(at=(800,1450), s=1.2, mood='happy'), mom=dict(at=(250,1450), s=0.6, mood='happy', hidden=True)),
  ev=[('show','@girl','mom'),('sfx','@idea','ding'),('mood','@exactly','tom','happy'),('sfx','@best','cheer')]),
 dict(bg='bedroom', text="That night, Tom shrank back to normal size. His mom said, good night. Tom said, can I be tall again tomorrow? Just for the weekend.", post=1.0,
  stage=dict(tom=dict(at=(540,1450), s=0.8, mood='happy')),
  ev=[('act',0.1,2.5,'tom','grow',0.7),('sfx','@night','snore'),('sfx','@weekend','giggle')]),
])
STORIES = [e19, e20, e21, e22, e23, e24]
