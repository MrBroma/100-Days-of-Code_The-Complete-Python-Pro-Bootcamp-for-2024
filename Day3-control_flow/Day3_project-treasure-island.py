#!/usr/bin/env python3
"""
Project: treasure island project

Author: Loic aka Broma
Contact: 
Version: 1.0.0
Usage: python3 .py
"""

if __name__=="__main__":
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    
    way = input("You are at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n").lower()
    if way == "left":
        swim = input("You come to a lake. There is an island in the middle. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
        if swim == "wait":
            door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue*. Which color do you choose?\n").lower()
            if door == "red":
                print("Burned by fire. Game Over.")
            elif door == "yellow":
                print("You win!")
            elif door == "blue":
                print("Eaten by beasts.Game Over.")
            else:
                print("Game Over.")
        else:
            print("Attacked by trout. Game over.")
    else:
       print("Fall into a hole. Game over")
       
    