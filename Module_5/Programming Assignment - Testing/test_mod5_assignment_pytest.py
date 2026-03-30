'''
mod5_assignment_pytest.py
SDEV 220 Module 5 Programming Assignment - Testing
29 March, 2026
Steve Kepler
Assignment demonstrating use of pytest
'''

import pytest

# Converts Celcius to Fahrenheit
def convert_c_to_f(c):
    temp_c = c
    temp_f = (c * 1.8) + 32
    return temp_f

def test_integer():
    assert convert_c_to_f(100) == 212
    assert convert_c_to_f(0) == 32

def test_float_output():
    assert convert_c_to_f(26) == 78.8 # Expect possible IEEE 754 rounding error

def test_float_output_with_epsilon():
    epsilon = 0.001
    assert convert_c_to_f(26) - 78.8 < epsilon
    assert convert_c_to_f(-4.2) - 24.44 < epsilon

if __name__ == '__main__':
    test_integer()
    test_float_output()
    test_float_output_with_epsilon()