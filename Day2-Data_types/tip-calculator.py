# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:00:48 2024

@author: Databroma
"""

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Start of the program

# Welcome message
print("Welcome to the tip calculator!")

# Ask for the total bill
total_bill = float(input("What was the total bill? $"))

# Ask for the tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Ask the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calcul of the total bill

total_to_pay = round(((total_bill * (1 + tip/100)) / people), 2)

print(f"Each person should pay: ${total_to_pay}")

