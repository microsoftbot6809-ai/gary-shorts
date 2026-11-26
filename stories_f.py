from kit import *
SANTA = dict(color=RED, body='round', voice='am_santa', tc=(190,30,40), hat='beanie', hatc=RED, mustache=True, mustachec=(250,250,255), blush=True, belly=True)
ELF = dict(color=GREEN, body='small', voice='af_nova', vpitch=1.3, tc=(20,130,60), hat='party', hatc=RED, ears='cat')
RUD = dict(color=BRN, body='blob', voice='am_fenrir', vpitch=0.85, tc=(110,70,40), horns=True, ears='dog')
OWL = dict(color=(190,160,120), body='round', voice='bm_fable', vpitch=0.9, tc=(100,80,60), glasses=True, ears='cat')
GIRL = dict(color=PINK, body='small', voice='af_nova', vpitch=1.1, tc=(200,40,120), bow=True, hat='beanie', hatc=BLUE)
d28 = dict(id='d28', title='Santa Is Stuck In The Chimney (Part 1)', cast=dict(santa=SANTA, elf=ELF, rud=RUD, girl=GIRL), narr='bm_george', narr_speed=1.06, bpm=118, mscale=0, scenes=[
 dict(bg='snow', text="It was Christmas Eve. Santa had a very big job. Eight billion presents. One night. And he was running late.",
  stage=dict(santa=dict(at=(540,1450), s=0.95, mood='worry', arms='hold')),
  ev=[('prop','@presents','@end','🎁',(160,1050),(160,1050),200,{'bob':8}),('prop','@presents','@end','🎁',(920,1100),(920,1100),200,{'bob':8}),('prop','@billion','@end','🛷',(540,900),(540,900),280,{'bob':8}),('sfx','@late','tick'),('sfx','@late+0.5','tick'),('sfx','@late+1.0','tick')]),
 dict(bg='snow', text="At the very last house, Santa climbed onto the roof. He looked at the chimney. It was a very small chimney. Then he looked at his belly. His belly looked at the chimney. They were not friends.",
  stage=dict(santa=dict(at=(250,1450), s=0.9, mood='confused')),
  ev=[('prop','@chimney','@end','🧱',(820,1200),(820,1200),380,{}),('prop','@chimney','@end','🏠',(820,1100),(820,1100),320,{'back':True}),('look','@belly','santa',(0,1)),('sfx','@belly','gulp'),('mood','@friends','santa','sad')]),
 dict(bg='snow', text="Santa took a deep breath. He sucked in his belly. He jumped. And he got stuck. Halfway down. His legs were sticking out the top.",
  stage=dict(santa=dict(at=(540,1450), s=0.95, mood='worry')),
  ev=[('act','@jumped',0.6,'santa','jump',200),('sfx','@jumped','boing'),('mood','@stuck','santa','shock'),('act','@stuck',0.5,'santa','sink',260),('sfx','@stuck','thump'),('pop','@stuck','STUCK!',540,780,1.4,150,-4),('prop','@halfway','@end+0.6','🧱',(540,1500),(540,1500),420,{}),('prop','@halfway','@end+0.6','🧱',(430,1480),(430,1480),240,{}),('prop','@halfway','@end+0.6','🧱',(650,1480),(650,1480),240,{})]),
 dict(bg='snow', text="",
  stage=dict(santa=dict(at=(270,1480), s=0.8, mood='worry'), elf=dict(at=(820,1450), s=0.7, mood='scared')),
  ev=[('say',0.4,'elf',"Santa! Are you stuck?"),('say',None,'santa',"No. I am just... resting."),('say',None,'elf',"Your legs are kicking."),('say',None,'santa',"Resting very hard.")]),
 dict(bg='snow', text="The elves pulled. The reindeer pulled. A passing owl also pulled. Nothing worked. Santa was stuck tighter than a cork in a bottle.", 
  stage=dict(santa=dict(at=(540,1480), s=0.85, mood='scream'), elf=dict(at=(160,1450), s=0.6, mood='angry', arms='run'), rud=dict(at=(920,1450), s=0.6, mood='angry')),
  ev=[('act','@elves',3.0,'elf','wobble',6),('act','@reindeer',2.5,'rud','wobble',5),('sfx','@pulled','boing',0.5),('sfx','@owl','squawk'),('sfx','@nothing','sad'),('prop','@owl','@end','🦉',(540,700),(540,700),200,{'wob':8})]),
 dict(bg='bedroom', text="Inside the house, a little girl woke up. She heard a voice coming from the fireplace. She said, Mom, there is a man in our chimney. And he is asking for a snack. To be continued.", post=1.0,
  stage=dict(girl=dict(at=(300,1450), s=0.85, mood='confused')),
  ev=[('prop','@fireplace','@end','🔥',(780,1250),(780,1250),340,{'back':True,'wob':3}),('sfx','@fireplace','alien',0.5),('say','@snack','girl',"I have cookies."),('pop','@end+0.5','PART 2 TOMORROW',540,700,1.6,100,0)]),
])
d29 = dict(id='d29', title="Santa's Christmas Gas Emergency (Part 2)", cast=dict(santa=SANTA, elf=ELF, rud=RUD, girl=GIRL), narr='bm_george', narr_speed=1.06, bpm=118, mscale=0, scenes=[
 dict(bg='snow', text="Santa was still stuck in the chimney. The clock said three hours until Christmas morning. Every kid in the world was waiting. And Santa could not even move.",
  stage=dict(santa=dict(at=(540,1480), s=0.85, mood='sad')),
  ev=[('prop','@clock','@end','⏰',(540,900),(540,900),260,{'wob':6}),('sfx','@clock','tick'),('sfx','@clock+0.5','tick'),('sfx','@clock+1.0','tick'),('prop',0.1,'@end','🧱',(540,1500),(540,1500),420,{}),('prop',0.1,'@end','🧱',(430,1480),(430,1480),240,{}),('prop',0.1,'@end','🧱',(650,1480),(650,1480),240,{})]),
 dict(bg='snow', text="Then the smallest elf had an idea. Rudolph had eaten thirty carrots, and a whole bowl of brussels sprouts for dinner. His belly was very full. Very, very full.",
  stage=dict(elf=dict(at=(250,1450), s=0.75, mood='happy'), rud=dict(at=(800,1450), s=0.85, mood='sick', arms='belly')),
  ev=[('act','@idea',0.5,'elf','jump',150),('sfx','@idea','ding'),('prop','@carrots','@end','🥕',(480,1000),(480,1000),180,{'bob':6}),('prop','@sprouts','@end','🥦',(800,950),(800,950),180,{'bob':6}),('sfx','@belly','rumble'),('act','@belly',2.0,'rud','grow',1.2)]),
 dict(bg='snow', text="",
  stage=dict(elf=dict(at=(250,1450), s=0.75, mood='evil'), rud=dict(at=(800,1450), s=0.85, mood='scared', arms='belly')),
  ev=[('say',0.4,'elf',"Rudolph, aim at the chimney."),('say',None,'rud',"Um. I do not think..."),('say',None,'elf',"It is for Christmas."),('mood','@end','rud','sad'),('say',None,'rud',"...Fine. Cover your ears.")]),
 dict(bg='snow', text="Rudolph turned around. He took a deep breath. He thought about all the sad children. And then, he let it go. It was the loudest toot in North Pole history.", post=0.6,
  stage=dict(rud=dict(at=(800,1450), s=0.85, mood='scream')),
  ev=[('sfx','@toot','blast'),('shake','@toot',2.0,18),('flash','@toot',0.3),('pop','@toot','BRAAAP!',540,800,1.7,180,-5),('prop','@toot','@end+0.8','💨',(700,1330),(260,1330),460,{'fade':True}),('mood','@toot','rud','scream')]),
 dict(bg='sky', text="POP! Santa shot out of the chimney like a cork. He flew up through the clouds. Past the moon. And landed right in his sleigh. The reindeer cheered.",
  stage=dict(santa=dict(at=(540,1500), s=0.8, mood='scream', arms='up')),
  ev=[('act',0.2,3.0,'santa','float',800),('sfx',0.2,'pop'),('sfx','@pop','pop'),('prop','@moon','@end','🌕',(850,700),(850,700),260,{'back':True}),('sfx','@clouds','whistle'),('prop','@sleigh','@end','🛷',(540,1560),(540,1560),420,{'bob':6}),('sfx','@cheered','cheer')]),
 dict(bg='snow', text="With only three hours left, Santa needed to go fast. So Rudolph kept going. Toot, toot, toot. The sleigh flew faster than a rocket. Every present was delivered on time.", post=0.6,
  stage=dict(santa=dict(at=(300,1450), s=0.8, mood='happy', arms='cheer'), rud=dict(at=(800,1450), s=0.8, mood='proud')),
  ev=[('sfx','@toot','toot'),('sfx','@toot#2','toot'),('sfx','@toot#3','toot'),('prop','@sleigh','@end','🚀',(300,1200),(900,300),260,{'lin':True,'spin':0}),('sfx','@rocket','whoosh'),('sfx','@delivered','tada')]),
 dict(bg='bedroom', text="On Christmas morning, the little girl found a letter under the tree. It said, thank you for the cookies. Love, Santa. P S. We do not talk about the chimney. And that is why, every Christmas, Santa eats a very light dinner.", post=1.2,
  stage=dict(girl=dict(at=(540,1450), s=0.95, mood='happy', hold='✉️', arms='hold')),
  ev=[('prop','@tree','@end','🎄',(850,1150),(850,1150),520,{'back':True}),('sfx','@morning','bell'),('sfx','@chimney','giggle'),('sfx','@light','tada')]),
])
# ============ D30 return presents
FRUIT = dict(color=(150,90,50), body='box', voice='am_onyx', vpitch=0.8, tc=(90,50,20), glasses=False, mustache=False, antenna=False)
CLERK = dict(color=BLUE, body='pear', voice='af_jessica', tc=(40,70,190), hat='cap', hatc=BLUE, blush=True)
DAD30 = dict(color=(120,160,220), body='box', voice='am_onyx', tc=(40,70,160), mustache=True, glasses=True, hair=True)
d30 = dict(id='d30', title='Returning The Presents', cast=dict(dad=DAD30, clerk=CLERK, fruit=FRUIT), narr='am_michael', narr_speed=1.06, bpm=122, mscale=2, scenes=[
 dict(bg='market', text="The day after Christmas, Dad went to the store. He had a bag of presents to return. And the line was a mile long.",
  stage=dict(dad=dict(at=(540,1450), s=0.95, mood='worry', hold='🛍️', arms='hold')),
  ev=[('prop','@line','@end','🧍',(100,1100),(100,1100),160,{'bob':6}),('prop','@line','@end','🧍',(250,1100),(250,1100),160,{'bob':6}),('prop','@mile','@end','🧍',(400,1100),(400,1100),160,{'bob':6}),('prop','@mile','@end','🧍',(900,1100),(900,1100),160,{'bob':6}),('sfx','@line','sad')]),
 dict(bg='market', text="",
  stage=dict(dad=dict(at=(270,1450), s=0.85, mood='neutral'), clerk=dict(at=(810,1450), s=0.85, mood='happy')),
  ev=[('say',0.4,'dad',"I would like to return this sweater."),('say',None,'clerk',"Why is it returned?"),('say',None,'dad',"It has a moose. Wearing another sweater."),('mood','@end','clerk','confused'),('say',None,'clerk',"...That is fair.")]),
 dict(bg='market', text="Then Dad returned the singing fish. The fish sang one last song. Take me to the river. The clerk was not impressed. Dad got a refund.",
  stage=dict(dad=dict(at=(270,1450), s=0.85, mood='happy', arms='hold'), clerk=dict(at=(810,1450), s=0.85, mood='smug')),
  ev=[('prop','@fish','@end','🐟',(540,1000),(540,1000),260,{'wob':10}),('sfx','@song','whistle'),('prop','@song','@end','🎶',(400,900),(400,800),180,{'bob':12}),('sfx','@refund','cash'),('prop','@refund','@end','💵',(540,1000),(540,1000),200,{'bob':8})]),
 dict(bg='market', text="Finally, Dad pulled out the last thing in the bag. A fruitcake. Grandma had given it to him. The clerk went pale. Sir, she whispered. Where did you get that?",
  stage=dict(dad=dict(at=(270,1450), s=0.85, mood='confused', hold='🎂', arms='hold'), clerk=dict(at=(810,1450), s=0.85, mood='scared')),
  ev=[('sfx','@fruitcake','buzz'),('mood','@pale','clerk','scared'),('act','@pale',1.5,'clerk','tremble',5),('tint','@whispered','@end+0.5',(0,0,40,90))]),
 dict(bg='market', text="That fruitcake was returned in nineteen ninety four. And in two thousand three. And last Tuesday. It is the same fruitcake. It has been going around this town for thirty years.",
  stage=dict(dad=dict(at=(270,1450), s=0.85, mood='shock'), clerk=dict(at=(810,1450), s=0.85, mood='scared')),
  ev=[('prop','@fruitcake','@end','🎂',(540,950),(540,950),300,{'wob':5}),('sfx','@thirty','rumble'),('pop','@thirty','30 YEARS',540,740,1.8,110,0)]),
 dict(bg='market', text="Dad said, then I will not return it. I will keep it. I will end this. He took it home. And he put it in the attic. Where it sat for exactly one year.", post=0.6,
  stage=dict(dad=dict(at=(540,1450), s=0.95, mood='proud', hold='🎂', arms='hold')),
  ev=[('sfx','@end','tada'),('mood','@attic','dad','smug'),('prop','@year','@end','📅',(540,950),(540,950),260,{'wob':4})]),
 dict(bg='bedroom', text="The next Christmas, Dad opened a present from Grandma. It was wrapped very nicely. It was heavy. It was, of course, the fruitcake. Dad looked at the camera. And he said nothing at all.", post=1.2,
  stage=dict(dad=dict(at=(540,1450), s=0.95, mood='dead', hold='🎁', arms='hold')),
  ev=[('sfx','@heavy','thump'),('sfx','@course','trombone'),('prop','@opened','@end','🎄',(850,1150),(850,1150),520,{'back':True})]),
])
STORIES = [d28, d29, d30]
