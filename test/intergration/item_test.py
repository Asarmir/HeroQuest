from unittest import TestCase
from unittest.mock import patch

# Import All files for test
from users.char import Character, Hero
from assests.items import Item, Weapon, Potion
from assests.assests import create_item, pick_item
import json

class ItemTest(TestCase):

    def test_equip_on(self):
            """"Setting up character"""
            woodsword = create_item('Weapons', 'Wooden_Sword')
            woodsword = Weapon(woodsword[0], woodsword[1], woodsword[2], woodsword[3])
            hero = Hero(name='Asarmir', hp=100, maxhp=100, mp=1, maxmp=1, atk=10, defence=20, inventory=[], lvl=1, exp=0, maxexp=25, equip=[woodsword])

            """Item I want equip"""
            basic_sword = create_item('Weapons', 'Basic_Sword')
            basic_sword = Weapon(basic_sword[0], basic_sword[1], basic_sword[2], basic_sword[3])
            spoil = basic_sword

            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('y')
                hero.equip_on(hero, spoil)

            self.assertEqual(hero.equip[0], spoil)
           
    def test_useItem(self):

        #Create Hero
        hero = Hero(name='Asarmir', hp=100, maxhp=100, mp=1, maxmp=1, atk=10, defence=20, inventory=[], lvl=1, exp=0, maxexp=25, equip=[])

        #Create Potion
        pot = create_item('Potions', 'Basic Potion')
        pot = Potion(pot[0], pot[1], pot[2], pot[3], pot[4])
        pot.quantity = 5
        
        # Append it to inventory
        hero.inventory.append(pot)

        print(f'Hero hp before using pot: {hero.hp}')
        pot.heal_hero(hero)
        print(f'Hero hp is: {hero.hp}')
        self.assertGreater(hero.hp, 100)
     
        