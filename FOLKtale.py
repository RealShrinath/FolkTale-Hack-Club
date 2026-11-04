# Make sure you make it title thing and nstrigged

# 8:45 start

import time 
import sys

print("Welcome to escape room!")

while True:
    room = input("What room would you like to escape from? (Jail Cell, Office, Car, or Garage)")
    if room == "Jail Cell":
        print("Are you ready? Then let's start!")
        break
    if room == "Office" or "Car" or "Garage":
        print("Oops! It appears that option isn't available yet.")
        continue
    else:
        print("That is not a valid option, please try again")
print()
print()

quit = "quit"
continue

print("You wake up with a sharp pain, laying on a frigid brick floor.  A musty smell of an old basement runs through your nose. You have no idea where you are  or how you got here. As you look around you are filled with a sense of claustrophobia as you feel the tightly spaced walls of a cell. You've never been to prison or broke the law before. You start screaming and shouting and banging on the walls. As the last of your energy is drained in the panic, you sit back down and notice the complete and utter silence. There is noone here to help you. You must save yourself.")
print()

print("What would you like to do?")
Choice_1 = input("Just type: Look up, Look down, Look left, Look right, or look forward to begin. When valid, you may also use the inspect command")

# 8:50 break

inventory = ""

if Choice_1 == "Look up":
    print("You look at the tall ceilings, 15 feet above you there is a loose vent. You jump up to check your reach to no avail.")
elif Choice_1 == "Look left":
    print("You look to the left and see a big metal door before you. You don't remember coming through it.")
elif Choice_1 == "Look right":
    print("You look to the right and see a mirror above a sink, and notice a pipe attached to the sink")
elif Choice_1 == "Look forward":
    print("You look in front of you and wonder why the toilet is so close to the bed. You think to yourself atleast there is a pillow")
elif Choice_1 == "Look down":
    print("You look down and see a deteriorating floor made of stone bricks.")
else:
    print("That is not a valid option. You can either Look in one of the directions, or inspect an object. You may also use an object from your inventory on an item you find. For example, you can say, \"Use bat on baseball\"")

Choice_2 = input("What would you like to do?")

if Choice_2 == "Look up":
    print("You look at the tall ceilings, 15 feet above you there is a loose vent. You jump up to check your reach to no avail.")
elif Choice_2 == "Look left":
    print("You look to the left and see a big metal door before you. You don't remember coming through it.")
elif Choice_2 == "Look right":
    print("You look to the right and see a mirror above a sink, and notice a pipe attached to the sink")
elif Choice_2 == "Look forward":
    print("You look in front of you and wonder why the toilet is so close to the bed. You think to yourself atleast there is a pillow")
elif Choice_2 == "Look down":
    print("You look down and see a deteriorating floor made of stone bricks.")
else:
    print("That is not a valid option. You can either Look in one of the directions, or inspect an object. You may also use an object from your inventory on an item you find. For example, you can say, \"Use bat on baseball\"")

if Choice_1 == "Look up" and Choice_2 == "Inspect vent":
    print("The vent is too far away to see clearly, it appears to be loose")
if Choice_1 == "Look left" and Choice_2 == "Inspect door":
    print("You take a closer look at the door,  it is four inches of solid metal, probably not going to be your best escape route.")
if Choice_1 == "Look right" and Choice_2 == "Inspect mirror":
    print("Looking in the mirror you realize it has been a while since you last showered. WAIT What's that you see sticking out of the mirror? You pick up a rusty nail file. You begin to start filing your nails to pass the time")
if Choice_1 == "Look right" and Choice_2 == "Inspect sink":
    print("You turn the knobs on the sink, no water comes out.")
if Choice_1 == "Look right" and Choice_2 == "Inspect pipe":
    print("There is no waterflow you wonder why noone maintains these facilities.")
if Choice_1 == "Look Forward" and Choice_2 == "Inspect toilet":
    print("You try to flush the toilet nothing happens.")
if Choice_1 == "Look Forward" and Choice_2 == "Inspect pillow":
    print("You lay on the bed and rest your head on the pillow. oww. there was something sharp in there. You remove the pillow case and find a sharp shive inside. You think to yourself that you wouldn't want to get caught with this.")
if Choice_1 == "Look Forward" and Choice_2 == "Inspect bed":
    print(" You find a prison outfit under the bed and pick it up. You wonder who's it is")
if Choice_1 == "Look down" and Choice_2 == "Inspect floor":
    print("You kneel down and start feeling around the floor for something interesting. You remove a loose brick and to your surprise there is a wrench hidden in there. You decide this could help so you take the wrench and replace the brick.")
    inventory = inventory + "shiv"


#maybe use choice and keep replacing it instead of choice numbered
# After this point, This project has been scrapped, and all new code will be in the escape room file. I didn't want to have to account for every player action so I used a different approach