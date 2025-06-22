"""A module to calculate the sum of multiples of given numbers below a specified limit.
This passes 13/16 unit tests, but fails 3 tests related to the validation of inputs.
"""

def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    """Calculate the sum of all the multiples of given numbers below a specified limit.
    
    param: limit: The upper limit (exclusive) for the multiples.
    param: multiples: A list of numbers for which to find multiples.
    return: The sum of all unique multiples of the given numbers below the limit.
    """
    # Validate the input
    validate_input(limit, multiples)

    # Calculate the unique multiples
    unique_multiples = calculate_unique_multiples(limit, multiples)
    
    # Sum the unique multiples
    points = sum_unique_multiples(limit, unique_multiples)

    return points


# Helper functions
def validate_input(limit: int, multiples: list[int]) -> None:
    """Validate the input parameters for the sum_of_multiples function.
    
    param: limit: The upper limit (exclusive) for the multiples.
    param: multiples: A list of numbers for which to find multiples.
    raise: ValueError if the input is invalid.
    """
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer.")
    if not multiples:
        raise ValueError("The list of multiples cannot be empty.")
    if any(multiple <= 0 for multiple in multiples):
        raise ValueError("All multiples must be positive integers.")
    if not all(isinstance(multiple, int) for multiple in multiples):
        raise ValueError("All multiples must be integers.")


def calculate_unique_multiples(limit: int, multiples: list[int]) -> set[int]:
    """Calculate the unique multiples of given numbers below a specified limit.
    
    param: limit: The upper limit (exclusive) for the multiples.
    param: multiples: A list of numbers for which to find multiples.
    return: A set of unique multiples of the given numbers below the limit.
    """
    # Initialize a set to store unique multiples
    unique_multiples = set()
    
    # Calculate multiples for each number in the list
    for multiple in multiples:
        for i in range(1, (limit // multiple) + 1):
            unique_multiples.add(multiple * i)

    return unique_multiples


def sum_unique_multiples(limit: int, unique_multiples: set[int]) -> int:
    """Calculate the sum of all the multiples of given numbers below a specified limit.
    
    param: limit: The upper limit (exclusive) for the multiples.
    param: multiples: A set of numbers for which to find multiples.
    return: The sum of all unique multiples of the given numbers below the limit.
    """
    # Initialize the sum of multiples
    points = 0

    # Sum the unique multiples
    for multiple in unique_multiples:
        if multiple < limit:
            points += multiple

    return points


# Example usage:
if __name__ == "__main__":
    try:
        result = sum_of_multiples(10, [2, 3])
        print(f"The sum of multiples is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
