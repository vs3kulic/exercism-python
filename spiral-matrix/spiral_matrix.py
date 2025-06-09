"""Spiral Matrix Generator
This module provides a function to generate an n x n spiral matrix 
filled with numbers from 1 to n^2.
"""
# ------------------------------------------
# Main functions to generate a spiral matrix
# ------------------------------------------

def spiral_matrix(size: int) -> list[list[int]]:
    """Return n x n spiral matrix filled from 1 to n^2."""
    # Validate the input size
    if size < 0:
        raise ValueError("Size must be a non-negative integer.")
    
    # Create an n x n matrix initialized with zeros
    matrix = [[0] * size for _ in range(size)]
    
    # Define the boundaries of the spiral, initialise the starting number
    left, right, top, bottom = 0, size - 1, 0, size - 1
    num = 1
    
    # Fill the matrix in a spiral order
    while left <= right and top <= bottom:
        num = fill_layer(matrix, top, bottom, left, right, num)
        top, right, bottom, left = top + 1, right - 1, bottom - 1, left + 1
    return matrix

def fill_layer(matrix: list[list[int]], top: int, bottom: int, left: int, right: int, num: int) -> int:
    """
    Fill one layer of the spiral matrix.
    :param matrix: list[list[int]] - the matrix to fill.
    :param top: int - the top boundary of the layer.
    :param bottom: int - the bottom boundary of the layer.
    :param left: int - the left boundary of the layer.
    :param right: int - the right boundary of the layer.
    :param num: int - the starting number to fill.
    :return: int - the next number to fill in the matrix.
    """
    # Fill the top row of the current layer, then the right column
    num = fill_top(matrix, top, left, right, num)
    num = fill_right(matrix, right, top + 1, bottom, num)

    # If the current layer has a bottom row, fill it
    if top < bottom:
        num = fill_bottom(matrix, bottom, right - 1, left, num)

    # If the current layer has a left column, fill it
    if left < right:
        num = fill_left(matrix, left, bottom - 1, top + 1, num)
    return num

# -----------------
# Helper functions
# -----------------
def fill_top(matrix: list[list[int]], row: int, start: int, end: int, num: int) -> int:
    """Fill the top row of the current layer in the spiral matrix."""
    for col in range(start, end + 1):
        matrix[row][col] = num
        num += 1
    return num

def fill_right(matrix: list[list[int]], col: int, start: int, end: int, num: int) -> int:
    """Fill the right column of the current layer in the spiral matrix."""
    for row in range(start, end + 1):
        matrix[row][col] = num
        num += 1
    return num

def fill_bottom(matrix: list[list[int]], row: int, start: int, end: int, num: int) -> int:
    """Fill the bottom row of the current layer in the spiral matrix."""
    for col in range(start, end - 1, -1):
        matrix[row][col] = num
        num += 1
    return num

def fill_left(matrix: list[list[int]], col: int, start: int, end: int, num: int) -> int:
    """Fill the left column of the current layer in the spiral matrix."""
    for row in range(start, end - 1, -1):
        matrix[row][col] = num
        num += 1
    return num

# -------------------
# Example usage:
# -------------------
# SIZE = 5
# result = spiral_matrix(SIZE)
# for row in result:
#    print(' '.join(f"{val:2d}" for val in row)) # 2d formatting for better alignment
