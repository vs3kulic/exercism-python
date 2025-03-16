from math import sqrt

def score(x, y):
    """
    Return the score of a dart throw given its coordinates.

    imports: sqrt from math
    params x, y: int, int
    return: int
    """
    # Calculate the distance from the center
    try:
        distance = sqrt(x**2 + y**2)
    except Exception as exc:
        raise TypeError("x and y must be integers") from exc
    

    # Define scoring ranges in a dictionary
    scoring = {
        1: 10,  # Distance <= 1
        5: 5,   # Distance <= 5
        10: 1   # Distance <= 10
    }

    # Iterate through the scoring ranges
    for radius, points in scoring.items():
        if distance <= radius:
            return points

    return 0  # Default score if no range matches
