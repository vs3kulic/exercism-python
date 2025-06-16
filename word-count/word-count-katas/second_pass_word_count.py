"""This module implements a second-pass approach to the Word Count kata.
This approach is passing 7/17 tests."""

def count_words(text: str) -> dict:
    """The function counts words in a given text.
    
    param text: The input string containing words, punctuation, and whitespace.
    return: A dictionary where each key is a word (case-insensitive) and the value is the word count.
    """
    # Input validation
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    if not text:
        return {}

    # Call the normalise_text function to process the input text
    words = normalise_text(text)
    
    # Initialize an empty dictionary to hold word counts
    word_dictionary = {}

    # Loop through the words and count occurrences
    for word in words:
        word_dictionary[word] = word_dictionary.get(word, 0) + 1

    return word_dictionary

def normalise_text(text: str) -> list:
    """Normalises the text by converting it to lowercase and replacing punctuation with spaces."""
    # Convert to lowercase
    text = text.lower()

    # Replace punctuation with spaces, keeping apostrophes
    for char in ".,;:!?\"":
        text = text.replace(char, " ")

    # Split the text into words
    words = text.split()

    return words
