"""This module demonstrates a basic implementation of converting integers to Roman numerals.
This iteration passes 7/27 tests in the Roman Numerals Kata.
"""
# Map integers to Roman numeral symbols, list of tuples
ROMAN_NUMERALS = [
        (1000, "M"), (900, "CM"), (500, "D"),
        (100, "C"),(400, "CD"), (90, "XC"),
        (50, "L"), (40, "XL"), (10, "X"),
        (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

def roman(number) -> str:
    """Convert an integer to a Roman numeral.
    
    param number: Integer number to convert
    return: str - Roman numeral representation of the number.
    """
    # Add input validation
    if not isinstance(number, int) or not (1 <= number <= 3999):
        return(f'Input must be an integer number between 1 and 3999, got {number}')

    # Look up the number in the main mapping
    for value, numeral in ROMAN_NUMERALS:
        if number == value:
            return numeral
        if number > value:
            result = ""
            while number >= value:
                result += numeral
                number -= value
            return result
    # If no match or number < value, return a message
    return (f"Cannot convert {number} to Roman numeral")
