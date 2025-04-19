"""
Module to determine the resistance value of a resistor based on the colors of the bands.
"""
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

PREFIXES = {
    10**9: "gigaohms",
    10**6: "megaohms",
    10**3: "kiloohms",
    1: "ohms"
}


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
    for divisor, unit in PREFIXES.items():
        if _value >= divisor:
            _value /= divisor
            return f"{int(_value)} {unit}"
        
    return f"{int(_value)} ohms"


def resistor_label(colors):
    """
    A function to determine the resistance value of a resistor based on the colors of the bands.

    params: colors: list[str]: A list of colors representing the bands of the resistor.
    returns: str: The resistance value of the resistor.
    """
    if len(colors) == 1:
        return f"{COLORS.index(colors[0])} ohms"
    if len(colors) == 4: # 3 significant digits and a multiplier
        colors = ['black', *colors]
    if len(colors) != 5: # 3 significant digits, a multiplier, and a tolerance
        raise ValueError("Requires 1, 4, or 5 bands")

    try:
        significant = ''.join(str(COLORS.index(c)) for c in colors[:3]) # First three colors are significant
        value = int(significant) * 10 ** COLORS.index(colors[3]) # Fourth color is the multiplier
        tolerance = TOLERANCES[colors[4]] # Fifth color is the tolerance

    except (ValueError, KeyError) as exc:
        raise ValueError("Invalid color code") from exc

    # Check largest divisors first (giga -> mega -> kilo)
    for divisor, prefix in sorted(PREFIXES.items(), reverse=True):
        if value >= divisor:
            formatted_value = f"{value / divisor:.3g}"  # 3 significant figures
            return f"{formatted_value} {prefix} ±{tolerance}%"
    
    return f"{value:g} ohms ±{tolerance}%"
