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

    def __repr__(self):
        return self.name


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
        for item in hero.inventory:
            if item.name == 'Basic Potion' and item.quantity > 0:
                hero.hp = self.heal + hero.hp
                print(f"You slam back a potion like a cold one.\n"
                      f"It heals you for {self.heal}")
                item.quantity -= 1

            elif item.name == 'Basic Potion' and item.quantity == 0:
                print("You reach for a drink but there not a bottle in sight.\n"
                  "You grit your teeth for the beating that coming.")
                break

    def __str__(self):
        return f"=" * 32 + \
               f"\n{self.name:^32}" \
               f"\n" + "=" * 32 + \
               f"\n{self.description}" \
               f"\nValue: {self.value}" \
               f"\nHeal: {self.heal}" \
               f"Quantity: {self.quantity}"

    def __repr__(self):
        return ":".join([self.name, str(self.quantity)])


"""with open('item.json', 'r')as f:
    data = json.load(f)

for item in data["Weapons"]["Basic Sword"]:
    print((item['description']))

for stuff in data["Potions"]["Basic Potion"]:
    print(stuff["heal"])
"""
