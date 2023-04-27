import random


class Pokemon:

    def __init__(self, attack_choice):

        self.__attack_choice = attack_choice

    def attack(self):

        if self.__attack_choice == 1:
            attack_points = random.randint(18, 25)
            return attack_points

        elif self.__attack_choice == 2:
            attack_points = random.randint(10, 35)
            return attack_points

        else:
            print("That is not a selection. You lost your turn!")

    def heal(self):

        heal_points = random.randint(18, 25)
        return heal_points


user_health = 100
benoit_health = 100
battle_continue = True

while battle_continue == True:
    print("\nATTACK CHOICES\n1. Close range attack\n2. Far range attack\n3. Heal")
    attack_choice = eval(input("\nSelect an attack: "))

    if benoit_health == 100:
        benoit_choice = random.randint(1, 2)

    else:
        benoit_choice = random.randint(1, 3)

    benoit = Pokemon(benoit_choice)
    user_pokemon = Pokemon(attack_choice)

    if attack_choice == 1 or attack_choice == 2:
        damage_to_benoit = user_pokemon.attack()
        heal_self = 0
        print("You dealt", damage_to_benoit, "damage.")

    if benoit_choice == 1 or benoit_choice == 2:
        damage_to_user = benoit.attack()
        heal_benoit = 0
        print("Benoit dealt", damage_to_user, "damage.")

    if attack_choice == 3:
        heal_self = user_pokemon.heal()
        damage_to_benoit = 0
        print("You healed", heal_self, "health points.")

    if benoit_choice == 3:
        heal_mew = benoit.heal()
        damage_to_user = 0
        print("Benoit healed", heal_benoit, "health points.")

    user_health = user_health - damage_to_user + heal_self
    benoit_health = benoit_health - damage_to_benoit + heal_benoit

    if user_health > 100:
        user_health = 100

    elif user_health <= 0:
        user_health = 0
        battle_continue = False

    if benoit_health > 100:
        benoit_health = 100

    elif benoit_health <= 0:
        benoit_health = 0
        battle_continue = False

    print("Your current health is", user_health)
    print("Benoit's current health is", benoit_health)

print("Your final health is", user_health)
print("Benoit's final health is", benoit_health)

if user_health < benoit_health:

    print("\nYou lost! Better luck next time!")

else:

    print("\nYou won against Benoit!")
