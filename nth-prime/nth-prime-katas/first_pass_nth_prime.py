"""This module provides a function to find the nth prime number."""

def primes(limit: int) -> list[int]:
    """Determine the prime numbers up to a given limit.
    
    :param limit: The upper limit (inclusive) to find prime numbers
    :type limit: int
    :returns: A list of prime numbers up to the limit
    :rtype: list[int]
    """
    # Create collections to track non-prime numbers and primes
    not_prime = set()
    is_prime = []

    # Implement the Sieve of Eratosthenes algorithm
    for num in range(2, limit+1):
        if num not in not_prime:
            is_prime.append(num)
            not_prime.update(range(num*num, limit+1, num))
    return is_prime

def prime(number):
    """Return the nth prime number using the Sieve of Eratosthenes.

    :param number: The position of the prime number to find (1-based index)
    :type number: int
    :returns: The nth prime number
    :rtype: int
    """
    # Raise an error for invalid input
    if number == 0:
        raise ValueError("there is no zeroth prime")

    # Quick return for the first prime
    if number == 1:
        return 2

    # Generate primes until we have at least 'number' primes
    limit = 15  # Initial arbitrary limit
    primes_list = []
    while len(primes_list) < number:
        primes_list = primes(limit)
        limit *= 2  # Double the limit and try again if not enough primes found
    return primes_list[number - 1]


def main():
    """Main function to demonstrate the prime function."""
    n = 10001
    print(f"The {n}th prime number is: {prime(n)}")

if __name__ == "__main__":
    main()
