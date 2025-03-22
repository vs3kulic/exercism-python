"""
This module contains a function that returns the label of a resistor given its colors.
"""
import math

COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

TOLERANCES = {
    "brown": 1,
    "red": 2,
    "green": 0.5,
    "blue": 0.25,
    "violet": 0.1,
    "grey": 0.05,
    "gold": 5,
    "silver": 10
}

UNITS = ["ohms", "kiloohms", "megaohms"]


def resistor_label(colors: list[str]) -> str:
    """
    Returns the label of a resistor given its colors.

    params: colors: list of strings, each string is a color of the resistor. The first 3 colors
    represent the first 3 digits of the resistor value, the 4th color represents the
    multiplier, and the 5th color represents the tolerance.

    """
    if len(colors) == 1:
        value = COLORS.index(colors[0])
        return f"{value} {UNITS[0]}"

    # If the resistor has 4 colors, the first color is the tolerance
    if len(colors) == 4:
        colors.insert(0, COLORS[0])

    # If the resistor has 5 colors, the first 3 colors are the value, the 4th color is the multiplier, and the 5th color is the tolerance
    if len(colors) == 5:
        value = 0
        acc = 1

        for color in colors[-3::-1]: 
            value += COLORS.index(color) * acc
            acc *= 10
            
        value *= 10 ** COLORS.index(colors[3])

        unit_index = int(math.log10(value) / 3) # math.log10(1000) = 3
        unit = UNITS[unit_index]

        value /= 10 ** (3 * unit_index)

        tolerance = TOLERANCES[colors[4]]

        return f"{value:n} {unit} ±{tolerance:n}%"

    raise ValueError("Unexpected number of colors passed")