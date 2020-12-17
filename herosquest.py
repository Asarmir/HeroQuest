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

def act():
    choice = input("Enter F: Fight or R: Run:\n")
    if choice == "R".lower():
        print("You haul tail and run away! No one has to know!")
        if World.hold == True:
            World.ig_map[World.org][World.userX] = "H"
        elif World.hold == False:
            World.ig_map[World.userY][World.org] = "H"
    else:
        battle()


def battle():
    fight = True
    monsters = MonsterCreate.monster_choice()
    cls()


    input(f"You decided to stand your ground like a man.\n"
          f"{monsters.name} looks you in the face and snarls.\n"
          f"the battle is on.\n"
          f"Press enter to continue")

    while fight:
        cls()
        choice = input("What do you wish to do? Fight: F Potion: P Run: R\n")
        if choice == F.lower():
            Hero.stat(Hero)
            print(f"{Hero.name} hits {monster.name} for {Hero.attack(hero, monster)}")
            monsters.stat(monsters)
            if monsters.death(monsters):
                break
                Hero.gain_exp(hero, monster)
            else:
                continue
            cls()
            monsters.stat(Monsters)
            print(f"{monsters.name} really didn't like that."
                  f"so {monsters.name} hits you for {monsters.attack(monsters, hero)}")
            Hero.stat(Hero)
            if Hero.death(Hero):
                break
            else:
                continue
        elif choice == P.lower():
            print(f"You drink a potion.")
            Potion.heal_hero(Potion, Hero)


def main():
    cls()
    title()
    cls()
    create_hero()
    cls()
    hero = Hero(Hero.name, 12, 12, 1, 1, 5, 10, {}, 1, 0, 25, {})

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
        if World.event == True:
            act()


if __name__ == "__main__":
    main()
