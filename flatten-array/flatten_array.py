from typing import Any, Iterable, List

def flatten(nested_iterable: Iterable[Any]) -> List[Any]:
    """
    Flatten a nested list or tuple into a single flat list.

    param nested_iterable: An iterable (like a list or tuple), possibly nested.
    returns: A flat list with all non-None elements from the nested structure.
    raises: ValueError if the argument is not a list or tuple.
    """
    # Input Validation
    if not isinstance(nested_iterable, (list, tuple)):
        raise ValueError("Argument must be a list or tuple")
    if not nested_iterable:
        return []

    flat_result = []

    # Recursive flattening
    for element in nested_iterable:
        if isinstance(element, (list, tuple)):
            flat_result.extend(flatten(element)) # Recursive case: flatten further
        elif element is not None:
            flat_result.append(element) # Base case: add single element

    return flat_result
