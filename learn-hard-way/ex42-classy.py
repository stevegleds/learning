from sys import exit
from random import randint

class Game(object): # always has to have (object) after the name
    
    def __init__(self, start): # always has to have (self) but may also need other parameters
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mum would be proud. If she were smarter.", 
            "Such a loser.",
            "I have a small puppy that's better at this."
        ] # this needs to be under self.quips because really it all fits on one line
        self.start = start
    
    def play(self):
        next = self.start
        
        while True:
            print("\n--------")
            room = getattr(self, next)
            next = room()
            
    def death(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)
    
    def central_corridor(self):
        print("""The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron bomb from the Weapons Armoury, put it in the bridge, and blow the ship up after getting into an "escape pod.\n You're running down the central corridor to the Weapons Armoury when "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume flowing around his hate-filled body. He's blocking he door to the  Armoury and about to pull a weapon to blast you.""")
        
        action = input("What are you going to do? Shoot, dodge or tell a joke? or escape :-) ")
    
        if action == "shoot":
            print("Quick on the draw you yank out your blaster and fire it at the Gothon.")
            print("His clown costume is flowing and moving around his body, which throws")
            print("off your aim. Your laser hits his costume but misses him entirely. The")
            print("completely ruins his brand new costume his mother bought him which")
            print("makes him fly inton an insane rage and blast you repeatedly in the face until")
            print("you are dead. Then he eats you.")
            return 'death'
        
        elif action =="dodge":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out.")
            print("You wake up shortly after only to die as the Gothon stomps on")
            print("your head and eats you")
            return 'death'
            
        elif action == "tell a joke":
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
            print("The Gothon stops, tries not to laugh, then bursts out laughing")
            print("While he's laughing you run up and shoot him square in the head")
            print("putting him down, then jump through the Weapoin Armoury door.")
            return 'laser_weapon_armoury'
        
        elif action == "escape":
            return 'escape_pod'
        
        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
    
    def laser_weapon_armoury(self):
        print("""You do a dive roll into the Weapon Armoury, crouch and scan the room for more Gothons that might be hiding. It's dead quiet, too quiet. You stand up and run to the far side of a room and find the  neutron bomb in its container. There's a keypad lock on the box and you need te code to get the bomb out. If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits.""")
        code = "{}{}{}" .format(randint(1,9), randint(1,9), randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses <10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[kepad]> ")
        
        if guess == code:
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot.")
            return 'the_bridge'
        
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sounds as the mechanism is fused together.")
            print("You decide to sit there, and finally the Gothons blow up the ")
            print("ship from their shop and you die.")
            cheat = input("Do you want to cheat? y/n ")
            if cheat == 'y' or cheat == 'Y':
                return 'the_bridge'
            else:
                return 'death'
        
    def the_bridge(self):
        print("You burst onto the bridge with neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their weapons out yet, as they see the active bomb under your arm and don't want to set it off.")
            
        action = input("What do you do now? throw or place the bomb? ")
            
        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a ")
            print("Gothon shoots you right in the back killing you.")
            print("As you die, you see another Gothon frantically try to disarm ")
            print("the bomb. You die knowing they will probably blow up when ")
            print("it goes off.")
            return 'death'
            
        elif action == "place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the Gothons can't get out.")
            print("Now that the bomb is placed you run to the escape pod to ")
            print("get off this tin can.")
            return 'escape_pod'
            
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

    def escape_pod():
        print("You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and  now need to pick one to take. Some of them could be damaged but you don't have time to look. There's 5 pods, which one do you take?")
        
        good_pod = randint(1,5)
        guess = input("[pod #] > ")
        
        if int(guess) != good_pod:
            print("You jump into pod {} and hit the eject button." .format(guess))
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return 'death'
            
        else: 
            print("You jump into pod {} and hit the eject button." .format(guess))
            print("The pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look ")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the Gothon ship at the same")
            print("time. You woni!")
            exit(0)

a_game = Game("central_corridor")
a_game.play()            