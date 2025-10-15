"""This module implements a sieve of Eratosthenes algorithm to find all prime numbers up to a given limit."""

def _validate(limit: int) -> list[int] | None:
        # Handle edge cases
    if not isinstance(limit, int) or limit < 0:
        raise ValueError("Limit must be a non-negative integer.")
    if limit < 2:
        return []  # No primes less than 2
    if limit == 2:
        return [2]  # The only prime number is 2
    if limit > 1000:
        raise ValueError("Limit must not exceed 1000.")
    return None

def primes(limit: int) -> list[int]:
    """Return a list of all prime numbers up to the specified limit."""

    # Initialize a boolean array to track prime status of numbers
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    # Implement the Sieve of Eratosthenes
    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]

def main():
    """Main function to demonstrate the primes function."""
    limit = 30
    _validate(limit)
    print(f"Primes up to {limit}: {primes(limit)}")

if __name__ == "__main__":
    main()
