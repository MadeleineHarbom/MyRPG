

class MyColours:
    RED = '\033[93m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WARNING = '\033[93m' '\033[1m'

class Character(object):
    def __init__(self):



class Player:
    def __init__(self, name, race, cla, actions, Saction1, Saction2, maxhp, maxmp, magicstat, attackstat, defensestat, healingstat):
        self.name = name
        self.ap = 0  # Attack Points
        self.maxap = 0
        self.hp = maxhp  # Health
        self.maxhp = maxhp
        self.mp = maxmp  # Mana Points
        self.maxmp = maxmp
        self.race = race
        self.cla = cla  # class
        self.magic = magicstat  # Bonus to magic spells
        self.magicl = self.magic - 5
        self.magich = self.magic + 5
        self.attack = attackstat  # Bonus to melee dmg
        self.attackl = self.attack -5
        self.attackh = self.attack +5
        self.defense = defensestat
        self.defensel = self.defense -5
        self.defenseh = self.defense +5  # Lowers dmg taken
        self.actions = actions  # First action option
        self.Saction1 = Saction1
        self.Saction2 = Saction2
        self.eq = 'placeholder'  # Equipped gear

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





class Enemy:
    def __init__(self, cla, level, hp):
        self.cla = cla
        self.level = level

class Boss:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = 5
        self.hp = 800