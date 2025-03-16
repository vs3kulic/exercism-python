def is_isogram(string):
    """
    Determine if a word or phrase is an isogram.
    
    param string: str
    return: bool
    """
    # Create a string with only the letters of the word
    word = ''.join([char.lower() for char in string if char.isalpha()])

    # Check if the length of the word is equal to the length of the set of the word
    return len(word) == len(set(word))
