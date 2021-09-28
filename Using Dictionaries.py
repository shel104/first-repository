actor_bio = {
    "name": "Bill Murray",
    "known for": ["Lost in Translation","Rushmore"]
}

print(actor_bio["name"])

player_score = {
    "ann": 13,
    "michael": 20,
    "ava": 34
}
for player in player_score:
    print(player_score[player])

ticket = {
    "seat no.": 25,
    "first class": False
}
ticket["first class"] = True
print(ticket)

print(" do we access a value associated with a certain key in a dictionary")
print("By the name of its key")

print("Where do we code the key name when accessing a value?")
print("After the dictionary's name, between square brackets[]")

print("How can we reuse the value associated with a key after accessing it ?")
print("By storing it in a variable")

print("HOW can we loop through all keys in the dictionary?")
print("With a for loop")

winner_scores = {
    "first": ("Ted", 50),
    "second": ("Jess", 47)
}

for winner in winner_scores:
    print(winner_scores[winner])

print("It's displaying the tuple value associated with the key stored in the winner variable")

print("Accessing the current value associated with the key")

participants = {
    "Meg": True,
    "KIm": False,
}

participants["KIm"] = True

print(" It updates the value associated with the key Kim to True")

air = {
    "nitrogen": "78%",
    "oxygen": "21%",
    "argon": "0.93%",
    "carbon dioxide": "0.04%",
    "other": "0.03%"
}

print(air["argon"])
print(air["oxygen"])
print("argon" in air)

participants = {
    "Meg": True,
    "Kim": False,
    "Luis":True,
    "Luis M.": False
}

meg = participants["Meg"]
print(meg)

participants["Luis"] = False

print(participants)

contents = {
    "ch. 1": "A long-expected party",
    "ch. 2": "The shadow of the past",
    "ch. 3": "Three is company"
}

contents["ch. 4"] = "A Short Cut to Mushrooms"

print(contents)

for chapter in contents:
    print(contents[chapter])

toppings = {
    "olives": True,
    "anchovies": False,
    "extra chess": False
}

toppings["salami"] = True
toppings["cheese"] = False

print(toppings)

toppings["extra chess"] = True
print(toppings)

toppings["olives"] = False
print(toppings)

ticket = {
    "seat no.": 25
}

ticket["window"] = True
print(ticket)

winner_scores = {
    "first": ("Ted", 50),
    "second": ("Jess", 47)
}

winner_scores["third"] = ("Jo", 30)

print(winner_scores)

routine = {
    "squats": 40,
    "push-ups": 20,
}

routine["lunges"] = 30
print(routine)

toppings = {
    "olives": True,
    "anchovies": False,
    "chees": True
}

toppings["salami"] = True
toppings["cheese"] = False

print(toppings)

personal_data = {
    "name": "Mac Miller",
    "telephone": "0047865791"
}

print("name" in personal_data)

print("adress" in personal_data)

has_address = "address" in personal_data
print(has_address)

promotinos = {
    "laptops": False,
    "desktops": True,
    "accesories": True
}

print("phones" in promotinos)
print("laptops" in promotinos)

stock = {
    "S": 17,
    "M": 30,
    "L": 20,
}
has_XS = "XS" in stock
print(has_XS)

ticket = {
    "seat no.": 25,
    "window": True
}
winner_seat = ticket.pop("window")

if "destination" in ticket:
    ticket.pop("destinations")
print(ticket)
print(winner_seat)

winner_scores = {
    "first": ("Ted", 50),
    "second": ("Jess", 47)
}

winner_scores.pop("second")
print(winner_scores)

participants = {
    "Meg": True,
    "Kim": False,
    "Luis": True,
    "Luis M": False
}

kim = participants.pop("Kim")
print(kim)

routine = {
    "squats": 40,
    "push-ups": 20,
    "lunges": 30
}

routine.pop("lunges")
print(routine)

cast = {
    "Chief": "Bryan Cranston",
    "Nutmeg": "Scarlet Johanson",
    "Rex": "Edward Nortan"
}

cast.pop("Rex")
print(cast)


if "Oracle" in cast:
    cast.pop("Oracle")

