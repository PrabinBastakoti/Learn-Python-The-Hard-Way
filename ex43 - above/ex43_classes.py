
from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while True:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        


class Death(Scene):
    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud... if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
                The Gothons of Planet Percal #25 have invaded your ship and
                destroyed your entire crew. You are the last surviving
                member and your last mission is to get the neutron destruct
                bomb from the Weapons Armory, put it in the bridge, and
                blow the ship up after getting into an escape pod.
                
                You're running down the central corridor to the Weapons
                Armory when a Gothon jumps out, red scaly skin, dark grimy
                teeth, and evil clown costume flowing around his hate
                filled body. He's blocking the door to the Armory and
                about to pull a weapon to blast you.
                """))
        
        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                23 it at the Gothon. His clown costume is flowing and
                24 moving around his body, which throws off your aim.
                25 Your laser hits his costume but misses him entirely.
                26 This completely ruins his brand new costume his mother
                27 bought him, which makes him fly into an insane rage
                28 and blast you repeatedly in the face until you are
                29 dead. Then he eats you.
                """))
            return 'death'
        elif action == 'dodge!':
            print(dedent("""
                Like a world class boxer you dodge, weave, slip and
                36 slide right as the Gothon's blaster cranks a laser
                37 past your head. In the middle of your artful dodge
                38 your foot slips and you bang your head on the metal
                39 wall and pass out. You wake up shortly after only to
                40 die as the Gothon stomps on your head and eats you.
                """))
            return 'death'
        
        elif action == "tell a joke":
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                47 the academy. You tell the one Gothon joke you know:
                48 Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                49 fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                50 not to laugh, then busts out laughing and can't move.
                51 While he's laughing you run up and shoot him square in
                52 the head putting him down, then jump through the
                53 Weapon Armory door.
                """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                You do a dive roll into the Weapon Armory, crouch and scan
                6 the room for more Gothons that might be hiding. It's dead
                7 quiet, too quiet. You stand up and run to the far side of
                8 the room and find the neutron bomb in its container.
                9 There's a keypad lock on the box and you need the code to
                10 get the bomb out. If you get the code wrong 10 times then
                11 the lock closes forever and you can't get the bomb. The
                12 code is 3 digits.
                """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0 

        while guess != code and guesses <10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input ("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                27 gas out. You grab the neutron bomb and run as fast as
                28 you can to the bridge where you must place it in the
                29 right spot.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                35 sickening melting sound as the mechanism is fused
                36 together. You decide to sit there, and finally the
                37 Gothons blow up the ship from their ship and you die.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
                You burst onto the Bridge with the netron destruct bomb
                48 under your arm and surprise 5 Gothons who are trying to
                49 take control of the ship. Each of them has an even uglier
                50 clown costume than the last. They haven't pulled their
                51 weapons out yet, as they see the active bomb under your
                52 arm and don't want to set it off.
                """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb at the group of Gothons
                60 and make a leap for the door. Right as you drop it a
                61 Gothon shoots you right in the back killing you. As
                62 you die you see another Gothon frantically try to
                63 disarm the bomb. You die knowing they will probably
                64 blow up when it goes off.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You point your blaster at the bomb under your arm and
                71 the Gothons put their hands up and start to sweat.
                72 You inch backward to the door, open it, and then
                73 carefully place the bomb on the floor, pointing your
                74 blaster at it. You then jump back through the door,
                75 punch the close button and blast the lock so the
                76 Gothons can't get out. Now that the bomb is placed
                77 you run to the escape pod to get off this tin can.
                """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return "the_bridge"



class EscapePod(Scene):
    def enter(self):
        print(dedent("""
                You rush through the ship desperately trying to make it to
                91 the escape pod before the whole ship explodes. It seems
                92 like hardly any Gothons are on the ship, so your run is
                93 clear of interference. You get to the chamber with the
                94 escape pods, and now need to pick one to take. Some of
                95 them could be damaged but you don't have time to look.
                96 There's 5 pods, which one do you take?
                """))  
        good_pod = randint(1,5)
        guess = input("[pod #1]> ")

        if int(guess) != good_pod:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                106 The pod escapes out into the void of space, then
                107 implodes as the hull ruptures, crushing your body into
                108 jam jelly.
                """))
            return 'death'

        else:
            print(dedent("""
                You jump into pod {guess} and hit the eject button.
                114 The pod easily slides out into space heading to the
                115 planet below. As it flies to the planet, you look
                116 back and see your ship implode then explode like a
                117 bright star, taking out the Gothon ship at the same
                118 time. You won!
                """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")

        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'death': Death(),
        'finished': Finished()
        }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('Central Corridor')
a_game = Engine(a_map)
a_game.play()
