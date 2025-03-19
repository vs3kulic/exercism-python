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
        index = (alphabet.index(char) + key) % len(alphabet) # modulo to wrap around the alphabet
        rotated += alphabet[index]
    return rotated

print(rotate("Hello, World!", 5))  # "mjqqtbtwqi"
