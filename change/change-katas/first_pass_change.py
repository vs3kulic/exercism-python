"""This module contains a function to solve the Change Kata.
It finds the fewest number of coins needed to make a given amount of change.

This is the first pass implementation, which uses a greedy approach. Passes 4/13 tests. 
"""

def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Find the fewest number of coins needed to make a given amount of change.
    
    param coins: A list of available coin denominations.
    param target: The target amount of change to make.
    return: A list of coins that make up the target amount.
    
    raises ValueError: If the target amount is negative or cannot be made with the given coins
    """
    # -----------------------------------
    # VALIDATIONS
    # -----------------------------------
    if target < 0:
        raise ValueError("target can't be negative")

    if not coins or target < min(coins):
        raise ValueError("can't make target with given coins")

    # TODO: if target cannot be made with the given coins e.g. ([5, 5, 5], 13):
    #       raise ValueError("can't make target with given coins")
    
    # -----------------------------------
    # CALCULATION
    # -----------------------------------
    change = [] # Initialise the list to hold the coins used for change
    coins.sort(reverse=True)  # Sort coins in descending order for greedy approach
    remaining = target # Initialise remaining amount to target

    for coin in coins:
        while remaining >= coin:
            change.append(coin)
            remaining -= coin

    return change
