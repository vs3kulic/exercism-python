"""
Functions for calculating grains on a chessboard.
"""

def square(number):
    """
    Calculate the number of grains on a specific square of a chessboard.
    
    param number: int - the square number on a chessboard (1 to 64)
    :return: int - the number of grains on that square
    """
    # Raise an error if the number is not in the valid range
    if (number < 1) or (number > 64):
        raise ValueError("square must be between 1 and 64")

    # Calculate the number of grains on the given square
    grains_on_square = 2 ** (number - 1)

    return grains_on_square

def total():
    """
    Calculate the total number of grains on a chessboard.
    
    param: None
    :return: int - total number of grains on the chessboard
    """
    # Calculate the total number of grains on the chessboard
    # Sum of powers of 2, from 2^0 to 2^63
    total_grains = (2 ** 64) - 1
    
    return total_grains
