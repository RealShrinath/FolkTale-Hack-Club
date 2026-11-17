#These plugins are for exiting and delaying text.

import time 
import sys

print("Welcome to escape room!")

# This is to switch modes for when I decide to add on to this project if I decide to ever do.

while True:
    room = input("What room would you like to escape from? (Jail Cell, Office, Car, or Garage)").strip().lower()
    if room == "Jail Cell":
        print("Are you ready? Then let's start!")
        break
    if room == "office":
        print("Oops! It appears that option isn't available yet.")
        
        continue
    if room == "car":
        print("Oops! It appears that option isn't available yet.")
        continue

    if room == "car":
        print("Oops! It appears that option isn't available yet.")
        continue
    else:
        print("That is not a valid option, please try again")
        continue
print()
print()

quit = "quit"
sys.exit()

print("You wake up with a sharp pain, laying on a frigid brick floor.  A musty smell of an old basement runs through your nose. You have no idea where you are  or how you got here. As you look around you are filled with a sense of claustrophobia as you feel the tightly spaced walls of a cell. You've never been to prison or broke the law before. You start screaming and shouting and banging on the walls. As the last of your energy is drained in the panic, you sit back down and notice the complete and utter silence. There is noone here to help you. You must save yourself.")
print()

inventory = ""


# I was stuck on this point for a pretty long time/ was procrastinating this because I wasn't proficient in while loops. I sort of know what to do now.


while True:
    print("What would you like to do?")
    Choice_1 = input("Just type: Look up, Look down, Look left, Look right, or look forward to begin. When valid, you may also use the inspect command")

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
    print("That is not a valid option. You can either Look in one of the directions, or inspect an object. You may also use an object from your inventory on an item you find. For example, to execute this command, type \"Inspect\"")