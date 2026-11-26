import datetime, json
START = datetime.date(2026, 12, 27)
M = [
('e01',"Sam's New Year's Resolution Lasted 4 Seconds 🎆🍪",'Sam promised to quit snacks forever. The cookies had other plans.',None),
('e02','What My Dog Thinks When I Leave For 5 Minutes 🐶😭','Minute one: she is gone forever. Minute five: best day of my life.',None),
('e03','What If Gravity Turned Off For One Minute? 🌍🎈','Your dog would float. Your lunch would float. Your teacher would float, still giving a speech.',None),
('e04','The Substitute Teacher Is A Wizard 🧙📚 (Part 1)','A new sub walks in with a pointy hat and a very long beard. Part 1 of 3.','1/3'),
('e05','The Wizard Teacher Casts A New Year Spell 🎆🧙 (Part 2)','A New Year party with magic goes slightly wrong. The principal has a dragon for a desk. Part 2 of 3.','2/3'),
('e06','The Wizard Teacher Gets Fired 🧙🏰 (Part 3)','The principal fires the wizard. The wizard turns the school into a castle. Part 3 of 3.','3/3'),
('e07','Fluffy The Hamster Runs For President 🐹🗳️','Her only promise: more seeds. For everyone.',None),
('e08','Pizza Pete Delivers To The Moon 🍕🌕','The order was four minutes late. That is a bad review.',None),
('e09','Back To School: Everyone Forgot Everything 🎒🧠','What is two plus two? Is it a fish? Is it Tuesday?',None),
('e10','Boris Built A Burp-Powered Time Machine ⏰💨','One burp. One dinosaur. Zero dinosaurs left.',None),
('e11','What Your Fridge Does When The Door Is Closed 🧊🪩','The milk is on the turntables. The eggs are doing a conga line.',None),
('e12','Penny The Pigeon Steals A Whole Pizza 🕊️🍕 (Part 1)','Penny does not want a crumb. She wants the whole pizza. Part 1 of 3.','1/3'),
('e13','Penny The Pigeon Starts A Pigeon Gang 🕊️🧮 (Part 2)','Gerald the pigeon calculated 104 ways it goes wrong. Part 2 of 3.','2/3'),
('e14','Penny The Pigeon Takes Over The City 🕊️🏙️ (Part 3)','Ten thousand pigeons. One demand. Free pizza forever. Part 3 of 3.','3/3'),
('e15','The Principal Who Cancelled The Snow Day ⛄🏫','Forty inches of snow. School is open. The principal has a shovel.',None),
('e16','Grandma Learns To Use Her Phone 📱👵','The camera pointed at her left nostril for forty minutes.',None),
('e17','The Shopping Cart With A Mind Of Its Own 🛒💨','You know the one. It only wants to go left.',None),
('e18','My Brain At 3 AM 🧠🌙','Remember that embarrassing thing from 2011? Is bread just flat cake?',None),
('e19','The Dentist Found Something In My Tooth 🦷🏴‍☠️','A tiny door. A tiny doorbell. A tiny pirate.',None),
('e20','The Ghosts Who Bought The Wrong House 👻🏠','Two ghosts moved in. So did a very loud family.',None),
("e21","The World's Slowest Race: Snail Vs Turtle 🐌🐢",'Ten feet. One tree grew. It was a tie.',None),
("e22","The Boy Who Couldn't Stop Growing 🌱📏 (Part 1)",'Tom woke up with two extra feet. By dinner, he was in the attic. Part 1 of 3.','1/3'),
("e23","The Boy Who Couldn't Stop Growing 🏀 (Part 2)",'Ten feet tall. The coach is very interested. Part 2 of 3.','2/3'),
("e24","The Boy Who Couldn't Stop Growing 🙈 (Part 3)",'The hardest game of hide and seek in history. Part 3 of 3.','3/3'),
('e25','Mr. Pickle Gets A Haircut 🥒✂️','Just a little off the top. There is nothing on top.',None),
('e26','My Alarm Clock Has Trust Issues ⏰😤','What is seven times eight? Who is your favorite alarm clock?',None),
('e27','Octopus Tries To Tie His Shoes 🐙👟','Eight shoes. One hour. One very tangled octopus.',None),
('e28','The Elf On The Shelf Is Still Here In January 🧝📅','Nobody told him Christmas was over.',None),
('e29','My Superpower Is Finding The Other Sock 🧦🦸','A villain steals every left sock in the city. Sock Man to the rescue.',None),
('e30','The Great Cheese Heist 🧀🐭','Step one: sneak past the cat. Step three: the cat ate the cheese.',None),
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
    json.dump(r, open('out/meta2.json', 'w'), ensure_ascii=False, indent=1)
