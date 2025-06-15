"""This module demonstrates a basic implementation of converting integers to Roman numerals.
This iteration passes all tests in the Roman Numerals Kata.
"""
# Map integers to Roman numeral symbols, list of tuples
ROMAN_NUMERALS = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

def roman(number: int) -> str:
    """Convert an integer to a Roman numeral.
    
    param number: Integer number to convert
    return: str - Roman numeral representation of the number.
    """
    # Add input validation
    if not isinstance(number, int) or not (1 <= number <= 3999):
        raise ValueError(f'Input must be an integer number between 1 and 3999, got {number}')

    # Initialise the result string outside the loop
    roman_numeral = ""

    for decimal, numeral in ROMAN_NUMERALS:
        count, number = divmod(number, decimal)  # Get quotient and remainder
        roman_numeral += numeral * count
    return roman_numeral
