"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""
# Constants for the lasagna preparation in minutes
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time

    return remaining_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: int - number of layers in the lasagna.
    :return: int - total preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers in the lasagna as an argument and
    returns how many minutes it would take to prepare the lasagna based on the
    `PREPARATION_TIME`.
    """
    preparation_time = number_of_layers * PREPARATION_TIME

    return preparation_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time.
    
    :param number_of_layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that takes the number of layers in the lasagna and the actual minutes
    the lasagna has been in the oven as arguments and returns the total elapsed time.
    """
    elapsed_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    return elapsed_time
