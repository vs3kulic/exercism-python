def is_valid(isbn):
    """
    Check if the given ISBN is valid
    :param isbn: str
    :return: bool
    """
    # Remove hyphens and convert to uppercase
    cleaned = isbn.replace("-", "").upper()
    if len(cleaned) != 10:
        return False
    
    weights = {"d1": 10, "d2": 9, "d3": 8, "d4": 7, "d5": 6, "d6": 5, "d7": 4, "d8": 3, "d9": 2, "d10": 1}
    total = 0
    
    # enumerate(cleaned, 1) starts index `i` at 1, allows to directly use `i` to access weights dict
    for i, char in enumerate(cleaned, 1):
        weight = weights[f"d{i}"]
        if i == 10 and char == "X":
            total += 10 * weight
        elif char.isdigit():
            total += int(char) * weight
        else:
            return False
    
    return total % 11 == 0
