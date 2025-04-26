"""
A module to transform legacy data into a new format. 
The legacy data is a dictionary where the keys are scores and the values are lists of letters: 
"""

def transform(legacy_data):
    """
    A function to transform legacy data into a new format:

    Args:
        legacy_data (dict): The legacy data to be transformed.
    Returns:
        dict: The transformed data.
    Raises:
        ValueError: If the legacy data is not in the expected format.
    Example:
        >>> legacy_data = {1: ["A", "E", "I", "O", "U"]}
        current_data = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}

        >>> legacy_data = {1: ["A", "E"], 2: ["D", "G"]}
        current_data = {'a': 1, 'd': 2, 'e': 1, 'g': 2}
    """
    current_data = {}

    for score, letters in legacy_data.items():
        for letter in letters:
            current_data[letter.lower()] = score # add key (letter) with value (score) to dict

    return current_data
