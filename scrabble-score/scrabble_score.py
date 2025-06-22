"""This module contains the implementation of the scrabble score kata."""

# Define the mapping for letter scores
SCORE_GROUPS = {
    "aeioulnstr": 1,
    "dg": 2, 
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}

def score(word: str) -> int:
    """Calculate the Scrabble score for a given word.
    
    param word: str - The word to score.
    return: int - The score of the word.
    """
    # Validate the input
    if not word or not isinstance(word, str):
        return 0

    # Calculate the score by summing the scores of each letter
    word_score = sum(letter_scoring(letter) for letter in word.lower())

    return word_score

# Helper function to calculate the score for a letter
def letter_scoring(letter: str) -> int:
    """Calculate the score for a single letter."""
    for letters, letter_score in SCORE_GROUPS.items(): # items() returns key-value pairs
        if letter in letters:
            return letter_score

    return 0  # If the letter is not found, return 0
