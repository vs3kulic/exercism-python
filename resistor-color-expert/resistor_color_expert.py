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
    Takes list of color names and returns the resistor value.

    param: color names as str, limited to two colors e.g. ["brown", "black"] 
    return: int value of the resistor band, concatenated from the color codes
    """
    if len(colors) != 2:
        raise ValueError("Exactly two colors are required.")

    duo_codes = [color_code(color) for color in colors[0:2:1]] # list comprehension, iterating over the first two elements of the list
    duo_code = int(''.join(map(str, duo_codes))) # map() function returns a map object (-> iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

    return duo_code

def label(colors):
    """
    Returns the label of the resistor value.

    param: color names as str, limited to three colors e.g. ["brown", "black", "red"]
    return: str label of the resistor value
    """
    multiplier = 10 ** color_code(colors[2])
    _value = value(colors[:2]) * multiplier

    # check if the value is in the range of the resistor value
    unit_dict = {
        1e9: "gigaohms",
        1e6: "megaohms",
        1e3: "kiloohms",
        1: "ohms"
    }

    for divisor, unit in unit_dict.items():
        if _value >= divisor:
            _value /= divisor
            return f"{int(_value)} {unit}"
        
    return f"{int(_value)} ohms"


def resistor_label(colors):
    """
    Returns the label of the resistor value and tolerance.

    param: color names as str, limited to five colors e.g. ["brown", "black", "red", "gold", "green"]
    return: str label of the resistor value and tolerance
    """
    tolerance_dict = {
        "silver": 10,
        "gold": 5,
        "brown": 1,
        "red": 2,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "grey": 0.05,
    }
