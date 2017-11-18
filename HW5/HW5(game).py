import random
import time


class Archers:

    quantity = 0

    def getcf(self, enemy):
        if isinstance(enemy, Archers):
            return 1
        if isinstance(enemy, Knights):
            return 2
        if isinstance(enemy, Wizards):
            return 0.5


class Knights:

    quantity = 0

    def getcf(self, enemy):
        if isinstance(enemy, Knights):
            return 1
        if isinstance(enemy, Wizards):
            return 2
        if isinstance(enemy, Archers):
            return 0.5


class Wizards:

    quantity = 0

    def getcf(self, enemy):
        if isinstance(enemy, Wizards):
            return 1
        if isinstance(enemy, Archers):
            return 2
        if isinstance(enemy, Knights):
            return 0.5

army = 100
archers = Archers()
knights = Knights()
wizards = Wizards()

comp_archers = Archers()
comp_knights = Knights()
comp_wizards = Wizards()

print('Welcome to the fight game! You need strong army =)')
print('Choose how many Archers, Knights and Wizards do you need! Army quantity cant be > 100. Good luck!')

while True:
    print('----------------------------------------')
    print('░░░░░░░░░░░░░░░░░░▄██▄░░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░▄█░░█▄░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░▄█░░░░█▄░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░▀▀█░░░░█▀▀░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░▄▄▄██░░██▄▄▄░░░░░░░░░░░░░░')
    print('░░░░░░░░░░▄██▀▀▀░▄█░░█▄░▀▀▀██▄░░░░░░░░░░')
    print('░░░░░░░▄█▀▀▄▄▄█▀▀▀█░░█▀▀▀█▄▄░▀▀█▄░░░░░░░')
    print('░░░░░▄█▀░▄█▀▀░░░░░█░░█░░░░░▀▀█▄░▀█▄░░░░░')
    print('░░░▄█▀░▄█▀░░░░░░░░█░░█░░░░░░░░▀█▄░▀█▄░░░')
    print('░▄▄█░▄█▀░░░░░░░░░░█░░█░░░░░░░░░░▀█▄░█▄▄░')
    print('█▀░░▄█░░░░░░░░░▄▄▄█░░█▄▄▄░░░░░░░░░█▄░░▀█')
    print('▀█▄██▄▄▄░░░░░░░██░█░░█░██░░░░░░░▄▄▄██▄█▀')
    print('░░░░░░▀▀▀▀▀█▄▄▄██░█░░█░██▄▄▄█▀▀▀▀▀░░░░░░')
    print('░░░░░░░░░░░░░░░██░█░░█░██░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░██░█░░█░██░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░▀█░█░░█░█▀░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░███░░███░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░██░░██░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░░█░░█░░░░░░░░░░░░░░░░░░')
    print('░░░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░░░░░░░░░░')
    archersnewquantity = int(input("How many archers do you need?   "))
    if archersnewquantity > army:
        print('Army quantity cant be > 100')
        continue
    if archersnewquantity == army:
        knightsnewquantity = 0
        wizardsnewquantity = 0
        break
    if archersnewquantity < army:
        print('------------------------------')
        print('░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄▄▄')
        print('░░░░░░░░░░░░░░░░░░░░░░░▄▀▀░░░█')
        print('░░░░░░░░░░░░░░░░░░░░░▄▀░░▄▀░▄▀')
        print('░░░░░░░░░░░░░░░░░░░▄▀░░▄▀░░▄▀')
        print('░░░░░░░░░░░░░░░░░▄▀░░▄▀░░▄▀')
        print('░░░░░░░░░░░░░░░▄▀░░▄▀░░▄▀')
        print('░░░░░░░░░░░░░▄▀░░▄▀░░▄▀')
        print('░░░░░░▄▄░░░▄▀░░▄▀░░▄▀')
        print('░░░░░░█░▀▄▀░░▄▀░░▄▀')
        print('░░░░░░░▀▄░▀▄▀░░▄▀')
        print('░░░░░░▄█▀▀▄░▀▄▀')
        print('░░░░▄█▀█▄▄█▀▄░▀▄')
        print('░▄▀▀▀▄░▄█▀░░░▀▀▀')
        print('█░░░░░█▀')
        print('▀▄░░░▄▀')
        print('░░▀▀▀')
        knightsnewquantity = int(input("How many knights do you need?   "))
    if (archersnewquantity + knightsnewquantity) > army:
        print('Army quantity cant be > 100, try again!')
        continue
    if (archersnewquantity + knightsnewquantity) == army:
        wizardsnewquantity = 0
        break
    if (archersnewquantity + knightsnewquantity) < army:
        print('--------------------------------')
        print('░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░░')
        print('░░░░░░░░░░░░░░▄██▄░░░░░░░░░░░░░░')
        print('░░░░░░░░░░░░░▄████▄░░░░░░░░░░░░░')
        print('░░░░██▄▄▄▄░░░██████░░░▄▄▄▄██░░░░')
        print('░░░░░██████░░░████░░░██████░░░░░')
        print('░░░░░▀██████▄▄████▄▄██████▀░░░░░')
        print('░░░░░░▀▀▀██████████████▀▀▀░░░░░░')
        print('░░░▄▄█▄░░▄█████▀▀█████▄░░▄█▄▄░░░')
        print('▄▄███████████▀░░░░▀███████████▄▄')
        print('▀▀███████████▄░░░░▄███████████▀▀')
        print('░░░▀▀█▀░░▀█████▄▄█████▀░░▀█▀▀░░░')
        print('░░░░░░▄▄▄██████████████▄▄▄░░░░░░')
        print('░░░░░██████▀░░████░░▀█████░░░░░░')
        print('░░░░░██████░░░████░░░██████░░░░░')
        print('░░░░██▀▀▀▀░░░██████░░░▀▀▀▀██░░░░')
        print('░░░░░░░░░░░░░▀████▀░░░░░░░░░░░░░')
        print('░░░░░░░░░░░░░░▀██▀░░░░░░░░░░░░░░')
        print('░░░░░░░░░░░░░░░▀▀░░░░░░░░░░░░░░░')
        wizardsnewquantity = int(input("How many wizards do you need?   "))
    if (wizardsnewquantity + archersnewquantity + knightsnewquantity) > army:
        print('Army quantity cant be > 100, try again!')
        continue
    if (wizardsnewquantity + archersnewquantity + knightsnewquantity) < army:
        print('You need more wizards, try again!')
        continue
    if (wizardsnewquantity + archersnewquantity + knightsnewquantity) == army:
        break
