import time
import random

from Game.rooms import get_monsters
from Game.lists import actions_fighter, actions_healer, actions_mage, actions_warrior, meleelist_fighter, \
    meleelist_warrior, magiclist_healer, magiclist_mage, heallist_healer, randomname


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


def chose_name():
    while True:
        print('Your hero needs a name')
        print('Enter a name or type random (r)')
        nameinput = input().capitalize()
        if nameinput == 'Random' or nameinput == 'R':
            name = randomname[random.randint(0, len(randomname)) - 1]
            return name
        elif nameinput == '' or nameinput == ' ' or len(nameinput) < 2:
            print('Invalid name')
        else:
            name = nameinput
            return name


def chose_race(name):
    print('Your character can be Human, elf, dwarf or orc. Or type stats (s) to hear about the races.')
    while True:
        racechoice = input().lower()
        if racechoice.startswith('s'):
            print('Something about humans')
            print('Something about elves')
            print('Something about dwarfs')
            print('Something about smelly orcs')
        elif racechoice.startswith('h'):
            print('You have chosen your adventurer, ' + name + ', to be human')
            return 'human'
        elif racechoice.startswith('e'):
            print('You have chosen your adventurer, ' + name + ', to be an elf')
            return 'elf'
        elif racechoice.startswith('d'):
            print('You have chosen your adventurer, ' + name + ', to be a dwarf')
            return 'dwarf'
        elif racechoice.startswith('o'):
            print('You have chosen your adventurer, ' + name + ', to be an orc')
            return 'orc'
        elif racechoice.startswith('r'):
            racelist = ('human', 'elf', 'dwarf', 'orc')
            race = racelist[random.randint(0,3)]
            return race
        else:
            print('Huh?')


def chose_class(name):
    print(name, 'needs a class. You can chose between warrior, fighter, mage or healer')
    while True:
        clas = input().lower()
        if clas.startswith('w'):
            return 'warrior'  # Can use a shield
        elif clas.startswith('f'):
            return 'fighter'  # Can use big weapons
        elif clas.startswith('m'):
            return 'mage'
        elif clas.startswith('h'):
            return 'healer'
        elif clas.startswith('r'):
            classlist = ('warrior', 'fighter', 'mage', 'healer')
            cla = classlist[random.randint(0, 3)]
            return cla
        else:
            print('Huh?')


def generate_actions(cla):
    if cla == 'warrior':
        actions = actions_warrior
    elif cla == 'fighter':
        actions = actions_fighter
    elif cla == 'healer':
        actions = actions_healer
    elif cla == 'mage':
        actions = actions_mage
    return actions


def generate_melee(cla):
    if cla == 'mage' or cla == 'healer':
        melee_actions = None
    elif cla == 'warrior':
        melee_actions = meleelist_warrior
    elif cla == 'fighter':
        melee_actions = meleelist_fighter
    return melee_actions


def generate_healing(cla):
    if cla == 'warrior' or cla == 'fighter':
        healing_actions = None
    elif cla == 'mage':
        healing_actions = None
    elif cla == 'healer':
        healing_actions = heallist_healer
    return healing_actions


def generate_magic(cla):
    if cla == 'warrior' or cla == 'fighter':
        magic_actions = None
    elif cla == 'healer':
        magic_actions = magiclist_healer
    elif cla == 'mage':
        magic_actions = magiclist_mage
    return magic_actions



def generate_hp(cla):
    if cla == 'warrior':
        maxhp = 150
    elif cla == 'fighter':
        maxhp = 120
    else:
        maxhp = 100
    return maxhp


def generate_rage(cla): #Not in use
    if cla == 'warrior' or cla == 'fighter':
        maxrage = 80
    else:
        maxrage = None
    return maxrage


def generate_mp(cla):
    if cla == 'mage' or cla == 'healer':
        maxmp = 200
    else:
        maxmp = None
    return maxmp


def generate_magic_stat(cla, race):
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


def generate_attack_stat(cla, race):
    attackbonus = 10
    if race == 'human':
        attackbonus += 0
    elif race == 'elf':
        attackbonus -= 2
    elif race == 'dwarf':
        attackbonus += 0
    elif race == 'orc':
        attackbonus += 2

    if cla == 'warrior':
        attackbonus += 2
    elif cla == 'fighter':
        attackbonus += 7
    elif cla == 'mage':
        attackbonus -= 5
    elif cla == 'healer':
        attackbonus -= 7

    return attackbonus


def generate_defense_stat(cla, race):
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


def generate_healing_stat(cla, race):
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


def enter_cave_story(): #Commented out for debugging reasons
    '''print('You enter the cave')
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
    print('Left with no other choice, you move towards the sound')'''
    input('Press enter to continue and see what is in the next room')


def first_room(party_level):
    '''Returns a monsterlist with only one monster'''
    print('An ugly creature in snarling at you from the dark inner corner')
    monster = 1  # Monster is the number of monsters
    monsters = get_monsters(monster, party_level)
    return monsters
