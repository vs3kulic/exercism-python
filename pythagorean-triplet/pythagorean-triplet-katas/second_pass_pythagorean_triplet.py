def triplets_with_sum2(total: int) -> list[list[int]]:
    """Find all Pythagorean triplets that sum to the given total using sets."""
    triplets = []
    squares = {x: x**2 for x in range(1, total)}  # Precompute squares for all numbers

    for a in range(1, total // 2):
        for b in range(a, total // 2):
            c = total - a - b
            if c > b and squares[a] + squares[b] == squares.get(c, 0):
                triplets.append([a, b, c])  # Append the triplet as a list

    return triplets
