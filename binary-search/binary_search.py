"""
Binary Search Module.

This module provides an implementation of the binary search algorithm, which is
an efficient method for finding the position of a target value within a sorted list.
"""

def find(search_list, value):
    """
    Perform a binary search to find the index of a value in a sorted (!) list.

    Binary search is an efficient algorithm for finding an item in a sorted list
    by repeatedly dividing the search interval in half.

    Args:
        search_list (list): A sorted list of values to search.
        value (Any): The value to search for in the list.

    Returns:
        int: The index of the value in the list.

    Raises:
        ValueError: If the value is not found in the list.

    Example:
        >>> find([1, 3, 5, 7, 9], 5)
        2
        >>> find([1, 3, 5, 7, 9], 4)
        Traceback (most recent call last):
        ...
        ValueError: value not in array
    """
    if not search_list:
        raise ValueError("value not in array")
    
    lower = 0
    upper = len(search_list) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        mid_value = search_list[mid]

        if mid_value < value:
            lower = mid + 1
        elif mid_value > value:
            upper = mid - 1
        else:
            return mid  # Value found

    raise ValueError("value not in array")  # Value not found