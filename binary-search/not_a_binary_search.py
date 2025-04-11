"""
Linear Search Module.

This module provides an implementation of a linear search algorithm, which is
a simple method for finding the position of a target value within a list.
"""

def find(search_list, value):
    """
    Performs a linear search to find the index of a value in a sorted list, 
    by checking each element in the list sequentially until the desired value is found 
    or the list is exhausted.

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
    try:
        # Validate input types
        if not isinstance(search_list, list):
            raise TypeError("search_list must be a list")
        if not all(isinstance(i, (int, float)) for i in search_list):
            raise TypeError("search_list must contain only numbers")
        if not isinstance(value, (int, float)):
            raise TypeError("value must be a number")

        # Validate list properties
        if len(search_list) == 0:
            raise ValueError("array is empty")
        if not all(search_list[i] <= search_list[i + 1] for i in range(len(search_list) - 1)):
            raise ValueError("search_list must be sorted in ascending order")
        if value < search_list[0] or value > search_list[-1]:
            raise ValueError("value not in array")

        # Perform the search
        return search_list.index(value)

    except ValueError as e:
        # Handle value not found or invalid list properties
        raise ValueError(str(e)) from e
    
    except TypeError as e:
        # Handle invalid input types
        raise TypeError(str(e)) from e
