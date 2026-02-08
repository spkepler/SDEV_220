'''
module_2_7_2.py

Steve Kepler
SDEV220
08 February 2026
Loop practice

Input the value 7 into a varible guess_me, and 1 to the variable number.
Create a while loop that compares the two and then increments number each
iteration.  Exit the loop when number exceeds value.
'''

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
    else:
        print("oops")
        break
    number += 1