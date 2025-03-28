"""
A module that generates a diamond shape given a letter.
"""

def rows(letter):
    """
    Generate a diamond shape given a letter.
    
    param letter: a string character    
    return: a list of strings that represent the diamond shape
    """
    letters = [chr(c) for c in range(ord("A"), ord(letter)+1)]
    x_axis = letters[::-1] + letters[1:] # x_axis is the horizontal axis
    y_axis = letters[:-1:] + letters[-1::-1] # y_axis is the vertical axis
    result = ["".join(x if x == y else " " for x in x_axis) for y in y_axis]

    return result
