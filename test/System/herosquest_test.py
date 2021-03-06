from unittest import TestCase
from unittest.mock import patch

from assests.assests import *
from assests.items import *
from users.char import *
from herosquest import title


class Test_Heroquest(TestCase):

    def test_Title(self):
        
        EndGame = '\nThank you for playing\n'

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('1')
            title()

        self.assertTrue(create_hero, True)

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('2')
            with patch('builtins.print') as mocked_print:
                title()

                mocked_print.assert_called_with(EndGame)

    def test_create_hero(self):
        expected = 'Asarmir'

        with patch('builtins.input', return_value='Asarmir') as mocked_input:
            create_hero()
            hero = Hero(name=Hero.name, hp=100, maxhp=100, mp=1, maxmp=1, atk=10, defence=20, inventory=[], lvl=1, exp=0,
                maxexp=25, equip=[])
        
        self.assertEqual(hero.name, expected)
            

        