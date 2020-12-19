# Python Packages
import os

from assests.items import *
### Game files that need to be imported ###
from users.char import *
from theworld.map import World
from users.monsters import MonsterCreate


def json_load(filepath, filename):
    with open(f"{filepath}/{filename}.json", "r") as f:
        data = json.load(f)
        f.close()
    print('Loading World assests')
    return data


def create_item():
    item_data = json_load('assests', 'item')
    return item_data
    """for item in item_data["Weapons"]["Basic_Sword"]:
        print(item['description'])"""


def title():
    while True:
        print(f"{'':=^32}\n"
              f"{'Heros Quest':^32}\n"
              f"{'':=^32}")

        print(f"\n{'Menu':^20}\n"
              f"{f'':-<20}\n"
              f"\n1: New game\n"
              f"2: Exit program\n"
              f"\n{'':=^32}\n")

        answer = int(input("Please type 1 or 2: \n"))
        if answer == 1:
            break
            cls()
            create_hero()

        elif answer == 2:
            print("\nThank you for playing\n")
            break


def create_hero():
    Hero.name = input("What is thy name hero?\n")
    return Hero.name


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def battle(hero):
    fight = True
    cls()
    monsters = MonsterCreate.monster_choice()

    while fight:
        cls()
        choice = input("What do you wish to do? Fight: F Potion: P Run: R\n")
        if choice == "F".lower():
            hero.stat()
            if hero.hp <= 0:
                hero.death()
                break
            hero.attack(monsters)
            monsters.stat()
            if monsters.hp <= 0:
                monsters.death()
                hero.gain_exp(monsters)
                World.ig_map[World.userY][World.userX] = "H"
                input("Press enter to continue")
                break

            else:
                cls()

                input(f"{monsters.name} growls and lashes out.")
                hero.stat()
                monsters.attack(hero)
                monsters.stat()


        elif choice == "P".lower():
            print(f"You drink a potion.")
            Potion.heal_hero(Potion, Hero)
        else:
            continue

"""def adventure(hero):"""


def main():
    cls()
    title()
    cls()
    create_hero()
    cls()
    hero = Hero(name=Hero.name, hp=12, maxhp=12, mp=1, maxmp=1, atk=80, defence=10, inventory=[], lvl=1, exp=0,maxexp= 25, equip={})

    input(f"Welcome {hero.name} to a world of magic.\n"
          f"You have just decided to leave your small town of Falkenville.\n"
          f"You have a can do attitude for fame and fortune.\n"
          f"Flexing your bicep you feel ready to take on any monsters.\n"
          f"Press enter to continue.")
    """Map loop"""
    cls()
    moving = True
    World.hero_location()
    while moving:
        cls()
        World.draw_map()
        World.input_dir()
        World.hero_location()
        if World.event and World.atk == True:
            battle(hero)




if __name__ == "__main__":
    main()
