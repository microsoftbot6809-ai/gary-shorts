from kit import *
# ===== batch 2, part I: e13-e18 =====
PEN = dict(color=GRAY, body='round', voice='af_bella', vpitch=1.15, tc=(80,85,110), ears='cat')
PEN2 = dict(color=(190,195,215), body='round', voice='am_puck', vpitch=1.1, tc=(80,85,110), ears='cat', hat='cap', hatc=BLUE)
PEN3 = dict(color=(150,155,175), body='small', voice='am_eric', vpitch=1.1, tc=(80,85,110), ears='cat', glasses=True)
CHEF = dict(color=RED, body='pear', voice='bm_lewis', tc=(190,40,40), hat='party', hatc=WHT, mustache=True)
MAYOR = dict(color=ORG, body='tall', voice='bm_lewis', tc=(180,70,20), hat='tophat', mustache=True, glasses=True)
CASTPEN = dict(pen=PEN, p2=PEN2, p3=PEN3, chef=CHEF, mayor=MAYOR)
# ---- e13
e13 = dict(id='e13', title='Penny The Pigeon Starts A Pigeon Gang (Part 2)', cast=CASTPEN, narr='am_michael', narr_speed=1.08, bpm=126, mscale=3, scenes=[
 dict(bg='street', text="Last time, Penny threw away a pineapple pizza. This time, she was done doing it alone. She needed a gang.",
  stage=dict(pen=dict(at=(540,1450), s=0.9, mood='evil', arms='hips')),
  ev=[('pop',0.15,'PIGEON GANG',540,720,1.5,100,0),('prop','@pineapple','@end','🍍',(850,1000),(850,1000),200,{'wob':5}),('sfx','@alone','sad'),('sfx','@gang','ding')]),
 dict(bg='park', text="She found two other pigeons on a bench. One was named Pete. One was named Gerald. Gerald wore tiny glasses. He did the math.",
  stage=dict(pen=dict(at=(540,1450), s=0.8, mood='smug'), p2=dict(at=(180,1450), s=0.75, mood='happy', hidden=True), p3=dict(at=(900,1450), s=0.65, mood='proud', hidden=True)),
  ev=[('show','@pigeons','p2'),('show','@gerald','p3'),('prop','@math','@end','🧮',(900,1050),(900,1050),200,{'wob':6}),('sfx','@math','ding')]),
 dict(bg='park', text="Penny said, here is the plan. We steal the biggest pizza in town. Gerald said, I calculated one hundred and four ways it goes wrong. Pete said, I will fly in circles. For morale.",
  stage=dict(pen=dict(at=(540,1450), s=0.8, mood='proud'), p2=dict(at=(180,1450), s=0.75, mood='happy'), p3=dict(at=(900,1450), s=0.65, mood='worry')),
  ev=[('prop','@biggest','@end','🍕',(540,950),(540,950),360,{'wob':3}),('sfx','@hundred','buzz'),('pop','@hundred','104',540,740,1.8,140,0),('sfx','@circles','whistle'),('act','@circles',2.5,'p2','float',60)]),
 dict(bg='restaurant', text="They flew into the pizza shop at midnight. They carried a pizza as big as a door. But the pizza was too heavy. The gang fell on the chef's head.", post=0.3,
  stage=dict(pen=dict(at=(180,1450), s=0.8, mood='scream'), p2=dict(at=(430,1450), s=0.75, mood='scream'), chef=dict(at=(800,1450), s=0.9, mood='shock')),
  ev=[('tint','@midnight','@end',(0,0,40,100)),('prop','@pizza','@end','🍕',(300,1250),(300,1250),480,{'bob':6}),('sfx','@heavy','fall'),('act','@fell',0.6,'chef','sink',150),('sfx','@fell','thump'),('pop','@fell','OOF!',540,760,1.4,150,-5)]),
 dict(bg='restaurant', text="The chef looked at the pigeons. The pigeons looked at the chef. Then the chef said, take the pizza. Just stop falling on me. To be continued.", post=0.8,
  stage=dict(chef=dict(at=(250,1450), s=0.9, mood='sad'), pen=dict(at=(800,1450), s=0.8, mood='grin')),
  ev=[('sfx','@take','giggle'),('sfx','@stop','sad'),('pop','@end+0.2','PART 3 TOMORROW',540,700,1.6,100,0)]),
])
e14 = dict(id='e14', title='Penny The Pigeon Takes Over The City (Part 3)', cast=CASTPEN, narr='am_michael', narr_speed=1.08, bpm=128, mscale=3, scenes=[
 dict(bg='city_night', text="Penny now had a gang, and a free pizza every night. But Penny wanted more. She wanted the whole city.",
  stage=dict(pen=dict(at=(540,1450), s=0.9, mood='evil', arms='up'), p2=dict(at=(200,1450), s=0.7, mood='happy'), p3=dict(at=(880,1450), s=0.6, mood='worry')),
  ev=[('pop',0.15,'PIGEON CITY',540,720,1.5,100,0),('prop','@pizza','@end','🍕',(540,950),(540,950),240,{'bob':8}),('sfx','@whole','powerup')]),
 dict(bg='city_night', text="She called every pigeon in town. Ten thousand pigeons landed on the town hall. All at once. They were very organized.",
  stage=dict(pen=dict(at=(540,1450), s=0.9, mood='proud')),
  ev=[('prop','@ten','@end','🕊️',(100,500),(100,500),180,{'bob':10}),('prop','@ten','@end','🕊️',(300,300),(300,300),180,{'bob':12}),('prop','@thousand','@end','🕊️',(500,450),(500,450),180,{'bob':9}),('prop','@thousand','@end','🕊️',(740,300),(740,300),180,{'bob':11}),('prop','@landed','@end','🕊️',(940,480),(940,480),180,{'bob':8}),('sfx','@landed','squawk'),('sfx','@thousand','squawk')]),
 dict(bg='city_night', text="",
  stage=dict(mayor=dict(at=(250,1450), s=0.9, mood='scared'), pen=dict(at=(800,1450), s=0.8, mood='smug')),
  ev=[('say',0.4,'mayor',"What do you pigeons want?!"),('say',None,'pen',"Free pizza. For every pigeon. Forever."),('say',None,'mayor',"That is... a lot of pizza."),('say',None,'pen',"We are a lot of pigeons.")]),
 dict(bg='city_night', text="The mayor thought about it. Then he made a rule. Every Friday is Pigeon Pizza Night. The whole city celebrated. Even Gerald smiled.", post=0.3,
  stage=dict(mayor=dict(at=(250,1450), s=0.9, mood='happy', arms='cheer'), pen=dict(at=(800,1450), s=0.8, mood='proud', arms='cheer')),
  ev=[('sfx','@rule','tada'),('pop','@friday','PIZZA NIGHT',540,720,1.6,100,0),('prop','@city','@end','🍕',(300,900),(300,900),200,{'bob':8}),('prop','@city','@end','🍕',(780,900),(780,900),200,{'bob':8}),('sfx','@celebrated','cheer'),('sfx','@smiled','giggle')]),
 dict(bg='city_night', text="And that is why, if you ever see a pigeon, you should smile. She might own the city.", post=1.0,
  stage=dict(pen=dict(at=(540,1450), s=0.9, mood='smug')),
  ev=[('sfx','@smile','giggle'),('sfx','@might','tada')]),
])
# ---- e15 snow day
PRIN = dict(color=GREEN, body='box', voice='am_onyx', tc=(30,110,50), tie=True, glasses=True, mustache=True)
KIDS = dict(color=PINK, body='small', voice='af_nova', vpitch=1.1, tc=(200,40,120), bow=True, hat='beanie', hatc=BLUE)
e15 = dict(id='e15', title='The Principal Who Cancelled The Snow Day', cast=dict(prin=PRIN, kid=KIDS), narr='bm_george', narr_speed=1.08, bpm=124, mscale=2, scenes=[
 dict(bg='snow', text="It snowed forty inches overnight. Every kid in town was praying for a snow day. And then the phone rang.",
  stage=dict(kid=dict(at=(540,1450), s=0.85, mood='worry', arms='up')),
  ev=[('pop',0.15,'SNOW DAY?',540,720,1.5,100,0),('prop','@snowed','@end','❄️',(300,300),(300,900),160,{'lin':True}),('prop','@snowed','@end','❄️',(780,200),(780,800),160,{'lin':True}),('sfx','@phone','phone'),('prop','@phone','@end','📱',(540,980),(540,980),260,{'wob':8})]),
 dict(bg='office', text="It was the principal. He said, school is open. The kid said, but it is snowing. He said, I have a snowplow. And a shovel. And a very big coat.",
  stage=dict(prin=dict(at=(540,1450), s=0.95, mood='smug', arms='hips')),
  ev=[('sfx','@open','buzz'),('prop','@snowplow','@end','🚜',(850,1250),(850,1250),320,{'bob':6}),('prop','@shovel','@end','🧣',(200,1100),(200,1100),200,{'bob':6}),('mood','@coat','prin','proud')]),
 dict(bg='snow', text="Every kid showed up. The principal shoveled the whole school by himself. It took nine hours. At the end, he was a snowman.",
  stage=dict(prin=dict(at=(540,1450), s=0.95, mood='sad', arms='hold')),
  ev=[('sfx','@shoveled','thump'),('sfx','@nine','tick'),('tint','@end','@end+1',(220,235,255,90)),('prop','@snowman','@end+0.6','⛄',(540,1250),(540,1250),240,{'bob':4}),('act','@snowman',2.5,'prin','grow',0.8)]),
 dict(bg='snow', text="The kids made a deal. They made him a real snowman. And they got the day off. Tomorrow. Just kidding. It was already tomorrow.", post=1.0,
  stage=dict(prin=dict(at=(250,1450), s=0.85, mood='cry'), kid=dict(at=(800,1450), s=0.8, mood='happy', arms='cheer')),
  ev=[('sfx','@deal','tada'),('sfx','@day','cheer'),('sfx','@kidding','trombone')]),
])
# ---- e16 grandma phone
GRAN = dict(color=(215,190,235), body='round', voice='bf_emma', vpitch=0.9, tc=(110,60,150), glasses=True, hair=True, blush=True)
e16 = dict(id='e16', title='Grandma Learns To Use Her Phone', cast=dict(gran=GRAN), narr='am_michael', narr_speed=1.08, bpm=126, mscale=3, scenes=[
 dict(bg='bedroom', text="Grandma got a new phone. She called her grandson. And she said, how do I turn off the picture?",
  stage=dict(gran=dict(at=(540,1450), s=0.95, mood='confused', hold='📱', arms='hold')),
  ev=[('pop',0.15,'GRANDMA + PHONE',540,720,1.5,90,0),('sfx','@called','phone'),('sfx','@picture','scratch')]),
 dict(bg='bedroom', text="He said, Grandma, that is the camera. It was pointed at her left nostril. For forty minutes. He had seen everything.",
  stage=dict(gran=dict(at=(540,1450), s=1.0, mood='shock')),
  ev=[('zoom',0.2,'@end',1.0,1.6,540,1250),('prop','@nostril','@end','🔍',(540,1000),(540,1000),260,{'wob':5}),('sfx','@forty','tick'),('sfx','@everything','trombone')]),
 dict(bg='bedroom', text="Then Grandma sent a text. It said, K. And then, a thousand heart emojis. By accident. Her finger was stuck.", post=0.3,
  stage=dict(gran=dict(at=(540,1450), s=0.95, mood='worry', hold='📱', arms='hold')),
  ev=[('sfx','@text','pop'),('prop','@thousand','@end','❤️',(300,1000),(180,200),150,{'lin':True}),('prop','@thousand','@end','❤️',(540,1000),(540,150),170,{'lin':True}),('prop','@thousand','@end','❤️',(780,1000),(900,220),150,{'lin':True}),('sfx','@heart','giggle'),('act','@stuck',1.5,'gran','tremble',5)]),
 dict(bg='bedroom', text="She also learned the voice assistant. She said, hello? The phone said, how can I help? Grandma said, I was talking to the cat.", post=0.3,
  stage=dict(gran=dict(at=(540,1450), s=0.95, mood='happy')),
  ev=[('sfx','@voice','ding'),('sfx','@help','ding'),('prop','@cat','@end','🐱',(850,1350),(850,1350),220,{'bob':6}),('sfx','@cat','giggle')]),
 dict(bg='bedroom', text="By the end of the week, Grandma was the best at it. She now has four hundred followers. And she only posts pictures of soup.", post=1.0,
  stage=dict(gran=dict(at=(540,1450), s=0.95, mood='proud', hold='📱', arms='hold')),
  ev=[('sfx','@best','tada'),('pop','@four','400 FOLLOWERS',540,720,1.5,85,0),('prop','@soup','@end','🍲',(300,1000),(300,1000),260,{'bob':6}),('sfx','@soup','giggle')]),
])
# ---- e17 shopping cart
CART = dict(color=GRAY, body='box', voice='am_puck', vpitch=1.3, tc=(60,70,90))
SHOP = dict(color=GREEN, body='tall', voice='bf_emma', tc=(30,110,50), hair=True, blush=True)
e17 = dict(id='e17', title='The Shopping Cart With A Mind Of Its Own', cast=dict(shop=SHOP, cart=CART), narr='bm_george', narr_speed=1.08, bpm=128, mscale=2, scenes=[
 dict(bg='market', text="Everyone has that one shopping cart. The one with a bad wheel. The one that wants to go left. Forever.",
  stage=dict(shop=dict(at=(300,1450), s=0.85, mood='worry', arms='hold'), cart=dict(at=(750,1450), s=0.8, mood='evil')),
  ev=[('pop',0.15,'THAT CART',540,720,1.5,100,0),('sfx','@wheel','scratch'),('sfx','@left','whoosh'),('act','@left',2.0,'cart','lean',-12)]),
 dict(bg='market', text="She pushed it straight. It went left. She pushed it harder. It went left, faster. It knocked over the whole cereal tower.",
  stage=dict(shop=dict(at=(300,1450), s=0.85, mood='angry'), cart=dict(at=(750,1450), s=0.8, mood='grin')),
  ev=[('move','@went','@faster','cart',100,1450,'run'),('sfx','@went','whoosh'),('prop','@cereal','@end','🥣',(200,1000),(200,1500),200,{'spin':300}),('prop','@tower','@end','📦',(120,1100),(120,1500),240,{'spin':-200}),('sfx','@knocked','blast'),('shake','@knocked',1.0,14)]),
 dict(bg='market', text="Then the cart got away. It rolled out of the store. Down the street. Across the highway. It beat a car in a race.", post=0.3,
  stage=dict(cart=dict(at=(100,1450), s=0.8, mood='grin')),
  ev=[('move','@rolled','@end','cart',900,1450,'run'),('sfx','@rolled','engine'),('sfx','@highway','blast',0.6),('prop','@car','@end','🚗',(1100,1550),(-200,1550),320,{'lin':True}),('sfx','@race','cheer')]),
 dict(bg='market', text="The cart came back by itself. With a trophy. And a medal. And a cart girlfriend. The shopper said, I will take the other cart.", post=1.0,
  stage=dict(shop=dict(at=(260,1450), s=0.85, mood='confused'), cart=dict(at=(800,1450), s=0.8, mood='proud')),
  ev=[('prop','@trophy','@end','🏆',(800,1000),(800,1000),240,{'bob':6}),('prop','@medal','@end','🥇',(960,1100),(960,1100),160,{'bob':6}),('sfx','@girlfriend','kiss'),('sfx','@other','trombone')]),
])
# ---- e18 brain at 3am
BRAIN = dict(color=PINK, body='blob', voice='am_fenrir', vpitch=1.1, tc=(200,40,120), blush=True)
SLP = dict(color=BLUE, body='pear', voice='am_adam', tc=(40,80,200), hat='beanie', hatc=YEL, blush=True)
e18 = dict(id='e18', title='My Brain At 3 AM', cast=dict(brain=BRAIN, slp=SLP), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='bedroom', text="It is three in the morning. I am trying to sleep. And my brain decides this is the perfect time to talk.",
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='sad', arms='hold'), brain=dict(at=(800,1450), s=0.8, mood='evil')),
  ev=[('pop',0.15,'3:00 AM',540,720,1.6,110,0),('tint','@three','@end',(0,0,50,100)),('sfx','@three','tick'),('prop','@talk','@end','💭',(800,1050),(800,1050),240,{'bob':8})]),
 dict(bg='bedroom', text="",
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='worry'), brain=dict(at=(800,1450), s=0.8, mood='grin')),
  ev=[('say',0.4,'brain',"Remember that embarrassing thing from 2011?"),('say',None,'slp',"No. Please. Go to sleep."),('say',None,'brain',"You said 'you too' to the waiter. When he said enjoy your meal."),('mood','@end','slp','shock')]),
 dict(bg='bedroom', text="Then the brain showed a slideshow. Every awkward moment in his life. In high definition. With sound effects. And a trumpet.",
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='scream'), brain=dict(at=(800,1450), s=0.8, mood='evil')),
  ev=[('prop','@slideshow','@end','📽️',(540,950),(540,950),300,{'wob':4}),('sfx','@slideshow','tick'),('sfx','@trumpet','trombone'),('act','@trumpet',1.5,'slp','tremble',5)]),
 dict(bg='bedroom', text="Finally, the brain asked a very important question. What if bread is just flat cake? Sam stared at the ceiling. He did not sleep until sunrise.", post=0.3,
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='confused'), brain=dict(at=(800,1450), s=0.8, mood='smug')),
  ev=[('prop','@bread','@end','🍞',(540,950),(540,950),260,{'wob':4}),('sfx','@cake','scratch'),('sfx','@sunrise','bell')]),
 dict(bg='bedroom', text="And at seven A M, the alarm rang. The brain said, good morning! Ready for a great day? And that is why I am always tired.", post=1.0,
  stage=dict(slp=dict(at=(250,1450), s=0.85, mood='dead'), brain=dict(at=(800,1450), s=0.8, mood='happy')),
  ev=[('tint',0.1,'@end',(255,230,150,30)),('sfx','@alarm','buzz'),('sfx','@good','giggle'),('sfx','@tired','trombone')]),
])
STORIES = [e13, e14, e15, e16, e17, e18]
