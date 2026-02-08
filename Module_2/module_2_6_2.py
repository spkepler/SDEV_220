'''
module_2_6_2.py

Steve Kepler
SDEV220
08 February 2026
Conditional practice

User inputs whether something is small and if it is green.  Program
then lists matches to those choices.
'''

small = input("Is it small (Y/N): ")
green = input("Is it green (Y/N): ")

small = small.upper() == "Y"
green = green.upper() == "Y"

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")