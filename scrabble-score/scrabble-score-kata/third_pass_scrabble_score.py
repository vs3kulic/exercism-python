"""This module contains the first pass implementation of the scrabble score kata."""

# Define the mapping for letter scores
SCORE_GROUPS = {
    1: "aeioulnstr",
    2: "dg", 
    3: "bcmp",
    4: "fhvwy",
    5: "k",
    8: "jx",
    10: "qz"
}

def score(word: str) -> int:
    """Calculate the Scrabble score for a given word.
    
    param word: str - The word to score.
    return: int - The score of the word.
    """
    # Validate the input
    validate_input(word)

    # Calculate the score by summing the scores of each letter
    word_score = sum(letter_scoring(letter) for letter in word.lower())

    return word_score


# Helper function to validate input
def validate_input(word):
    """Validate the input word."""
    if not word or not isinstance(word, str):
        return 0
    return word

# Helper function to calculate the score for a letter
def letter_scoring(letter: str) -> int:
    """Calculate the score for a single letter."""
    for letter_score, letters in SCORE_GROUPS.items(): # items() returns key-value pairs
        if letter in letters:
            return letter_score
    return 0  # If the letter is not found, return 0
