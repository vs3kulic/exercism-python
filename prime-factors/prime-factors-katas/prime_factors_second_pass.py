"""This module provides the functionality to compute prime factors of a number."""

def factors(value: int) -> list[int]:
    """Return the prime factors of the given natural number.
    :param value: The natural number to factor
    :type value: int
    :returns: A list of prime factors
    :rtype: list[int]
    """
    if value < 2:
        return []

    prime_factors = []
    divisor = 2

    while value > 1:
        if value % divisor == 0:
            value //= divisor
            prime_factors.append(divisor)
        else:
            divisor += 1

    return prime_factors

def main():
    """Main function to demonstrate the factors function."""
    number = 73
    print(f"The prime factors of {number} are: {factors(number)}")

if __name__ == "__main__":
    main()
