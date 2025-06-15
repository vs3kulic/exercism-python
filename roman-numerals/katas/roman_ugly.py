"""This module demonstrates a basic implementation of converting integers to Roman numerals.
This iteration passes all tests in the Roman Numerals Kata.
"""
# Map integers to Roman numeral symbols, list of tuples
ROMAN_NUMERALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

def roman_ugly(number):
    """Convert an integer to a Roman numeral using a less efficient method."""
    if number >= 1000:
        return "M" * (number // 1000) + roman_ugly(number % 1000)
    elif number >= 900:
        return "CM" + roman_ugly(number - 900)
    elif number >= 500:
        return "D" + roman_ugly(number - 500)
    elif number >= 400:
        return "CD" + roman_ugly(number - 400)
    elif number >= 100:
        return "C" * (number // 100) + roman_ugly(number % 100)
    elif number >= 90:
        return "XC" + roman_ugly(number - 90)
    elif number >= 50:
        return "L" + roman_ugly(number - 50)
    elif number >= 40:
        return "XL" + roman_ugly(number - 40)
    elif number >= 10:
        return "X" * (number // 10) + roman_ugly(number % 10)
    elif number >= 9:
        return "IX" + roman_ugly(number - 9)
    elif number >= 5:
        return "V" + roman_ugly(number - 5)
    elif number >= 4:
        return "IV" + roman_ugly(number - 4)
    elif number >= 1:
        return "I" * number
    else:
        return ""