"""This module implements a sieve of Eratosthenes algorithm to find all prime numbers up to a given limit."""

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

def main():
    """Main function to demonstrate the primes function."""
    limit = 2
    print(f"Primes up to {limit}: {primes(limit)}")

if __name__ == "__main__":
    main()
