"""This module contains the implementation of the scrabble score kata."""

# Define the mapping for letter scores
LETTER_SCORES = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
    'd': 2, 'g': 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    'q': 10, 'z': 10
}

def score(word: str) -> int:
    """Calculate the Scrabble score for a given word.
    
    param word: str - The word to score.
    return: int - The score of the word.
    """
    # Validate the input
    if not word or not isinstance(word, str):
        return 0

    # Calculate the score by summing the scores of each letter, using get function for safety
    # Generator expression returns a lazy iterator that yields each letter's score when consumed
    word_score = sum(LETTER_SCORES.get(letter, 0) for letter in word.lower())

    return word_score

# Helper function to calculate the score for a letter
def letter_scoring(letter: str) -> int:
    """Calculate the score for a single letter."""
    for letters, letter_score in LETTER_SCORES.items(): # items() returns key-value pairs
        if letter in letters:
            return letter_score

    return 0  # If the letter is not found, return 0
