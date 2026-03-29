'''
test_sum1.py
SDEV 220 Module 5 Programming Assignment - Testing
29 March, 2026
Steve Kepler
This is an introduction to automated Python testing
'''

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")