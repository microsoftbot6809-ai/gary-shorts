from kit import *
# ============ D06 hiccup moon
TIM = dict(color=YEL, body='round', voice='am_puck', vpitch=1.1, tc=(190,120,10), hat='beanie', hatc=BLUE, blush=True)
ASTRO = dict(color=WHT, body='pear', voice='am_echo', tc=(60,70,120), hat='helmet', glasses=True)
d06 = dict(id='d06', title='I Hiccupped And Flew To The Moon', cast=dict(tim=TIM, astro=ASTRO), narr='am_fenrir', narr_speed=1.08, bpm=130, mscale=2, scenes=[
 dict(bg='park', text="Tim got the hiccups. Normal hiccups. Hic. But each one was louder than the last.",
  stage=dict(tim=dict(at=(540,1450), s=0.95)),
  ev=[('pop','@hic',"HIC",540,800,0.7,100,-4),('act','@hic',0.3,'tim','jump',60),('sfx','@hic','pop'),
      ('pop','@louder','HIC!',540,780,0.8,140,5),('act','@louder',0.4,'tim','jump',120),('sfx','@louder','pop'),('pop','@last','HIC!!!',540,760,0.9,190,-5),('act','@last',0.5,'tim','jump',200),('sfx','@last','boing'),('mood','@last','tim','shock')]),
 dict(bg='park', text="On the tenth hiccup, Tim floated off the ground. On the twentieth, he flew over the school.",
  stage=dict(tim=dict(at=(540,1450), s=0.95, mood='shock', arms='up')),
  ev=[('act','@tenth',3.0,'tim','float',500),('sfx','@floated','whistle'),('mood','@twentieth','tim','scream'),('act','@twentieth',2.0,'tim','float',900),('pop','@twentieth','HIC!',540,900,0.8,160,6),('sfx','@twentieth','pop')]),
 dict(bg='sky', text="Tim shot through the clouds. A pilot waved. A bird looked very confused. Tim kept going up.",
  stage=dict(tim=dict(at=(540,1300), s=0.8, mood='scream', arms='up')),
  ev=[('act',0.3,4.2,'tim','float',250),('prop','@pilot','@end','✈️',(1250,1000),(-250,1000),300,{'lin':True}),('prop','@bird','@end','🐦',(1200,1400),(-200,1400),200,{'lin':True,'flip':False}),('mood','@bird','tim','confused'),('sfx','@pilot','whoosh'),('sfx','@bird','squawk')]),
 dict(bg='space', text="Past the satellites. Past the astronauts. All the way to the moon.",
  stage=dict(tim=dict(at=(540,1250), s=0.7, mood='scream', arms='up')),
  ev=[('prop','@satellites','@end','🛰️',(1200,800),(-200,1100),230,{'lin':True,'spin':30}),('prop','@astronauts','@end','🧑‍🚀',(-200,1300),(1250,900),230,{'lin':True,'spin':-40}),('prop','@moon','@end+1','🌕',(540,1450),(540,1450),700,{'back':True}),('act','@moon',2,'tim','sink',200),('sfx','@moon','powerup')]),
 dict(bg='space', text="Tim finally landed on the moon. He took a deep breath. And held it. And the hiccups were gone.", post=0.8,
  stage=dict(tim=dict(at=(300,1450), s=0.85, mood='neutral'), astro=dict(at=(800,1440), s=0.85, mood='shock')),
  ev=[('act','@landed',0.7,'tim','jump',130),('sfx','@landed','thump'),('mood','@breath','tim','proud'),('act','@held',1.2,'tim','grow',1.15),('mood','@held','tim','sick'),('mood','@gone','tim','happy'),('act','@gone',0.4,'tim','grow',1.0),('sfx','@gone','tada'),('say','@end+0.1','astro',"How did you get up here?"),('say',None,'tim',"Hic.")]),
 dict(bg='bedroom', text="The next morning, Tim woke up in his own bed. His mom asked, did you sleep well? Tim said, I went to the moon. His mom laughed. And then, Tim hiccuped.", post=1.0,
  stage=dict(tim=dict(at=(540,1450), s=0.95, mood='happy')),
  ev=[('sfx','@hiccuped','pop'),('act','@hiccuped',0.5,'tim','jump',150),('mood','@hiccuped','tim','shock'),('act','@hiccuped',2.5,'tim','float',250),('pop','@hiccuped','HIC!',540,800,1.0,170,-5),('sfx','@hiccuped','whistle')]),
])
# ============ D07-D08 Fluffy
FLUFF = dict(color=ORG, body='round', ears='bear', voice='af_nova', vpitch=1.35, vspeed=1.1, tc=(200,100,20), blush=True)
KIDF = dict(color=TEAL, body='small', voice='am_liam', tc=(10,120,120), hat='cap', hatc=PUR)
GUARD = dict(color=GRAY, body='tall', voice='am_onyx', vpitch=0.9, tc=(70,70,90), hat='cap', hatc=(50,50,90), mustache=True)
d07 = dict(id='d07', title="Fluffy The Hamster's Great Escape (Part 1)", cast=dict(fluff=FLUFF, kid=KIDF), narr='bf_isabella', narr_speed=1.05, bpm=132, mscale=1, scenes=[
 dict(bg='bedroom', text="This is Fluffy. Fluffy is a hamster. And Fluffy had a plan. Tonight, he was escaping.",
  stage=dict(fluff=dict(at=(540,1450), s=0.8, mood='evil', arms='hips')),
  ev=[('prop','@plan','@end+1','🗺️',(540,1000),(540,1000),280,{'wob':4}),('mood','@escaping','fluff','smug'),('sfx','@escaping','ding'),('prop',0.3,'@end+1','⚙️',(150,1250),(150,1250),180,{'back':True}),('prop',0.3,'@end+1','🪜',(930,1200),(930,1200),180,{'back':True})]),
 dict(bg='bedroom', text="Plan A was the wheel. Fluffy ran on it for three hours. Nothing happened. Plan B was more wheel.",
  stage=dict(fluff=dict(at=(540,1450), s=0.9, mood='angry')),
  ev=[('prop','@wheel','@end','🎡',(540,1230),(540,1230),400,{'spin':220,'back':True}),('act','@three',3,'fluff','bounce',9),('sfx','@three','tick'),('sfx','@three+0.6','tick'),('sfx','@three+1.2','tick'),('mood','@nothing','fluff','sad'),('sfx','@nothing','sad'),('mood','@more','fluff','angry')]),
 dict(bg='bedroom', text="Plan C was digging. Fluffy dug for one whole minute. He found a hole. Which was the other side of the cage.", 
  stage=dict(fluff=dict(at=(300,1450), s=0.9, mood='angry')),
  ev=[('act','@digging',1.6,'fluff','sink',200),('prop','@dug','@dug+1','💨',(300,1500),(300,1400),260,{'fade':True}),('sfx','@dug','whoosh'),('move','@hole','@end','fluff',800,1450,'walk'),('prop','@found','@end','🕳️',(800,1500),(800,1500),220,{'back':True}),('mood','@which','fluff','confused')]),
 dict(bg='bedroom', text="Then Fluffy noticed something. The cage door was open. It had been open all day. He walked right out.",
  stage=dict(fluff=dict(at=(240,1450), s=0.85, mood='shock')),
  ev=[('prop','@door','@end','🚪',(240,1200),(240,1200),300,{'back':True,'wob':3}),('sfx','@door','clank'),('mood','@walked','fluff','happy'),('move','@walked','@end','fluff',900,1450,'walk'),('pop','@right','FREE!',540,760,1.3,150,-4),('sfx','@right','tada')]),
 dict(bg='bedroom', text="",
  stage=dict(fluff=dict(at=(300,1450), s=0.85, mood='grin', arms='cheer'), kid=dict(at=(800,1440), s=0.8, mood='sleepy')),
  ev=[('say',0.4,'fluff',"I am free! I can go ANYWHERE!"),('mood','@end','kid','sleepy'),('sfx','@end','snore'),('say',None,'fluff',"Even... the kitchen."),('prop',4.2,6,'🍪',(540,1000),(540,1000),200,{'bob':8})]),
 dict(bg='kitchen', text="Fluffy found the cookie jar. He ate one cookie. Then another. Then he heard footsteps. To be continued.", post=1.2,
  stage=dict(fluff=dict(at=(540,1450), s=0.9, mood='yum')),
  ev=[('sfx','@ate','chomp'),('sfx','@another','chomp'),('mood','@heard','fluff','scared'),('sfx','@footsteps','thump'),('sfx','@footsteps+0.5','thump'),('pop','@end','PART 2 TOMORROW',540,700,1.6,100,0),('look','@footsteps','fluff',(1,0))]),
])
d08 = dict(id='d08', title='Fluffy The Hamster Takes Over The Mall (Part 2)', cast=dict(fluff=FLUFF, guard=GUARD, kid=KIDF), narr='bf_isabella', narr_speed=1.05, bpm=132, mscale=1, scenes=[
 dict(bg='kitchen', text="Last time, Fluffy escaped his cage. The footsteps were the mailman. Fluffy slipped out the door and ran to the one place he had always dreamed of. The mall.",
  stage=dict(fluff=dict(at=(240,1450), s=0.85, mood='happy')),
  ev=[('move','@slipped','@ran','fluff',900,1450,'run'),('prop','@mall','@end+0.5','🏬',(540,1050),(540,1050),420,{'wob':2}),('sfx','@mall','tada')]),
 dict(bg='market', text="Fluffy found a remote control car. He hopped inside and drove down the aisle. Everyone stared. Nobody believed it.",
  stage=dict(fluff=dict(at=(100,1450), s=0.7, mood='grin')),
  ev=[('prop','@remote','@end','🏎️',(100,1500),(1000,1500),350,{'lin':True}),('move','@hopped','@end','fluff',1000,1420,'slide'),('sfx','@drove','engine'),('prop','@everyone','@end','😲',(300,1000),(300,1000),150,{'bob':6}),('prop','@everyone','@end','😲',(780,1050),(780,1050),150,{'bob':6})]),
 dict(bg='restaurant', text="In the food court, Fluffy ate fifty french fries. He ate a whole pizza slice. He ate a pretzel bigger than himself.",
  stage=dict(fluff=dict(at=(540,1450), s=0.8, mood='yum')),
  ev=[('prop','@fries','@end','🍟',(200,1100),(420,1200),210,{'spin':30}),('sfx','@fries','chomp'),('sfx','@pizza','chomp'),('prop','@pizza','@end','🍕',(880,1100),(660,1200),210,{}),('sfx','@pretzel','chomp'),('prop','@pretzel','@end','🥨',(540,1000),(540,1250),420,{}),('act','@pretzel',2,'fluff','grow',1.4)]),
 dict(bg='market', text="But then, the security guard spotted him. Stop that hamster! he shouted. The chase was on.",
  stage=dict(fluff=dict(at=(900,1450), s=0.7, mood='scared'), guard=dict(at=(160,1440), s=0.85, mood='angry', arms='point')),
  ev=[('say','@stop','guard',"STOP THAT HAMSTER!"),('move','@chase','@end+1','fluff',100,1450,'run'),('move','@chase+0.3','@end+1.3','guard',700,1440,'run'),('sfx','@chase','whoosh')]),
 dict(bg='market', text="Fluffy ran through the toy store. Through the shoe store. Straight into a giant pile of pillows.", 
  stage=dict(fluff=dict(at=(80,1450), s=0.7, mood='scared')),
  ev=[('move',0.2,'@pillows','fluff',900,1450,'run'),('prop','@toy','@toy+0.9','🧸',(100,1000),(1000,1000),220,{'lin':True,'spin':100}),('prop','@shoe','@shoe+0.9','👟',(1000,1200),(100,1200),220,{'lin':True,'spin':-120}),('prop','@pile','@end','🛏️',(780,1350),(780,1350),460,{'back':True}),('sfx','@pile','thump'),('mood','@pile','fluff','happy')]),
 dict(bg='bedroom', text="Fluffy fell asleep in the pillows. The kid found him and carried him home. Fluffy is back in his cage now. But the door stays open. Because Fluffy has a new plan. A bigger one.", post=1.2,
  stage=dict(fluff=dict(at=(300,1450), s=0.8, mood='sleepy'), kid=dict(at=(800,1440), s=0.8, mood='happy')),
  ev=[('sfx','@asleep','snore'),('mood','@found','fluff','smug'),('mood','@bigger','fluff','evil'),('sfx','@bigger','ding')]),
])
# ============ D09 elevator
DAVE = dict(color=BLUE, body='tall', voice='bm_daniel', tc=(40,70,190), hat='tophat', hatc=(60,60,90), tie=True, glasses=True)
d09 = dict(id='d09', title='The Elevator That Stops On Every Floor', cast=dict(dave=DAVE), narr='am_adam', narr_speed=1.08, bpm=128, mscale=2, scenes=[
 dict(bg='office', text="Dave was late for work. He jumped in the elevator and pressed floor ten. The doors closed.",
  stage=dict(dave=dict(at=(540,1450), s=0.95, mood='worry', arms='hold')),
  ev=[('prop','@pressed','@end','🔟',(540,950),(540,950),200,{'wob':4}),('sfx','@pressed','ding'),('sfx','@closed','clank')]),
 dict(bg='office', text="Ding! Floor two. The doors opened. A cow got in. Dave did not ask questions.",
  stage=dict(dave=dict(at=(300,1450), s=0.85, mood='neutral')),
  ev=[('sfx','@ding','ding'),('pop','@ding','2',540,760,0.9,200,0),('prop','@cow','@end','🐄',(900,1300),(780,1300),420,{}),('sfx','@cow','squawk'),('mood','@cow','dave','confused'),('mood','@dave','dave','neutral')]),
 dict(bg='office', text="Floor three. A jungle. A monkey got in. Floor four. A disco. Everyone danced for no reason.", 
  stage=dict(dave=dict(at=(300,1450), s=0.85, mood='confused')),
  ev=[('pop','@three','3',540,760,0.9,200,0),('prop','@jungle','@four','🌴',(900,1150),(900,1150),260,{'bob':6}),('prop','@monkey','@four','🐒',(780,1350),(780,1350),300,{'wob':8}),('sfx','@monkey','squawk'),('pop','@four','4',540,760,0.9,200,0),('prop','@disco','@end','🪩',(540,560),(540,560),280,{'spin':50}),('sfx','@disco','sparkle'),('act','@danced',2,'dave','bounce',5),('mood','@danced','dave','happy')]),
 dict(bg='office', text="Floor five. A dinosaur. Floor six. A wedding. Dave was now a groomsman. He had never met these people.",
  stage=dict(dave=dict(at=(300,1450), s=0.85, mood='scared')),
  ev=[('pop','@five','5',540,760,0.9,200,0),('prop','@dinosaur','@six','🦖',(850,1250),(850,1250),480,{'wob':3}),('sfx','@dinosaur','boom',0.6),('pop','@six','6',540,760,0.9,200,0),('prop','@wedding','@end','💒',(850,1150),(850,1150),420,{}),('prop','@wedding','@end','🤵',(650,1350),(650,1350),230,{'bob':6}),('sfx','@wedding','bell'),('mood','@groomsman','dave','confused')]),
 dict(bg='office', text="Floor seven. Floor eight. Floor nine. Floor ten! Dave finally got off. His boss was waiting.", 
  stage=dict(dave=dict(at=(300,1450), s=0.85, mood='worry')),
  ev=[('pop','@seven','7',540,760,0.7,160,0),('sfx','@seven','ding'),('pop','@eight','8',540,760,0.7,160,0),('sfx','@eight','ding'),('pop','@nine','9',540,760,0.7,160,0),('sfx','@nine','ding'),('pop','@ten','10',540,760,1.0,220,0),('sfx','@ten','tada'),('prop','@boss','@end+1','😠',(800,1250),(800,1250),360,{'wob':4})]),
 dict(bg='office', text="",
  stage=dict(dave=dict(at=(300,1450), s=0.85, mood='worry')),
  ev=[('say',0.4,'dave',"I am so sorry I am late!"),('prop','@end+0.2','@end+8','😠',(800,1250),(800,1250),360,{'wob':4}),('say',None,'dave',"There was a cow."),('prop',3.2,6,'🚪',(800,1250),(800,1250),300,{'back':True}),('pop',3.6,'THE END',540,700,1.4,120,0),('sfx',3.6,'sad')]),
])
# ============ D10 red button
MOM = dict(color=PINK, body='tall', voice='af_bella', tc=(200,40,120), hat='crown', blush=True, belly=False)
KIDR = dict(color=GREEN, body='small', voice='am_puck', vpitch=1.15, tc=(20,130,60), hat='party', hatc=ORG)
d10 = dict(id='d10', title="Mom Said Don't Touch The Red Button", cast=dict(mom=MOM, kid=KIDR), narr='af_heart', narr_speed=1.06, bpm=124, mscale=3, scenes=[
 dict(bg='kitchen', text="Mom had one rule. Never, ever, ever touch the big red button. Max asked why. Mom said, because I said so.",
  stage=dict(mom=dict(at=(260,1450), s=0.85, mood='angry', arms='point'), kid=dict(at=(800,1450), s=0.75, mood='confused')),
  ev=[('prop','@button','@end','🔴',(540,980),(540,980),360,{'bob':6}),('sfx','@never','buzz',0.7),('mood','@why','kid','confused'),('act','@why',0.5,'kid','jump',60)]),
 dict(bg='kitchen', text="Max stared at the button for one hour. Two hours. Three hours. It was so red. It was so shiny.",
  stage=dict(kid=dict(at=(540,1450), s=0.95, mood='think')),
  ev=[('prop','@button','@end','🔴',(540,1000),(540,1000),420,{'bob':8}),('look','@hour','kid',(0,-1)),('pop','@three','3 HOURS LATER',540,700,1.5,90,0),('mood','@shiny','kid','love'),('sfx','@shiny','sparkle')]),
 dict(bg='kitchen', text="Max reached out his finger. Closer. Closer. He pressed the button.", 
  stage=dict(kid=dict(at=(540,1450), s=1.05, mood='scared', arms='point')),
  ev=[('zoom',0.2,'@pressed',1.0,1.6,540,1200),('prop','@finger','@end','🔴',(700,1180),(700,1180),240,{}),('act','@closer',2.0,'kid','lean',8),('sfx','@pressed','pop'),('shake','@pressed',0.5,6),('tint','@pressed','@end+0.4',(255,50,50,70))]),
 dict(bg='kitchen', text="Nothing happened. Max waited. Still nothing. Then the whole kitchen went dark.", 
  stage=dict(kid=dict(at=(540,1450), s=0.95, mood='confused', arms='shrug')),
  ev=[('look','@waited','kid',(1,0)),('look','@still','kid',(-1,0)),('tint','@whole','@end+1.2',(0,0,0,235)),('sfx','@whole','rumble'),('mood','@dark','kid','scared')]),
 dict(bg='kitchen', text="SURPRISE! The lights came on. It was a party. There was cake. Balloons. All of Maxs friends.", post=0.8, music=0.9,
  stage=dict(kid=dict(at=(540,1450), s=0.95, mood='wow', arms='cheer'), mom=dict(at=(240,1450), s=0.7, mood='happy', arms='cheer', hidden=True)),
  ev=[('flash','@surprise',0.5),('sfx','@surprise','cheer'),('show','@lights','mom'),('prop','@cake','@end+1','🎂',(540,1000),(540,1000),330,{'bob':8}),('prop','@balloons','@end+1','🎈',(160,760),(160,700),240,{'bob':14}),('prop','@balloons','@end+1','🎈',(900,780),(900,720),240,{'bob':14}),('prop','@friends','@end+1','🎉',(860,1130),(860,1130),220,{'wob':8}),('sfx','@cake','tada')]),
 dict(bg='kitchen', text="Mom said, I told you not to touch the button. It was supposed to be a surprise. Max said, sorry. Then he ate the cake anyway.", post=1.0,
  stage=dict(kid=dict(at=(800,1450), s=0.85, mood='yum', hold='🎂', arms='hold'), mom=dict(at=(250,1450), s=0.85, mood='angry', arms='hips')),
  ev=[('mood','@sorry','mom','smug'),('sfx','@ate','chomp'),('sfx','@anyway','chomp'),('mood','@anyway','mom','happy')]),
])
STORIES = [d06, d07, d08, d09, d10]
