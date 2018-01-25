import random
import time

from Game.classes import Enemy
from Game.lists import meleelist_warrior, meleelist_fighter, monsterclasses, \
    monsterrace, heallist_healer, magiclist_mage
from Game.fight import fight

def get_roomroll(party, previous):
    '''Returns roomroll, dependant on partysize and and how many monsters encountered in the previous room'''
    if len(party) == 1:
        roomroll = random.randint(0, 2)
        roomroll -= random.randint(0, previous)
    elif len(party) in range(2, 4):  # 2 up to, but not including, 4 (check this)
        roomroll = random.randint(0, len(party) + 3)
        roomroll -= random.randint(0, previous)
    else:
        roomroll = random.randint(0, len(party) + 4)
        roomroll -= random.randind(0, previous)
    if roomroll < 0:
        roomroll = 0
    return roomroll


def empty_room(party, party_level, dead_monster_list,  dead_player_list):
    '''NOT DONE
    When a room is empty you can rest or search the room
    When you search, you can get treasure or monster(s)
    What should I return?'''
    print('The room you have entered is empty!')
    print('You can relax and regain vitality (r) or search the room for hidden treasures or dangers (s)')
    while True:
        emptyroom = input().lower()
        if emptyroom.startswith('r'):
            for member in party:
                member.regeneration()
            print('You rest for a while')
            time.sleep(4)
            print('You feel revitalized and ready to press on')
            return None
        elif emptyroom.startswith(('s')):
            emptyroomroll = search_empty_room(party, dead_monster_list, dead_player_list)
            if emptyroomroll == 0:
                print('The room is completely empty and you move further into the cave')
            elif emptyroomroll == 1:
                print('You see a chest')
                print('It contains:')
                print('placeholder for loot')
                return None
            else:
                ('As you search the room, you stumble')
                time.sleep(1)
                ('You hear noices')
                time.sleep(2)
                ('Someone must have heard you')
                emptyroomroll =- 1
                monsters = get_monsters(emptyroomroll, party_level)
                fight(party, monsters, dead_monster_list, dead_player_list)



def search_empty_room(party, dead_monster_list, dead_player_list):
    '''Used aftedr searching a empty room, in empty_room()
    Returns a roll, determined by party size'''
    emptyroomroll = random.randint(0,2)
    if emptyroomroll == 0:
        print('The room is completely empty and you move further into the cave')
    elif emptyroomroll == 1:
        print('You see a chest')
        print('It contains:')
        print('placeholder for loot')
    else:
        if len(party) == 1:
            emptyroomroll = random.randint(0, 1)
        elif len(party) in range(2, 4):  # 2 up to, but not including, 4 (check this)
            emptyroomroll = random.randint(0, len(party) + 2)
        else:
            emptyroomroll = random.randint(0, len(party) + 3)
        fight(party, emptyroomroll, dead_monster_list, dead_player_list)

def get_monsters(monster, party_level):
    '''Input requires: monster, an integer that determines the number of monsters in a room
    Returns a list of monsters'''
    monsters = []
    for i in range(monster):
        if monster == 1:
            cla = monsterclasses[random.randint(0,2)]
        else:
            cla = monsterclasses[random.randint(0, 3)]
        race = monsterrace[random.randint(0, len(monsterrace)-1)]
        if cla == 'warrior':
            actions = meleelist_warrior
            maxhp = 150 + party_level * 30
            magicstat = 0
            attackstat = party_level * 5
            defensestat = party_level * 10
            healingstat = 0
        elif cla == 'fighter':
            maxhp = 120 + party_level * 20
            actions = meleelist_fighter
            magicstat = 0
            attackstat = party_level * 7
            defensestat = party_level * 5
            healingstat = 0
        elif cla == 'mage':
            actions = magiclist_mage
            maxhp = 100 + party_level * 5
            magicstat = party_level * 5
            attackstat = 0
            defensestat = party_level
            healingstat = party_level * 2
        elif cla == 'healer':
            actions = heallist_healer
            maxhp = 100 + party_level * 5
            magicstat = party_level * 7
            attackstat = 0
            defensestat = 0
            healingstat = party_level * 10
        maxmp = 300 + party_level * 50
        maxhp -= 100   # This is to make testing easier, delete later
        monsters.append(Enemy(party_level, race, cla, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat, actions))
    return monsters
