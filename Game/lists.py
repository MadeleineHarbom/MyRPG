


from Game.classes import SpecAttack, Magic, Healing, Const


# Melee Attacks for warrior
PowerAttack = SpecAttack('Power Attack', 5, 5, 'none', 1) #Standard attack
Fury = SpecAttack('Fury', 10, 6, 'none', 2) #Hits two random targets
Taunt = SpecAttack('Taunt', 0, 0, 'taunt', 'all') #Focus all enemies on you for one round
RainOfPain = SpecAttack('Rain of Pain', 20, 4, 'none', 'all') #Dmg all enemies
meleelist_warrior = [PowerAttack, Fury, Taunt, RainOfPain]

#Melee Attacks for fighter
ConsumedByRage = SpecAttack('Consumed by Rage', 15, 15, 'none', 1) #Standard attack
Fury = SpecAttack('Fury', 10, 6, 'none', 2) #Hits two random targets
Rage = SpecAttack('Provoke', 0, 0, 'self + rage', 0) # You get extra rage
RainOfPain = SpecAttack('Rain of Pain', 20, 4, 'none', 'all') #Dmg all enemies
meleelist_fighter = [ConsumedByRage, Fury, Rage, RainOfPain]

# Magic Attacks for mage
FireBreath = Magic('Fire Breath', 40, 10,'none', 'random')  # Hits a random number of targets
IceBolt = Magic('Ice Bolt', 40, 15, 'ap', 1)  # Reduced Attack Power for one round
ShadowTongue = Magic('Shadow Tongue', 50, 10, 'magic', 1)  # Reducded Magic, permanent
Chill = Magic('Chill', 60, 5, 'attack', 'all')  # 20% chance for enemy to loose a turn, permanent
magiclist_mage = [FireBreath, IceBolt, ShadowTongue, Chill]

# Magic Attacks for healer
FireBreath = Magic('Fire Breath', 40, 10,'none', 'random')  # Hits a random number of targets
IceBolt = Magic('Ice Bolt', 40, 15, 'ap', 1)  # Reduced Attack Power for one round
ShadowTongue = Magic('Shadow Tongue', 50, 10, 'magic', 1)  # Reduced Magic, permanent
Chill = Magic('Chill', 60, 5, 'attack', 'all')  # 20% chance for enemy to loose a turn, permanent
magiclist_healer = [FireBreath, IceBolt, ShadowTongue, Chill]

# Healing for healers
SmallHeal = Healing('Small Heal,', 30, 11, 1)
MediumHeal = Healing('Heal', 60, 20, 1)
GreatHeal = Healing('Great Heal', 80, 27, 1)
FromAbove = Healing('From Above', 100, 16, 'all')
heallist_healer = [SmallHeal, MediumHeal, GreatHeal, FromAbove]

# Healing for mages
SmallHeal = Healing('Small Heal,', 30, 11, 1)
MediumHeal = Healing('Heal', 60, 20, 1)
GreatHeal = Healing('Great Heal', 80, 27, 1)
FromAbove = Healing('From Above', 100, 16, 'all')
heallist_mage = [SmallHeal, MediumHeal, GreatHeal, FromAbove]

actions_warrior = [{'description':'Special Attack', 'action':Const.SPECIALATTACK},
                   {'description':'White damage', 'action':Const.WHITEDMG},
                   {'description':'Regenerate Rage', 'action':Const.REGEN},
                   {'description':'Potions', 'action':Const.POTS}]
actions_fighter = [{'description':'Special Attack', 'action':Const.SPECIALATTACK},
                   {'description':'White damage', 'action':Const.WHITEDMG},
                   {'description':'Regenerate Rage', 'action':Const.REGEN},
                   {'description':'Potions', 'action':Const.POTS}]
actions_mage = [{'description':'Magic', 'action':Const.MAGIC},    # Add debuffs
                {'description':'Regenerate mana', 'action':Const.REGEN},
                {'description':'Potions', 'action':Const.POTS}]
actions_healer = [{'description':'Healing', 'action':Const.HEALING},
                  {'description':'Magic', 'action':Const.MAGIC},   # This would be more fun as buffs
                  {'description':'Regenerate mana', 'action':Const.REGEN},
                  {'description':'Potions', 'action':Const.POTS}]


monsterclasses = ['warrior', 'fighter', 'mage', 'healer']
monsterrace = ['Dark Elf', 'Orc', 'Haunted']


randomname = ['Roch', 'Asa',  # Female healers
              'Kyra', 'Dani', 'Jalen',  # Male healers
              'Adair', 'Barrie', 'Boadicea', 'Gerardine', 'Haralda',  # Female warriors
              'Luella', 'Meave', 'Sloane', 'Trista', 'Xenia', 'Zarya',  # Female warriors
              'Abner', 'Alejandro', 'Andre', 'Alvar', 'Andrian', 'Barack', 'Bearach',  # Male warriors
              'Caballero', 'Caius', 'Charro', 'Donahue', 'Eginhard', 'Gareth', 'Garrick',  # Male warriors
              'George', 'Harlow',  # Male warriors
              'Aoife', 'Ayla', 'Brett', 'Ceridwen', 'Christabel', 'Clelia', 'Consuelo', 'Desdemona',  # Female heroes
              'Gilda', 'Halfrida', 'Hildegard', 'Jemima', 'Leonora', 'Rowena', 'Valkyrie',  # Female heroes
              'Amory', 'Bayard', 'Cedric', 'Cassander', 'Conlan', 'Decatur', 'Egil', 'Einar',  # Male heroes
              'Fearghas', 'Flainn', 'Gwayne', 'Horatius', 'Leandro', 'Roland', 'Sigvard',  # Male heroes
              'Glenda', 'Medea', 'Ursula',  # Witch
              'Merlin', # Wizard
              'Ailsa', 'Albreda', 'Alverdine', 'Elfrida',  # Female elf
              'Elger',  # Male elf
              'Alvis', 'Fafnir']  # Male dwarf