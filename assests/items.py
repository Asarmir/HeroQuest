import json


class Item:

    # Base Class for all items
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return f"=" * 32 + \
               f"\n{self.name:^32}" \
               f"\n" + "=" * 32 + \
               f"\n{self.description}\nValue: {self.value}\n"


class Weapon(Item):
    def __init__(self, name, description, value, atk):
        self.atk = atk
        Item.__init__(self, name, description, value)

    def __str__(self):
        return f"=" * 32 + \
               f"\n{self.name:^32}" \
               f"\n" + "=" * 32 + \
               f"\n{self.description}" \
               f"\nValue: {self.value}" \
               f"\nDamage: {self.atk}"


class Potion(Item):
    def __init__(self, name, description, value, heal, quantity):
        self.quantity = quantity
        self.heal = heal
        Item.__init__(self, name, description, value)

    def heal_hero(self, hero):
        hero.hp = self.heal + hero.hp

    def __str__(self):
        return f"=" * 32 + \
               f"\n{self.name:^32}" \
               f"\n" + "=" * 32 + \
               f"\n{self.description}" \
               f"\nValue: {self.value}" \
               f"\nDamage: {self.heal}"


"""with open('item.json', 'r')as f:
    data = json.load(f)

for item in data["Weapons"]["Basic Sword"]:
    print((item['description']))

for stuff in data["Potions"]["Basic Potion"]:
    print(stuff["heal"])
"""
