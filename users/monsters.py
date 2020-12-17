from users.char import Character
from theworld.map import World


class MonsterCreate:

    @staticmethod
    def monster_choice():
        Goblin = Character('Goblin', hp=100, maxhp=100, mp=5, maxmp=5, atk=20, defence=10, inventory={'Basic Sword': 1},
                           exp=25)
        Ogre = Character('Orge', hp=250, maxhp=250, mp=5, maxmp=5, atk=45, defence=60, inventory={'Skull Splitter': 1},
                         exp=75)
        Cave_Worm = Character('Cave Worm', hp=350, maxhp=350, mp=5, maxmp=5, atk=60, defence=100,
                              inventory={'Potion': 5}, exp=120)
        Spider = Character('Cave Spider', hp=350, maxhp=350, mp=5, maxmp=5, atk=60, defence=100,
                           inventory={'Potion': 5}, exp=120)
        Demon = Character('Demon', hp=500, maxhp=500, mp=5, maxmp=5, atk=120, defence=100, inventory={'Potion': 5},
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

