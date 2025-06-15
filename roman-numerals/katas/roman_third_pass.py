"""This module demonstrates a basic implementation of converting integers to Roman numerals.
This iteration passes all tests in the Roman Numerals Kata.
"""
# Map integers to Roman numeral symbols, list of tuples
ROMAN_NUMERALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
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
    result = ""
    
    # Process ALL values, don't return early
    for value, numeral in ROMAN_NUMERALS:
        count = number // value  # How many times this value fits
        if count:
            result += numeral * count  # Add all instances of this symbol
            number -= value * count    # Subtract what we used
    return result
