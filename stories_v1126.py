from kit import *
GARY = dict(color=SKIN, body='round', voice='am_michael', vpitch=0.95, tc=(40,90,200), hair=True, blush=True)
LIBR = dict(color=PUR, body='pear', voice='bf_isabella', tc=(120,50,160), hair=True, glasses=True, bow=True, blush=True)
v1126 = dict(id='v1126', title='Gary Goes To The Library', cast=dict(gary=GARY, libr=LIBR), narr='bm_george', narr_speed=1.08, bpm=124, mscale=0, scenes=[
 dict(bg='school', text="Gary went to the library. The sign said, silence please. But Gary had eaten ten burritos.",
  stage=dict(gary=dict(at=(300,1450), s=0.9, mood='happy'), libr=dict(at=(800,1450), s=0.85, mood='neutral')),
  ev=[('pop',0.15,'SILENCE!',540,720,1.6,120,0),('sfx','@library','bell'),('prop','@sign','@end','🤫',(800,950),(800,950),220,{'wob':6}),('sfx','@burritos','rumble'),('prop','@burritos','@end','🌯',(300,1000),(300,1000),200,{'bob':8}),('mood','@burritos','gary','worry')]),
 dict(bg='school', text="",
  stage=dict(gary=dict(at=(300,1450), s=0.9, mood='worry'), libr=dict(at=(800,1450), s=0.85, mood='angry')),
  ev=[('say',0.4,'libr',"Shhh."),('say',None,'gary',"I did not say anything."),('say',None,'libr',"Your stomach did."),('sfx',3.0,'rumble'),('act',3.0,1.4,'gary','tremble',5)]),
 dict(bg='school', text="Gary held it in. His face turned red. The books began to shake. A candle fell over. And then. It happened.", post=0.2,
  stage=dict(gary=dict(at=(540,1450), s=1.0, mood='scared', arms='belly'), libr=dict(at=(850,1450), s=0.6, mood='shock')),
  ev=[('act','@held',3.0,'gary','tremble',8),('tint','@red','@end',(255,0,0,50)),('prop','@books','@end','📚',(200,900),(200,900),230,{'wob':10}),('shake','@shake',2.0,10),('sfx','@candle','clank'),('sfx','@then','rumble',1.0),('mood','@happened','gary','scream')]),
 dict(bg='school', text="Gary let it go. It was the loudest toot in library history. Everyone stared at Gary. Gary whispered, sorry.", post=0.3,
  stage=dict(gary=dict(at=(300,1450), s=0.9, mood='scream'), libr=dict(at=(800,1450), s=0.85, mood='shock')),
  ev=[('sfx','@loudest','blast'),('shake','@loudest',1.6,18),('flash','@loudest',0.35),('pop','@loudest','BRRAAAP!',540,820,1.5,170,5),('act','@loudest',0.8,'gary','jump',1),('mood','@stared','gary','worry'),('sfx','@whispered','sad')]),
 dict(bg='school', text="",
  stage=dict(gary=dict(at=(300,1450), s=0.9, mood='worry'), libr=dict(at=(800,1450), s=0.85, mood='happy')),
  ev=[('say',0.4,'libr',"Do not be sorry."),('say',None,'libr',"I have been holding that in since nineteen ninety eight."),('say',None,'gary',"Same."),('sfx',6.2,'giggle')]),
 dict(bg='school', text="The library put up a new sign. Silence please. Except Gary.", post=1.0,
  stage=dict(gary=dict(at=(300,1450), s=0.9, mood='proud'), libr=dict(at=(800,1450), s=0.85, mood='happy')),
  ev=[('pop','@except','EXCEPT GARY',540,720,1.6,110,-4),('sfx','@except','tada'),('sfx','@end','toot')]),
])
STORIES = [v1126]
