import random

from Game.classes import Const
from Game.lists import GreatHeal, FromAbove, MediumHeal, SmallHeal




def fight(party, monsters, dead_monster_list, dead_player_list):
    """The fight, shows HP for players and creatures
    Lets you attack and be attack
    Should be able to kill players and monsters
    Return a list of the dead monsters levels, so loot can be generated"""
    dead_monster_list = []
    while True:
        display_combat_stats(party, monsters)

        fight_player_turn(party, monsters, dead_monster_list)
        fight_enemy_turn(party, monsters, dead_player_list)
        dead_players(party, dead_player_list)
        if len(party) == 0:
            print('Game Over')
            break
        elif len(monsters) == 0:
            print('You have conquered the room')
            break


    return dead_monster_list


def display_combat_stats(party, monsters):
    for i in range(len(party)):
        party[i].display_current()
    for j in range(len(monsters)):
        monsters[j].display_current()


def fight_player_turn(party, monsters, dead_monster_list):
    """Uses the following methods"""
    for member in party:
        fight_player_actions(member, party, monsters)
        dead_enemies(monsters, dead_monster_list)


def fight_player_actions(member, party, monsters):
    retreat = None
    while True:
        if retreat == Const.TURNOVER:
            break
        elif len(monsters) == 0:
            break
        else:
            print(member.name + "'s turn")
            for i in range(len(member.actions)):
                print(str(i + 1) + ': ' + str(member.actions[i]['description']))
            action_choice = input()
            if not action_choice.isdigit():
                print('Invalid input, please enter a number')
            elif int(action_choice) - 1 in range(len(member.actions)):
                action_type = member.actions[int(action_choice) - 1]['action']
                retreat = fight_player_attack(member, action_type, party, monsters)
            else:
                print('Invalid input, please enter one of the spells')


def fight_player_attack(member, action_type, party, monsters):
    """Returns action or Const.Back"""
    if action_type == Const.SPECIALATTACK:
        retreat = fight_player_specialattack(member, monsters)
    elif action_type == Const.WHITEDMG:
        retreat = fight_player_whitedmg(member, monsters)
    elif action_type == Const.REGEN:
        retreat = fight_player_regen(member)
    elif action_type == Const.POTS:
        retreat = fight_player_pots(member, party, monsters)
    elif action_type == Const.MAGIC:
        retreat = fight_player_magic(member, monsters)
    elif action_type == Const.HEALING:
        retreat = fight_player_healing(member, party, monsters)
    return retreat


def fight_player_specialattack(member, monsters):
    retreat = None
    while True:
        if retreat == Const.BACK:
            return retreat
        elif retreat == Const.TURNOVER:
            return retreat
        else:
            for i in range(len(member.melee_actions)):
                print(str(i + 1) + ': ' + str(member.melee_actions[i].name))
            print('Pick an attack or type back (b) to pick a different action')
            attack_choice = input()
            if attack_choice.lower().startswith('b'):
                retreat = Const.BACK
            elif not attack_choice.isdigit():
                print('Invalid choice, please enter a number')
            elif int(attack_choice) -1 in range(len(member.melee_actions)):
                attack = member.melee_actions[int(attack_choice) -1]
                retreat = fight_player_target_enemy(member, attack, monsters)
            else:
                print('Invalid input, please enter one of the spells')


def fight_player_whitedmg(member, monsters):
    print('placeholder, needs weapon dmg')
    return Const.TURNOVER


def fight_player_regen(member):
    print('placeholder, figure this shit out')
    return Const.TURNOVER


def fight_player_pots(member, party, monsters):
    print('placeholder, needs pots')
    return Const.BACK


def fight_player_magic(member, monsters):
    retreat = None
    while True:
        if retreat == Const.BACK:
            return retreat
        elif retreat == Const.TURNOVER:
            return retreat
        for i in range(len(member.magic_actions)):
            print(str(i + 1) + ': ' + str(member.magic_actions[i].name))
        print('Pick an attack or type back (b) to pick a different action')
        attack_choice = input()
        if attack_choice.lower().startswith('b'):
            return Const.BACK
        elif not attack_choice.isdigit():
            print('Invalid choice, please enter a number')
        elif int(attack_choice) -1 in range(len(member.magic_actions)):
            attack = member.magic_actions[int(attack_choice) -1]
            retreat = fight_player_target_enemy(member, attack, monsters)
        else:
            print('Invalid input, please enter one of the spells')


