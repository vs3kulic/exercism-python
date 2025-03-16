"""
This module contains a function that takes a year as input and returns True if the year is a leap year, False otherwise.
"""

def leap_year(year):
    """
    This function takes a year as input and returns True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
    return False 