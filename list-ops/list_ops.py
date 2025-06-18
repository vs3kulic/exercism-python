"""A module to practice list operations."""
from typing import Callable, Any

def length(lst: list) -> int:
    """Return the length of the list."""
    _validate_list(lst)

    return len(lst)


def append(list1: list, list2: list) -> list:
    """Append two lists together and return the new list."""
    # Validate inputs
    _validate_list(list1)
    _validate_list(list2)

    # Copy list to avoid modifying in place, then extend the copy
    extended_list = list1.copy()
    extended_list.extend(list2)

    return extended_list


def concat(lists: list[list]) -> list:
    """Concatenate a list of lists into a single list."""
    # Validate input
    _validate_list(lists)

    # Initialise an empty list, then iterate through each list to extend the concatenated list
    concatenated_list = []

    for lst in lists: 
        concatenated_list.extend(lst)
    
    return concatenated_list


def map(function: Callable, lst: list) -> list:
    """Apply a function to each element in the list and return a new list."""
    _validate_list(lst)

    mapped_list = [function(item) for item in lst]
    
    return mapped_list


def filter(function: Callable, lst: list) -> list:
    """Filter elements in a list based on a function."""
    _validate_list(lst)

    filtered_list = [item for item in lst if function(item)]
    
    return filtered_list


def foldl(function: Callable, lst: list, initial: Any) -> Any:
    """Fold a list from the left using a function and an initial value.
    
    param function: The function to apply to each element.
    param lst: The list to fold.
    param initial: The initial value for the accumulator.
    return: The final accumulated value.
    
    Example: foldl(lambda acc, el: el * acc, [1, 2, 3], 1) returns 6.
    """
    _validate_list(lst)

    accumulator = initial # Initialise accumulator with the initial value
    
    for item in lst:
        accumulator = function(accumulator, item)

    return accumulator


def foldr(function: Callable, lst: list, initial: Any) -> Any:
    """Fold a list from the right using a function and an initial value."""
    _validate_list(lst)

    accumulator = initial

    for item in reversed(lst):
        accumulator = function(accumulator, item)

    return accumulator


def reverse(lst: list) -> list:
    """Reverse the input list and return it."""
    _validate_list(lst)

    reversed_list = lst[::-1]  # Slicing to reverse the list

    return reversed_list


def _validate_list(lst: list) -> bool:
    """Validate that the input is a list."""
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return True