def fight_player_healing(member, party, monsters):
    retreat = None
    while True:
        if retreat == Const.BACK:
            return retreat
        elif retreat == Const.TURNOVER:
            return retreat
        for i in range(len(member.healing_actions)):
            print(str(i + 1) + ': ' + str(member.healing_actions[i].name))
        print('Pick an attack or type back (b) to pick a different action')
        attack_choice = input()
        if attack_choice.lower().startswith('b'):
            return Const.BACK
        elif not attack_choice.isdigit():
            print('Invalid choice, please enter a number')
        elif int(attack_choice) -1 in range(len(member.healing_actions)):
            heal = member.healing_actions[int(attack_choice) -1]
            retreat = fight_player_target_friendly(member, heal, party, monsters)
        else:
            print('Invalid input, please enter one of the spells')


def fight_player_target_enemy(member, attack, monsters):
    """Targets an enemy
    The enemy takes dmg and player resources are removed
    Used by ....
    Returns Const.BACK or Const.TURNOVER"""
    while True:
        if attack.target == 1:
            for i in range(len(monsters)):
                print(str(i + 1) + ': ' + str(monsters[i].name))
            print('Pick a target to attack, or type back (b) to pick another attack (target=1)')
            target_choice = input()
            if target_choice.lower().startswith('b'):
                return Const.BACK
            elif not target_choice.isdigit():
                print('Invalid. Please enter a number')
            elif int(target_choice) - 1 in range(len(monsters)):
                target = monsters[int(target_choice) - 1]
                dmg = member.make_attack(attack)
                target.take_dmg(dmg, attack)
                print('You hit ' + str(target.name) + ' for ' + str(dmg) + ' dmg with ' + str(attack.name))
                return Const.TURNOVER
            else:
                print('Invalid target, please pick a living target')
        elif attack.target == 2:
            while True:
                for i in range(len(monsters)):
                    print(str(i + 1) + ': ' + str(monsters[i].name))
                print('Pick your first target to attack, or type back (b) to pick another attack (target = 2)')
                if len(monsters) < 2:
                    print('Note that your chosen special attack till attack two targets only if there are two targets alive')
                target_choice = input()
                if target_choice.lower().startswith('b'):
                    return Const.BACK
                elif not target_choice.isdigit():
                    print('Invalid. Please enter a number')
                elif int(target_choice) - 1 in range(len(monsters)):
                    target1 = monsters[int(target_choice) - 1]
                    break
            monsterlist2 = monsters
            monsterlist2.remove(target1)
            if len(monsterlist2) > 0:
                while True:
                    for i in range(len(monsterlist2)):
                        print(str(i + 1) + ': ' + str(monsters[i].name))
                    print('Pick your second target to attack')
                    target_choice = input()
                    if not target_choice.isdigit():
                        print('Invalid. Please enter a number')
                    elif int(target_choice) - 1 in range(len(monsters)):
                        target2 = monsters[int(target_choice) - 1]

            dmg1 = member.make_attack(attack)
            target1.take_dmg(dmg1, attack)
            print('You hit ' + str(target1.name) + ' for ' + str(dmg1) + ' dmg with ' + str(attack.name))
            if len(monsterlist2) > 0:
                dmg2 = member.make_attack(attack)
                target2.take_dmg(dmg, attack)
                print('You hit ' + str(target2.name) + ' for ' + str(dmg2) + ' dmg with ' + str(attack.name))
            return Const.TURNOVER
        elif attack.target == 'all':
            for target in monsters:
                dmg = member.make_attack(attack)
                target.take_dmg(dmg, attack)
                print('You hit ' + str(target.name) + ' for ' + str(dmg) + ' dmg with ' + str(attack.name))
            return Const.TURNOVER
        elif attack.target == 'random':
            target_number = random.randint(1, len(monsters))
            random_targets = []
            monsterlistrandom = monsters
            while len(random_targets) < target_number:
                random_target = monsterlistrandom[random.randint(1, len(monsterlistrandom)) - 1]
                random_targets.append(random_target)
                monsterlistrandom.remove(random_target)
            for target in random_targets:
                dmg = member.make_attack(attack)
                target.take_dmg(dmg, attack)
                print('You hit ' + str(target.name) + ' for ' + str(dmg) + ' dmg with ' + str(attack.name))
            return Const.TURNOVER


