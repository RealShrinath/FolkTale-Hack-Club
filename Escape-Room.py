#These plugins are for exiting and delaying text.
#Go ask if its too hard and hints are necessary
#I prob have to be better with github :()

import time 
import sys

hint = 4

print("Welcome to escape room!")

# This is to switch modes for when I decide to add on to this project if I decide to ever do.



while True:
    room = input("What room would you like to escape from? (Jail Cell, Office, Car, or Garage)").strip().lower()
    if room == "jail cell":
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

#quit = "quit"
#sys.exit()

print("You wake up with a sharp pain, laying on a frigid brick floor.  A musty smell of an old basement runs through your nose. You have no idea where you are  or how you got here. As you look around you are filled with a sense of claustrophobia as you feel the tightly spaced walls of a cell. You've never been to prison or broke the law before. You start screaming and shouting and banging on the walls. As the last of your energy is drained in the panic, you sit back down and notice the complete and utter silence. There is noone here to help you. You must save yourself.")
print()

inventory = [""]
# This is to keep track of all the progress they have gotten
step = [""]

# I was stuck on this point for a pretty long time/ was procrastinating this because I wasn't proficient in while loops. I sort of know what to do now.

# Add step 1 for when they 
#inventory.append()

while True:
    print("What would you like to do?")
    Choice_1 = input("Just type: Look up, Look down, Look left, Look right, or look forward to begin. When valid, you may also use the inspect command").lower().strip

    if Choice_1 == "look up":
        print("You look at the tall ceilings, 15 feet above you there is a loose vent. You jump up to check your reach to no avail.")

    elif Choice_1 == "look left":
        print("You look to the left and see a big metal door before you. You don't remember coming through it.")

    elif Choice_1 == "look right":
        print("You look to the right and see a mirror above a sink, and notice a pipe attached to the sink")

    elif Choice_1 == "look forward":
        print("You look in front of you and wonder why the toilet is so close to the bed. You think to yourself atleast there is a pillow")

    elif Choice_1 == "look down":
        print("You look down and see a deteriorating floor made of stone bricks.")

    else:
        print("That is not a valid option. You can either Look in one of the directions,. You may also use an object from your inventory on an item you find. For example, to execute this command, type \"Use ____\"")
        continue

