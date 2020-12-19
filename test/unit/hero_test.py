from unittest import TestCase
from users.char import Character
from users.char import Hero

class CharacterTest(TestCase):
    def test_create_monster(self):
        monster = Character('Goblin', 100, 100, 5, 5, 20, 10, {'dagger': 1}, 25)

        self.assertEqual('Goblin', monster.name)
        self.assertEqual(100, monster.hp)
        self.assertEqual(100, monster.maxhp)
        self.assertEqual(5, monster.mp)
        self.assertEqual(5, monster.maxmp)
        self.assertEqual(20, monster.atk)
        self.assertEqual(10, monster.defence)
        self.assertDictEqual({'dagger': 1}, monster.inventory)

    def test_create_hero(self):
        hero = Hero('Asarmir', 12, 12, 1, 1, 5, 10, {}, 1, 0, 25, [])

        self.assertEqual('Asarmir', hero.name)
        self.assertEqual(12, hero.hp)
        self.assertEqual(12, hero.maxhp)
        self.assertEqual(1, hero.mp)
        self.assertEqual(1, hero.maxmp)
        self.assertEqual(5, hero.atk)
        self.assertEqual(10, hero.defence)
        self.assertDictEqual({}, hero.inventory)
        self.assertEqual(1, hero.lvl)
        self.assertEqual(0, hero.exp)
        self.assertEqual(25, hero.maxexp)
        self.assertEqual([], hero.equip)
