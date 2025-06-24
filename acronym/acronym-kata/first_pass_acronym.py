"""A module to abbreviate words into their initials."""

DELIMITERS = ['-', '_', ',', ';', ':', '!', '?', '.']

def abbreviate(words: str) -> str:
    """Output the initials of each word in a given input text.
    
    param words (str): The input text to be abbreviated.
    return (str): The acronym formed by the initials of each word, in uppercase.
    """
    if not words or words.isspace():
        return ""
    if not isinstance(words, str):
        raise ValueError("Input must be a string.")

    # Replace delimiters with spaces
    for delimiter in DELIMITERS:
        words = words.replace(delimiter, " ")

    first_letters = ''.join(word[0].upper() for word in words.split())
    acronym = ''.join(first_letters)

    return acronym


# Example usage:
if __name__ == "__main__":
    example = "Portable Network Graphics"
    print(f"The acronym for '{example}' is: {abbreviate(example)}")
    # Output: The acronym for 'Portable Network Graphics' is: PNG
