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

    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = ""
    
    for key, value in sounds.items():
        if number % key == 0:
            result += value
    
    if result:
        return result
    return str(number)