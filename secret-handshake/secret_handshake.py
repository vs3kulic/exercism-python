"""
A module to decode a binary string into a list of secret handshake actions.
In binary, the least significant bit (rightmost bit) represents the smallest value (e.g., 2^0), 
and the most significant bit (leftmost bit) represents the largest value (e.g., 2^4 for a 5-bit binary number).
"""
def commands(binary_str) -> list[str]:
    """
    Convert a binary string to a list of secret handshake actions.

    param binary_str: A string representing a binary number (e.g., "11001").
    return: A list of actions corresponding to the binary string.
    """
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = [actions[i] for i, bit in enumerate(binary_str[1:][::-1]) if bit == '1']
    return result if binary_str[0] == '0' else result[::-1]
