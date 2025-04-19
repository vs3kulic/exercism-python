"""
Module containing unit tests for the VLQ encoding and decoding functions.
These tests are auto-generated with following test data: 
[0, 0x40, 0x7F, 0x80, 0x2000, 0x3FFF, 0x4000, 0x100000,
0x1FFFFF, 0x200000, 0x8000000, 0xFFFFFFF, 0x10000000, 0xFF000000, 0xFFFFFFFF]
"""

import unittest
from variable_length_quantity import (
    decode,
    encode,
)

class VariableLengthQuantityTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(encode([0x0]), [0x0])
        self.assertEqual(decode([0x0]), [0x0])
    
    def test_arbitrary_single_byte(self):
        self.assertEqual(encode([0x40]), [0x40])
        self.assertEqual(decode([0x40]), [0x40])

    def test_largest_single_byte(self):
        self.assertEqual(encode([0x7F]), [0x7F])
        self.assertEqual(decode([0x7F]), [0x7F])
    
    def test_smallest_double_byte(self):
        self.assertEqual(encode([0x80]), [0x81, 0x0])
        self.assertEqual(decode([0x81, 0x0]), [0x80])