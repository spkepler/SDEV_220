'''
test_sum_unittest.py
SDEV 220 Module 5 Programming Assignment - Testing
29 March, 2026
Steve Kepler
This is an introduction to automated Python testing using unittest
'''

import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == "__main__":
    unittest.main()