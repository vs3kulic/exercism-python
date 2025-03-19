ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
            "U", "V", "W", "X", "Y", "Z"]

def rows(letter):
    """
    Generate the rows of the diamond.
    """
    if letter not in ALPHABET:
        raise ValueError("Invalid letter")
    
    letter_index = ALPHABET.index(letter) # returns 0 for A, 1 for B, etc.
    diamond_size = 2 * letter_index + 1
    
    diamond = []
    for i in range(letter_index + 1):
        row = [" "] * diamond_size
        row[letter_index - i] = ALPHABET[i] # left side
        row[letter_index + i] = ALPHABET[i] # right side
        diamond.append("".join(row))
        
    for i in range(letter_index - 1, -1, -1):
        row = [" "] * diamond_size
        row[letter_index - i] = ALPHABET[i]
        row[letter_index + i] = ALPHABET[i]
        diamond.append("".join(row))
    return diamond