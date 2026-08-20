import random
import sys

# Allpurpose functional entity
# These should be true and consistant for all players, enemies and even npcs
class Entity():
    '''The base function and variables for all entities created.'''

    def __init__(self, stats: dict):
        '''All the variables that make up an entity'''
        self.alive = True
        self.health =stats['health']
        self.mana = stats['mana']
        self.attack_power = stats['attack_power']
        self.magic_power = stats['magic_power']
        self.physical_defense = stats['physical_defense']
        self.magical_resistance = stats['magical_resistance']
        self.attack_speed = stats['attack_speed']
        self.cast_speed = stats['cast_speed']
        self.accuracy = stats['accuracy']
        self.dodge_rate = stats['dodge_rate']
        self.critical_chance = stats['critical_chance']
        self.critical_multiplier = stats['critical_multiplier']

    def damage_application(self, targeted) -> None:
        '''The core method to apply damage from the self->attacker to the targeted->defender'''

        # Runs this function to see if damage should be applied or not.
        hit_success = self.accuracy_check(targeted.dodge_rate)
        if hit_success == True:
            # Very simple damage calculation of subtracting the targets defense from the attacker's attack power
            damage = self.attack_power - targeted.physical_defense
            targeted.health -= damage
            print(f'{self.name.capitalize()} landed a hit on {targeted.name.capitalize()} for {damage} damage.')
            if targeted.health <= 0:
                targeted.death_check()
        elif hit_success == False:
            print(f'{self.name.capitalize()} missed.')

    def death_check(self):
        self.health = 0
        self.alive = False
        if not self.alive:
            print(f'{self.name.capitalize()} died.')
            sys.exit()

    # Used specifically for damage_application() to test the targets dodge against the attackers accuracy
    def accuracy_check(self, target_dodge) -> bool:
        '''Should only really be used in class. Takes the Entity's accuracy and the targets dodge_rate'''

        hit_rate = self.accuracy * 100
        dodge_chance = (target_dodge * 100) // 2 # halves dodge rate as a simple solution to make it harder for mobs that are low level to 100% dodge just because of low accuracy. NEEDS BETTER SOLUTION
        hit_outcome = random.randint(1, int(hit_rate))
        if hit_outcome >= dodge_chance:
            success = True
        elif hit_outcome <= dodge_chance:
            success = False
        return success


class Player(Entity):
    '''Handles the User/Players character creation and management'''
    def __init__(self, name: str, spieces:str, class_role:str, stats: dict):
        self.name = name
        self.class_role = class_role
        self.spieces = spieces
        self.level = 1
        self.main_hand = ''
        self.off_hand = ''
        self.helmet = ''
        self.chest = ''
        self.leggings = ''
        self.boots = ''
        super().__init__(stats)
        self.inventory = []

    def printing_character(self) -> None:
        print(f'Name: {self.name}\nClass: {self.class_role}\nSpieces: {self.spieces}\nLevel: {self.level}')

    # unsure if i need this but to handle gear equipping and make sure everything is where it should be
    def equip_gear(self):
        pass
        
class Enemy(Entity):
    '''Handles the Enemy's creation and management'''
    def __init__(self, name: str, stats: dict):
        self.name = name
        super().__init__(stats)

    def drop_loot(self):
        pass