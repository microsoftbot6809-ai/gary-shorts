from kit import *
# ===== batch 2, part G: e01-e06 =====
SAM = dict(color=BLUE, body='pear', voice='am_adam', tc=(40,80,200), blush=True, hat='beanie', hatc=RED)
# ---- e01 new year resolution
e01 = dict(id='e01', title="Sam's New Year's Resolution Lasted 4 Seconds", cast=dict(sam=SAM), narr='am_michael', narr_speed=1.08, bpm=128, mscale=3, scenes=[
 dict(bg='bedroom', text="Sam made a New Year's resolution. No more snacks. Ever.",
  stage=dict(sam=dict(at=(540,1450), s=0.95, mood='proud', arms='cheer')),
  ev=[('pop',0.15,'RESOLUTION #1',540,720,1.5,100,0),('sfx','@resolution','tada'),('prop','@snacks','@end','🚫',(540,980),(540,980),300,{'wob':5}),('sfx','@snacks','buzz')]),
 dict(bg='kitchen', text="Four seconds later, Sam walked past the kitchen. The cookies saw him. The cookies waved.",
  stage=dict(sam=dict(at=(300,1450), s=0.9, mood='worry')),
  ev=[('move',0.2,'@kitchen','sam',420,1450,'walk'),('prop','@cookies','@end','🍪',(780,1180),(780,1180),240,{'bob':10}),('prop','@cookies','@end','🍪',(900,1250),(900,1250),180,{'bob':12}),('sfx','@waved','giggle'),('mood','@saw','sam','confused'),('look','@saw','sam',(1,0))]),
 dict(bg='kitchen', text="Sam said, I am strong. I am a rock. A rock does not eat cookies. Then the rock ate eleven cookies.", post=0.2,
  stage=dict(sam=dict(at=(540,1450), s=0.95, mood='proud', arms='hips')),
  ev=[('mood','@rock#2','sam','grin'),('sfx','@ate','gulp'),('sfx','@eleven','gulp'),('sfx','@eleven+0.3','gulp'),('act','@eleven',1.2,'sam','grow',1.3),('pop','@eleven','CHOMP!',540,760,1.4,150,-5),('prop','@ate','@end','🍪',(300,1000),(540,1300),150,{'spin':400,'out':'@end'}),('prop','@eleven','@end','🍪',(800,1000),(560,1300),150,{'spin':-400,'out':'@end'})]),
 dict(bg='bedroom', text="So Sam made a new resolution. Tomorrow, I will quit quitting snacks. And that one, he kept perfectly.", post=1.0,
  stage=dict(sam=dict(at=(540,1450), s=0.95, mood='sick', arms='belly')),
  ev=[('sfx','@perfectly','tada'),('mood','@perfectly','sam','happy'),('pop','@perfectly','RESOLUTION KEPT',540,720,1.5,90,0),('sfx','@kept','cheer')]),
])
# ---- e02 dog thoughts
DOG = dict(color=BRN, body='blob', voice='am_puck', vpitch=1.15, tc=(110,70,40), ears='dog', blush=True)
OWNER = dict(color=SKIN, body='tall', shirt=GREEN, belly=False, voice='bf_emma', tc=(30,110,50), hair=True)
e02 = dict(id='e02', title="What My Dog Thinks When I Leave For 5 Minutes", cast=dict(dog=DOG, owner=OWNER), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='bedroom', text="I left the house to get the mail. I was gone for five minutes. This is what my dog thought.",
  stage=dict(owner=dict(at=(250,1450), s=0.85, mood='happy'), dog=dict(at=(780,1450), s=0.85, mood='happy')),
  ev=[('move',1.0,'@mail','owner',-250,1450,'walk'),('hide','@mail+0.5','owner'),('prop','@five','@end','⏱️',(540,900),(540,900),220,{'wob':4}),('sfx','@five','tick'),('mood','@thought','dog','confused')]),
 dict(bg='bedroom', text="Minute one. She is gone. She is gone forever. I will never see her again. I have so much love left to give.",
  stage=dict(dog=dict(at=(540,1450), s=1.0, mood='cry')),
  ev=[('pop',0.2,'MINUTE 1',540,720,1.4,110,0),('sfx','@forever','sad'),('act','@forever',2.0,'dog','tremble',5),('prop','@love','@end','💔',(540,980),(540,980),260,{'bob':8})]),
 dict(bg='bedroom', text="Minute three. I guess I will guard the door. For the rest of my life. I am a very good guard dog. Nobody is coming.",
  stage=dict(dog=dict(at=(540,1450), s=1.0, mood='worry')),
  ev=[('pop',0.2,'MINUTE 3',540,720,1.4,110,0),('prop','@door','@end','🚪',(540,1050),(540,1050),420,{'back':True}),('mood','@guard','dog','proud'),('mood','@nobody','dog','sad')]),
 dict(bg='bedroom', text="Minute five. The door opened. She is back! She is alive! This is the best day of my entire life! Again!", post=0.8,
  stage=dict(dog=dict(at=(300,1450), s=0.95, mood='scream'), owner=dict(at=(800,1450), s=0.85, mood='neutral', hidden=True)),
  ev=[('show','@door','owner'),('sfx','@door','bell'),('act','@alive',1.0,'dog','jump',200),('act','@best',1.0,'dog','jump',200),('act','@Again',1.0,'dog','jump',220),('sfx','@alive','cheer'),('pop','@best','BEST DAY EVER',540,720,1.5,100,-4),('prop','@entire','@end','❤️',(300,900),(300,900),240,{'bob':10})]),
 dict(bg='bedroom', text="Then she left for the trash. And the whole thing started again.", post=1.0,
  stage=dict(dog=dict(at=(540,1450), s=0.95, mood='cry')),
  ev=[('sfx','@trash','sad'),('prop','@again','@end','🔁',(540,950),(540,950),260,{'wob':6}),('mood','@again','dog','cry')]),
])
# ---- e03 gravity
WALT = dict(color=(250,230,150), body='box', voice='bm_lewis', tc=(120,90,10), glasses=True, hair=True, mustache=True)
KIDG = dict(color=PINK, body='small', voice='af_nova', vpitch=1.1, tc=(200,40,120), bow=True)
e03 = dict(id='e03', title='What If Gravity Turned Off For One Minute', cast=dict(walt=WALT, kid=KIDG), narr='am_michael', narr_speed=1.08, bpm=126, mscale=2, scenes=[
 dict(bg='park', text="What if gravity turned off for one minute? Everything would float. Everything.",
  stage=dict(walt=dict(at=(300,1450), s=0.9, mood='neutral'), kid=dict(at=(780,1450), s=0.75, mood='happy')),
  ev=[('pop',0.15,'GRAVITY: OFF',540,720,1.4,100,0),('sfx','@float','whistle'),('act','@float',3.0,'walt','float',500),('act','@float',3.0,'kid','float',650),('mood','@Everything','walt','shock'),('prop','@float','@end','🎈',(540,1450),(540,300),240,{'lin':True})]),
 dict(bg='sky', text="Your dog would float. Your lunch would float. Your homework would float. Your teacher would float, still giving a speech.",
  stage=dict(walt=dict(at=(540,1250), s=0.85, mood='proud', arms='up')),
  ev=[('prop','@dog','@end','🐶',(180,1300),(180,500),220,{'lin':True}),('prop','@lunch','@end','🥪',(880,1350),(880,450),180,{'lin':True,'spin':120}),('prop','@homework','@end','📄',(400,1400),(400,300),180,{'lin':True,'spin':-100}),('act','@teacher',3.0,'walt','float',200),('sfx','@speech','giggle')]),
 dict(bg='sky', text="After one minute, gravity turned back on. Everything fell. And the dog landed on the teacher.", post=0.3,
  stage=dict(walt=dict(at=(540,1450), s=0.9, mood='scream')),
  ev=[('sfx','@gravity','fall'),('act','@fell',0.8,'walt','sink',120),('sfx','@fell','thump'),('prop','@landed','@end','🐶',(540,1100),(540,1330),260,{}),('pop','@landed','THUD!',540,760,1.4,150,5),('shake','@landed',0.8,14)]),
 dict(bg='park', text="The teacher said, class dismissed. And that is why you should never turn off gravity on a school day.", post=1.0,
  stage=dict(walt=dict(at=(540,1450), s=0.9, mood='smug', arms='hips')),
  ev=[('sfx','@dismissed','bell'),('sfx','@school','tada')]),
])
# ---- e04-e06 substitute wizard
WIZ = dict(color=PUR, body='tall', voice='bm_fable', vpitch=0.9, tc=(90,50,170), hat='party', hatc=PUR, mustache=True, mustachec=(240,240,250), glasses=True, hair=False)
ZOE = dict(color=PINK, body='small', voice='af_nova', vpitch=1.1, tc=(200,40,120), bow=True)
LEO = dict(color=TEAL, body='pear', voice='am_puck', vpitch=1.1, tc=(30,130,130), hat='cap', hatc=YEL, blush=True)
PRIN = dict(color=GREEN, body='box', voice='am_onyx', tc=(30,110,50), tie=True, glasses=True, mustache=True)
CAST_W = dict(wiz=WIZ, zoe=ZOE, leo=LEO, prin=PRIN)
e04 = dict(id='e04', title='The Substitute Teacher Is A Wizard (Part 1)', cast=CAST_W, narr='am_michael', narr_speed=1.08, bpm=120, mscale=3, scenes=[
 dict(bg='school', text="Monday morning. The substitute teacher walked in. He had a pointy hat. And a very long beard.",
  stage=dict(zoe=dict(at=(250,1450), s=0.75, mood='confused'), leo=dict(at=(420,1450), s=0.75, mood='confused'), wiz=dict(at=(800,1450), s=0.95, mood='proud', hidden=True)),
  ev=[('pop',0.15,'NEW SUB',540,720,1.4,110,0),('show','@walked','wiz'),('sfx','@walked','thump'),('mood','@hat','wiz','smug'),('sfx','@beard','whistle')]),
 dict(bg='school', text="",
  stage=dict(wiz=dict(at=(780,1450), s=0.95, mood='proud'), zoe=dict(at=(250,1450), s=0.75, mood='confused')),
  ev=[('say',0.4,'wiz',"Good morning, class. I am Professor Merlin."),('say',None,'zoe',"Like the wizard?"),('say',None,'wiz',"I do not know any wizards. Open your books."),('mood','@end','zoe','shock')]),
 dict(bg='school', text="He taught math. When the chalk broke, he just waved his hand. The chalk fixed itself. Then it wrote the whole lesson. By itself.",
  stage=dict(wiz=dict(at=(780,1450), s=0.95, mood='happy', arms='up'), leo=dict(at=(250,1450), s=0.75, mood='shock')),
  ev=[('sfx','@waved','powerup'),('prop','@chalk#2','@end','✏️',(540,900),(540,900),200,{'wob':10,'bob':8}),('prop','@lesson','@end','✨',(540,900),(540,900),300,{'wob':6}),('sfx','@itself','tada')]),
 dict(bg='school', text="Leo whispered, Zoe, he is a wizard. Zoe said, he cannot be. Then the teacher turned the whole class into frogs.", post=0.3,
  stage=dict(zoe=dict(at=(250,1450), s=0.75, mood='scared'), leo=dict(at=(540,1450), s=0.75, mood='scared')),
  ev=[('sfx','@frogs','zap'),('flash','@frogs',0.4),('prop','@frogs','@end+0.8','🐸',(250,1450),(250,1450),220,{'bob':12}),('prop','@frogs','@end+0.8','🐸',(540,1450),(540,1450),220,{'bob':12}),('pop','@frogs','RIBBIT!',540,760,1.5,150,-4),('hide','@frogs+0.1','zoe'),('hide','@frogs+0.1','leo')]),
 dict(bg='school', text="He turned them back at lunch. But Zoe now has a little tail. And she loves it. To be continued.", post=0.8,
  stage=dict(zoe=dict(at=(540,1450), s=0.85, mood='proud', hidden=True)),
  ev=[('show','@back','zoe'),('sfx','@back','pop'),('prop','@tail','@end','🐸',(700,1250),(700,1250),160,{'bob':6}),('pop','@end+0.2','PART 2 TOMORROW',540,700,1.6,100,0)]),
])
e05 = dict(id='e05', title='The Wizard Teacher Casts A New Year Spell (Part 2)', cast=CAST_W, narr='am_michael', narr_speed=1.08, bpm=124, mscale=3, scenes=[
 dict(bg='school', text="It was New Year's Eve. The wizard substitute had a plan. He was going to make a New Year's party. With magic.",
  stage=dict(wiz=dict(at=(540,1450), s=1.0, mood='evil', arms='up')),
  ev=[('pop',0.15,'NEW YEAR SPELL',540,720,1.5,90,0),('sfx','@plan','ding'),('prop','@party','@end','🎉',(540,900),(540,900),300,{'wob':6}),('sfx','@magic','powerup')]),
 dict(bg='school', text="He waved his hand. Balloons filled the room. Confetti rained from the ceiling. And a disco ball dropped down. The class went wild.",
  stage=dict(zoe=dict(at=(250,1450), s=0.75, mood='happy', arms='cheer'), leo=dict(at=(820,1450), s=0.75, mood='happy', arms='cheer'), wiz=dict(at=(540,1450), s=0.9, mood='happy')),
  ev=[('prop','@balloons','@end','🎈',(180,1300),(180,400),220,{'lin':True}),('prop','@balloons','@end','🎈',(900,1300),(900,350),220,{'lin':True}),('prop','@confetti','@end','🎊',(540,200),(540,1100),320,{'lin':True}),('prop','@disco','@end','🪩',(540,150),(540,500),260,{'spin':60}),('sfx','@wild','cheer')]),
 dict(bg='school', text="Then the principal walked in. He said, what is going on here? The wizard said, a small spell. The principal said, and why is my desk a dragon?", post=0.3,
  stage=dict(prin=dict(at=(250,1450), s=0.9, mood='angry', hidden=True), wiz=dict(at=(800,1450), s=0.95, mood='worry')),
  ev=[('show','@principal','prin'),('sfx','@principal','thump'),('mood','@spell','wiz','worry'),('sfx','@dragon','alien'),('prop','@dragon','@end','🐉',(540,1000),(540,1000),400,{'wob':4}),('mood','@dragon','prin','shock')]),
 dict(bg='school', text="The dragon sneezed. The principal lost his eyebrows. Everyone counted down from ten. And at midnight, the wizard disappeared. In a puff of smoke.", post=0.4,
  stage=dict(prin=dict(at=(250,1450), s=0.9, mood='shock'), wiz=dict(at=(800,1450), s=0.95, mood='smug')),
  ev=[('sfx','@sneezed','blast'),('flash','@sneezed',0.3),('sfx','@ten','tick'),('sfx','@midnight','bell'),('prop','@puff','@end','💨',(800,1250),(800,1250),420,{'fade':True}),('hide','@puff','wiz'),('sfx','@puff','whoosh'),('pop','@midnight','HAPPY NEW YEAR!',540,720,1.6,85,0)]),
 dict(bg='school', text="Only his pointy hat was left. It was still warm. And it was whispering. See you in the new year. To be continued.", post=1.0,
  stage=dict(zoe=dict(at=(540,1450), s=0.85, mood='confused')),
  ev=[('prop','@hat','@end','🎩',(540,1200),(540,1200),240,{'bob':6}),('sfx','@whispering','alien',0.5),('pop','@end+0.2','PART 3 TOMORROW',540,700,1.6,100,0)]),
])
e06 = dict(id='e06', title='The Wizard Teacher Gets Fired (Part 3)', cast=CAST_W, narr='am_michael', narr_speed=1.08, bpm=120, mscale=3, scenes=[
 dict(bg='school', text="It was the first day of the new year. The students came back. And there, at the front of the class, was the wizard.",
  stage=dict(wiz=dict(at=(800,1450), s=0.95, mood='happy'), zoe=dict(at=(250,1450), s=0.75, mood='shock'), leo=dict(at=(430,1450), s=0.75, mood='shock')),
  ev=[('pop',0.15,'HE IS BACK',540,720,1.5,100,0),('sfx','@wizard','powerup'),('mood','@front','wiz','proud')]),
 dict(bg='school', text="",
  stage=dict(prin=dict(at=(250,1450), s=0.9, mood='angry'), wiz=dict(at=(800,1450), s=0.95, mood='neutral')),
  ev=[('say',0.4,'prin',"Professor Merlin. You are fired."),('say',None,'wiz',"For what reason?"),('say',None,'prin',"You turned my desk into a dragon."),('say',None,'wiz',"It is a very good desk now.")]),
 dict(bg='school', text="The principal pointed at the door. The wizard sighed. He said, fine. Then he waved his hand. And the whole school became a castle.", post=0.3,
  stage=dict(wiz=dict(at=(540,1450), s=1.0, mood='evil', arms='up')),
  ev=[('sfx','@sighed','sad'),('sfx','@castle','zap'),('flash','@castle',0.5),('tint','@castle','@end+0.5',(60,40,120,50)),('prop','@castle','@end+0.5','🏰',(540,980),(540,980),700,{'back':True,'wob':1.5}),('shake','@castle',1.0,12)]),
 dict(bg='castle', text="Everyone loved it. The principal got a crown. The students got swords. And the wizard got a raise.", post=0.4,
  stage=dict(prin=dict(at=(250,1450), s=0.85, mood='happy'), zoe=dict(at=(540,1450), s=0.75, mood='happy', arms='cheer'), wiz=dict(at=(830,1450), s=0.9, mood='proud')),
  ev=[('prop','@crown','@end','👑',(250,1100),(250,1100),180,{'bob':6}),('prop','@swords','@end','⚔️',(540,1100),(540,1100),180,{'bob':6}),('sfx','@raise','cash'),('sfx','@loved','cheer')]),
 dict(bg='castle', text="Now every substitute teacher is a wizard. Check yours. Their beard might be glowing.", post=1.0,
  stage=dict(wiz=dict(at=(540,1450), s=0.95, mood='smug')),
  ev=[('sfx','@glowing','powerup'),('tint','@glowing','@end+0.5',(120,200,255,40)),('pop','@glowing','CHECK YOURS',540,720,1.4,100,0)]),
])
STORIES = [e01, e02, e03, e04, e05, e06]
