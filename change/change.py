"""This module contains a function to solve the Change Kata.
It finds the fewest number of coins needed to make a given amount of change.

This is the fourth pass implementation, using dynamic programming. Passes all tests.
"""
def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Find the fewest number of coins needed to make a given amount of change.
    
    param coins: A list of available coin denominations.
    param target: The target amount of change to make.
    return: A list of coins that make up the target amount.
    raises ValueError: If the target amount is negative or cannot be made with the given coins
    """
    # Handle edge case early
    if target == 0:
        return []
    
    # Validate inputs
    _validate_inputs(coins, target)
    
    # Build DP table
    dp = _build_dp_table(coins, target)
    
    # Validate solution exists
    _validate_solution_exists(dp, target)
    
    # Reconstruct and return solution
    return _reconstruct_solution(coins, target, dp)


def _validate_inputs(coins: list[int], target: int) -> None:
    """Validate input parameters and raise appropriate errors."""
    if target < 0:
        raise ValueError("target can't be negative")
    
    if not coins:
        raise ValueError("can't make target with given coins")


def _build_dp_table(coins: list[int], target: int) -> list[int]:
    """Build and fill the DP table with minimum coins needed for each amount.
    
    param coins: A list of available coin denominations.
    param target: The target amount of change to make.
    return: A list where the index represents the amount and the value is the minimum coins needed
    """
    # Use a large number instead of float('inf')
    overflow = target + 1  # Larger than any possible solution
    dp = [0] + [overflow] * target
    
    # Fill the DP table
    for amount in range(1, target + 1):
        for coin in coins:
            if coin <= amount:
                coins_with_this_option = dp[amount - coin] + 1
                dp[amount] = min(dp[amount], coins_with_this_option)
    
    return dp


def _validate_solution_exists(dp: list[int], target: int) -> None:
    """Check if a solution was found after DP calculation."""
    overflow = target + 1
    if dp[target] == overflow:  # Changed from float('inf')
        raise ValueError("can't make target with given coins")


def _reconstruct_solution(coins: list[int], target: int, dp: list[int]) -> list[int]:
    """Reconstruct which coins were used to make the target amount from the DP table."""
    change = []
    remaining = target
    
    while remaining > 0:
        for coin in coins:
            if (coin <= remaining and dp[remaining - coin] == dp[remaining] - 1):
                change.append(coin)
                remaining -= coin
                break
    
    return sorted(change, reverse=False)
