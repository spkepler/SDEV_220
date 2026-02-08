'''
module_ch_8.py

Steve Kepler
SDEV220
08 February 2026
Chapter 8 Practice Exercises

'''

# 8.4
things = ["mozzarella", "cinderella", "salmonella"]
print(f"{things}\n")

# 8.5
things[1] = things[1].capitalize()
print(f"{things}\n")

#8.6
things[0] = things[0].upper()
print(f"{things}\n")

#8.7
things.pop()
print(f"{things}\n")

#8.10
even = [number for number in range(0, 10, 2)]
print(f"{even}\n")