import random

from Game.classes import Enemy
from Game.lists import magiclist, meleewlist, meleeflist, monsterclasses, \
    monsterrace, heallist, GreatHeal, FromAbove, MediumHeal, SmallHeal


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


def empty_room(party):
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


def search_empty_room(party):
    '''Used aftedr searching a empty room, in empty_room()
    Returns a roll, determined by party size'''
    if len(party) == 1:
        emptyroomroll = random.randint(0, 3)
    elif len(party) in range(2, 4):  # 2 up to, but not including, 4 (check this)
        emptyroomroll = random.randint(0, len(party) + 2)
    else:
        emptyroomroll = random.randint(0, len(party) + 3)
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


def fight(party, monsters, dead_player_list):
    '''NOT DONE
    The fight, shows HP for players and creatures
    Lets you attack and be attack
    Should be able to kill players and mosters
    Return a list of the dead monsters levels, so loot can be generated'''
    fighting = True
    dead_monster_list = []
    while fighting is True:
        for i in range(len(party)):
            party[i].display_current()
        for j in range(len(monsters)):
            monsters[j].display_current()

        fight_player_attack(party, monsters)
        fight_enemy_attack(party, monsters)
        dead_players(party, dead_player_list)
        dead_enemies(monsters, dead_monster_list)
        if len(party) == 0 or len(monsters) == 0:
            fighting = False



def fight_player_attack(party, monsters):
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
                while Saction_choice == False:  # Let's the player choose its Secondary Action
                    if int(action) == 1:  #
                        for i in range(len(member.Saction)):
                            print(str(i + 1) + ': ' + str(member.Saction[i].name))
                        print('Or type back (b) to get to the previous menu') # Doesnt work
                        Saction = input()
                        if Saction.isdigit():
                            if int(Saction) - 1 in range(len(member.Saction)):
                                attack = member.Saction[int(Saction) - 1]
                                target_chosen = False
                                while target_chosen == False:
                                    print('Chose a target')
                                    for j in range(len(monsters)):
                                        print(str(j + 1) + ': ', end='')
                                        monsters[j].display_current()
                                    target_choice = input()
                                    if target_choice.isdigit():
                                        if int(target_choice) - 1 in range(len(monsters)):
                                            target = monsters[int(target_choice) - 1]
                                            player_attack(member, target, attack)
                                            for i in range(len(party)):
                                                party[i].display_current()
                                            for j in range(len(monsters)):
                                                monsters[j].display_current()
                                            target_chosen = True
                                            Saction_choice = True
                                            action_choice = True
                                            # Make a lot of shit True
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
                    elif int(action) == 3:
                        print('Potions, placeholder')
                        Saction_choice = True
            else:
                print('Invalid input (i)')



