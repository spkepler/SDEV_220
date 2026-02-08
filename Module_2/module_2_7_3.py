'''
module_2_7_3.py

Steve Kepler
SDEV220
08 February 2026
Loop practice

Input the value 5 into a varible guess_me, then use a for loop to 
iterate a variable number over range(10)
'''

guess_me = 5

for number in range(10):
    if number < guess_me:
        print("too low")
    elif number > guess_me:
        print("too high")
        break
    else:
        print("found it!")
        break
