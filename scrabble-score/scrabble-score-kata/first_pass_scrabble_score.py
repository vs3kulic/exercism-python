"""This module contains the first pass implementation of the scrabble score kata."""

# Define the mapping for letter scores
LETTER_SCORES = {
    ('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'): 1,
    ('g'): 2,
    ('b', 'c', 'm', 'p'): 3,
    ('f', 'h', 'v', 'w', 'y'): 4,
    ('k'): 5,
    ('j', 'x'): 8,
    ('q', 'z'): 10
}

def score(word: str) -> int:
    """Calculate the Scrabble score for a given word.
    
    param word: str - The word to score.
    return: int - The score of the word.
    """
    # Validate the input
    validate_input(word)

    # Initialize the score
    word_score = 0
    
    # Calculate the score


    return word_score


# Helper function to validate input
def validate_input(word):
    """Validate the input word."""
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    if not word:
        return 0
    return word.lower()