"""A module to calculate the sum of multiples of given numbers below a specified limit."""

def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Calculate the sum of all the multiples of given numbers below a specified limit.
    
    param: limit: The upper limit (exclusive) for the multiples.
    param: multiples: A list of numbers for which to find multiples.
    return: The sum of all unique multiples of the given numbers below the limit.
    """
    # Validate the input
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer.")
    if not multiples:
        raise ValueError("The list of multiples cannot be empty.")
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers.")
    if not all(isinstance(multiple, int) for multiple in multiples):
        raise ValueError("All multiples must be integers.")

    # Initialize the sum of multiples
    points = 0

    # Calculate the sum of multiples
    for multiple in multiples:
        while points < limit:
            points += multiple

    return points


# Example usage:
if __name__ == "__main__":
    try:
        result = sum_of_multiples(10, [2, 3])
        print(f"The sum of multiples is: {result}")
    except ValueError as e:
        print(f"Error: {e}")