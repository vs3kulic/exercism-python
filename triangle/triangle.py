"""
This module contains functions to determine the type of a triangle
"""

def all_sides_positive(sides):
    """
    Returns True if all sides are positive, False otherwise
    """
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        return True
    return False

def equilateral(sides):
    """
    Returns True if the triangle is equilateral, False otherwise
    """
    return all_sides_positive(sides) and sides[0] == sides[1] == sides[2]

def isosceles(sides):
    """
    Returns True if the triangle is isosceles, False otherwise
    """
    # Check triangle properties
    if len(sides) != 3 or not all_sides_positive(sides):
        return False
    
    # Check triangle inequality
    if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[0] + sides[2] <= sides[1]:
        return False

    # Check if at least two sides are equal
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]


def scalene(sides):
    """
    Returns True if the triangle is scalene, False otherwise
    """
    # Check triangle properties
    if len(sides) != 3 or not all_sides_positive(sides):
        return False

    if (sides[0] + sides[1] <= sides[2]) or (sides[1] + sides[2] <= sides[0]) or (sides[0] + sides[2] <= sides[1]):
        return False

    return len(set(sides)) == 3
