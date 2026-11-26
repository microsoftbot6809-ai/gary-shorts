from kit import *
GARY = dict(color=SKIN, body='round', voice='am_michael', vpitch=0.95, tc=(40,90,200), hair=True, blush=True)
BOSS = dict(color=(170,175,200), body='box', voice='am_onyx', tc=(60,60,110), tie=True, glasses=True, mustache=True)
CHIEF = dict(color=TEAL, body='tall', voice='af_sarah', tc=(10,120,120), hat='headband', hatc=PINK, glasses=True, belly=False)
# ============ D11-13 Gary gets a job
d11 = dict(id='d11', title='Gary Gets A Job (Part 1)', cast=dict(gary=GARY, boss=BOSS), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='office', text="Gary needed a job. Rent was due. And beans are not free. So Gary went to a job interview.",
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='worry', arms='hold')),
  ev=[('prop','@beans','@end','🫘',(540,1000),(540,1000),220,{'bob':8}),('sfx','@rent','ding'),('prop','@rent','@rent+1','💸',(900,1100),(900,1100),200,{'bob':8}),('mood','@job','gary','proud')]),
 dict(bg='office', text="",
  stage=dict(gary=dict(at=(260,1450), s=0.85, mood='neutral'), boss=dict(at=(800,1450), s=0.85, mood='neutral')),
  ev=[('say',0.4,'boss',"Tell me about yourself."),('say',None,'gary',"I am Gary. I am very powerful."),('mood','@end','boss','confused'),('say',None,'boss',"What is your biggest weakness?"),('say',None,'gary',"Beans."),('mood','@end','boss','think')]),
 dict(bg='office', text="The boss asked, what is your biggest strength? Gary smiled. Then Gary got a very strange feeling.",
  stage=dict(gary=dict(at=(260,1450), s=0.85, mood='grin'), boss=dict(at=(800,1450), s=0.85, mood='think')),
  ev=[('mood','@strange','gary','sick'),('arms','@strange','gary','belly'),('sfx','@feeling','rumble'),('act','@feeling',1.5,'gary','tremble',5),('prop','@strange','@end','🫘',(260,1000),(260,1000),170,{'bob':8})]),
 dict(bg='office', text="Toot! It was a small toot. But the boss's papers flew everywhere. And his tie flew up and hit the ceiling.", 
  stage=dict(gary=dict(at=(260,1450), s=0.85, mood='scared'), boss=dict(at=(800,1450), s=0.85, mood='shock')),
  ev=[('sfx','@toot','toot'),('pop','@toot','TOOT!',540,800,1.0,150,-4),('prop','@papers','@end','📄',(300,1300),(1000,700),160,{'spin':400}),('prop','@papers','@end','📄',(300,1350),(900,950),160,{'spin':-300}),('prop','@papers','@end','📄',(300,1250),(1100,1100),160,{'spin':300}),('prop','@tie','@end','👔',(800,1200),(800,420),160,{'spin':20}),('act','@flew',0.6,'boss','lean',-18)]),
 dict(bg='office', text="Gary was so embarrassed. He tried to leave. But the boss stood up and said, that was amazing.",
  stage=dict(gary=dict(at=(260,1450), s=0.85, mood='sad'), boss=dict(at=(800,1450), s=0.85, mood='proud', arms='cheer')),
  ev=[('move','@tried','@leave','gary',100,1450,'walk'),('sfx','@boss','tada'),('mood','@amazing','boss','wow'),('act','@amazing',0.7,'boss','jump',160),('mood','@amazing','gary','confused')]),
 dict(bg='office', text="You are hired, said the boss. Your job title is Chief Of Air Delivery. Gary had no idea what that meant. But he said yes. To be continued.", post=1.0,
  stage=dict(gary=dict(at=(260,1450), s=0.85, mood='happy'), boss=dict(at=(800,1450), s=0.85, mood='proud')),
  ev=[('prop','@hired','@end','📜',(540,1000),(540,1000),280,{'wob':4}),('sfx','@hired','tada'),('pop','@end','PART 2 TOMORROW',540,700,1.6,100,0)]),
])
d12 = dict(id='d12', title='Gary Delivers Packages With Gas (Part 2)', cast=dict(gary=GARY, boss=BOSS), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='office', text="On his first day, Gary got a package. It had to go to the top of the tallest building in town. Delivery trucks were too slow. So the boss said, use your talent.",
  stage=dict(gary=dict(at=(260,1450), s=0.85, mood='confused', hold='📦', arms='hold'), boss=dict(at=(800,1450), s=0.85, mood='smug', arms='point')),
  ev=[('prop','@tallest','@end','🏢',(900,950),(900,950),520,{'back':True}),('mood','@talent','gary','shock'),('sfx','@talent','ding')]),
 dict(bg='street', text="Gary stood on the sidewalk. He took a deep breath. He thought about beans. And then, he let it rip.", 
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='think', arms='belly')),
  ev=[('prop',0.2,'@end','🏢',(540,820),(540,820),520,{'back':True}),('mood','@beans','gary','smug'),('sfx','@beans','rumble'),('act','@beans',1.5,'gary','tremble',6),('mood','@rip','gary','scream'),('sfx','@rip','blast')]),
 dict(bg='sky', text="WHOOOSH! Gary shot up like a rocket. Past the third floor. Past the tenth floor. Past a pigeon who dropped his sandwich.",
  stage=dict(gary=dict(at=(540,1500), s=0.8, mood='scream', arms='up', hold='📦')),
  ev=[('act',0.2,5.0,'gary','float',900),('prop','@shot','@end','💨',(540,1650),(540,1400),500,{'fade':True}),('sfx','@shot','whoosh'),('prop','@pigeon','@end','🐦',(1100,900),(150,1000),200,{'lin':True}),('prop','@sandwich','@end','🥪',(250,1000),(220,1800),150,{'spin':200}),('sfx','@pigeon','squawk')]),
 dict(bg='sky', text="Gary reached the roof. He did a perfect landing. He put the package down. And checked the label.", 
  stage=dict(gary=dict(at=(540,1450), s=0.9, mood='proud', hold='📦', arms='hold')),
  ev=[('prop','@roof','@end','🏢',(540,1620),(540,1620),900,{'back':True}),('sfx','@landing','thump'),('mood','@label','gary','confused'),('hold','@put','gary',None),('prop','@down','@end','📦',(540,1380),(540,1380),230,{}),('sfx','@down','thump')]),
 dict(bg='sky', text="The package was for floor one. The very first floor. Gary had just flown to the top of the building, to deliver something to the bottom.",
  stage=dict(gary=dict(at=(540,1450), s=0.9, mood='dead')),
  ev=[('sfx','@floor','trombone'),('pop','@floor','FLOOR ONE',540,760,1.4,130,-4),('mood','@bottom','gary','sad')]),
 dict(bg='street', text="Gary took the elevator down. The boss gave him a thumbs up. Great job, he said. You were on time. By accident, but still.", post=1.0,
  stage=dict(gary=dict(at=(270,1450), s=0.85, mood='neutral'), boss=dict(at=(800,1450), s=0.85, mood='proud', arms='cheer')),
  ev=[('prop','@thumbs','@end','👍',(800,950),(800,950),220,{'bob':6}),('sfx','@thumbs','ding'),('mood','@accident','gary','smug')]),
])
d13 = dict(id='d13', title='Gary Is Employee Of The Month (Part 3)', cast=dict(gary=GARY, boss=BOSS, chief=CHIEF), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='office', text="After a month, Gary was the best worker in the whole company. Everyone said it was his unique style. Nobody said it was the smell.",
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='proud', arms='cheer')),
  ev=[('prop','@best','@end','🏆',(540,980),(540,980),300,{'bob':8}),('sfx','@best','tada'),('prop','@smell','@end','💨',(780,1400),(900,1350),240,{'bob':8}),('sfx','@smell','toot',0.7),('mood','@smell','gary','smug')]),
 dict(bg='stage', text="At the big awards party, Gary was named Employee Of The Month. He walked up to the stage. And everyone clapped.",
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='happy', arms='cheer')),
  ev=[('sfx','@clapped','cheer'),('prop','@named','@end','🏆',(540,1000),(540,1000),320,{'wob':6}),('act','@walked',1.0,'gary','bounce',2),('prop','@clapped','@end','👏',(160,1100),(160,1100),170,{'bob':10}),('prop','@clapped','@end','👏',(920,1100),(920,1100),170,{'bob':10})]),
 dict(bg='stage', text="Then the boss said, Gary, please say a few words. Gary stepped up to the microphone. He was so nervous. He had a lot of beans for lunch.",
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='worry', arms='hold')),
  ev=[('prop','@microphone','@end','🎤',(540,1020),(540,1020),220,{'wob':3}),('mood','@nervous','gary','scared'),('mood','@beans','gary','sick'),('arms','@beans','gary','belly'),('sfx','@lunch','rumble'),('act','@lunch',1.5,'gary','tremble',6)]),
 dict(bg='stage', text="Thank you, everyone. I would like to thank my mom. And my beans. And then... BRRRAAAP! It was so loud, the microphone echoed it ten times.", post=0.6,
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='scream')),
  ev=[('say','@thank','gary',"Thank you!"),('sfx','@brrraaap','blast'),('shake','@brrraaap',1.8,16),('flash','@brrraaap',0.3),('pop','@brrraaap','BRRRAAAP!',540,820,1.6,170,-5),('prop','@echoed','@end','💨',(540,1350),(540,1350),500,{'fade':True})]),
 dict(bg='stage', text="The whole audience stood up. And ran. Out the doors. Out the windows. Out of town. Gary was alone on the stage.", 
  stage=dict(gary=dict(at=(540,1450), s=0.95, mood='sad')),
  ev=[('prop','@ran','@end','🏃',(60,1250),(1100,1250),240,{'lin':True}),('prop','@doors','@end','🏃',(1100,1350),(-100,1350),240,{'lin':True,'flip':True}),('prop','@windows','@end','🏃',(1100,1150),(-100,1150),240,{'lin':True}),('sfx','@ran','whoosh'),('mood','@alone','gary','sad'),('sfx','@alone','sad')]),
 dict(bg='office', text="The next day, the boss called Gary into his office. We have to let you go, he said. Gary was sad. But then the boss smiled. Just kidding. You are the new CEO. The whole board quit.", post=1.2,
  stage=dict(gary=dict(at=(270,1450), s=0.85, mood='sad'), boss=dict(at=(800,1450), s=0.85, mood='proud')),
  ev=[('mood','@smiled','gary','confused'),('sfx','@kidding','tada'),('mood','@kidding','gary','wow'),('prop','@ceo','@end+1','👑',(270,900),(270,900),220,{'bob':8}),('pop','@board','CEO GARY',540,700,1.8,120,0)]),
])
# ============ D14 sneeze
SAM = dict(color=GREEN, body='pear', voice='am_adam', tc=(20,130,60), hat='cap', hatc=ORG, blush=True)
d14 = dict(id='d14', title='The Sneeze That Never Ended', cast=dict(sam=SAM), narr='am_michael', narr_speed=1.1, bpm=134, mscale=2, scenes=[
 dict(bg='park', text="Sam had a tickle in his nose. A small tickle. Then a big tickle. Then he felt it coming.",
  stage=dict(sam=dict(at=(540,1450), s=0.95, mood='neutral')),
  ev=[('act','@big',0.5,'sam','pulse',0.1),('mood','@coming','sam','scared'),('prop','@tickle','@end','🌸',(300,1000),(540,1150),160,{'spin':120}),('act','@felt',1.5,'sam','grow',1.2),('pop','@felt','AH...',540,760,1.0,120,0)]),
 dict(bg='park', text="AAAH... AAAH... ACHOOOO! The first sneeze blew the leaves off every tree in the park.", post=1.0,
  stage=dict(sam=dict(at=(300,1450), s=0.9, mood='scream')),
  ev=[('pop','@aaah','AH...',540,780,0.8,120,0),('pop','@achoooo','ACHOO!!',540,800,1.4,180,-6),('sfx','@achoooo','blast'),('shake','@achoooo',1.2,14),('prop','@achoooo','@end','💨',(480,1280),(1000,1280),400,{'fade':True}),
      ('prop','@leaves','@end+1','🍂',(500,700),(1100,500),130,{'spin':400}),('prop','@leaves','@end+1','🍂',(500,900),(1100,1000),130,{'spin':-300}),('prop','@leaves','@end+1','🍂',(500,1100),(1100,1300),130,{'spin':350})]),
 dict(bg='street', text="The second sneeze flipped over a bus. The third sneeze blew away a whole bakery. Sam said sorry. And sneezed again.", post=0.9,
  stage=dict(sam=dict(at=(300,1450), s=0.9, mood='scream')),
  ev=[('sfx','@second','blast',0.8),('prop','@bus','@third','🚌',(800,1350),(900,300),340,{'spin':300}),('shake','@second',0.8,10),('sfx','@third','blast',0.9),('prop','@bakery','@end','🥐',(800,1150),(1200,500),260,{'spin':250}),('shake','@third',0.8,12),('mood','@sorry','sam','sad'),('pop','@third','ACHOO!',540,780,1.0,160,5)]),
 dict(bg='sky', text="The fourth sneeze was the biggest of all. It blew Sam across the ocean. All the way to a different country.", post=0.4,
  stage=dict(sam=dict(at=(300,1450), s=0.9, mood='scream')),
  ev=[('sfx','@fourth','blast'),('act','@fourth',3.5,'sam','fly',1),('shake','@fourth',1.2,14),('pop','@fourth','ACHOOOO!!!',540,760,1.4,170,-5),('prop','@ocean','@end','🌊',(540,1700),(540,1700),600,{'back':True})]),
 dict(bg='beach', text="Sam landed on a beach in Hawaii. A friendly local handed him a coconut. Welcome, he said. Have you tried the pepper? Sam said, no thank you. I have had enough sneezing.",
  stage=dict(sam=dict(at=(300,1450), s=0.9, mood='dizzy', hold='🥥', arms='hold')),
  ev=[('sfx','@landed','thump'),('prop','@local','@end','🌺',(850,1150),(850,1150),240,{'bob':8}),('mood','@welcome','sam','happy'),('prop','@pepper','@end','🌶️',(850,1350),(850,1350),230,{'wob':6}),('mood','@pepper','sam','scared')]),
 dict(bg='beach', text="Too late. Sam breathed in the pepper. And sneezed. And the island is now a very long way from where it used to be.", post=1.0,
  stage=dict(sam=dict(at=(540,1450), s=0.95, mood='scream')),
  ev=[('pop','@breathed','AH...',540,780,0.9,130,0),('sfx','@sneezed','blast'),('flash','@sneezed',0.4),('shake','@sneezed',2.0,16),('pop','@sneezed','ACHOOOO!',540,820,1.6,170,-5),('prop','@sneezed','@end+1','💨',(540,1350),(540,1350),600,{'fade':True})]),
])
# ============ D15 cat homework
CATH = dict(color=GRAY, body='round', ears='cat', voice='af_nicole', vpitch=1.15, tc=(90,90,120), glasses=True, blush=True, stripes=True)
TEACH = dict(color=PUR, body='tall', voice='bf_lily', tc=(100,40,160), glasses=True, hat='wizard', belly=False)
KID15 = dict(color=ORG, body='small', voice='am_puck', vpitch=1.1, tc=(200,100,20), hat='cap', hatc=GREEN)
d15 = dict(id='d15', title='I Taught My Cat To Do My Homework', cast=dict(cat=CATH, kid=KID15, teach=TEACH), narr='bf_emma', narr_speed=1.08, bpm=126, mscale=1, scenes=[
 dict(bg='bedroom', text="I had a lot of homework. Math, science, and a ten page essay. So I did what any smart kid would do. I trained my cat.",
  stage=dict(kid=dict(at=(260,1450), s=0.85, mood='worry'), cat=dict(at=(800,1450), s=0.8, mood='smug')),
  ev=[('prop','@homework','@end','📚',(540,1000),(540,1000),280,{'wob':4}),('mood','@trained','kid','evil'),('sfx','@trained','ding')]),
 dict(bg='bedroom', text="Step one, teach the cat to hold a pencil. Step two, teach the cat to read. Step three, teach the cat to do fractions. It took one week.", 
  stage=dict(cat=dict(at=(540,1450), s=0.95, mood='think', hold='✏️', arms='hold')),
  ev=[('pop','@one','1',200,760,0.8,150,0),('pop','@two','2',540,760,0.8,150,0),('pop','@three','3',880,760,0.8,150,0),('prop','@fractions','@end','➗',(540,1000),(540,1000),230,{'wob':6}),('sfx','@three','ding'),('mood','@week','cat','proud')]),
 dict(bg='school', text="On Monday, the cat did my math homework. She got every single answer right. The teacher was very impressed.", 
  stage=dict(teach=dict(at=(260,1450), s=0.85, mood='wow'), kid=dict(at=(560,1450), s=0.75, mood='grin', arms='hold'), cat=dict(at=(870,1450), s=0.6, hidden=True)),
  ev=[('prop','@math','@end','💯',(540,950),(540,950),280,{'bob':8}),('sfx','@math','tada'),('mood','@teacher','teach','proud')]),
 dict(bg='school', text="But then the teacher asked a question. Can you explain this answer out loud? And the cat meowed. The whole class went silent.",
  stage=dict(teach=dict(at=(260,1450), s=0.85, mood='confused'), kid=dict(at=(560,1450), s=0.75, mood='scared', arms='hold'), cat=dict(at=(870,1450), s=0.6, mood='smug', hidden=True)),
  ev=[('say','@explain','teach',"Please explain your answer."),('show','@meowed','cat'),('pop','@meowed','MEOW',870,980,1.2,130,-4),('sfx','@meowed','squawk'),('mood','@silent','kid','scream')]),
 dict(bg='school', text="But the teacher nodded slowly. That is the correct answer, she said. In cat language, anyway. The cat got an A plus. And I got a detention.", post=1.0,
  stage=dict(teach=dict(at=(260,1450), s=0.85, mood='proud'), kid=dict(at=(560,1450), s=0.75, mood='sad'), cat=dict(at=(870,1450), s=0.6, mood='smug')),
  ev=[('sfx','@plus','tada'),('prop','@plus','@end','🅰️',(870,950),(870,950),260,{'bob':8}),('mood','@detention','kid','dead'),('sfx','@detention','sad')]),
])
# ============ D16 snowman
SNOW = dict(color=WHT, body='round', voice='bm_fable', tc=(90,130,200), hat='tophat', hatc=(60,70,110), blush=True, belly=False)
d16 = dict(id='d16', title='The Snowman Who Wanted To Go To The Beach', cast=dict(snow=SNOW), narr='am_adam', narr_speed=1.06, bpm=118, mscale=0, scenes=[
 dict(bg='snow', text="Frosty was a snowman. He lived in the snow. And he was so, so bored. Every day, the same thing. Cold, white, and more cold.",
  stage=dict(snow=dict(at=(540,1450), s=0.95, mood='sad')),
  ev=[('sfx','@bored','sad'),('mood','@cold','snow','sleepy')]),
 dict(bg='snow', text="One day, he saw a postcard. A picture of a beach. Sun. Sand. Ice cream. Frosty said, I need to go there.",
  stage=dict(snow=dict(at=(540,1450), s=0.95, mood='neutral')),
  ev=[('prop','@postcard','@end','🏖️',(540,980),(540,980),380,{'wob':4}),('mood','@beach','snow','love'),('sfx','@beach','sparkle'),('mood','@said','snow','proud'),('act','@said',0.6,'snow','jump',150)]),
 dict(bg='snow', text="So Frosty packed a suitcase. A tiny scarf. A pair of sunglasses. And one carrot, just in case.",
  stage=dict(snow=dict(at=(540,1450), s=0.95, mood='happy', arms='cheer')),
  ev=[('prop','@suitcase','@end','🧳',(250,1250),(250,1250),240,{}),('prop','@scarf','@end','🧣',(850,1100),(850,1100),200,{'bob':6}),('prop','@sunglasses','@end','🕶️',(540,1000),(540,1000),200,{'bob':6}),('prop','@carrot','@end','🥕',(850,1350),(850,1350),180,{})]),
 dict(bg='desert', text="He walked south for three days. It got warmer. And warmer. And warmer. Frosty started to feel a little weird. Then a little smaller.",
  stage=dict(snow=dict(at=(540,1450), s=0.95, mood='happy', hold='🕶️')),
  ev=[('act','@warmer',5.0,'snow','grow',0.6),('mood','@weird','snow','sick'),('sfx','@weird','hiss'),('prop','@weird','@end','💧',(380,1300),(380,1450),120,{'fade':True}),('prop','@smaller','@end','💧',(700,1250),(700,1450),120,{'fade':True})]),
 dict(bg='beach', text="But he made it. Frosty reached the beach. He felt the sun. He felt the sand. He felt very, very wet.", post=0.6,
  stage=dict(snow=dict(at=(540,1450), s=0.6, mood='happy')),
  ev=[('act','@sun',3.0,'snow','sink',100),('mood','@wet','snow','scared'),('sfx','@wet','hiss'),('prop','@sand','@end','💧',(540,1450),(540,1500),200,{'fade':True})]),
 dict(bg='beach', text="A little girl came by. She saw a puddle with a hat, a carrot, and sunglasses. She said, aw. A snowman melted. And then she ate her ice cream.", post=1.2,
  stage=dict(snow=dict(at=(540,1500), s=0.35, mood='happy')),
  ev=[('prop','@girl','@end','👧',(900,1300),(900,1300),320,{'bob':5}),('prop','@puddle','@end','🎩',(540,1470),(540,1470),170,{}),('prop','@carrot','@end','🥕',(480,1520),(480,1520),90,{}),('sfx','@melted','sad'),('prop','@ice','@end','🍦',(760,1120),(760,1120),170,{'wob':6}),('mood','@ice','snow','happy')]),
])
STORIES = [d11, d12, d13, d14, d15, d16]
