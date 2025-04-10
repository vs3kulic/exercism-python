"""
Binary Search Algorithm.
"""

def find(search_list, value):
    """
    Find the index of a value in a sorted list using binary search.

    :param search_list: A sorted list of values
    :param value: The value to search for
    :return: The index of the value in the list
    :raises ValueError: If the value is not found in the list
    """

    try:
        sorted_list = sorted(search_list)

        while len(sorted_list) > 1:
            mid_index = len(sorted_list) // 2
            mid_index_value = sorted_list[mid_index]
            
            if value > mid_index_value:
                sorted_list = sorted_list[mid_index:]

            if value < mid_index_value:
                sorted_list = sorted_list[:mid_index]

            if value == mid_index_value:
                return value

        if len(sorted_list) == 1 and not value in sorted_list:
            raise ValueError from None

    except ValueError:
        print("value not in array")

