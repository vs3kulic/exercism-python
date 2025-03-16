def rotate(text, key):
    """
    Given a string and a rotation key, return the string with each letter rotated by the key.
    params: text: str, key: int
    return: str
    """
    cleaned = ''.join([char.lower() for char in text if char.isalpha()])
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = ''

    for char in cleaned:
        index = (alphabet.index(char) + key) % 26
        rotated += alphabet[index]
    return rotated


def rotate2(text, key):
    """
    Given a string and a rotation key, return the string with each letter rotated by the key.
    params: text: str, key: int
    return: str
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = ''

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            index = (alphabet.index(char.lower()) + key) % 26    
            new_char = alphabet[index].upper() if is_upper else alphabet[index]
            rotated += new_char
        else:
            rotated += char
    return rotated


print(rotate("Hello, World!", 5))  # "mjqqtbtwqi"

print(rotate2("Hello, World!", 5))  # "Mjqqt, Btwqi!"