def fight_enemy_attack(party, monsters):
    for enemy in monsters:
        if enemy.cla == 'healer':
            very_low_monster = [] # Finds monsters in desperate need of healing
            low_monster = [] # Finds monsters in need of healing
            high_monster = [] # Finds monsters who are not full and could use a small heal
            for enemytarget in monsters: # Creates lists based on healing
                if enemytarget.hp < enemytarget.maxhp * 0.2:
                    very_low_monster.append(enemytarget)
                elif enemytarget.hp < enemytarget.maxhp * 0.5:
                    low_monster.append(enemytarget)
                elif enemytarget.hp < enemytarget.maxhp * 0.85:
                    high_monster.append(enemytarget)
            if len(very_low_monster) == 1: # If a monster is very low on health, it gets a large heal
                target = very_low_monster[0]
                heal = GreatHeal
                heal_dmg = enemy.cast_heal(heal, target)
                target.get_healed(heal_dmg)
            elif len(very_low_monster) == 2: # If two monsters are very low, one of them gets a large heal
                target = very_low_monster[random.randint(0,1)]
                heal = GreatHeal
                heal_dmg = enemy.cast_heal(heal, target)
                target.get_healed(heal_dmg)
            elif len(very_low_monster) > 2: # Many are desperate for healing, all monsters get healed
                heal = FromAbove
                heal_dmg = enemy.cast_heal(heal, target)
                for target in monsters:
                    target.get_healed(heal_dmg)
            elif len(low_monster) == 1:
                target = low_monster[0]
                heal = MediumHeal
                heal_dmg = enemy.cast_heal(heal, target)
                target.get_healed(heal_dmg)
            elif len(low_monster) == 2:
                target = low_monster[random.randint(0,1)]
                heal = MediumHeal
                heal_dmg = enemy.cast_heal(heal, target)
                target.get_healed(heal_dmg)
            elif len(low_monster) > 2:
                heal = FromAbove
                heal_dmg = enemy.cast_heal(heal, target)
                for target in monsters:
                    target.get_healed(heal_dmg)
            elif len(high_monster) == 1:
                target = high_monster[0]
                heal = SmallHeal
                heal_dmg = enemy.cast_heal(heal, target)
                target.get_healed(heal_dmg)
            elif len(high_monster) > 1:
                target = high_monster[random.randint(0, len(high_monster) -1)]
                heal = SmallHeal
                heal_dmg = enemy.cast_heal(heal, target)
                target.get_healed(heal_dmg)
            else:
                print('Placeholder for mana-regen')
        else:
            low_player = []  # Finds low-HP targets to attack
            for player in party:
                if player.hp > player.maxhp * 0.5:
                    low_player.append(player)
            if len(party) == 1:
                single_target_attacks = []
                for strike in enemy.actions:
                    if strike.target == 1:
                        single_target_attacks.append(strike)
                attack = single_target_attacks[random.randint(0, len(single_target_attacks) -1)]
                target = party[0]
                dmg = enemy.make_attack(attack)
                target.take_dmg(dmg, attack)
            elif len(low_player) == 0: #If there are no players with low health
                attack = enemy.actions[random.randint(0, len(enemy.actions) -1)]
                if attack.name == 'Taunt':
                    print('Taunt placeholder')
                elif attack.name == 'Rage':
                    print('Rage placeholder')
                elif attack.target == 1: #The attack has one target
                    target = party[random.randint(0, len(party) -1)]
                    dmg = enemy.make_attack(attack)
                    target.take_dmg(dmg, attack)
                elif attack.target == 2: #The attack has 2 targets
                    if len(party) == 2:
                        target1 = party[0]
                        target2 = party[1]
                        dmg = enemy.make_attack(attack)
                        target1.take_dmg(dmg, attack)
                        target2.take_dmg(dmg, attack)
                    else:
                        target1 = party[0, random.randint(0, len(party) -1)]
                        target2 = None
                        while target2 == None:
                            targetX = party[0, random.randint(0, len(party) -1)]
                            if targetX != target1:
                                target2 = targetX
                        dmg = enemy.make_attack(attack)
                        target1.take_dmg(dmg, attack)
                        target2.take_dmg(dmg, attack)
                elif attack.target == 'all':
                    dmg = enemy.make_attack(attack)
                    for player in party:
                        player.take_dmg(dmg, attack)
                elif attack.target == 'random':
                    dmg = enemy.make_attack(attack)
                    number_of_targets = random.randint(1, len(party))
                    random_targets = []
                    while len(random_targets) > number_of_targets:
                        target = party[random.randint(0, len(party) -1)]
                        if target not in random_targets:
                            random_targets.append(target)
                            target.take_dmg(dmg, attack)
            elif len(low_player) == 1: #One player has low health
                target = low_player[0]
                single_target_attacks = []
                for strike in enemy.actions:
                    if strike.target == 1:
                        single_target_attacks.append(strike)
                attack = single_target_attacks[random.randint(0, len(single_target_attacks) -1)]
                dmg = enemy.make_attack(attack)
                target.take_dmg(dmg, attack)
            elif len(low_player) == 2:
                dual_target_attacks = []
                for strike in enemy.actions:
                    if strike.target == 2:
                        dual_target_attacks.append(strike)
                    if len(dual_target_attacks) == 1:
                        attack = dual_target_attacks[0]
                    else:
                        attack = dual_target_attacks[random.randint(0, len(dual_target_attacks) -1)]
                    dmg = enemy.make_attack(attack)
                    target1 = low_player[0]
                    target2 = low_player[1]
                    target1.take_dmg(dmg, attack)
                    target2.take_dmg(dmg, attack)
            elif len(party) == 2:
                single_dual_attacks = []
                for strike in enemy.actions:
                    if strike.target == 1 or strike.target == 2:
                        single_dual_attacks.append(strike)
                    attack = single_dual_attacks[random.randint(0, len(single_dual_attacks) -1)]
                    if attack.target == 1:
                        target = party[random.randint(0,1)]
                        dmg = enemy.make_attack(attack)
                        target.take_dmg(dmg, attack)
                    else:
                        target1 = party[0]
                        target2 = party[1]
                        dmg = enemy.make_attack(attack)
                        target1.take_dmg(dmg, attack)
                        target2.take_dmg(dmg, attack)
            else:
                multiple_attacks = []
                for strike in enemy.actions:
                    if strike.target != 1 and strike.target != 2:
                        multiple_attacks.append(strike)
                attack = multiple_attacks[random.randint(0, len(multiple_attacks) -1)]
                dmg = enemy.make_attack(attack)
                random_targets = []
                while len(random_targets) > attack.target: #If error, this might not to object
                    target = party[random.randint(0, len(party) -1)]
                    if target not in random_targets:
                        random_targets.append(target)
                        target.take_dmg(dmg, attack)
 # Add debuffs to player / target before and after attacks


def player_attack(attacker, target, attack):
    """Generates dmg and removes resources used for the attack"""
    dmg = attacker.make_attack(attack)
    target.take_dmg(dmg, attack)


def dead_players(party, dead_player_list):
    """Checks for dead players, removes them from party and returns a list of dead players"""

    for member in party:
        if member.hp <= 0:
            party.remove(member)
            dead_player_list.append(member)


def dead_enemies(monsters, dead_monster_list):
    """Check if monsters are dead and removes them from the monsters list and returns a list of dead monsters"""
    dead_monster_list
    for enemy in monsters:
        if enemy.hp <= 0:
            monsters.remove(enemy)
            dead_monster_list.append(enemy)

    return dead_enemies