archers.quantity = archersnewquantity
knights.quantity = knightsnewquantity
wizards.quantity = wizardsnewquantity

comp_archersnewquantity = int(random.randint(1, 99))
comp_knightsnewquantity = int(random.randint(1, 99 - comp_archersnewquantity))
comp_wizardsnewquantity =\
    int(100 - (comp_archersnewquantity+comp_knightsnewquantity))

comp_archers.quantity = comp_archersnewquantity
comp_knights.quantity = comp_knightsnewquantity
comp_wizards.quantity = comp_wizardsnewquantity

print(" " * 200)

userarmy = [archers, knights, wizards]
comparmy = [comp_archers, comp_knights, comp_wizards]

print('This is your Army!')
for division in userarmy:
    print(str(division.quantity) + "  " + str(type(division).__name__))
print(" " * 200)
print("This is Computer Army!")
for division in comparmy:
    print(str(division.quantity) + "  " + str(type(division).__name__))

print(" " * 200)

time.sleep(5)


def fight(user_division, comp_division):
    user_damage = int(user_division.quantity*user_division.getcf(comp_division))
    comp_damage = int(comp_division.quantity*comp_division.getcf(user_division))
    if user_damage >= comp_division.quantity:
        comp_division.quantity = 0
    else:
        comp_division.quantity = comp_division.quantity - user_damage
    if comp_damage >= user_division.quantity:
        user_division.quantity = 0
    else:
        user_division.quantity = user_division.quantity - comp_damage

RoundCounter = 1

while len(userarmy) != 0 and len(comparmy) != 0:
    if RoundCounter > 1:
        time.sleep(5)
    print(" " * 200)
    print('Round ' + str(RoundCounter))
    print('--------------------------------')
    print('This is your Army!')
    for division in userarmy:
        print(str(division.quantity) + "  " + str(type(division).__name__))
    print(" " * 200)
    print("This is Computer Army!")
    for division in comparmy:
        print(str(division.quantity) + "  " + str(type(division).__name__))
    fight(userarmy[0], comparmy[0])
    if userarmy[0].quantity == 0:
        userarmy.pop(0)
    if comparmy[0].quantity == 0:
        comparmy.pop(0)
    RoundCounter = RoundCounter + 1

print('╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦▐▌═╦═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩▐▌═╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═▀██═╦═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═▌██═╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═╦═╩═▌██═╦═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦═╩═▄▄▄▄╦═╩═╦═╩═╦═▌██═╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩▄████████▄═╩═╦═╩═▌██═╦═╩▄╦═╩═╦')
print('╦═╩═╦═╩═▄███████▀─▄═╦═╩═╦═▌███████╩═╦═╩')
print('╩═╦═╩═╦▐█████▄──█─▄▄╩═╦═╩═▌██████▀╦═╩═╦')
print('╦═╩═╦═╩▐███████▄────▀▄╩═╦▄▄███╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═███─█████───▄▀╦═╩═▀▄▄██═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦████████───▀▄╩═╦═╩█──█═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩═██████▀──█▀▀╦═╩▄███▄█═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦█████████▄═╦═╩▄███████═╦═╩═╦═╩')
print('╩═╦═╩═╦═████████████▄▄██████████╩═╦═╩═╦')
print('╦═╩═╦═╩████████████████████═█████═╩═╦═╩')
print('╩═╦═╩═╦███████████████████╦═█████═╦═╩═╦')
print('╦═╩═╦═╩█████████████████▀═╩═█████═╩═╦═╩')
print('╩═╦═╩═╦████████████▀╩═╦═╩═╦═█████═╦═╩═╦')
print('╦═╩═╦═╩═███████████▌╦═╩═╦═╩═╦▀██▀═╩═╦═╩')
print('╩═╦═╩═╦═╩███████████╩═╦═╩═╦═╩═╦═╩═╦═╩═╦')
print('╦═╩═╦═▄█████████████▌═╩═╦═╩═╦═╩═╦═╩═╦═╩')
print('╩═╦▄████▀▀▀██████████═╦═╩═╦═╩═╦═╩═╦═╩═╦')
print('╦████▀╩═╦═╩═█████████═╩═╦═╩═╦═╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩═╦═▐████████═╦═╩═╦═╩═╦═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦═╩═████╩████═╩═╦═╩═╦═╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩═╦═████╦████═╦═╩═╦═╩═╦═╩═╦═╩═╦')
print('╦═╩═╦═╩═╦═╩████═╩████═╩═╦═╩═╦═╩═╦═╩═╦═╩')
print('╩═╦═╩═╦═╩═▐█████▄█████▄▄╩═╦═╩═╦═╩═╦═╩═╦')

if len(userarmy) > len(comparmy):
    print('You are win!')
elif len(comparmy) > len(userarmy):
    print('Computer is win!')

time.sleep(60)
