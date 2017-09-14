from Game.classes import Player, SpecAttack, Magic, Healing
import sys
import time
import random


def setup_party():
    adventurer = input('Please choose the size of your party, but remember, more wont guarantee you an easier fight.\n')
    party = False
    while party is False:
        if not adventurer.isdigit():
            print('You need to enter a number')
            adventurer = input()
        elif int(adventurer) > 5:
            print('It\'s a party, not a raid!')
            adventurer = input()
        elif int(adventurer) == 1:
            print('You have chosen to go as a lonely hero')
            party = True
            return int(adventurer)
        elif int(adventurer) in range(2, 6):  # 2 up to, but not including 6
            print('You have', adventurer, 'adventurers in your party')
            party = True
            return int(adventurer)
        else:
            print('Error')
            adventurer = input()


def chose_race(name):
    print('Your character can be Human, elf, dwarf or orc. Or type stats (s) to hear about the races.')
    race = False
    while race is False:
        racechoice = input().lower()
        if racechoice.startswith('s'):
            print('Something about humans')
            print('Something about elves')
            print('Something about dwarfs')
            print('Something about smelly orcs')
        elif racechoice.startswith('h'):
            print('You have chosen you adventurer, '+ name + ', to be human')
            return 'human'
            race = True
        elif racechoice.startswith('e'):
            print('You have chosen you adventurer, '+ name + ', to be an elf')
            return 'elf'
            race = True
        elif racechoice.startswith('d'):
            print('You have chosen you adventurer, '+ name + ', to be a dwarf')
            return 'dwarf'
            race = True
        elif racechoice.startswith('o'):
            print('You have chosen you adventurer, '+ name + ', to be an orc')
            return 'orc'
            race = True
        else:
            print('Huh?')


def chose_class(name):
    global name
    given = False
    print(name, 'needs a class. You can chose between warrior, fighter, mage or healer')
    while given is False:
        clas = input().lower()
        if clas.startswith('w'):
            given = True
            return 'warrior'  # Can use a shield
        elif clas.startswith('f'):
            given = True
            return 'fighter'  # Can use big weapons
        elif clas.startswith('m'):
            given = True
            return 'mage'
        elif clas.startswith('h'):
            given = True
            return 'healer'
        else:
            print('Huh?')


def generate_actions():
    global cla
    if cla == 'warrior' or cla == 'fighter':
        actions = meleeactions
    elif cla == 'healer' or cla == 'mage':
        actions = casteractions
    return actions


def generate_sactions1():
    global cla
    if cla == 'mage' or cla == 'healer':
        Sactions1 = magiclist
    elif cla == 'warrior':
        Sactions1 = meleewlist
    elif cla == 'fighter':
        Sactions1 = meleeflist
    return Sactions1


def generate_sactions2():
    global cla
    if cla == 'mage' or cla == 'healer':
        Sactions2 = heallist
    elif cla == 'warrior' or cla == 'fighter':
        Sactions2 = None
    return Sactions2


def generate_hp():
    global cla
    if cla == 'warrior':
        maxhp = 150
    elif cla == 'fighter':
        maxhp = 120
    else:
        maxhp = 100
    return maxhp


def generate_ap():
    global cla
    if cla == 'warrior' or cla == 'fighter':
        maxap = 80
    else:
        maxap = None
    return maxap


def generate_mp():
    global cla
    if cla == 'mage' or cla == 'healer':
        maxmp = 200
    else:
        maxmp = None
    return maxhp


def generate_magic_stat():
    global cla
    global race
    magic = 10
    if race == 'human':
        magic += 0
    elif race == 'elf':
        magic += 2
    elif race == 'dwarf':
        magic -= 2
    elif race == 'orc':
        magic -= 2

    if cla == 'warrior':
        magic -= 7
    elif cla == 'fighter':
        magic -= 7
    elif cla == 'mage':
        magic += 6
    elif cla == 'healer':
        magic += 2

    return magic


