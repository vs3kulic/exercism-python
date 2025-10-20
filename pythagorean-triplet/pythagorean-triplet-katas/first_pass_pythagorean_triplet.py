"""This module provides functions to generate Pythagorean triplets."""

def triplets_with_sum(number):
    """Find all Pythagorean triplets that sum to the given number.
    
    :param number: The total sum of the triplet
    :type number: int
    :returns: A list of lists, each containing a Pythagorean triplet
    :rtype: list[list[int]]
    """
    triplets = []
    for a in range(1, number):
        for b in range(a, number - a):
            c = number - a - b
            if a * a + b * b == c * c:
                triplets.append([a, b, c])
    return sorted(enumerate(triplets), reverse=True)

def main():
    """Main function to demonstrate triplet generation."""
    total = 108
    triplets = triplets_with_sum(total)
    print(f"Pythagorean triplets that sum to {total}: {triplets}")

if __name__ == "__main__":
    main()
