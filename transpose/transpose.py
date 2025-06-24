"""A module to transpose text input."""

from itertools import zip_longest

def transpose(text: str) -> str:
    """Output a given input text transposed.
    
    param text (str): The input text to be transposed.
    return (str): The transposed text, with rows and columns swapped.
    """
    # Split the input text into lines - keepends=False to avoid trailing newlines
    lines = text.splitlines(keepends=False)

    # Pad with '-' instead of spaces
    padded_lines = zip_longest(*lines, fillvalue='-')

    # Join the characters from each line, stripping only trailing '-' characters
    joined_lines = [''.join(line).rstrip('-') for line in padded_lines]

    # Convert remaining '-' back to spaces
    transposed_lines = '\n'.join(joined_lines).replace('-', ' ')

    return transposed_lines
