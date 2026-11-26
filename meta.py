import datetime, json
START = datetime.date(2026, 11, 27)
M = [
('d01','The Burp That Shook The Town 🥤💨','Boris drank ten sodas in one minute. The burp that followed was heard in space.',None),
('d02','Pizza Pete Delivers To A HAUNTED House 🍕👻 (Part 1)','A very strange pizza order sends Pete up Spooky Hill. Part 1 of 3.','1/3'),
('d03','Pizza Pete And The 100 Hungry Ghosts 👻🌶️ (Part 2)','Pizza falls right through ghosts. Pete finds the one thing they can eat. Part 2 of 3.','2/3'),
('d04','Pizza Pete Opens A Ghost Restaurant 👻🍕 (Part 3)','Boo-roni Pizza opens, and the line goes around the block. Part 3 of 3.','3/3'),
("d05","Grandpa's Cookie Jar Has A Monster 🍪👾",'Forty-nine cookies vanish every night. Grandpa sets a trap.',None),
('d06','I Hiccupped And Flew To The Moon 🚀🌕','Every hiccup is louder than the last. Then Tim starts floating.',None),
('d07',"Fluffy The Hamster's Great Escape 🐹🏃 (Part 1)",'Plan A: the wheel. Plan B: more wheel. Part 1 of 2.','1/2'),
('d08','Fluffy The Hamster Takes Over The Mall 🐹🏬 (Part 2)','One tiny hamster. One remote control car. One very confused mall. Part 2 of 2.','2/2'),
('d09','The Elevator That Stops On EVERY Floor 🛗😵','Floor two has a cow. Floor four has a disco. Dave is very late for work.',None),
('d10',"Mom Said Don't Touch The Red Button 🔴😱",'Max stares at the big red button for three hours. Then he presses it.',None),
('d11','Gary Gets A Job 💨💼 (Part 1)','Gary needs rent money, so he goes to a job interview. His biggest weakness is beans. Part 1 of 3.','1/3'),
('d12','Gary Delivers Packages With Gas 📦💨 (Part 2)','Gary flies to the top of the tallest building. The package was for floor one. Part 2 of 3.','2/3'),
('d13','Gary Is Employee Of The Month 🏆💨 (Part 3)','The awards speech goes exactly how you think it does. Part 3 of 3.','3/3'),
('d14','The Sneeze That Never Ended 🤧🌍','Sam sneezes once. Then he sneezes across the ocean.',None),
('d15','I Taught My Cat To Do My Homework 🐱📚','Math, science and a ten page essay, all done by the cat.',None),
('d16','The Snowman Who Wanted To Go To The Beach ⛄🏖️','Frosty packs his tiny suitcase and heads south. What could go wrong?',None),
('d17','The Alien Who Ordered Takeout 👽🍔 (Part 1)','Zorp traveled four million miles for lunch. He ate the tablecloth. Part 1 of 2.','1/2'),
('d18','The Alien Brings His Mom To Earth 👽🍔 (Part 2)','Zorp calls his mom. She brings forty-seven cousins. Part 2 of 2.','2/2'),
('d19','Dad Vs. The WiFi 📶😤','Dad yells at the router in two languages. The fix was one wire.',None),
('d20','The Last Slice 🍕😈','One slice of pizza. Four hungry people. One very fast grandma.',None),
('d21',"The Birthday Candle That Wouldn't Blow Out 🎂🕯️",'Lily blows. Dad blows. The fire department blows. Nothing works.',None),
('d22','Bob The Robot Vacuum Takes Over The House 🤖🏠','Bob only wanted to be useful. He also locked the front door.',None),
('d23','Kevin Can Hear Food 🥪😱 (Part 1)','His sandwich begged him not to eat it. Then the pizza started screaming. Part 1 of 3.','1/3'),
('d24',"Kevin's Food Friends 🥪🍟 (Part 2)",'Ice cubes are quiet. Chips are proud. His stomach has a face. Part 2 of 3.','2/3'),
('d25',"Kevin's Big Decision 🍰👨‍🍳 (Part 3)",'Some food wants to be eaten. Kevin finds it. Part 3 of 3.','3/3'),
('d26','My Dad Sleepwalked Onto A Cruise Ship 🚢😴','He only meant to go to the fridge.',None),
('d27',"I Ate The World's Spiciest Pepper 🌶️🔥",'My face turned red, then purple, then a color I did not know.',None),
('d28','Santa Is Stuck In The Chimney 🎅🧱 (Part 1)','Eight billion presents, one tiny chimney. Part 1 of 2.','1/2'),
('d29',"Santa's Christmas Gas Emergency 🎅💨 (Part 2)",'Rudolph had a lot of brussels sprouts for dinner. Part 2 of 2.','2/2'),
('d30','Returning The Presents 🎁🎂','Dad returns a sweater, a singing fish, and a very old fruitcake.',None),
]
TAGS = '#Shorts #Animation #Funny #Cartoon #Comedy'
def rows():
    out = []
    for i, (vid, title, line, part) in enumerate(M):
        d = START + datetime.timedelta(days=i)
        desc = line + ('\n\nNew animated Short every day. Subscribe so you do not miss the next part!' if part else '\n\nNew animated Short every day. Subscribe for more!') + '\n\n' + TAGS
        out.append(dict(id=vid, date=d.isoformat(), dow=d.strftime('%a'), day=d.strftime('%b %-d'), file=f"{d.isoformat()}_{vid}.mp4", title=title, desc=desc, part=part))
    return out
if __name__ == '__main__':
    r = rows(); print(len(r), max(len(x['title']) for x in r), r[0]['file'], r[-1]['date'])
    json.dump(r, open('out/meta.json', 'w'), ensure_ascii=False, indent=1)
