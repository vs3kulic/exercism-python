def is_pangram(sentence):
    """
    Determine if the given sentence is a pangram.
    param sentence: str - sentence to check.
    return: bool - True if sentence is a pangram, False otherwise.
    """
    string = "".join(char.lower() for char in sentence if char.isalpha())

    return len(set(string)) == 26