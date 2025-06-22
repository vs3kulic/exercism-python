"""This module contains the first pass implementation of the scrabble score kata."""

# Define the mapping for letter scores
LETTER_SCORES = {}
score_groups = {
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

    # Initialize the score
    word_score = 0

    # Calculate the score
    for letter in word.lower():
        word_score += letter_score(letter)

    return word_score


# Helper function to validate input
def validate_input(word):
    """Validate the input word."""
    if not word or not isinstance(word, str):
        return 0
    return word.lower()

# Helper function to calculate the score for a letter
def letter_score(letter: str) -> int:
    """Calculate the score for a single letter."""
    for scoring, letters in score_groups.items():
        if letter in letters:
            return scoring
    return 0  # If the letter is not found, return 0
