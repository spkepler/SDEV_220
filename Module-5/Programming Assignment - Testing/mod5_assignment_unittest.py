'''
mod5_assignment_unittest.py
SDEV 220 Module 5 Programming Assignment - Testing
29 March, 2026
Steve Kepler
Assignment demonstrating use of unittest
'''

import unittest

# Converts Celcius to Fahrenheit
def convert_c_to_f(c):
    temp_c = c
    temp_f = (c * 1.8) + 32
    return temp_f

class TestTempConversion(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(convert_c_to_f(100), 212)
        self.assertEqual(convert_c_to_f(0), 32)

    def test_float_output(self):
        self.assertEqual(convert_c_to_f(26), 78.8) # Expect possible IEEE 754 rounding error

    def test_float_output_with_epsilon(self):
        epsilon = 0.001
        self.assertTrue(convert_c_to_f(26) - 78.8 < epsilon)
        self.assertTrue(convert_c_to_f(-4.2) - 24.44 <  epsilon)


if __name__ == '__main__':
    unittest.main(verbosity=2)