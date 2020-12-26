from users.char import Character, Hero
from assests.items import Potion, Weapon
from theworld.map import World
import json
import os

"Creates assests from json files"


def json_load(filepath, filename):
    with open(f"{filepath}/{filename}.json", "r") as f:
        data = json.load(f)
        f.close()
    print('Loading World assests')
    return data


def create_item(types, name):
    item_data = json_load('assests', 'item')

    item = item_data[types][name]
    for val in item:
        stuff = list(val.values())
        return stuff


def create_hero():
    Hero.name = input("What is thy name hero?\n")
    return Hero.name


# For clearing the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def battle(hero):
    fight = True
    cls()
    monsters = MonsterCreate.monster_choice()
    pot = create_item('Potions', 'Basic Potion')
    pot = Potion(pot[0], pot[1], pot[2], pot[3], pot[4])

    while fight:
        cls()
        hero.stat()
        choice = input("What do you wish to do? Fight: F Potion: P Run: R\n")
        if choice == "F".lower():
            hero.stat()
            if hero.hp <= 0:
                hero.death()
                input("What!!!")
                break
            hero.attack(monsters)
            monsters.stat()
            if monsters.hp <= 0:
                cls()
                monsters.death()
                spoil = monsters.remove_inventory()
                input(f"{monsters.name} dropped {spoil.name}")
                hero.add_inventory(spoil)
                hero.equip_on(hero, spoil)
                hero.gain_exp(monsters)
                World.ig_map[World.userY][World.userX] = "H"
                World.pause_it()
                break
            World.pause_it()
            hero.stat()
            monsters.attack(hero)
            monsters.stat()
            World.pause_it()

        elif choice == "P".lower():
            for item in hero.inventory:
                if item.name == 'Basic Potion':
                    pot.heal_hero(hero)
                    hero.stat()


def pick_item(hero, drop_item):
    if World.ig_map[World.userY][World.userX] == "P":
        choice = input("Do you wish to pick up item? Yes: Y or No: N \n")
        if choice == "Y".lower():
            drop_item.quantity = 5
            hero.add_inventory(drop_item)
            World.ig_map[World.userY][World.userX] = "H"
            print(f"You picked up {drop_item.name} {drop_item.description}")
            World.pause_it()

        if choice == "N".lower():
            print(f"You decide against picking up {drop_item['Basic Potion']}")


class MonsterCreate:

    @staticmethod
    def monster_choice():
        pot = create_item('Potions', 'Basic Potion')
        pot = Potion(pot[0], pot[1], pot[2], pot[3], pot[4])
        pot.quantity = 5
        # ---------[ Weapons for the game ] -------------------------------------------
        basic_sword = create_item('Weapons', 'Basic_Sword')
        basic_sword = Weapon(basic_sword[0], basic_sword[1], basic_sword[2], basic_sword[3])
        skull_splitter = create_item('Weapons', 'Skull_Splitter')
        skull_splitter = Weapon(skull_splitter[0], skull_splitter[1], skull_splitter[2], skull_splitter[3])
        # ------------------------------------------------------------------------------

        Goblin = Character('Goblin', hp=100, maxhp=100, mp=5, maxmp=5, atk=10, defence=10, inventory=basic_sword,
                           exp=25)
        Ogre = Character('Orge', hp=250, maxhp=250, mp=5, maxmp=5, atk=45, defence=60,
                         inventory=skull_splitter,
                         exp=75)
        Cave_Worm = Character('Cave Worm', hp=350, maxhp=350, mp=5, maxmp=5, atk=60, defence=100,
                              inventory=pot, exp=120)
        Spider = Character('Cave Spider', hp=350, maxhp=350, mp=5, maxmp=5, atk=60, defence=100,
                           inventory=pot, exp=120)
        Demon = Character('Demon', hp=500, maxhp=500, mp=5, maxmp=5, atk=120, defence=100, inventory={},
                          exp=500)

        monster = [Goblin, Ogre, Cave_Worm, Spider, Demon]

        if World.ig_map[World.userY][World.userX] == "G":
            return monster[0]

        elif World.ig_map[World.userY][World.userX] == "O":
            return monster[1]

        elif World.ig_map[World.userY][World.userX] == "W":
            return monster[3]

        elif World.ig_map[World.userY][World.userX] == "S":
            return monster[4]

        elif World.ig_map[World.userY][World.userX] == "M":
            return monster[4]
