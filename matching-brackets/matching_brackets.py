"""
A module to ensure matching brackets, braces and parentheses 
"""

def is_paired(input_string):
    """
    Function that checks input string for brackets [], braces {}, parentheses ()

    dict pairs: key - opening bracket, value - closing bracket
    list stack: stores opening brackets, pops them when closing bracket is found
    
    param: str - input_string
    returns: boolean - is_paired, True if all items are matching, False if not 
    """
    
    pairs = {'[': ']', '{': '}', '(': ')'}
    stack = []

    for char in input_string:
        if char in pairs:
            stack.append(char)
        if char in pairs.values():
            if not stack or pairs[stack[-1]] != char: # check if stack is empty or if last opening bracket does not match closing bracket
                return False
            stack.pop()
    
    return len(stack) == 0  # final check for unmatched opening brackets
