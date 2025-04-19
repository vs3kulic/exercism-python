"""
This module implements the Collatz conjecture, which is a sequence defined as follows:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    - Repeat the process until the number reaches 1.

When recursive_steps() returns a value (e.g., counter), 
that value is passed back to the steps() function, which then returns it to the caller.
"""

def steps(number):
    """
    Calculate the number of steps required to reach 1 in the Collatz sequence, 
    starting from a given positive integer.
    
    Args:
        number (int): The starting positive integer for the Collatz sequence.
    Returns:
        int: The number of steps taken to reach 1.
    Raises:
        ValueError: If the input is not a positive integer.
    Example:
        >>> steps(6)
        8
        >>> steps(1)
        0
        >>> steps(16)
        4
        >>> steps(12)
        9
        >>> steps(0)
        Traceback (most recent call last):
            ...
        ValueError: Only positive integers are allowed
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")

    def recursive_steps(num, counter=0):
        """
        Helper function to recursively calculate the number of steps in the Collatz sequence.
        
        Args:
            num (int): The current number in the sequence.
            counter (int): The current step count.
        Returns:
            int: The total number of steps taken to reach 1.
        """
        if num == 1:
            return counter
        if num % 2 == 0:
            return recursive_steps(num // 2, counter + 1)
        else: # if num % 2 == 1:
            return recursive_steps(3 * num + 1, counter + 1)

    return recursive_steps(number)
