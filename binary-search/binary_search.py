"""
Binary Search Module.

This module provides an implementation of the binary search algorithm, which is
an efficient method for finding the position of a target value within a sorted list.
"""
from bisect import bisect_left

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

    # by default, lo is set to 0, hi is set to len(list)
    index = bisect_left(search_list, value)
    
    if index != len(search_list) and search_list[index] == value:
        return index
    raise ValueError("value not in array")
