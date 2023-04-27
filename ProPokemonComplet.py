import json

class Pokemon:

    def __init__(self, name, type, attack_power=0, defense=0, health=100, level=1):
        self.__name = name
        self.type = type
        self.attack_power = attack_power
        self.defense = defense
        self.__health = health
        self.level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def set_health(self, health):
        self.__health = health

    def print_info(self):
        print("Name:", self.__name)
        print("Health:", self.__health)
        print("Defense:", self.defense)
        print("Attack power:", self.attack_power)


class Normal(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Normal", attack_power, defense, health, level)
        self.defense += 10
        self.attack_power += 5

class Fire(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Fire", attack_power, defense, health, level)
        self.defense -= 5
        self.attack_power += 10

class Water(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Water", attack_power, defense, health, level)
        self.defense += 5
        self.attack_power -= 5

class Electric(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Electric", attack_power, defense, health, level)
        self.defense -= 12
        self.attack_power += 15

class Grass(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Grass", attack_power, defense, health, level)
        self.defense -= 4
        self.attack_power += 8

class Ice(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Ice", attack_power, defense, health, level)
        self.defense += 16
        self.attack_power -= 14

class Fighting(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Fighting", attack_power, defense, health, level)
        self.defense -= 9
        self.attack_power += 9

class Poison(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Poison", attack_power, defense, health, level)
        self.defense -= 6
        self.attack_power += 22

class Ground(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Ground", attack_power, defense, health, level)
        self.defense += 15
        self.attack_power -= 10

class Flying(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Flying", attack_power, defense, health, level)
        self.defense -= 7
        self.attack_power += 7

class Psychic(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Psychic", attack_power, defense, health, level)
        self.defense += 21
        self.attack_power -= 14

class Bug(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Bug", attack_power, defense, health, level)
        self.defense -= 8
        self.attack_power += 7

class Rock(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Rock", attack_power, defense, health, level)
        self.defense += 20
        self.attack_power -= 18

class Ghost(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Ghost", attack_power, defense, health, level)
        self.defense -= 11
        self.attack_power += 11

class Dragon(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Dragon", attack_power, defense, health, level)
        self.defense += 24
        self.attack_power += 26

class Dark(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Dark", attack_power, defense, health, level)
        self.defense -= 6
        self.attack_power += 5

class Steel(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Steel", attack_power, defense, health, level)
        self.defense += 19
        self.attack_power += 17

class Fairy(Pokemon):
    def __init__(self, name, attack_power=0, defense=0, health=100, level=1):
        super().__init__(name, "Fairy", attack_power, defense, health, level)
        self.defense -= 8
        self.attack_power += 4


import random


class Combat:

    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def is_alive(self, pokemon):
        return pokemon.get_health() > 0

    def get_winner(self):
        if not self.is_alive(self.pokemon1):
            return self.pokemon2.get_name()
        elif not self.is_alive(self.pokemon2):
            return self.pokemon1.get_name()
        else:
            return None

    def attack(self, pokemon_attacker, pokemon_defender):
        if random.randint(0, 1) == 1:
            attack_power = pokemon_attacker.attack_power * self.get_attack_multiplier(pokemon_attacker,
                                                                                      pokemon_defender)
            damage = attack_power - pokemon_defender.defense
            if damage < 0:
                damage = 0
            new_health = pokemon_defender.get_health() - damage
            pokemon_defender.set_health(new_health)
            print(pokemon_attacker.get_name(), "attacks", pokemon_defender.get_name(), "for", damage,"damage")
