'''
module_3_hwk_ch_12.py

Steve Kepler
SDEV220
22 February 2026
Modules and packages


'''

# Problem 12-1
import zoo
zoo.hours()

# Problem 12-2
import zoo as menagerie
menagerie.hours()

# Problem 12-3
from zoo import hours
hours()

# Problem 12-4
from zoo import hours as info
info()

# Problem 12-5
plain = {'a':1, 'b':2, 'c':3}
for key, value in plain.items():
    print(f"{key}:{value}")

# Problem 12-6
from collections import OrderedDict
fancy = OrderedDict([
    ('a', 1),
    ('b', 2),
    ('c', 3)
])
for key, value in fancy.items():
    print(f"{key}:{value}")

'''
My IDE prints out the same order for both 12-5 and 12-6
'''