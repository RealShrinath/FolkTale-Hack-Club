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