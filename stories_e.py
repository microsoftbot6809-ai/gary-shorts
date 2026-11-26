from kit import *
KEV = dict(color=BLUE, body='round', voice='am_puck', vpitch=1.1, tc=(30,70,190), hair=True, blush=True)
SAMMY = dict(color=(240,205,130), body='box', voice='am_puck', vpitch=1.35, tc=(160,110,30), blush=True, belly=False)
PIZZ = dict(color=ORG, body='round', voice='am_fenrir', vpitch=1.0, tc=(190,70,20), belly=False)
LADY = dict(color=PUR, body='pear', voice='bf_lily', tc=(100,40,150), hat='chef', blush=True)
CLASS = dict(color=TEAL, body='small', voice='af_nova', vpitch=1.1, tc=(10,120,120), bow=True)
d23 = dict(id='d23', title='Kevin Can Hear Food (Part 1)', cast=dict(kev=KEV, sammy=SAMMY, pizza=PIZZ, lady=LADY, cl=CLASS), narr='am_adam', narr_speed=1.08, bpm=126, mscale=2, scenes=[
 dict(bg='school', text="Kevin was a normal kid. He had a normal lunch. A sandwich, an apple, and juice. Then one day, his sandwich spoke to him.",
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='happy', arms='hold')),
  ev=[('prop','@sandwich','@end','🥪',(540,1020),(540,1020),280,{'bob':6}),('prop','@apple','@end','🍎',(200,1100),(200,1100),170,{'bob':6}),('prop','@juice','@end','🧃',(880,1100),(880,1100),170,{'bob':6}),('mood','@spoke','kev','shock'),('sfx','@spoke','ding')]),
 dict(bg='school', text="",
  stage=dict(kev=dict(at=(270,1450), s=0.85, mood='shock'), sammy=dict(at=(810,1450), s=0.75, mood='scared')),
  ev=[('say',0.4,'sammy',"Please do not eat me!"),('say',None,'kev',"You can TALK?!"),('say',None,'sammy',"I have a family! Two slices of bread and a lot of cheese!"),('mood','@end','kev','scream')]),
 dict(bg='school', text="Kevin screamed. The whole cafeteria turned around. His friend said, Kevin, are you okay? Kevin said, my sandwich is alive. His friend said, then why are you holding it?",
  stage=dict(kev=dict(at=(270,1450), s=0.85, mood='scream'), cl=dict(at=(820,1450), s=0.7, mood='confused')),
  ev=[('shake','@screamed',0.6,8),('sfx','@screamed','gasp'),('mood','@friend','cl','confused'),('pop','@alive','ALIVE?!',540,780,1.3,130,-5),('sfx','@holding','sad')]),
 dict(bg='restaurant', text="So Kevin tried to eat something else. He grabbed a slice of pizza. And the pizza screamed even louder.",
  stage=dict(kev=dict(at=(270,1450), s=0.85, mood='confused', hold='🍕', arms='hold'), pizza=dict(at=(820,1450), s=0.75, mood='scream')),
  ev=[('say','@screamed','pizza',"NOT THE CRUST!"),('mood','@screamed','kev','scream'),('shake','@screamed',0.5,8)]),
 dict(bg='market', text="Kevin dropped it. He ran to the salad bar. The lettuce was crying. The tomatoes begged for mercy. A carrot just said, I forgive you.", 
  stage=dict(kev=dict(at=(540,1450), s=0.9, mood='scared')),
  ev=[('prop','@lettuce','@end','🥬',(160,1050),(160,1050),200,{'wob':8}),('prop','@tomatoes','@end','🍅',(420,1100),(420,1100),200,{'wob':8}),('prop','@carrot','@end','🥕',(900,1050),(900,1050),200,{'bob':5}),('sfx','@crying','sad'),('sfx','@tomatoes','giggle'),('mood','@forgive','kev','sad')]),
 dict(bg='school', text="Kevin walked out of the cafeteria. He looked at his hands. He listened. And he heard a thousand tiny voices. Everything in the school was talking. To be continued.", post=1.0, music=0.5,
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='scared')),
  ev=[('tint',0.3,'@end+1',(0,0,50,100)),('prop','@thousand','@end+1','🍎',(200,900),(200,900),150,{'bob':8}),('prop','@tiny','@end+1','🍌',(880,860),(880,860),150,{'bob':8}),('prop','@voices','@end+1','🍪',(150,1200),(150,1200),150,{'bob':8}),('prop','@everything','@end+1','🍩',(900,1220),(900,1220),150,{'bob':8}),('sfx','@voices','alien',0.6),('pop','@end','PART 2 TOMORROW',540,700,1.6,100,0)]),
])
d24 = dict(id='d24', title="Kevin's Food Friends (Part 2)", cast=dict(kev=KEV, sammy=SAMMY, cl=CLASS), narr='am_adam', narr_speed=1.08, bpm=126, mscale=2, scenes=[
 dict(bg='bedroom', text="Kevin was in trouble. He could hear all food. He was hungry. And everything he looked at begged him not to eat it. So he did something smart. He made friends.",
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='sad', arms='belly')),
  ev=[('sfx','@hungry','rumble'),('prop','@begged','@end','🍞',(160,1000),(160,1000),170,{'wob':8}),('prop','@begged','@end','🧀',(900,1050),(900,1050),170,{'wob':8}),('mood','@smart','kev','happy'),('sfx','@friends','sparkle')]),
 dict(bg='bedroom', text="",
  stage=dict(kev=dict(at=(270,1450), s=0.85, mood='happy'), sammy=dict(at=(810,1450), s=0.75, mood='happy')),
  ev=[('say',0.4,'kev',"I will not eat you. I promise."),('say',None,'sammy',"Then you are my best friend!"),('mood','@end','sammy','love'),('say',None,'kev',"But I am so hungry."),('say',None,'sammy',"Try the ice cubes. They are very quiet.")]),
 dict(bg='kitchen', text="Kevin tried an ice cube. It said nothing. He crunched it. Still nothing. Finally, a food that did not talk. But it was only ice. And Kevin was still hungry.",
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='happy', hold='🧊', arms='hold')),
  ev=[('sfx','@crunched','chomp'),('mood','@nothing','kev','proud'),('mood','@only','kev','sad'),('sfx','@hungry','rumble')]),
 dict(bg='kitchen', text="Then he found a bag of chips. They said, go ahead, we are very proud to be chips. Kevin said, really? The chips said, we were born for this.", 
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='wow')),
  ev=[('prop','@chips','@end','🍟',(540,1000),(540,1000),300,{'wob':5}),('mood','@proud','kev','love'),('sfx','@born','tada'),('prop','@born','@end','🇺🇸',(540,780),(540,780),140,{'wob':10})]),
 dict(bg='kitchen', text="Kevin was about to take a bite. But then, he heard a deep voice. It was coming from inside him. It said, feed me. It was his stomach.", 
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='scared')),
  ev=[('sfx','@deep','rumble'),('act','@coming',1.5,'kev','tremble',5),('mood','@feed','kev','shock'),('pop','@feed','FEED ME',540,780,1.4,140,-4),('sfx','@stomach','alien',0.8)]),
 dict(bg='kitchen', text="Kevin looked down. His stomach had a face. It had a tiny angry mouth. And it said, I have been patient for hours. Next time, get the cake. To be continued.", post=1.0,
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='shock', arms='belly')),
  ev=[('prop','@face','@end','😠',(540,1330),(540,1330),230,{'wob':6}),('sfx','@angry','buzz'),('pop','@end','PART 3 TOMORROW',540,700,1.6,100,0)]),
])
d25 = dict(id='d25', title="Kevin's Big Decision (Part 3)", cast=dict(kev=KEV, cake=dict(color=PINK, body='round', voice='af_bella', tc=(200,40,120), hat='party', hatc=YEL, blush=True, belly=False), cl=CLASS), narr='am_adam', narr_speed=1.08, bpm=126, mscale=2, scenes=[
 dict(bg='kitchen', text="Kevin had a problem. His stomach was angry. His food was scared. And he could not decide who to listen to. So he went for a walk.",
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='think', arms='belly')),
  ev=[('prop','@stomach','@end','😠',(300,1100),(300,1100),160,{'wob':6}),('prop','@food','@end','😨',(780,1100),(780,1100),160,{'wob':6}),('sfx','@stomach','buzz',0.6)]),
 dict(bg='park', text="In the park, there was a birthday party. A big cake sat on the table. Kevin walked closer. He expected to hear screaming. But the cake said something else.",
  stage=dict(kev=dict(at=(260,1450), s=0.85, mood='worry'), cake=dict(at=(820,1440), s=0.75, mood='grin')),
  ev=[('prop','@party','@end','🎈',(150,800),(150,740),220,{'bob':10}),('prop','@party','@end','🎈',(930,820),(930,760),220,{'bob':10}),('mood','@closer','kev','scared'),('sfx','@screaming','buzz',0.5)]),
 dict(bg='park', text="",
  stage=dict(kev=dict(at=(260,1450), s=0.85, mood='worry'), cake=dict(at=(820,1440), s=0.75, mood='grin')),
  ev=[('say',0.4,'cake',"Hello! It is my birthday! Please, eat me!"),('mood','@end','kev','shock'),('say',None,'kev',"You WANT to be eaten?"),('say',None,'cake',"Of course! That is what cakes are FOR!")]),
 dict(bg='park', text="Kevin could not believe it. Some food wanted to be eaten. He just had to find the food that was ready. He took a bite of cake. And it was the happiest day of his life.", 
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='yum', hold='🍰', arms='hold')),
  ev=[('sfx','@bite','chomp'),('mood','@bite','kev','love'),('sfx','@happiest','sparkle'),('prop','@happiest','@end','✨',(540,1000),(540,1000),360,{'wob':8})]),
 dict(bg='restaurant', text="Years later, Kevin became a chef. His restaurant was called Consent. Every dish on the menu volunteered. The cakes, the pies, the cookies, they all begged to be eaten.",
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='proud', hat='chef', arms='cheer')),
  ev=[('prop','@restaurant','@end','🪧',(540,900),(540,900),340,{'wob':3}),('prop','@cakes','@end','🍰',(160,1150),(160,1150),190,{'bob':6}),('prop','@pies','@end','🥧',(900,1150),(900,1150),190,{'bob':6}),('sfx','@menu','tada'),('prop','@cookies','@end','🍪',(540,1000),(540,1000),190,{'bob':6})]),
 dict(bg='restaurant', text="There is only one item that is not on the menu. Salad. Because the salad said, I am not ready. And Kevin, being a good chef, respected that.", post=1.0,
  stage=dict(kev=dict(at=(540,1450), s=0.95, mood='happy')),
  ev=[('prop','@salad','@end','🥗',(540,1000),(540,1000),260,{'wob':8}),('sfx','@ready','sad'),('mood','@respected','kev','proud'),('sfx','@respected','sparkle')]),
])
# ============ D26 sleepwalking dad
SDAD = dict(color=(150,190,240), body='box', voice='am_onyx', tc=(40,70,160), mustache=True, hair=True, hat='beanie', hatc=(100,100,210))
CAPT = dict(color=WHT, body='round', voice='bm_daniel', tc=(40,60,130), hat='cowboy', mustache=True, mustachec=(200,200,210), belly=False)
d26 = dict(id='d26', title='My Dad Sleepwalked Onto A Cruise Ship', cast=dict(dad=SDAD, capt=CAPT, kid=KIDW if False else dict(color=PINK, body='small', voice='af_nova', vpitch=1.1, tc=(200,40,120), bow=True)), narr='am_michael', narr_speed=1.06, bpm=118, mscale=0, scenes=[
 dict(bg='bedroom', text="My dad sleepwalks. Usually, he only walks to the fridge. But last night, he walked right out the front door.",
  stage=dict(dad=dict(at=(300,1450), s=0.9, mood='sleepy', arms='point')),
  ev=[('sfx','@sleepwalks','snore'),('prop','@fridge','@end','🧊',(900,1200),(900,1200),280,{'back':True}),('move','@usually','@fridge','dad',900,1450,'walk'),('move','@walked','@end','dad',-200,1450,'walk'),('prop','@door','@end','🚪',(540,1100),(540,1100),360,{'back':True})]),
 dict(bg='street', text="He walked through the town. He walked past the bakery, and bought a loaf of bread. Asleep. Then he got on a bus. Asleep. Then a train. Still asleep.",
  stage=dict(dad=dict(at=(100,1450), s=0.8, mood='sleepy', arms='point')),
  ev=[('move',0.2,'@bus','dad',900,1450,'walk'),('prop','@bakery','@end','🥖',(300,1100),(300,1100),200,{'wob':6}),('prop','@bus','@train','🚌',(900,1250),(900,1250),400,{}),('prop','@train','@end','🚆',(540,1250),(540,1250),420,{}),('sfx','@bus','engine',0.5),('sfx','@train','whoosh'),('sfx','@asleep','snore',0.5)]),
 dict(bg='beach', text="At the harbor, he followed a crowd up a long ramp. A sign said, Welcome to the Sunshine Cruise. Dad said, mmm, pancakes. And kept walking.",
  stage=dict(dad=dict(at=(200,1450), s=0.8, mood='sleepy')),
  ev=[('move',0.2,'@end','dad',900,1400,'walk'),('prop','@ramp','@end','🚢',(540,950),(540,950),620,{'back':True,'bob':6}),('prop','@sign','@end','🪧',(260,1100),(260,1100),220,{'wob':4}),('sfx','@pancakes','sparkle')]),
 dict(bg='sky', text="The ship sailed away. Dad woke up on the deck. He looked left. He looked right. He was surrounded by ocean. And he was wearing pajamas with ducks on them.",
  stage=dict(dad=dict(at=(540,1450), s=0.95, mood='sleepy')),
  ev=[('sfx','@woke','pop'),('mood','@woke','dad','shock'),('look','@left','dad',(-1,0)),('look','@right','dad',(1,0)),('prop','@ocean','@end','🌊',(540,1750),(540,1750),700,{'back':True,'bob':10}),('mood','@pajamas','dad','scream'),('prop','@ducks','@end','🦆',(540,1150),(540,1150),150,{'bob':6})]),
 dict(bg='sky', text="",
  stage=dict(dad=dict(at=(270,1450), s=0.85, mood='scared'), capt=dict(at=(820,1450), s=0.85, mood='neutral')),
  ev=[('say',0.4,'capt',"Ticket, please."),('say',None,'dad',"I am sorry, I was asleep."),('say',None,'capt',"Everyone says that."),('mood','@end','dad','sad'),('say',None,'dad',"No, really. I was.")]),
 dict(bg='stage', text="The captain let him stay. Dad entered the karaoke contest. He sang a song. And he did it in his sleep. He won first place. He also won a free cruise. A whole other cruise. Which was fine, because the first one was already free.", post=1.2,
  stage=dict(dad=dict(at=(540,1450), s=0.95, mood='sleepy', hold='🎤', arms='hold')),
  ev=[('sfx','@karaoke','tada'),('prop','@song','@end','🎶',(300,1000),(300,900),180,{'bob':12}),('prop','@song','@end','🎶',(800,1050),(800,950),180,{'bob':12}),('sfx','@first','cheer'),('prop','@first','@end','🏆',(540,950),(540,950),260,{'bob':8})]),
])
# ============ D27 spicy pepper
HOT = dict(color=RED, body='pear', voice='am_puck', vpitch=1.05, tc=(190,30,40), hat='headband', hatc=WHT, blush=False)
d27 = dict(id='d27', title="I Ate The World's Spiciest Pepper", cast=dict(hot=HOT, kid=dict(color=PINK, body='small', voice='af_nova', vpitch=1.1, tc=(200,40,120), bow=True)), narr='am_fenrir', narr_speed=1.1, bpm=134, mscale=3, scenes=[
 dict(bg='kitchen', text="My friend said, I bet you cannot eat the world's spiciest pepper. I said, watch me. It was a big mistake.",
  stage=dict(hot=dict(at=(270,1450), s=0.85, mood='smug', arms='hips'), kid=dict(at=(820,1450), s=0.75, mood='evil', hold='🌶️', arms='hold')),
  ev=[('prop','@pepper','@end','🌶️',(540,960),(540,960),300,{'wob':5}),('sfx','@bet','ding'),('mood','@mistake','hot','scared')]),
 dict(bg='kitchen', text="I took a small bite. It was fine. Then I took a bigger bite. Then my face turned red. Then purple. Then a color I did not know.",
  stage=dict(hot=dict(at=(540,1450), s=0.95, mood='happy', hold='🌶️', arms='hold')),
  ev=[('sfx','@small','chomp'),('sfx','@bigger','chomp'),('mood','@bigger','hot','scared'),('tint','@red','@purple',(255,40,40,70)),('tint','@purple','@color',(140,40,220,80)),('tint','@color','@end',(0,255,120,80)),('act','@face',2.0,'hot','tremble',6)]),
 dict(bg='kitchen', text="Then I opened my mouth. And fire came out. Real fire. A giant flame, three meters long.", post=0.6,
  stage=dict(hot=dict(at=(300,1450), s=0.95, mood='scream')),
  ev=[('sfx','@fire','flame'),('prop','@fire','@end+1','🔥',(560,1280),(900,1280),520,{'wob':5,'flip':False}),('shake','@fire',1.8,12),('pop','@fire','FIRE!!!',540,800,1.5,170,-4),('flash','@fire',0.3)]),
 dict(bg='kitchen', text="The curtains burned. The cat ran away. The smoke alarm went off. And the pizza in the oven? It was done in four seconds.",
  stage=dict(hot=dict(at=(300,1450), s=0.9, mood='scream')),
  ev=[('prop','@curtains','@end','🔥',(900,800),(900,800),300,{'wob':8}),('prop','@cat','@end','🐈',(1100,1450),(-200,1450),220,{'lin':True}),('sfx','@alarm','buzz'),('sfx','@pizza','ding'),('prop','@pizza','@end','🍕',(850,1200),(850,1200),220,{'bob':6}),('mood','@pizza','hot','happy')]),
 dict(bg='kitchen', text="I drank water. I drank milk. I drank a whole bottle of ketchup. Nothing worked. So I did the only thing left. I ran to the ocean.",
  stage=dict(hot=dict(at=(100,1450), s=0.8, mood='scream', arms='run')),
  ev=[('prop','@water','@milk','💧',(540,1000),(540,1000),200,{'out':'@milk'}),('prop','@milk','@ketchup','🥛',(540,1000),(540,1000),200,{'out':'@ketchup'}),('prop','@ketchup','@nothing','🍅',(540,1000),(540,1000),200,{'out':'@nothing'}),('move','@ran','@end','hot',1000,1450,'run'),('sfx','@ran','whoosh')]),
 dict(bg='beach', text="I jumped in the sea. Hiss. The whole ocean boiled for a minute. A very confused fish said, hey, who ordered soup? And I was finally cool. Until the next day. When I realized I had bought a pepper again.", post=1.2,
  stage=dict(hot=dict(at=(540,1450), s=0.95, mood='sleepy')),
  ev=[('sfx','@jumped','splash'),('sfx','@hiss','hiss'),('prop','@boiled','@end','♨️',(300,1250),(300,1050),240,{'fade':True}),('prop','@fish','@end','🐟',(850,1300),(850,1300),240,{'bob':8}),('sfx','@soup','giggle'),('prop','@pepper','@end+1','🌶️',(540,980),(540,980),260,{'wob':6}),('sfx','@pepper','sad')]),
])
STORIES = [d23, d24, d25, d26, d27]
