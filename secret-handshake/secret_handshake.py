"""
A module to decode a binary string into a list of secret handshake actions.
In binary, the least significant bit (rightmost bit) represents the smallest value (e.g., 2^0), 
and the most significant bit (leftmost bit) represents the largest value (e.g., 2^4 for a 5-bit binary number).
"""

actions = ["wink", "double blink", "close your eyes", "jump"]

def commands(binary_str):
    """
    Convert a binary string to a list of secret handshake actions.

    param binary_str: A string representing a binary number (e.g., "11001").
    return: A list of actions corresponding to the binary string.
    """
    reversed_binary = binary_str[::-1] # reverse the binary string
    secret_actions = [actions[i] for i, bit in enumerate(reversed_binary) if bit == "1" and i < len(actions)]

    if reversed_binary[4] == "1":
        secret_actions.reverse()

    return secret_actions

print(commands("11111"))  # ['wink', 'double blink', 'close your eyes', 'jump']