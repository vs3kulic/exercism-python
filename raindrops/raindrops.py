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

    # Dictionary of factors and their corresponding sounds
    factor_sounds = {3: "Pling", 5: "Plang", 7: "Plong"} 
    
    # Generator expression to get the sound of the factors by iterating through the dictionary as tuples
    result = (sound for factor, sound in factor_sounds.items() if number % factor == 0)

    # Join the sounds if any, else return the number
    return "".join(result) or str(number)