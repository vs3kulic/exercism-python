"""This is a pre-solution for the OCR Numbers kata.
It is designed to be used as a starting point for solving the kata."""

# The input is a list of strings, each representing a line of OCR output.
INPUT = [" _ ", # 3 characters wide
         "| |", 
         "|_|",
         "   ", # 4 characters high, the fourth row is always empty
         ]

# The output is a string representing the recognized number.
OUTPUT = "0"

# Requirements for the OCR Numbers kata:
# - The binary font uses pipes and underscores, four rows high and three columns wide.
# - Each digit is represented by a 3x4 grid of characters.
# - The fourth row is always empty.
# - Raise an error if the number of input lines is not a multiple of four (hint: modulo).
# - Raise an error if the number of input columns is not a multiple of three (hint: modulo).
# - Determine the digit it represents by comparing it to a predefined mapping of digits.
# - I'm MATCHING visual patterns to known digits. This is a FINITE, SMALL set of only 10 digits (0-9).

# Solution approach:
# Create a dictionary that maps each digit to its corresponding 3x4 pattern.
# Store all 10 patterns and look them up! Dictionary lookup is O(1) - super fast!
