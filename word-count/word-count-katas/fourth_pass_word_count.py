"""This module implements a third-pass approach to the Word Count kata.
This approach is passing ALL tests."""

from collections import Counter

def count_words(text: str) -> dict[str, int]:
    """The function counts words in a given text.
    
    param text: The input string containing words, punctuation, and whitespace.
    return: A dictionary where each key is a word (case-insensitive) and the value is the word count.
    """
    # Input validation
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    if not text:
        return {}

    # Call the _normalise_text helper function to process the input text
    words = _normalise_text(text)
    
    # Count word occurrences using Counter
    word_dictionary = Counter(words)

    return dict(word_dictionary)

def _normalise_text(text: str) -> list:
    """Helper function that normalises text.
    
    param text: The input string to be normalised.
    return: A list of words, where each word is in lowercase and punctuation is replaced with spaces.
    """
    # Convert to lowercase
    text = text.lower()

    # Replace punctuation with spaces, keeping apostrophes
    for char in ".,;:!?\"&@$%^_":
        text = text.replace(char, " ")

    # Strip leading and trailing apostrophes, but keep internal ones
    _words = []
    
    for word in text.split():
        cleaned = word.strip("'")
        if cleaned:  # Only add non-empty words
            _words.append(cleaned)

    return _words
