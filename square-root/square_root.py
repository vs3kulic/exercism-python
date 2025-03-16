"""
This module contains a function to calculate the square root of a number
"""

def square_root(number):
    """
    Function to calculate the square root of a number using Newton's method
    param number: int - number to calculate the square root, positive integer
    return: float - square root of the number, with a tolerance of 1e-10
    """
    est = number / 2 # initial estimate
    tolerance = 1e-10
    
    while abs(est * est - number) > tolerance:
        est = (est + number / est) / 2
    return int(est)