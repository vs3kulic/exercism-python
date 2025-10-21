"""This module provides a function to find the nth prime number."""

def prime(number):
    """Return the nth prime number.

    :param number: The position of the prime number to find (1-based index)
    :type number: int
    :returns: The nth prime number
    :rtype: int
    """
    # Raise an error for invalid input
    if number == 0:
        raise ValueError("there is no zeroth prime")

    # TODO: Implement generator for primes
    # TODO: Store primes in hash map for quick lookup
    # TODO: Return the nth one


def main():
    """Main function to demonstrate the prime function."""
    n = 0
    print(f"The {n}th prime number is: {prime(n)}")

if __name__ == "__main__":
    main()
