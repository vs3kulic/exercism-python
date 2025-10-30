"""This module provides a function to find the nth prime number."""
from math import log

# Global constant - PNT not accurate for small n
SMALL_LIMITS = {1: 2, 2: 5, 3: 10, 4: 15, 5: 15}

def _primes(limit: int) -> list[int]:
    """Determine the prime numbers up to a given limit.
    
    :param limit: The upper limit (inclusive) to find prime numbers
    :type limit: int
    :returns: A list of prime numbers up to the limit
    :rtype: list[int]
    """
    # Create collections to track non-prime numbers and primes
    is_prime = []
    not_prime = set()

    # Implement the Sieve of Eratosthenes algorithm
    for num in range(2, limit + 1):
        if num not in not_prime:
            is_prime.append(num)
            not_prime.update(range(num * num, limit + 1, num))

    return is_prime

def _limit_estimate(n: int) -> int:
    """Estimate an upper limit to find at least n prime numbers,
    using the prime number theorem (PNT).
    
    :param n: The number of primes needed
    :type n: int
    :returns: An estimated upper limit for at least n primes
    :rtype: int
    """
    # For small n, return a safe constant limit
    if n in SMALL_LIMITS:
        return SMALL_LIMITS[n]

    # Use the PNT for estimation, for p(n) ~ n(ln(n) + ln(ln(n)))
    estimate = int(n * (log(n) + log(log(n))))

    return estimate

def prime(number):
    """Return the nth prime number.

    :param number: The position of the prime number to find (1-based index)
    :type number: int
    :returns: The nth prime number
    :rtype: int
    """
    # Raise an error for invalid input
    if number < 1:
        raise ValueError("there is no zeroth prime")

    # Generate primes until we have at least 'number' primes
    limit = _limit_estimate(number)
    primes_list = _primes(limit)

    return primes_list[number - 1]


def main():
    """Main function to demonstrate the prime function."""
    n = 1000001
    print(f"The {n}th prime number is: {prime(n)}")

if __name__ == "__main__":
    main()
