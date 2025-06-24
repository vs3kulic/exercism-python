"""A module to abbreviate words into their initials."""

DELIMITERS = ['-', '_', ',', ';', ':', '!', '?', '.']

def abbreviate(words: str) -> str:
    """Output the initials of each word in a given input text.
    
    param words (str): The input text to be abbreviated.
    return (str): The acronym formed by the initials of each word, in uppercase.
    """
    # Copy the input to avoid modifying the original string
    cleaned_words = words

    # Replace delimiters with spaces
    for delimiter in DELIMITERS:
        cleaned_words = cleaned_words.replace(delimiter, " ")

    # Assemble the acronym by taking the first letter (upper case) of each word
    acronym = ''.join(word[0].upper() for word in cleaned_words.split())

    return acronym

# Example usage:
if __name__ == "__main__":
    example = "Portable Network Graphics"
    print(f"The acronym for '{example}' is: {abbreviate(example)}")
