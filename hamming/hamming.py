"""A module to calculate the Hamming distance between two DNA strands.
The Hamming distance is the number of positions at which the corresponding symbols are different.
"""

def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming distance between two DNA strands.
    
    param strand_a (str): The first DNA strand.
    param strand_b (str): The second DNA strand.
    return: int - The Hamming distance between the two strands.
    """
    validate_strands(strand_a, strand_b)
    hamming_distance = sum(1 for a, b in zip(strand_a, strand_b) if a != b)

    return hamming_distance

# Helper function to validate the strands
def validate_strands(strand_a, strand_b):
    """Validate the input strands for Hamming distance calculation."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    if not all(chars in 'ACGT' for chars in strand_a + strand_b):
        raise ValueError("Strands must only contain A, C, G, or T")
    return True