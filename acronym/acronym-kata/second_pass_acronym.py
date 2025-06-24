"""A module to abbreviate words into their initials."""
import re

REGEX = "[A-Z]+['a-z]*|['a-z]+"

def abbreviate(words: str) -> str:
    """Abbreviate a given string into its acronym.
    
    param words (str): The input text to be abbreviated.
    return (str): The acronym formed by the initials of each word, in uppercase."""
    acronym = ''.join(word[0].upper() for word in re.findall(REGEX, words))
    
    return acronym

# Example usage:
if __name__ == "__main__":
    example = "Portable Network Graphics"
    print(f"The acronym for '{example}' is: {abbreviate(example)}")
    # Output: The acronym for 'Portable Network Graphics' is: PNG