def generate_attack_stat():
    global race
    global cla
    attack = 10
    if race == 'human':
        attack += 0
    elif race == 'elf':
        attack -= 2
    elif race == 'dwarf':
        attack += 0
    elif race == 'orc':
        attack += 2

    if cla == 'warrior':
        attack += 2
    elif cla == 'fighter':
        attack += 7
    elif cla == 'mage':
        attack -= 5
    elif cla == 'healer':
        attack -= 7

    return attack


def generate_defense_stat():
    global race
    global cla
    defense = 10
    if race == 'human':
        defense -= 1
    elif race == 'elf':
        defense += 0
    elif race == 'dwarf':
        defense += 2
    elif race == 'orc':
        defense += 0

    if cla == 'warrior':
        defense += 8
    elif cla == 'fighter':
        defense += 2
    elif cla == 'mage':
        defense -= 10
    elif cla == 'healer':
        defense -= 7

    return defense


def generate_healing_stat():
    global race
    global cla
    healing = 10
    if race == 'human':
        healing += 2
    elif race == 'elf':
        healing += 1
    elif race == 'dwarf':
        healing += 0
    elif race == 'orc':
        healing -= 2

    if cla == 'warrior':
        healing -= 10
    elif cla == 'fighter':
        healing -= 10
    elif cla == 'mage':
        healing += 4
    elif cla == 'healer':
        healing += 11

    return healing


def enter_cave_story():
    print('You enter the cave')
    time.sleep(1)
    print('It is dark and damp.')
    time.sleep(1)
    print('You hear the walls crack.')
    time.sleep(1)
    print('You run for the exit!')
    print('You feel a sharp pain in your hear and everything does dark...')
    time.sleep(3)
    print('A cough wakes you from your aching sleep.')
    time.sleep(1)
    print('Through the dust you hear ominous cracking.')
    time.sleep(2)
    print('Left with no other choice, you move towards the sound')


def get_roomroll():
    global size
    global previous
    if size == 1:
        roomroll = random.randint(0, 2)
        roomroll -= random.randint(0, previous)
    elif size in range(2, 4):  # 2 up to, but not including, 4 (check this)
        roomroll = random.randint(0, size + 2)
        roomroll -= random.randint(0, previous)
    else:
        roomroll = random.randint(0, size + 3)
        roomroll -= random.randind(0, previous)
    if roomroll < 0:
        roomroll = 0
    return roomroll


def empty_room():
    print('The room you have entered is empty!')
    print('You can relax and regain vitality (r) or search the room for hidden treasures or dangers (s)')
    empty = True
    while empty:
        emptyroom = input().lower()
        if emptyroom.startswith('r'):
            for char in party:
                self.generate()
        elif emptyroom.startswith(('s')):
            emptyroomroll = seach_empty_room()
            if emptyroomroll == 0:
                print('The room is completely empty and you move further into the cave')
                emptyroomtuple = (True, False, 0)
            elif emptyroomroll == 1:
                print('You see a chest')
                print('It contains:')
                emptyroomtuple = (False, True, 0)
            else:
                ('As you search the room, you stumble')
                time.sleep(1)
                ('You hear noices')
                time.sleep(2)
                ('Someone must have heard you')
                emptyroomroll =- 1
                emptyroomtuple (False, False, emptyroomroll)



    pass


def search_empty_room()
    global size
    if size == 1:
        emptyroomroll = random.randint(0, 3)
    elif size in range(2, 4):  # 2 up to, but not including, 4 (check this)
        emptyroomroll = random.randint(0, size + 2)
    else:
        emptyroomroll = random.randint(0, size + 3)
    return emptyroomroll

def get_monsters():


    #Needs to return previous += monsters
    pass


def get_loot(lootluck):

    pass


def level_up():
    # Chose where you want +1 when you gain a level
    pass




