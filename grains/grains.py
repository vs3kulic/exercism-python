def square(number):
    """
    Calculate the number of grains on a given square of a chessboard.

    Each square number has double the grains of the previous square, starting with 1 grain on the first square.

    Args:
        number (int): The square number (must be between 1 and 64).

    Returns:
        int: The number of grains on the specified square.

    Raises:
        ValueError: If the square number is not between 1 and 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)

print(square(5))

def total():
    """
    Calculate the total number of grains on all squares of a chessboard.

    The total is the sum of grains on all 64 squares, where each square has double the grains of the previous square.

    Returns:
        int: The total number of grains on the chessboard.
    """
    return (2 ** 64) - 1 #sum of powers of 2 from 2^0 to 2^63 is equal to 2^64 - 1

print(total())