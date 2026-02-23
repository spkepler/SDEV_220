'''
module_GFG_ex2.py

Steve Kepler
SDEV220
22 February 2026
Modules and packages


'''

class Solution:
    def binarysearch(self, arr, k):
        min_idx = 0
        max_idx = len(arr)-1
        
        check = lambda x, k: "High" if x > k else "Low" if x < k else "Equal"
        
        while min_idx <= max_idx:
            mid_idx = (min_idx + max_idx) // 2
            match check(arr[mid_idx], k):
                case "Low":
                    min_idx = mid_idx + 1
                case "High":
                    max_idx = mid_idx - 1
                case "Equal":
                    return mid_idx
                
        return -1