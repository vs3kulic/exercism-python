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
    # VALIDATIONS (Keep your perfect validation!)
    # -----------------------------------
    if target < 0:
        raise ValueError("target can't be negative")
    
    if target == 0:
        return []  # Edge case: no coins needed for 0
    
    if not coins:
        raise ValueError("can't make target with given coins")

    # -----------------------------------
    # DP CALCULATION (Replace greedy with DP)
    # -----------------------------------
    
    # Create DP table using list repetition
    dp = [float('inf')] * (target + 1)  # Start with "infinity" for all amounts
    dp[0] = 0  # set base case: 0 coins needed for amount 0
    
    # Step 2: Fill the DP table
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:  # Can we use this coin?
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # Step 3: Check if solution exists
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")
    
    # Step 4: Reconstruct the actual coins used
    change = []
    remaining = target
    
    while remaining > 0:
        # Find which coin was used for this amount
        for coin in coins:
            if (coin <= remaining and 
                dp[remaining - coin] == dp[remaining] - 1):
                change.append(coin)
                remaining -= coin
                break
    
    # Step 5: Sort to match expected format (largest first)
    change.sort(reverse=True)
    return change
