"""This is a pre-pass for the Change Kata.
It is used to outline the structure of the kata and provide a starting point for implementation."""

# -----------------------------------
# VALIDATIONS
# -----------------------------------
# - ValueError("can't make target with given coins") # target amount is less than the smallest coin
# - ValueError("can't make target with given coins") # less change than target amount
# - ValueError("target can't be negative") # target amount is negative

# -----------------------------------
# INPUT
# -----------------------------------
# The function receives available coins and target amount as parameters
# coins, target ([2, 5, 10, 20, 50], 21)

# -----------------------------------
# OUTPUT
# -----------------------------------
# The function should return a list of coins that make up the target amount
# solution [2, 2, 2, 5, 10]

# -----------------------------------
# REQUIREMENTS / CONSTRAINTS
# -----------------------------------
# each available coin can be used multiple times
# the goal is to return the fewest number of coins possible
