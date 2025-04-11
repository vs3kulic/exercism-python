def log2(n):
    """
    Manual calculation of the base-2 logarithm of a number.

    This function calculates the highest power of 2 that is less than or equal to `n`.
    It does this by iteratively increasing the exponent until the result exceeds `n`.

    Args:
        n (int): The number for which to calculate the base-2 logarithm.

    Returns:
        int: The base-2 logarithm of `n`.

    Raises:
        ValueError: If `n` is less than 1.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 0
    
    i = 0

    while (2 ** i) <= n:
        i += 1

    return i - 1 # subtract 1 to get the last valid exponent

def decimal_to_binary_log(n):
    """
    Converts a decimal number to binary using the base-2 logarithm.

    This function iteratively calculates the position of each '1' in the binary representation
    by finding the highest power of 2 that does not exceed the remaining decimal value.
    It then constructs the binary string by prepending '1' and filling in zeros as necessary.

    Args:
        n (int): The decimal number to convert to binary.

    Returns:
        str: The binary representation of `n`.

    Raises:
        No exceptions: The function does not raise exceptions for invalid inputs.
    """
    binary = ''

    while n > 0:
        pos = log2(n) # Get the position of the highest power of 2
        binary = '1' + binary # Prepend '1' to the binary string
        
        for _ in range(pos - len(binary) + 1): 
            binary = '0' + binary # Prepend '0's to the binary string
        
        n -= 2 ** pos # Subtract the value of the highest power of 2 from n
        
    return binary

# Example usage
print(decimal_to_binary_log(24))
