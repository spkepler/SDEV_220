'''
module_GFG_ex1.py

Steve Kepler
SDEV220
22 February 2026
Modules and packages


'''
class Solution:
    def sort012(self, arr):
        zeros = 0
        ones = 0
        twos = 0
        for num in arr:
            match num:
                case 0:
                    zeros += 1
                case 1:
                    ones += 1
                case 2: 
                    twos += 1
        arr.clear() 
        for idx in range(0, zeros):
            arr.append(0)
        for idx in range(0, ones):
            arr.append(1)
        for idx in range(0, twos):
            arr.append(2)
        return arr