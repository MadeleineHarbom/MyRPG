from Game.classes import Player, SpecAttack, Magic, Healing, Enemy
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
    elif cla == 'healer':
        actions = healeractionsctions
    elif cla == 'mage':
        actions = mageactions
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


def generate_rage():
    global cla
    if cla == 'warrior' or cla == 'fighter':
        maxrage = 80
    else:
        maxrage = None
    return maxrage


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


def first_room():
    '''Returns a monsterlist with only one monster'''
    print('An ugly creature in snarling at you from the dark inner corner')
    monster = 1 #Moster is the numer of monsters
    #monsters = [] #Monsters is a list of monsters
    monsters = get_monsters(monster, party_level)
    return monsters

def get_roomroll():
    '''Returns roomroll, dependant on partysize and and how many monsters encountered in the previous room'''
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
    '''NOT DONE
    When a room is empty you can rest or search the room
    When you search, you can get treasure or monster(s)
    What should I return?'''
    print('The room you have entered is empty!')
    print('You can relax and regain vitality (r) or search the room for hidden treasures or dangers (s)')
    empty = True
    while empty:
        emptyroom = input().lower()
        if emptyroom.startswith('r'):
            for i in party:
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
                emptyroomtuple = (False, False, emptyroomroll)


def search_empty_room():
    '''Used aftedr searching a empty room, in empty_room()
    Returns a roll, determined by party size'''
    global size
    if size == 1:
        emptyroomroll = random.randint(0, 3)
    elif size in range(2, 4):  # 2 up to, but not including, 4 (check this)
        emptyroomroll = random.randint(0, size + 2)
    else:
        emptyroomroll = random.randint(0, size + 3)
    return emptyroomroll


def get_monsters(monster, party_level):
    '''Input requires: monster, an integer that determines the number of monsters in a room
    Returns a list of monsters'''
    monsters = []
    for i in range(monster):
        cla = monsterclasses[random.randint(0, 3)]
        race = monsterrace[random.randint(0, len(monsterrace)-1)]
        if cla == 'warrior':
            actions = meleewlist
            maxhp = 150 + party_level * 30
            magicstat = 0
            attackstat = party_level * 5
            defensestat = party_level * 10
            healingstat = 0
        elif cla == 'fighter':
            maxhp = 120 + party_level * 20
            actions = meleeflist
            magicstat = 0
            attackstat = party_level * 7
            defensestat = party_level * 5
            healingstat = 0
        elif cla == 'mage':
            actions = magiclist
            maxhp = 100 + party_level * 5
            magicstat = party_level * 5
            attackstat = 0
            defensestat = party_level
            healingstat = party_level * 2
        elif cla == 'healer':
            actions = heallist
            maxhp = 100 + party_level * 5
            magicstat = party_level * 7
            attackstat = 0
            defensestat = 0
            healingstat = party_level * 10
        maxmp = 300 + party_level * 50
        monsters.append(Enemy(party_level, race, cla, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat, actions))
        return monsters


def fight(party, monsters):
    '''NOT DONE
    The fight, shows HP for players and creatures
    Lets you attack and be attack
    Should be able to kill players and mosters
    Return a list of the daed monsters levels, so loot can be generated'''
    fight = True
    while fight is True:
        for i in range(len(party)):
            party[i].display_current()
        for j in range(len(monsters)):
            monsters[j].display_current()

        for member in party:
            action_choice = False
            while action_choice == False:
                Saction_choice = False
                for i in range(len(member.actions)):
                    print(str(i + 1) + ': ' + str(member.actions[i]))
                print('Chose an action')
                action = input()
                if not action.isdigit():
                    print('Invalid input (s)')
                elif int(action) - 1 in range(len(member.actions)):
                    print('working')
                    while Saction_choice == False: #Let's the player choose its Secondary Action
                        if int(action) == 1: #
                            for i in range(len(member.Saction1)):
                                print(str(i + 1) + ': ' + str(member.Saction1[i].name))
                            print('Or type back (b) to get to the previous menu')
                            Saction = input()
                            if Saction.isdigit():
                                if int(Saction) -1 in range(len(member.Saction1)):
                                    attack = member.Saction1[int(Saction) -1]
                                    target_chosen = False
                                    while target_chosen == False:
                                        print('Chose a target')
                                        for j in range(len(monsters)):
                                            print(str(j +1) + ': ', end='')
                                            monsters[j].display_current()
                                        target_choice = input()
                                        if target_choice.isdigit():
                                            if int(target_choice) - 1 in range(len(monsters)):
                                                target = monsters[int(target_choice) - 1]
                                                player_attack(member, target, attack)
                                                target_chosen = True
                                            else:
                                                print('There are not that many enemies')
                                        elif target_choice.lower().startswith('b'):
                                            action_choice = False
                                        else:
                                            continue
                        elif int(action) == 2:
                            if member.cla == 'warrior' or member.cla == 'fighter':
                                print('Placeholder, white dmg')
                            elif member.cla == 'mage' or member.cla == 'healer':
                                print('Placeholder, mana regen')
                            Saction_choice = True

                else:
                    print('Invalid input (i)')

                action = int(action)

                if action == 3:
                    print('Potins, placeholder')





def player_attack(attacker, target, attack):
    dmg = attacker.make_attack(attack)
    target.take_dmg(dmg, attack)



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

meleeactions = ['Special Attack', 'White damage', 'Potions']
mageactions = ['Magic', 'Regenerate mana', 'Potions']
healeractions = ['Healing', 'Regenerate mana', 'Potions']


monsterclasses = ['warrior', 'fighter', 'mage', 'healer']
monsterrace = ['Dark Elf', 'Orc', 'Haunted']

print('Welcome to the world of I-cant-be-bothered-making-up-name')

size = setup_party()

party = []
party_level = 1
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

monsters = first_room() #Monsters is a list
fight(party, monsters)

'''
while partyalive:
    roomroll = get_roomroll()
    if roomroll == 0:
        emptyroomtuple = empty_room()
        if emptyroomtuple[0] == True:
            continue
        elif emptyroomtuple[1] == True:
            lootluck = 0
            get_loot()
        else:
            monsterroll == emptyroomtuple[2]
    else:
        monsterroll = roomroll

    if monsterroll == 0:
        continue
    else:
        get_monsters(monsterroll, party_level)
'''








#You can browse your inventory before leaving any room