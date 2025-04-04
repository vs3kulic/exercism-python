def annotate(minefield) -> list[str]:
    if not minefield: return []

    w = len(minefield[0]) # establish matrix width as length of the first row element (e.g. " *  * ")
    h = len(minefield) # establish matrix height as length of the entire list (e.g. [" *  * ", "  *   ", "    * ", "   * *", " *  * ", "      "])

    minefield = [list(row) for row in minefield]
    
    for y, row in enumerate(minefield):
        if len(row) != w or any(c not in ("*", " ") for c in row):
            raise ValueError("The board is invalid with current input.")
        
        for x, item in [(x, v) for x, v in enumerate(row) if v == " "]:
            coords = set((
                (-1, -1), (0, -1), (1, -1), 
                (-1,  0),          (1,  0), 
                (-1,  1), (0,  1), (1,  1)
            ))

            if y == 0: coords.difference_update(set(((-1, -1), (0, -1), (1, -1)))) # prune coordinates if y is 0
            if x == 0: coords.difference_update(set(((-1, -1), (-1, 0), (-1, 1)))) # prune coordinates if x is 0
            if y == h - 1: coords.difference_update(set(((-1,  1), (0,  1), (1,  1)))) # prune coordinates if y is h - 1
            if x == w - 1: coords.difference_update(set(((1 , -1), (1 , 0), (1 , 1)))) # prune coordinates if x is w - 1
            
            total = sum([minefield[y + c[1]][x + c[0]] == "*" for c in coords])

            if total > 0:
                minefield[y][x] = str(total)

    return (["".join(row) for row in minefield])
