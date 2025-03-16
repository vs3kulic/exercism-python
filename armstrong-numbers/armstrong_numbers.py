number = 153

def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.

    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(digit) for digit in str(number)]
    armstrong_candidate = 0

    for digit in digits:
        armstrong_candidate += digit ** len(digits)
    if armstrong_candidate == number:
        return True
    else:
        return False

print(is_armstrong_number(number))