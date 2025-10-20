"""This module provides a function to find Pythagorean triplets that sum to a given total."""

def triplets_with_sum(total: int) -> list[list[int]]:
    """Find all Pythagorean triplets that sum to the given total using sets.
    
    :param total: The total sum of the triplet
    :type total: int
    :returns: A list of lists, each containing a Pythagorean triplet
    :rtype: list[list[int]]
    """
    # Initialize a list to store triplets
    triplets = []

    # Iterate through possible values of a and b
    for a in range(1, total // 3):  # a must be less than (total // 3)
        for b in range(a, total // 2): # b must be >= a and less than (total // 2)
            c = total - a - b
            if a * a + b * b == c * c:
                triplets.append([a, b, c])  # Append the triplet as a list

    return triplets

def main():
    """Main function to demonstrate triplet generation."""
    total = 108
    triplets = triplets_with_sum(total)
    print(f"Pythagorean triplets that sum to {total}: {triplets}")

if __name__ == "__main__":
    main()
