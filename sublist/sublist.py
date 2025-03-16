"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    """
    Determine the relationship between two lists: SUBLIST, SUPERLIST, EQUAL, or UNEQUAL.

    Parameters:
        list_one (list): The first list.
        list_two (list): The second list.

    Returns:
        str: The relationship between the two lists.
    """
    if list_one == list_two:
        return EQUAL

    # Dynamically determine which is smaller and which is larger, call is_sublist function
    if len(list_one) <= len(list_two) and is_sublist(list_one, list_two):
            return SUBLIST
            
    if len(list_two) <= len(list_one) and is_sublist(list_two, list_one):
            return SUPERLIST

    return UNEQUAL

def is_sublist(smaller, larger):
    """
    Check if 'smaller' is a sublist of 'larger'.
    The order of elements must be the same.

    Parameters:
        smaller (list): The potential sublist.
        larger (list): The list in which to check for the sublist.

    Returns:
        bool: True if 'smaller' is a sublist of 'larger', False otherwise.
    """
    # An empty list is always a sublist of any other list
    if not smaller:
        return True

    # Iterate through the larger list, checking slices of the same length as 'smaller'
    for i in range(len(larger) - len(smaller) + 1):
        # Compare the slice of 'larger' with 'smaller'
        if larger[i:i + len(smaller)] == smaller:
            return True

    # If no matching slice is found, return False
    return False
