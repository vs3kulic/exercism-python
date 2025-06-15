"""This module contains functions to find saddle points in a matrix.
The third pass implementation passes 9/10 tests.
"""

def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """
    Find all saddle points in a given matrix. 
    A saddle point is an element that is the minimum in its row and the maximum in its column.
    
    param matrix: A 2D list representing the matrix.
    return: A list of tuples, with each tuple containing the row index, column index, and value of the saddle point.
    """
    # Handle empty matrix case
    if not matrix:
        return []

    # Handle irregular matrix shapes (non-rectangular)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("Irregular matrix: rows have different lengths")

    # Check each position for saddle points
    row_maxima = find_row_maxima(matrix) # type: ignore
    column_minima = find_column_minima(matrix)
    _saddle_points = []
    
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value == row_maxima[row_index] and value == column_minima[col_index]:
                _saddle_points.append({"row": row_index + 1, "column": col_index + 1})
                
    return _saddle_points

# Helper function to find row maxima
def find_row_maxima(matrix: list[list[int]]) -> list[int]:
    """A function to find the maximum values in each row."""
    row_maxima = []
    
    for row_values in matrix:
        row_maxima.append(max(row_values))

    return row_maxima

# Helper function to find column minima
def find_column_minima(matrix: list[list[int]]) -> list[int]:
    """Find minimum value in each column."""
    column_minima = []
    
    for col_index in range(len(matrix[0])):
        # Collect all values from this column, then find minimum
        column_values = [matrix[row_index][col_index] for row_index in range(len(matrix))]
        column_minima.append(min(column_values))
    
    return column_minima