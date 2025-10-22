"""This module provides a function to find the nth prime number."""

def prime(number):
    """Return the nth prime number using a basic trial division method.
    
    :param number: The position of the prime number to find (1-based index)
    :type number: int
    :returns: The nth prime number
    :rtype: int
    """
    if number < 1:
        raise ValueError('there is no zeroth prime')
    n = 2
    primes = [2]
    while len(primes) < number:
        n += 1
        if all(n % p > 0 for p in primes):
            primes.append(n)

    return primes[number - 1]

def main():
    """Main function to demonstrate the prime function."""
    n = 10001
    print(f"The {n}th prime number is: {prime(n)}")

if __name__ == "__main__":
    main()