def fight_player_target_friendly(member, heal, party, monsters):
    """Target a party member"""
    while True:
        if heal.target == 1:
            for i in range(len(party)):
                print(str(i + 1) + ': ' + str(party[i].name))
            print('Pick a target to heal')
            target_choice = input()
            if target_choice.lower().startswith('b'):
                return Const.BACK
            elif not target_choice.isdigit():
                print('Invalid input, please enter a number')
            elif int(target_choice) - 1 in range(len(party)):
                target = party[int(target_choice) - 1]
                heal_dmg = member.cast_heal(heal)
                target.get_healed(heal_dmg)
                print('You heal ' + str(member.name) + ' for ' + str(heal_dmg) + ' hitpoints with ' + str(heal.name))
                return Const.TURNOVER
            else:
                print('Invalid target, please pick a living target')
        elif heal.target == 'all':
            for target in party:
                heal_dmg = member.cast_heal(heal)
                target.get_healed(heal_dmg)
                print('You heal ' + str(target.name) + ' for ' + str(heal_dmg) + ' hitpoints with ' + str(heal.name))
            return Const.TURNOVER


def fight_enemy_turn(party, monsters, dead_player_list):
    for enemy in monsters:
        if enemy.cla == 'healer':
            fight_enemy_healer(enemy, monsters)
        else:  # Fighting enemy is a damage-dealer
            low_player = low_player_list(party)
            if len(party) == 1:
                target = party[0]
                fight_enemy_single_target(enemy, target)
            elif len(low_player) == 1:
                target = low_player[0]
                fight_enemy_single_target(enemy, target)
            elif len(party) == 2:
                roll = random.randint(1,2)
                if roll == 1:
                    target = party[random.randint(0,1)]
                    fight_enemy_single_target(enemy, target)
                elif roll == 2:
                    targets = party
                    fight_enemy_dual_target(enemy, targets)
            elif len(low_player) == 2:
                roll = random.randint(1, 2)
                if roll == 1:
                    target = low_player[random.randint(0,1)]
                    fight_enemy_single_target(enemy, target)
                elif roll == 2:
                    targets = low_player
                    fight_enemy_dual_target(enemy, targets)
            else:  # There are no low-health players, the monster hits with a all or random attack
                roll = random.randint(1,3)
                if roll == 1:
                    target = party[random.randint(0, len(party) -1)]
                    fight_enemy_single_target(enemy, target)
                elif roll == 2:
                    targets = two_random_targets(party)
                    fight_enemy_dual_target(enemy, targets)
                elif roll == 3:
                    fight_enemy_multiple_target(enemy, party)
        dead_players(party, dead_player_list)
 # Add debuffs to player / target before and after attacks


def fight_enemy_healer(enemy, monsters):
    very_low_monster = []  # Finds monsters in desperate need of healing
    low_monster = []  # Finds monsters in need of healing
    high_monster = []  # Finds monsters who are not full and could use a small heal
    for enemytarget in monsters:  # Creates lists based on healing
        if enemytarget.hp < enemytarget.maxhp * 0.2:
            very_low_monster.append(enemytarget)
        elif enemytarget.hp < enemytarget.maxhp * 0.5:
            low_monster.append(enemytarget)
        elif enemytarget.hp < enemytarget.maxhp * 0.85:
            high_monster.append(enemytarget)
    if len(very_low_monster) == 1:  # If a monster is very low on health, it gets a large heal
        target = very_low_monster[0]
        heal = GreatHeal
        heal_dmg = enemy.cast_heal(heal, target)
        target.get_healed(heal_dmg)
        print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(very_low_monster) == 2:  # If two monsters are very low, one of them gets a large heal
        target = very_low_monster[random.randint(0, 1)]
        heal = GreatHeal
        heal_dmg = enemy.cast_heal(heal, target)
        target.get_healed(heal_dmg)
        print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(very_low_monster) > 2:  # Many are desperate for healing, all monsters get healed
        heal = FromAbove
        heal_dmg = enemy.cast_heal(heal, target)
        for target in monsters:
            target.get_healed(heal_dmg)
            print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(low_monster) == 1:
        target = low_monster[0]
        heal = MediumHeal
        heal_dmg = enemy.cast_heal(heal, target)
        target.get_healed(heal_dmg)
        print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(low_monster) == 2:
        target = low_monster[random.randint(0, 1)]
        heal = MediumHeal
        heal_dmg = enemy.cast_heal(heal, target)
        target.get_healed(heal_dmg)
        print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(low_monster) > 2:
        heal = FromAbove
        heal_dmg = enemy.cast_heal(heal, target)
        for target in monsters:
            target.get_healed(heal_dmg)
            print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(high_monster) == 1:
        target = high_monster[0]
        heal = SmallHeal
        heal_dmg = enemy.cast_heal(heal, target)
        target.get_healed(heal_dmg)
        print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    elif len(high_monster) > 1:
        target = high_monster[random.randint(0, len(high_monster) - 1)]
        heal = SmallHeal
        heal_dmg = enemy.cast_heal(heal, target)
        target.get_healed(heal_dmg)
        print(enemy.name + ' heals ' + target.name + ' for ' + str(heal_dmg) + ' hitpoints with ' + heal.name)
    else:
        print('Placeholder for enemy-mana-regen')

