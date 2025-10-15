"""This module holds the pre-pass version of the sieve of Eratosthenes algorithm."""

# --------------------
# INPUT
# --------------------
# The function we implement takes a single integer input `limit`

# --------------------
# VALIDATION
# --------------------
# We don't perform validation in this version

# --------------------
# ALGORITHM
# --------------------
# We will implement the Sieve of Eratosthenes algorithm to find all prime numbers
# up to the specified limit.
# We create two collections:
#   - set `not_prime` to keep track of numbers that are identified as not prime
#   - list `is_prime` to store the prime numbers we find
# We iterate through numbers starting from 2 up to the limit, using the range function.
#   - by starting from 2, we skip 0 and 1 which are not prime numbers
# For each number, if it is not in the `not_prime` set, we consider it a prime number
# and add it to the `is_prime` list, using the append method.
#   - the append method adds the prime number to the end of the list
# We then mark all multiples of this prime number as not prime by adding them to the `not_prime` set
# using the update method with a range that starts from the square of the prime number
# and goes up to the limit, with a step equal to the prime number.
#   - starting from the square of the prime number is an optimization, as all smaller multiples
#     will have already been marked by smaller prime factors
#   - the range function generates multiples of the prime number starting from its square

# --------------------
# OUTPUT
# --------------------
# The function will return a list of all prime numbers up to the specified limit.
