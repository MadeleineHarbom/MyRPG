import random

class MyColours:
    RED = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WARNING = '\033[93m' '\033[1m'

class Character(object):
    def __init__(self, race, cla, Saction1, Saction2, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat):
        self.ap = 0  # Attack Points
        self.maxap = 0
        self.hp = maxhp  # Health
        self.maxhp = maxhp
        self.mp = maxmp  # Mana Points
        self.maxmp = maxmp
        self.race = race
        self.cla = cla  # class
        self.magic = magicstat  # Bonus to magic spells
        self.attack = attackstat  # Bonus to melee dmg
        self.defense = defensestat #Reduces dmg taken
        self.healing = healingstat #Increases healing
        self.Saction1 = Saction1
        self.Saction2 = Saction2


class Player(Character):
    def __init__(self, name, race, cla, actions, Saction1, Saction2, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat):
        super(race, cla, Saction1, Saction2, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat)
        self.name = name
        self.deviation = 5
        self.eq = []  # Equipped Items
        self.actions = actions  # First action option



        def regeneration(self):
            self.hp = self.maxhp
            self.mp = self.maxmp
            self.ap = self.maxap

        def after_combat(self):
            self.hp += 420
            self.mp += 70
            self.ap += 30


        def start_potions(self, cla):
            pass

        def start_eq(self,cla):
            pass


class SpecAttack:
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


class Magic:
    def __init__(self, name, cost, dmg, effect, target):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.effect = effect
        self.target = target





class Enemy(Character):
    def __init__(self, partylevel):
        self.cla = cla
        self.level = level
        self.deviation = 5
        self.magic = magicstat  # Bonus to magic spells
        self.eq = 'placeholder'  # Equipped gear
        self.actions = actions  # First action option
        self.Saction1 = Saction1
        self.Saction2 = Saction2
        self.name = str(race + cla)



        return Enemy()


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
        shieldlist = ()

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


    def unequip(self, target):