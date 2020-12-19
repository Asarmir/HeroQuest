"""
    Character Class is the base class and used to create monsters.
    Also could add a skill class so monsters could hit harder.
"""


class Character:

    def __init__(self, name, hp, maxhp, mp, maxmp, atk, defence, inventory, exp):
        self.name = name

        # Health point if 0 your dead
        self.hp = hp
        self.maxhp = maxhp

        # magic points
        self.mp = mp
        self.maxmp = maxmp

        # Attack is the amount of damage objet can deal
        self.atk = atk

        # Defense blunts Attacks
        self.defence = defence

        # easier to pop from monster inventory to hero's
        self.inventory = inventory

        # monster need exp to give to hero's
        self.exp = exp

    def remove_inventory(self):
        drop_item = self.inventory.popitem()
        return drop_item

    def attack(self, target):
        if target.defence > self.atk:
            self.atk = 0
            target.defence = 0
        target.hp = target.hp - self.atk + target.defence
        dmg = abs(target.defence - self.atk)

        print(f"\n{self.name} hits {target.name} for {dmg} \n")

    def death(self):
        if self.hp <= 0:
            print(f'{self.name} has died')

    def stat(self):
        print('\n')
        print(f"{'Menu':=^32}")
        print(f'Name: {self.name}' + f"{f'Atk: {self.atk}':>12} Def: {self.defence}")
        print('=' * 32)
        print(f"Hp: {self.hp}/{self.maxhp}" + f'{f"Mp: {self.mp}/{self.maxmp}":>19}')
        print('=' * 32)

    def __str__(self):
        return (f"{self.name}, {self.hp}, {self.maxhp}, {self.mp}, {self.maxmp}, {self.atk}, {self.defence}, {self.inventory}, {self.exp}")

"""
    This creates the hero. Adding class with starter skills could an idea or a skill class.
"""


class Hero(Character):

    def __init__(self, name, hp, maxhp, mp, maxmp, atk, defence, inventory, lvl, exp, maxexp, equip):
        Character.__init__(self, name, hp, maxhp, mp, maxmp, atk, defence, inventory, exp)

        self.lvl = lvl

        # Numbers that symbolize when to level up
        self.maxexp = maxexp

        # Holds players items equip is item in hand
        self.equip = equip

    def add_inventory(self,drop_item):
        self.inventory.append(drop_item)

    def equip_on(self):
        print("Do you wish to equip this item?")
        

    def run_away(self):
        pass

    def gain_exp(self, target):

        self.exp = self.exp + target.exp

        if self.exp >= self.maxexp:
            self.lvl = self.lvl + 1
            self.maxexp = self.maxexp * 2
            self.exp = self.exp = 0
            print(f'\nYou have LEVELed UP! You are now {self.lvl}')
        else:
            print(f'\nYou recieved {target.exp} exp')

    def stats_up(self):
        self.hp = self.hp * 2
        self.max = self.hp * 2
        self.mp = self.mp * 2
        self.maxmp = self.maxmp *2
        self.atk = self.atk * 2
        self.defence = self.defence * 2
        print(f"Your health is now: {self.hp}/{self.maxhp}"
              f"Your Mana pool is now: {self.mp}/{self.maxmp}"
              f"Your Attack is now: {self.atk}"
              f"Your Defense is now: {self.defence}")

    def stat(self):

        print('\n')
        print(f"{'Menu':=^32}")
        print(f'Name: {self.name:15} / Lvl: {self.lvl}')
        print('=' * 32)
        print(f"{f'Hp: {self.hp}/{self.maxhp}':>15}" + " " * 5 + f'Mp: {self.mp}/{self.maxmp}')
        print('=' * 32)
        print(f'Atk: {self.atk}  Def: {self.defence}' + ' ' * 5 + f'| Exp: {self.exp}/{self.maxexp}')
        print('=' * 32)
        print(f"{f'Equipment: {self.equip}':^32}")
        print('=' * 32)


"""hero = Hero(name='Asarmir', hp=12, maxhp=12, mp=1, maxmp=1, atk=5, defence=10, inventory={None}, lvl=1, exp=0,maxexp= 25, equip={'Wooden Sword': 5})
monster = Character('Goblin', 100, 100, 5, 5, 20, 10, {'dagger': 1}, exp=25)

hero.stat()
hero.attack(monster)
monster.stat()"""