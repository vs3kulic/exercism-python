"""
Minesweeper Board Annotation Module

This module provides functionality to annotate a Minesweeper board by replacing empty spaces
with counts of adjacent mines. The board is represented as a list of strings where:
- '*' represents a mine
- ' ' represents an empty space

Example:
    Input board:  [" * ", "  *"]
    Annotated: ["1*1", " 12*"]
"""

def annotate(minefield: list[str]) -> list[str]:
    """Annotate a Minesweeper board with adjacent mine counts.

    Processes each empty space (' ') in the input board to show the number of
    mines in all 8 surrounding cells. Mine cells ('*') remain unchanged.

    Args:
        minefield: A list of strings representing the Minesweeper board.
            - All rows must be the same length
            - Valid characters: '*' (mine), ' ' (empty space)

    Returns:
        list[str]: A new list of strings representing the annotated board,
        where empty spaces adjacent to mines are replaced with digit characters
        ('1'-'8'), and other cells remain unchanged.

    Raises:
        ValueError: If the board is invalid due to:
            - Empty rows of inconsistent lengths
            - Characters other than '*' or ' '

    Example:
        >>> annotate([" * ", "  *"])
        ['1*1', ' 12*']
    """
    if not minefield:
        return []

    # ... (rest of the code remains unchanged) ...

    if not minefield:
        return []

    w = len(minefield[0])  # Width (columns)
    h = len(minefield)     # Height (rows)
    minefield = [list(row) for row in minefield]

    for y, row in enumerate(minefield):
        if len(row) != w or any(c not in {"*", " "} for c in row):
            raise ValueError("The board is invalid with current input.")

        for x, item in [(x, v) for x, v in enumerate(row) if v == " "]:
            coords = {
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1)
            }

            if y == 0: coords -= {(-1, -1), (0, -1), (1, -1)}
            if x == 0: coords -= {(-1, -1), (-1, 0), (-1, 1)}
            if y == h - 1: coords -= {(-1, 1), (0, 1), (1, 1)}
            if x == w - 1: coords -= {(1, -1), (1, 0), (1, 1)}

            # Formula: neighbor_column = x + dx (c[0]), neighbor_row = y + dy (c[1])
            total = sum(minefield[y + c[1]][x + c[0]] == "*" for c in coords)

            if total > 0:
                minefield[y][x] = str(total)

    return ["".join(row) for row in minefield]
