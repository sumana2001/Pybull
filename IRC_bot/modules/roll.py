import random

def roll(argument):
    dice = argument.strip().split("d")
    if (not len(dice) == 2) or \
       (not dice[0].isdigit()) or \
       (not dice[1].isdigit()):
        return "Roll dice by typing e.g. 1d6"

    amount = int(dice[0])
    sides = int(dice[1])
    if amount > 1000 or sides > 1000000:
        return "I don't have that kind of dice"

    result = []
    for i in range(amount):
        result.append(random.randint(1, sides))

    return ", ".join(str(x) for x in result)

def coin_flip():
    return ["Heads", "The coin landed on it's edge!", "Tails"][random.randint(0, 2)]
