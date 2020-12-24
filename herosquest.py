from assests.assests import *
from assests.items import *
from users.char import Hero




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




def main():
    """item = create_item('Weapons', 'Wooden_Sword')
    Woodswd = Weapon(item[0], item[1], item[2], item[3])
    This is how we create items using the function above.
    """
    # ---------[ Items for the game ]--------------------
    pot = create_item('Potions', 'Basic Potion')
    pot = Potion(pot[0], pot[1], pot[2], pot[3], pot[4])
    basic_sword = create_item('Weapons', 'Basic_Sword')
    basic_sword = Weapon(basic_sword[0], basic_sword[1], basic_sword[2], basic_sword[3])
    # ---------------------------------------------------

    cls()
    title()
    cls()
    create_hero()
    cls()
    hero = Hero(name=Hero.name, hp=100, maxhp=100, mp=1, maxmp=1, atk=160, defence=20, inventory=[], lvl=1, exp=0,
                maxexp=25, equip=[])

    input(f"Welcome {hero.name} to a world of magic.\n"
          f"You have just decided to leave your small town of Falkenville.\n"
          f"You have a can do attitude for fame and fortune.\n"
          f"Flexing your bicep you feel ready to take on any monsters.\n"
          f"Press enter to continue.")

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
        elif World.event == True and World.atk == False:
            pick_item(hero, pot)
        else:
            World.atk = False


if __name__ == "__main__":
    main()
