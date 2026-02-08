'''
module_2_7_1.py

Steve Kepler
SDEV220
08 February 2026
Loop practice

Use a for loop to print the values of the list [3, 2, 1, 0]
'''
# using range
for idx in range(3, -1, -1):
    print(idx)


# alternate approach
value_list = [3, 2, 1, 0]
for value in value_list:
    print(value)