class World:
    ig_map = [
##### X   0    1    2    3    4    5    6    7    8    9  #### Y
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 0
        ['-', 'B', '-', '-', '-', '-', '-', '-', '-', '-'],  # 1
        ['-', 'M', '-', '-', 'W', '-', '-', '-', '-', '-'],  # 2
        ['-', ' ', '-', '-', ' ', '-', '-', '-', '-', '-'],  # 3
        ['-', ' ', '-', '-', ' ', '-', '-', '-', '-', '-'],  # 4
        ['-', ' ', '-', '-', ' ', '-', '-', '-', '-', '-'],  # 5
        ['-', ' ', '-', '-', ' ', '-', '-', '-', '-', '-'],  # 6
        ['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'S', '-'],  # 7
        ['-', '-', '-', '-', ' ', '-', '-', '-', '-', '-'],  # 8
        ['-', '-', '-', '-', 'C', '-', '-', '-', '-', '-'],  # 9
        ['-', ' ', ' ', ' ', 'T', ' ', ' ', '-', '-', '-'],  # 10
        ['-', ' ', '-', '-', '-', '-', ' ', '-', '-', '-'],  # 11
        ['-', ' ', '-', '-', '-', '-', ' ', '-', '-', '-'],  # 12
        ['-', ' ', '-', '-', 'R', '-', ' ', '-', '-', '-'],  # 13
        ['-', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', '-'],  # 14
        ['-', '-', ' ', '-', ' ', '-', ' ', '-', '-', '-'],  # 15
        ['-', ' ', 'O', '-', ' ', '-', ' ', '-', 'P', '-'],  # 16
        ['-', 'P', '-', '-', 'F', '-', ' ', ' ', 'G', '-'],  # 17
        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 18
    ]

    userY = 17
    userX = 4

    org = None
    event = False
    atk = True
    setuser = None

    ### Creates the map and has to be redraw with the updated position of the hero. ###
    @staticmethod
    def draw_map():

        for row in World.ig_map:
            for col in row:
                print(col, end=" ")
            print()

        print("Instruction")
        print('UP: W | Down: S | Left: A | Right: D')
        print('R: Rock | P: Pots | F: Falkner Village')

    #### This takes the hero location and puts an 'H' on the position of the hero. ###
    @staticmethod
    def hero_location():
        if World.ig_map[World.userY][World.userX] == " ":
            World.ig_map[World.userY][World.userX] = "H"
            World.event = False
        elif World.ig_map[World.userY][World.userX] == "-":
            World.ig_map[World.userY][World.userX] = "-"
            if World.setuser == "userY":
                World.userY = World.org
            else:
                World.userX = World.org
            World.ig_map[World.userY][World.userX] = "H"
            print("\nI can't move here!\n")
            World.atk = False
            World.pause_it()

        else:
            World.event = True
            World.actions()

    #### Takes input from the user and moves the hero icon. ########
    @staticmethod
    def input_dir():

        direction = input("Where do wish to move:")

        ##### Move up ############
        if direction == "W".lower():
            World.ig_map[World.userY][World.userX] = " "
            World.userY -= 1
            World.org = World.userY + 1
            World.setuser = "userY"


        ###### Move Down ###############
        elif direction == "S".lower():
            World.ig_map[World.userY][World.userX] = " "
            World.userY += 1
            World.org = World.userY - 1
            World.setuser = "userY"

        ######## Move Left #############
        elif direction == "A".lower():
            World.ig_map[World.userY][World.userX] = " "
            World.userX -= 1
            World.org = World.userX + 1
            World.setuser = "userX"

        ######## Move Right #############
        elif direction == "D".lower():
            World.ig_map[World.userY][World.userX] = " "
            World.userX += 1
            World.org = World.userX - 1
            World.setuser = "userX"

    @staticmethod
    def actions():

        if World.ig_map[World.userY][World.userX] == "R":
            print("\nThere is a huge boulder in the way. You whistle has you walk off to a new direction.")
            World.userY += 1
            World.ig_map[World.userY][World.userX] = "H"
            World.atk = False
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "C":
            print("You enter the nastiest smelling cave ever."
                  "You really want to back out but every hero needs a intro story."
                  "So you press forward holding your nose as danger allows.")
            World.atk = False
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "W":
            print("You see a gaint cave worm pop out of a hole in the ground."
                  "You swear it was Petey your pet worm from your childhood."
                  "To bad this worm is coming in for the kill."
                  "FIGHT!")
            World.atk = True
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "M":
            print("A demon with a chain around it neck grins so big the shiver ran up and down your spine twice."
                  "'This has got to be the best day of my life' the demon laughs."
                  "'I can use you as my new host to leave this stupid cave"
                  " or the boy in the back' the demon chuckles."
                  "'Either way I will walk out of here a free demon.'"
                  "You smile point your sword at the demon then give him the bird with your other hand."
                  "Sadly to your dismay the demon responses. "
                  "'Oh you are to kind I almost done want to kill you now.'"
                  "You smack your head duh he's evil that wouldn't bother him."
                  "FIGHT!")
            World.atk = True
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "B":
            print("See a young teenager pass out on the ground."
                  "You kick him with your foot and he stirs."
                  "He wakes up and cries thanking you for saving his life."
                  "You request that all he has to do to repay you is tell everyone what happen."
                  "The boy agreed and ran off to tell everyone in the village."
                  "Now you got your first title. HERO! and your quest has just begun.")
            World.atk = False
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "O":
            print("You see a Ogre sitting by a fire BBQing a corpse. "
                  "You decide to come out laughing to see if you can scare the beast."
                  " It glares at you annoyingly making your smile even bolder. FIGHT!!")
            World.atk = True
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "P":
            print("Your grin couldn't be bigger. You hit the jack pot. You found 5 health potions.")
            World.atk = False
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "T":
            print("You see Olson's twin girls in front of the cave. "
                  "They are crying and shaking so you ask them what's up."
                  "They tell you the sad story about their brother being dragged into the cave."
                  "So you decide to go in and recuse him.")
            World.atk = False
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "G":
            print("\nA goblin jumps out from behind the brush. "
                  "You got a fight on your hands and your ready to show your stuff!\n")
            World.atk = True
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "S":
            print("You just met the biggest spider of you life!"
                  " You wanted to call it fido."
                  " But it did not take kindly to that name. It attacks you!")
            World.atk = True
            World.pause_it()

        elif World.ig_map[World.userY][World.userX] == "T":
            print("You see Olson's twin girls in front of the cave. "
                  "They are crying and shaking so you ask them what's up."
                  "They tell you the sad story about their brother being dragged into the cave."
                  "So you decide to go in and recuse him.")
            World.atk = False
            World.pause_it()

    @staticmethod
    def pause_it():
        input("Press ENTER to continue.")
