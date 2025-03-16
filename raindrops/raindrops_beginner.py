"""
Raindrops Module to convert a number to a string. 
Raindrops is a slightly more complex version of the FizzBuzz challenge. 
"""

def convert(number):
    """
    Convert a number to a string based on its factors.
    Params:
        - number: int
    Returns:
        - "Pling" if divisible by 3
        - "Plang" if divisible by 5
        - "Plong" if divisible by 7
        - A combination of these strings if divisible by multiple factors
        - The number itself as a string if none of the above apply
    """
    a = 3
    b = 5
    c = 7
    
    if number % a == 0 and number % b == 0 and number % c == 0:
        return "PlingPlangPlong"
    if number % a == 0 and number % b == 0:
        return "PlingPlang"
    if number % a == 0 and number % c == 0:
        return "PlingPlong"
    if number % b == 0 and number % c == 0:
        return "PlangPlong"
    if number % a == 0:
        return "Pling"
    if number % b == 0:
        return "Plang"
    if number % c == 0:
        return "Plong"
    
    return str(number)


print (convert(105)) # PlingPlangPlong