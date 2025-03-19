"""
Module for encoding and decoding text using the Atbash cipher.
"""

def atbash_char(char):
    """
    Helper function to encode/decode a single character using the Atbash cipher.
    
    param: char: str: The character to encode/decode.
    return: str: The encoded/decoded character.
    """
    if char.isalpha(): # if char is a letter, encode it
        char = chr(ord('z') - (ord(char.lower()) - ord('a'))) # atbash cipher formula
    
    return char if char.isalnum() else "" # strip out non-alphanumeric characters, e.g. punctuation


def encode(plain_text):
    """
    A function to encode a plain text using the Atbash cipher.
 
    param: plain_text: str: The text to encode.
    return: str: The encoded text.
    """
    encoded = "".join([atbash_char(char) for char in plain_text])
    ciphered = " ".join(encoded[i:i+5] for i in range(0, len(encoded), 5))
    
    return ciphered


def decode(ciphered_text):
    """
    A function to decode a ciphered text using the Atbash cipher.
 
    param: ciphered_text: str: The text to decode.
    return: str: The decoded text.
    """
    # decoded = encode(ciphered_text).replace(" ", "") # decoding is the same as encoding, just remove spaces
    decoded = "".join([atbash_char(char) for char in ciphered_text])

    return decoded
