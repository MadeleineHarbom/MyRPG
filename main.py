import sys
import time

from Game.classes import Player
from Game.rooms import get_roomroll, empty_room, get_monsters
from Game.fight import fight
from Game.introduction import chose_race, chose_class, generate_actions, generate_healing, generate_magic, \
    generate_melee, generate_hp, generate_mp, \
    generate_magic_stat, generate_attack_stat, generate_defense_stat, generate_healing_stat, enter_cave_story, \
    first_room, setup_party, chose_name

print('Welcome to the world of I-cant-be-bothered-making-up-name')

size = setup_party()

party = []
party_level = 1
inventory = []
dead_player_list = []
dead_monster_list = []

for i in range(size):
    name = chose_name()
    race = chose_race(name)
    cla = chose_class(name)
    actions = generate_actions(cla)
    melee_actions = generate_melee(cla)
    healing_actions = generate_healing(cla)
    magic_actions = generate_magic(cla)
    maxhp = generate_hp(cla)
    maxmp = generate_mp(cla)
    magic_stat = generate_magic_stat(cla, race)
    melee_stat = generate_attack_stat(cla, race)
    defense_stat = generate_defense_stat(cla, race)
    healing_stat = generate_healing_stat(cla, race)
    party.append(Player(name, race, cla, actions, melee_actions, healing_actions, magic_actions,
                        maxhp, maxmp, magic_stat, melee_stat, defense_stat, healing_stat))
    print('You are now ' + name +', the ' + race + '.')
    print('You have pledged your skills as a ' + cla + ' to rescue the people of I-cant-be bothered-making-up-a-name from whatever-is-in-this-cave-or-whatever-it-is.')


print('You stand in front of a dark cave')
print('Do you enter?')
print('Press enter to enter, or type quit to exit the game')
enter_cave = input().lower()
if enter_cave == 'quit':
    sys.exit()
else:
    enter_cave_story()

party_alive = True
previous = 0
exp = 0  # Not yet in use

monsters = first_room(party_level)  # Monsters is a list
fight(party, monsters, dead_player_list, dead_player_list)

print('Press enter to continue, or type q to quit the game')
next_room = input().lower()
if next_room == 'quit':
    sys.exit()
else:
    print('With trembling steps, you walk through a tunnel')
    print('It is small and you need to bow your head')
    print('You can feel the drippings from the roof of the rocks rolling down your face')
    time.sleep(2)
# Get Loot

while party_alive == True:
    roomroll = get_roomroll(party, previous)
    if roomroll == 0:
        empty_room(party, party_level, dead_monster_list ,dead_player_list)
    else:
        monsters = get_monsters(roomroll, party_level)
        print('Oh no, there\'s someone there!')
        print('Someone... or something!')
        fight(party, monsters, dead_monster_list, dead_player_list)
    if len(party) == 0:
        break
    print('Would you like to view your inventory')
    while True:
        print('Yes / No')
        inv_reply = input().lower()
        if inv_reply.startswith('y'):
            print('View inventory, placeholder')
            continue
        elif inv_reply.startswith('n'):
            print('You move further into the cave')
            break
        else:
            continue

print('Test')




#You can browse your inventory before leaving any room