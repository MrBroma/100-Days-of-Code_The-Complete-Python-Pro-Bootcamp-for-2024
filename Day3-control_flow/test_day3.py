# -*- coding: utf-8 -*-
"""
Broma script python
Day3

"""

height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height > 120:
    print("You can ride the rollercoaster.")
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $11.")
else:
    print("You can't ride the rollercoaster.")