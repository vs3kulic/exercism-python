"""A module to calculate the difference of squares."""

def square_of_sum(number: int) -> int:
    """Calculate the square of the sum of the first `number` natural numbers.
    
    param: number (int): The upper limit of the natural numbers to consider.
    return: int: The square of the the sum.
    """
    validate_input(number)
    square_sum = sum(_number for _number in range(1, number + 1)) ** 2

    return square_sum


def sum_of_squares(number: int) -> int:
    """Calculate the sum of the square of the first `number` natural numbers.
    
    param: number (int): The upper limit of the natural numbers to consider.
    return: int: The sum of the squares.
    """
    validate_input(number)
    sum_squares = sum(_number ** 2 for _number in range(1, number + 1))

    return sum_squares


def difference_of_squares(number: int) -> int:
    """Compute the difference between the square of the sum and the sum of the squares."""
    validate_input(number)
    squares_difference = square_of_sum(number) - sum_of_squares(number)

    return squares_difference


# Helper function to validate the input
def validate_input(number: int) -> None:
    """Validate the input number."""
    if not isinstance(number, int) or number < 0:
        raise ValueError('Input must be a non-negative integer.')


# Example usage:
if __name__ == "__main__":
    number = 5
    print(f"Square of sum for first {number} natural numbers: {square_of_sum(number)}")
    print(f"Sum of squares for first {number} natural numbers: {sum_of_squares(number)}")
    print(f"Difference of squares for first {number} natural numbers: {difference_of_squares(number)}")