# Melee Attacks for warrior
PowerAttack = SpecAttack('Power Attack', 5, 50, 'none', 1) #Standard attack
Fury = SpecAttack('Fury', 10, 60, 'none', 2) #Hits two random targets
Taunt = SpecAttack('Taunt', 0, 0, 'taunt', 'all') #Focus all enemies on you for one round
RainOfPain = SpecAttack('Rain of Pain', 20, 40, 'none', 'all') #Dmg all enemies
meleewlist = [PowerAttack, Fury, Taunt, RainOfPain]

#Melee Attacks for fighter
ConsumedByRage = SpecAttack('Consumed by Rage', 15, 150, 'none', 1) #Standard attack
Fury = SpecAttack('Fury', 10, 60, 'none', 2) #Hits two random targets
Rage = SpecAttack('Provoke', 0, 0, 'self + rage', 0) # You get extra rage
RainOfPain = SpecAttack('Rain of Pain', 20, 40, 'none', 'all') #Dmg all enemies
meleeflist = [ConsumedByRage, Fury, Rage, RainOfPain]

# Magic Attacks
FireBreath = Magic('Fire Breath', 40, 100,'none', 'random') #Hits a random number of targets
IceBolt = Magic('Ice Bolt', 40, 150, 'ap', 1) #Reduced Attack Power for one round
ShadowTongue = Magic('Shadow Tongue', 50, 100, 'magic', 1) #Reducded Magic, permanent
Chill = Magic('Chill', 60, 50, 'attack', 'all') #20% chance for enemy to loose a turn, permanent
magiclist = [FireBreath, IceBolt, ShadowTongue, Chill]

# Healing
SmallHeal = Healing('Small Heal,', 30, 115, 1)
Heal = Healing('Heal', 60, 200, 1)
GreatHeal = Healing('Great Heal', 80, 270, 1)
FromAbove = Healing('From Above', 100, 160, 'all')
heallist = [SmallHeal, Heal, GreatHeal, FromAbove]

meleeactions = ['Special Attack,' 'White damage', 'Potions']
casteractions = ['Magic', 'Healing', 'Regenerate mana', 'Potions']

ItemNameFirst =()
ItemNameSecond = ()

print('Welcome to the world of I-cant-be-bothered-making-up-name')

size = setup_party()

party = []
partylevel = 1
inventory = []

for i in range(size):
    name = input('Enter the name of your character\n')
    race = chose_race(name)
    cla = chose_class(name)
    actions = generate_actions()
    Sactions1 = generate_sactions1()
    Sactions2 = generate_sactions2()
    maxhp = generate_hp()
    maxmp = generate_mp()
    magicstat = generate_magic_stat()
    attackstat = generate_attack_stat()
    defensestat = generate_defense_stat()
    healingstat = generate_healing_stat()
    party.append(Player(name, race, cla, actions, Sactions1, Sactions2,
                           maxhp, maxmp, magicstat, attackstat, defensestat, healingstat))
    print('You are now ' + name +', the ' + race + '.')
    print('You have pledged your skills as a ' + cla + ' to rescue the people of I-cant-be bothered-making-up-a-name from whatever-is-in-this-cave-or-whatever-it-is.')


print('You stand in front of a dark cave')
print('Do you enter?')
print('Press enter to enter, or type quit to exit the game')
entercave = input().lower()
if entercave == 'quit':
    sys.exit()
else:
    enter_cave_story()

partyalive = True
previous = 0
exp = 0  # Not yet in use

while partyalive:
    roomroll = get_roomroll()
    if roomroll == 0:
        emptyroomtuple = empty_room()
        if emptyroomtuple[0] = True:
            continue
        elif emptyroomtuple[1] = True:
            lootluck = 0
            get_loot()
        else:
            monster = emptyroomtuple[2]
    else:
        monster = roomroll

    if monster == 0
        continue
    else:
        for i in monster:








#You can browse your inventory before leaving any room