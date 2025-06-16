"""This module implements a first-pass approach to the word count kata."""

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

    # Initialize an empty dictionary to hold word counts
    word_count = {}

    # TODO: Normalize the text to lowercase

    # TODO: Handle punctuation (replace with spaces, keep apostrophes)

    # TODO: Split the string into words and store them as keys in the dictionary

    # TODO: Loop through the keys, count occurrences of each word and store counts as values

    return word_count
