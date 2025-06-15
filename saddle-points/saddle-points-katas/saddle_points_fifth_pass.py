"""This module contains functions to find saddle points in a matrix.
The fifth pass implementation passes all tests with clean function separation.
"""

def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """Find all saddle points in a given matrix."""
    
    # Handle empty matrix case
    if not matrix:
        return []

    # Handle irregular matrix shapes
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")

    # Get row maxima and column minima
    row_maxima = find_row_maxima(matrix)
    column_minima = find_column_minima(matrix)
    found_saddle_points = find_saddle_point_positions(matrix, row_maxima, column_minima)
    
    return found_saddle_points

def find_saddle_point_positions(matrix: list[list[int]],
                               row_maxima: list[int],
                               column_minima: list[int]) -> list[dict[str, int]]:
    """Find positions where values are both row maximum and column minimum."""
    _saddle_points = []
    
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == row_maxima[row_index] and value == column_minima[col_index]:
                _saddle_points.append({"row": row_index + 1, "column": col_index + 1})
    
    return _saddle_points

def find_row_maxima(matrix: list[list[int]]) -> list[int]:
    """Find the maximum values in each row."""
    row_maxima = []
    
    for row_values in matrix:
        row_maxima.append(max(row_values))

    return row_maxima

def find_column_minima(matrix: list[list[int]]) -> list[int]:
    """Find minimum value in each column."""
    column_minima = []

    # Transpose the matrix first (rows become columns)
    t_matrix = list(zip(*matrix))

    for column in t_matrix:
        column_minima.append(min(column))

    return column_minima