def fight_enemy_single_target(enemy, target):
    single_target_attacks = []
    for strike in enemy.actions:
        if strike.target == 1:
            single_target_attacks.append(strike)
    attack = single_target_attacks[random.randint(0, len(single_target_attacks) - 1)]
    dmg = enemy.make_attack(attack)
    target.take_dmg(dmg, attack)
    print(enemy.name + ' hits ' + target.name + ' for ' + str(dmg) + ' hitpoints with ' + attack.name)


def fight_enemy_dual_target(enemy, targets):
    dual_target_attacks = []
    for strike in enemy.actions:
        if strike.target == 2:
            dual_target_attacks.append(strike)
        if len(dual_target_attacks) == 0:
            print('No dual target attacks available')
        attack = dual_target_attacks[random.randint(0, len(dual_target_attacks) - 1)]
        dmg = enemy.make_attack(attack)
        targets[0].take_dmg(dmg, attack)
        targets[1].take_dmg(dmg, attack)
        print(enemy.name + ' hits ' + targets[0].name + ' for ' + str(dmg) + 'damage with ' + attack.name)
        print(enemy.name + ' hits ' + targets[1].name + ' for ' + str(dmg) + 'damage with ' + attack.name)


def fight_enemy_multiple_target(enemy, party):
    multiple_attacks = []
    for strike in enemy.actions:
        if strike.target != 1 and strike.target != 2:
            multiple_attacks.append(strike)
    attack = multiple_attacks[random.randint(0, len(multiple_attacks) - 1)]
    if attack.target == 'all':
        dmg = enemy.make_attack(attack)
        for target in party:
            target.take_dmg(dmg, attack)
            print(enemy.name + ' hits ' + target.name + ' for ' + str(dmg) + 'damage with ' + attack.name)
    elif attack.target == 'random':
        targets = randomized_targets(party)
        for target in targets:
            target.take_dmg(dmg, attack)
            print(enemy.name + ' hits ' + target.name + ' for ' + str(dmg) + 'damage with ' + attack.name)
    else:
        print('Attack.target undefined')


def low_player_list(party):
    low_player = []  # Finds low-HP targets to attack
    for player in party:
        if player.hp > player.maxhp * 0.5:
            low_player.append(player)
    return low_player


def two_random_targets(party):
    """Does not work if there are less than 2 in party"""
    roll = random.sample(range(0, len(party)), 2)
    targets = [party[roll[0]], party[roll[1]]]
    return targets


def randomized_targets(party):
    targets = []
    roll = random.sample(range(0, len(party)), random.randint(1, len(party)))
    for i in range(len(roll)):
        targets.append(party[i])
    return targets


def dead_players(party, dead_player_list):
    """Checks for dead players, removes them from party and returns a list of dead players"""

    for member in party:
        if member.hp <= 0:
            party.remove(member)
            dead_player_list.append(member)


def dead_enemies(monsters, dead_monster_list):
    """Check if monsters are dead and removes them from the monsters list and returns a list of dead monsters"""
    for enemy in monsters:
        if enemy.hp <= 0:
            monsters.remove(enemy)
            dead_monster_list.append(enemy)

    return dead_enemies


def post_fight(party, dead_monster_list):
    pass