"""
A module for the Resistor Color exercise.
"""

COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def color_code(color):
    """
    Returns the numerical value of a resistor color band.

    param color: str
    return: int
    """
    code = COLORS.index(color)

    return code


def colors():
    """
    Returns the list of all resistor color bands.

    param: None
    return: list
    """

    return COLORS
