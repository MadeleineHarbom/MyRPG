import random
from enum import Enum

class MyColours:
    RED = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WARNING = '\033[93m' '\033[1m'


class Const(Enum):
    WHITEDMG = 'weapon attack without using of resources'
    REGEN = 'regenerate spendable resources'
    SPECIALATTACK = 'special attack, melee'
    POTS = 'Potions'
    BACK = 'return to previous menu'
    MAGIC = 'Offensive magic'
    HEALING = 'Healing magic'
    TURNOVER = 'The players turn is over'


class Player():
    def __init__(self, name, race, cla, actions, melee_actions, healing_actions, magic_actions, maxhp, maxmp,
                 magicstat, attackstat, defensestat, healingstat):
        self.name = name
        self.deviation = 5
        self.eq = []  # Equipped Items
        self.actions = actions  # First action option
        self.melee_actions = melee_actions  # Secondsary action option
        self.healing_actions = healing_actions  # Secondsary action option
        self.magic_actions = magic_actions  # Secondsary action option
        self.rage = 60  # Attack Points
        self.maxrage = 60
        self.hp = maxhp  # Health
        self.maxhp = maxhp
        self.mp = maxmp  # Mana Points
        self.maxmp = maxmp
        self.race = race
        self.cla = cla  # class
        self.magic_stat = magicstat  # Bonus to magic spells
        self.melee_stat = attackstat  # Bonus to melee dmg
        self.defense_stat = defensestat  # Reduces dmg taken
        self.healing_stat = healingstat  # Increases healing




    def regeneration(self):
        self.hp = self.maxhp
        self.mp = self.maxmp
        self.rage = self.maxrage

    def after_combat(self):
        self.hp += 420
        self.mp += 70
        self.rage += 30

    def display_current(self):
        if self.cla == 'warrior' or self.cla == 'fighter':
            print(self.name , ':')
            print('\t',  self.hp, '/', self.maxhp, ' Hitpoints')
            print('\t', self.rage, '/', self.maxrage, 'Attack Power')
        elif self.cla == 'mage' or self.cla == 'healer':
            print(self.name, ':')
            print('\t', self.hp, '/', self.maxhp, ' Hitpoints')
            print('\t', self.mp, '/', self.maxmp, 'Mana Points')

    def make_attack(self, attack):
        '''Removes resouces from player when attacking
        Generates amount of damage to be dealt'''
        if isinstance(attack, SpecAttack):
            self.rage -= attack.cost
        elif isinstance(attack, Magic):
            self.mp -= attack.cost

        if isinstance(attack, SpecAttack):
            base_dmg = attack.dmg + self.melee_stat
            dmg = random.randint(base_dmg - self.deviation, base_dmg + self.deviation)
        elif isinstance(attack, Magic):
            base_dmg = attack.dmg + self.magic_stat
            dmg = random.randint(base_dmg - self.deviation, base_dmg + self.deviation)
        return dmg

    def take_dmg(self, dmg, attack):
        self.hp -= dmg

    def cast_heal(self, heal):
        self.mp -= heal.cost
        base_heal = heal.heal + self.healing_stat
        heal_dmg = random.randint(base_heal - self.deviation, base_heal + self.deviation)
        return heal_dmg


    def get_healed(self, heal_dmg):
        self.hp += heal_dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp


    def start_potions(self):
        pass

    def start_eq(self):
        pass



class Enemy():
    def __init__(self, partylevel, race, cla, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat, actions):
        self.level = random.randint(partylevel - 1, partylevel +2)
        self.deviation = 5
        self.magic = magicstat  # Bonus to magic spells
        self.actions = actions
        self.name = str(race + ' ' + cla)
        self.rage = 60  # Attack Points
        self.maxrage = 60
        self.hp = maxhp  # Health
        self.maxhp = maxhp
        self.mp = maxmp  # Mana Points
        self.maxmp = maxmp
        self.race = race
        self.cla = cla  # class
        self.magic = magicstat  # Bonus to magic spells
        self.attack = attackstat  # Bonus to melee dmg
        self.defense = defensestat  # Reduces dmg taken
        self.healing = healingstat  # Increases healing

    def display_current(self):
        if self.cla == 'warrior' or self.cla == 'fighter':
            print(self.name, ':')
            print('\t',  self.hp, '/', self.maxhp, ' Hitpoints')
            print('\t', self.rage, '/', self.maxrage, 'Attack Power')
        elif self.cla == 'mage' or self.cla == 'healer':
            print(self.name, ':')
            print('\t', self.hp, '/', self.maxhp, ' Hitpoints')
            print('\t', self.mp, '/', self.maxmp, 'Mana Points')


    def make_attack(self, attack):
        '''Removes resources from Enemy when attack is made
        Generates amount of damage to be made'''
        if isinstance(attack, SpecAttack):
            self.rage -= attack.cost
        elif isinstance(attack, Magic):
            self.mp -= attack.cost

        if isinstance(attack, SpecAttack):
            base_dmg = attack.dmg + self.attack
            dmg = random.randint(base_dmg - self.deviation, base_dmg + self.deviation)
        elif isinstance(attack, Magic):
            base_dmg = attack.dmg + self.magic
            dmg = random.randint(base_dmg - self.deviation, base_dmg + self. deviation)
        return dmg


    def take_dmg(self, dmg, attack):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def cast_heal(self, heal, target):
        self.mp -= heal.cost
        base_heal = heal.heal + target.healing
        heal_dmg = random.randint(base_heal - self.deviation, base_heal + self.deviation)
        return heal_dmg

    def get_healed(self, heal_dmg):
        self.hp += heal_dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

