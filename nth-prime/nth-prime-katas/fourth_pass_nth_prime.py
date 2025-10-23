"""This module provides a function to find the nth prime number using an infinite generator."""
from itertools import count

def primes_generator():
    """Infinitely generate prime numbers using trial division.
    
    :yields: Prime numbers one at a time
    :rtype: Generator[int]
    """
    primes = []
    for n in count(2):
        if all(n % p > 0 for p in primes):
            primes.append(n)
            yield n

def prime(number):
    """Return the nth prime number using an infinite prime generator.
    
    :param number: The position of the prime number to find (1-based index)
    :type number: int
    :returns: The nth prime number
    :rtype: int
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")

    gen = primes_generator()
    for _ in range(number - 1):
        next(gen)
    return next(gen)

def main():
    """Main function to demonstrate the prime function."""
    n = 10001
    print(f"The {n}th prime number is: {prime(n)}")

if __name__ == "__main__":
    main()
