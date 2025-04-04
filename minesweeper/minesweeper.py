"""
A module for Minesweeper game logic.
This module provides a function to annotate a Minesweeper board with the number of adjacent mines.
"""

def annotate(minefield) -> list[str]:
    """
    Annotate a minefield with the number of adjacent mines.
    
    params: 
        minefield (list[str]): A list of strings representing the minefield.
    returns:
        list[str]: A list of strings representing the annotated minefield.
    """
    if not minefield:
        return []

    w = len(minefield[0])
    h = len(minefield)
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

            # total = sum([minefield[y + c[1]][x + c[0]] == "*" for c in coords])
            total = 0
            for dy, dx in coords:
                if minefield[y + dy][x + dx] == "*":
                    total += 1

            if total > 0:
                minefield[y][x] = str(total)

    return ["".join(row) for row in minefield]