class SpecAttack:
    def __init__(self, name, cost, dmg, effect, target):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.effect = effect
        self.target = target


class Magic:
    def __init__(self, name, cost, dmg, effect, target):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.effect = effect
        self.target = target


class Healing:
    def __init__(self, name, cost, heal, target):
        self.name = name
        self.cost = cost
        self.heal = heal
        self.target = target




class Boss:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = 5
        self.hp = 800



class Item:
    def __init__(self, partylevel):
        self.slot = find_slot()
        self.name = find_name()
        self.defence = random.randint(0, partylevel*3+1)
        self.magic = random.randint(0, partylevel*3+1)
        self.attack = random.randint(0, partylevel*3+1)
        self.healing = random.randint(0, partylevel*3+2)
        self.classes = 'placeholder'


    def find_slot(self):
        slotlist = ('Head', 'Hands', 'Shoulder', 'Torso', 'Legs', 'Feet', 'Ring', 'Necklace',
                    '1-handed', '2-handed',  'Staff', 'Shield')
        i = random.randint(0, len(slotlist))
        return slotlist[i]

    def find_name(self):
        headlist = ('Helmet', 'Mask', 'Bonnet', 'Hood', 'Cap', 'Turban', 'Hat', 'Fez', 'Beanie', 'Head Protector')
        handlist = ('Gloves', 'Hands', 'Mittens', 'Claws', 'Gauntlet', 'Fingers', 'Grip')
        shoulderlist = ('Shoulder Pads', 'Mantle', 'Wrap', 'Cape', 'Cloak', 'Shawl', 'Wrap')
        torsolist = ('Jacket', 'Armor', 'Robe', 'Dress', 'Chain-mail', 'Frock', 'Tunic', 'Vestments', 'Breastplate', 'Bra')
        leglist = ('Pants', 'Trousers', 'Leggings', 'Leg Protectors', 'Britches', 'Drawers', 'Pantaloons', 'Underpants')
        feetlist = ('Shoes', 'Boots', 'Slippers', 'Sandals', 'Gorgeous Heals', 'Flip-Flops', 'Pumps', 'Moccasins')
        ringlist = ('Ring', 'Band', 'Loop')
        neckielist = ('Pendant', 'Necklace', 'Choker')
        one_H_list = ('Danger Wand', 'Needle', 'Dagger', 'Dirk', 'Knife', 'Hatchet')
        two_H_list = ('Great Axe', 'Sword', 'Mighty Sword', 'Sharp Rod', 'Pokey Staff', 'Axe', 'Broadsword', 'Cleaver')
        stafflist = ('Might Stick', 'Staff', 'Poker', 'Rod', 'Pole', 'Stave', 'Cane', 'Walking Stick', 'Twig')
        shieldlist = ('Buckler')

        if self.slot == 'Head':
            roll = random.randint(0, len(headlist))
            First_name = headlist[roll]
        elif self.slot == 'Hand':
            roll = random.randint(0, len(handlist))
            First_name = handlist[roll]
        elif self.slot == 'Shoulder':
            roll = random.randint(0, len(shoulderlist))
            First_name = shoulderlist[roll]
        elif self.slot == 'Torso':
            roll = random.randint(0, len(torsolist))
            First_name = torsolist[roll]
        elif self.slot == 'Legs':
            roll = random.randint(0, len(leglist))
            First_name = leglist[roll]
        elif self.slot == 'Feet':
            roll = random.randint(0, len(feetlist))
            First_name = feetlist[roll]
        elif self.slot == 'Ring':
            roll = random.randint(0, len(ringlist))
            First_name = ringlist[roll]
        elif self.slot == 'Necklace':
            roll = random.randint(0,len(neckielist))
            First_name = neckielist[roll]
        elif self.slot == '1-Handed':
            roll = random.randint(0, len(one_H_list))
            First_name = OneHlist[roll]
        elif self.slot == '2-Handed':
            roll = random.randint(0, len(two_H_list))
            First_name = TwoHlist[roll]
        elif self.slot == 'Staff':
            roll = random.randint(0, len(stafflist))
            First_name = stafflist[roll]
        elif self.slot == 'Shield':
            roll = random.randint(0, len(shieldlist))
            First_name = shieldlist[roll]

        Second_name_list = ('Fury', 'Trickery', 'Mercy', 'the Night', 'Vengeance', 'Shadows', 'Might', 'Hurt',
                            'Darkness', 'Evil', 'Goodness', 'Righteousness', 'Pain', 'Strength', 'Orc Slaying',
                            'Protection', 'Hate')
        Second_name = Second_name_list[random.randint(0, len(Second_name_list))]
        name = First_name + ' of ' + Second_name
        return name


    def equip(self, target): #Targer is the player to equip


        target.magic += self.magic
        pass


    def unequip(self, target):
        pass