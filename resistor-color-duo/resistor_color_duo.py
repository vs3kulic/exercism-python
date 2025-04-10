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


def value(colors):
    """
    Calculates resistor value from two color bands.

    Args:
        colors (list[str]): Two color names from the resistor color code set
        (e.g., ["brown", "red"]).

    Returns:
        int: Combined numerical value of the first two bands.

    Raises:
        ValueError: If input isn't exactly two colors or contains invalid names.
    """
    if len(colors) != 2:
        raise ValueError("Exactly two colors required. Example: ['brown', 'black']")

    duo_codes = [color_code(color) for color in colors]
    duo_code = int(''.join(map(str, duo_codes)))

    return duo_code
