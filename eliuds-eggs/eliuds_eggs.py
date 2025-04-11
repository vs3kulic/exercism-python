"""
A simple module to count the number of eggs in a carton. 

The module takes a decimal display value and converts it to a binary value, 
which is then used to count the number of eggs (represented by 1 bits) in a carton. 
"""

def egg_count(display_value):
    """
    Converts a decimal display value to a binary value and counts the number of eggs (1 bits) in a carton.

    The % 2 operation isolates the least significant bit (LSB) of the binary representation.
    The // 2 operation shifts the binary representation to the right by one bit.
    By repeating these steps, the function processes all bits in the binary representation and counts the 1 bits.

    Args:
        display_value (int): The decimal display value to be converted.
    Returns:
        int: The number of eggs in the carton.
    Example:
        >>> egg_count(0)
        0
        >>> egg_count(16)
        1
        >>> egg_count(89)
        4
        >>> egg_count(2000000000)
        13
    """
    count = 0

    while display_value > 0:
        # check if the last bit is 1 (odd number)
        if display_value % 2 == 1:
            count += 1
        display_value //= 2 # remove the last bit with an int division by 2

    return count
