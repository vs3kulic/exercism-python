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
    # --------------------------------------------
    # INPUT VALIDATIONS
    # --------------------------------------------
    if target < 0:
        raise ValueError("target can't be negative")
    
    if target == 0:
        return []  # Edge case: no coins needed for 0
    
    if not coins:
        raise ValueError("can't make target with given coins")

    # ----------------------------------------
    # DYNAMIC PROGRAMMING CALCULATION
    # ----------------------------------------
    # Create DP table
    dp = [0] + [float('inf')] * target # Unpacking with Concatenation, starting with infinity

    # Fill the DP table
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                coins_with_this_option = dp[amount - coin] + 1 # +1 for using this coin
                dp[amount] = min(dp[amount], coins_with_this_option) # Update if fewer coins found

    # ----------------------------------------
    # VALIDATION - CHECK IF SOLUTION EXISTS
    # ----------------------------------------
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # -----------------------------------------
    # RECONSTRUCTION OF THE COINS USED
    # -----------------------------------------
    change = []
    remaining = target # Amount remaining to be made with coins

    while remaining > 0:
        for coin in coins:
            if (coin <= remaining and 
                dp[remaining - coin] == dp[remaining] - 1):
                change.append(coin)
                remaining -= coin
                break

    change.sort(reverse=True)

    return change
