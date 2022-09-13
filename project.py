# Dice roll Generator Project
import random

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Dice rolling....")
    print("The value is...")
    # randomly generated value of the first dice 
    print(random.randint(min_val,max_val))
    # randomly egenrated value for the second dice 
    print(random.randint(min_val,max_val))
    #Here the user enters yes or y to continue and any other input ends the program
    roll_again = input("roll the dice again?")