# Why does the continue go inside the else and not outside, doesn't continue apply to this

    Choice_2 = input("What would you like to do?").strip().lower()

    if Choice_1 == "look up" and Choice_2 == "inspect":
            print("The vent is too far away to see clearly, it appears to be loose")

    elif Choice_1 == "look left" and Choice_2 == "inspect":
            print("You take a closer look at the door,  it is four inches of solid metal, probably not going to be your best escape route.")

    elif Choice_1 == "look right" and Choice_2 == "inspect mirror":
        print("Looking in the mirror you realize it has been a while since you last showered. WAIT What's that you see sticking out of the mirror? You pick up a rusty nail file. You begin to start filing your nails to pass the time")
        inventory.append("nail file")
        print("You found a nail file! You can use it when the hint to use the nail file appears in the dialogue")

    elif Choice_1 == "look right" and Choice_2 == "inspect":
        print("You turn the knobs on the sink, no water comes out.")

    elif Choice_1 == "look right" and Choice_2 == "inspect":
        print("There is no waterflow, you wonder why noone maintains these facilities.")

    elif Choice_1 == "look Forward" and Choice_2 == "inspect":
        print("You try to flush the toilet nothing happens.")

    elif Choice_1 == "look Forward" and Choice_2 == "inspect pillow":
        print("You lay on the bed and rest your head on the pillow. oww. there was something sharp in there. You remove the pillow case and find a sharp shiv inside. You think to yourself that you wouldn't want to get caught with this.")
        inventory.append("shiv")
        print("You found a shiv! You can use it when the hint to use the shiv appears in the dialogue")

    elif Choice_1 == "look forward" and Choice_2 == "inspect bed":
        print(" You find a prison outfit under the bed and pick it up. You wonder who's it is")
        inventory.append("prison outfit")
        print("You found a prison outfit. You can use it when the hint to use the prison outfit appears in the dialogue")

    elif Choice_1 == "look down" and Choice_2 == "inspect":
        print("You kneel down and start feeling around the floor for something interesting. You remove a loose brick and to your surprise there is a wrench hidden in there. You decide this could help so you take the wrench and replace the brick.")
        inventory.append("wrench")
        print("You found a wrench. You can use it when the hint to use the wrench appears in the dialogue")

    elif Choice_1 == "look forward" and Choice_2 == "use wrench" and "wrench" in inventory:
        print("You take out you wrench and start turning the nuts holding the pipe. You turn the nuts 4 times to the right. You hear water starting to flow through the pipes again.")
        step.append("1")

    elif Choice_1 == "look forward" and Choice_2 == "throw prison garments in toilet" and "prison outfit" in inventory and 1 in step:
        print("You toss the prisoner outfit in the toilet now it's gross so you just leave it in there")
        step.append("2")

    elif Choice_1 == "look forward" and Choice_2 == "flush toilet" and 1 in step and 2 in step and "shiv" in inventory:
        print("You flush the toilet the prison garments are getting stuck in the toilet bowl and water is starting to fill up  the bowl. You flush it again more and more water begins coming through. It begins to overflow onto the floor something seems to be wrong and the water continues to fill the room until it goes over your head. You start to panic as the water reaches the ceiling. The water level rises until your head hits the vent. You think fast and pull out the shiv you retrieved from earlier and release the vent cover you crawl in and escape through the ventilation system into safety. Congratulations on your escape. It took you x lines to figure out the answer.")
        sys.exit()

    elif Choice_1 == "look forward" and Choice_2 == "flush toilet" and 1 in step and 2 in step and "shiv" in inventory:
        print("You flush the toilet the prison garments are getting stuck in the toilet bowl and water is starting to fill up  the bowl. You flush it again more and more water begins coming through. It begins to overflow onto the floor something seems to be wrong and the water continues to fill the room until it goes over your head. You start to panic as the water reaches the ceiling. The water level rises until your head hits the vent. You think fast and pull out the shiv you didn't retrieve from earlier to open the vent. Oh that's right, you didn't get the shiv 😂😂😂. You feel the water above you nose. You attempt to open the vent with your imagination, but that doesn't seem to work. You drown all alone in an empty,moldy cell. Congratulations on your death 😂😂. It took you __ lines to become a loser. Send back to lobby")
        sys.exit()
    
    elif Choice_1 == "quit" or Choice_2 == "quit":
        print("You want to quit? What a loser! 😂🫵")
        sys.exit()

    elif Choice_1 == "hint" or Choice_2 == "hint" and "wrench" not in inventory and hint >= 1:
        hint = hint - 1
        print(f"Hmmm, if only there was a conveniently placed tool under the floor that could fix the water flow of the toilet 🤔🤔🤔. You have {hint} hints left")
    elif Choice_1 == "hint" or Choice_2 == "hint" and "prison_clothes" not in inventory and hint >= 1:
        hint = hint - 1
        print(f"Hmmm, if only there was a conveniently placed tool under the floor that could fix the water flow of the toilet 🤔🤔🤔. You have {hint} hints left")")
    elif Choice_1 == "hint" or Choice_2 == "hint" and shiv not in inventory and 1 not in step and hint >= 1:
        hint = hint - 1
        print("If only the wrench you have in your pocket could help you escape. 🤔🤔🤔")
        print("Who knows, it might even be helpful to have a conveniently placed sharp object that could help you escape. I'm just saying tho.")
        print(f"You have {hint} hints left")

    elif Choice_1 == "hint" or Choice_2 == "hint" and "shiv" in inventory and 1 not in step and hint >= 1:
        hint = hint - 1 
        print("If only the wrench you have in your pocket could help you escape. 🤔🤔🤔")
        print(f"You have {hint} hints left.")
    
    elif Choice_1 == "hint" or Choice_2 == "hint" and "shiv" not in inventory and 2 not in step and hint >= 1:
        hint = hint - 1
        print("If only you could do something to block the water flow of the toilet. 🤔🤔🤔 ")
        print("Who knows, it might even be helpful to have a conveniently placed sharp object that could help you escape. I'm just saying tho.")

    elif Choice_1 == "hint" or Choice_2 == "hint" and "shiv" in inventory and 2 not in step and hint >= 1:
        hint = hint - 1
        print("If only you could do something to block the water flow of the toilet. 🤔🤔🤔 ")

    elif Choice_1 == "hint" or Choice_2 == "hint" and hint == 0:
        print("You have run out of hint")

    



    else:
        print("That is not a valid option. You can either Look in one of the directions, or inspect an object. You may also use an object from your inventory on an item you find. For example, you can say, \"Use bat on baseball\"")
        continue

# This is where the escape route section actually starts


# Use wrench on pipe
# You take the wrench and begin turning the nuts holding it. You turn the nuts 4 times to the right. You hear water starting to flow through the pipes again.
# Throw prisoner outfit in toilets
# You toss the prisoner outfit in the toilet now it's gross so you just leave it in there
# Flush the Toilet
#  You flush the toilet the prison garments are getting stuck in the toilet bowl and water is starting to fill up  the bowl. You flush it again more and more water begins coming through. It begins to overflow onto the floor something seems to be wrong and the water continues to fill the room until it goes over your head. You start to panic as the water reaches the ceiling. The water level rises until your head hits the vent. You think fast and pull out the shiv you retrieved from earlier and release the vent cover you crawl in and escape through the ventilation system into safety. Congratulations on your escape. It took you x lines to figure out the answer. Send back to lobby
#  You flush the toilet the prison garments are getting stuck in the toilet bowl and water is starting to fill up  the bowl. You flush it again more and more water begins coming through. It begins to overflow onto the floor something seems to be wrong and the water continues to fill the room until it goes over your head. You start to panic as the water reaches the ceiling. The water level rises until your head hits the vent. You think fast and pull out the shiv you didn't retrieve from earlier to open the vent. Oh that's right, you didn't get the shiv 😂😂😂. You feel the water above you nose. You attempt to open the vent with your imagination, but that doesn't seem to work. You drown all alone in an empty,moldy cell. Congratulations on your death 😂😂. It took you __ lines to become a loser. Send back to lobby
