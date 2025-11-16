"""This module contains functions for run-length encoding and decoding of strings."""


def decode(encoded_string: str) -> str:
    """Decode a run-length encoded string.
    
    :param code: The run-length encoded string ("2a3b4c")
    :type code: str
    :returns: The decoded string
    :rtype: str
    """
    decoded_string = ""
    count_str = ""
    for char in encoded_string:
        if char.isdigit():
            count_str += char
        else:
            count = int(count_str) if count_str else 1
            decoded_string += char * count
            count_str = ""
    return decoded_string


def encode(string):
    """
    Encode a string using run-length encoding.
    
    :param string: The raw string input
    :type string: str
    :returns: The run-length encoded string
    :rtype: str
    """
    if not string:
        return ""

    encoded_string = ""
    count = 1
    for i in range(1, len(string) + 1):
        if i == len(string) or string[i] != string[i-1]:
            if count > 1:
                encoded_string += str(count)
            encoded_string += string[i-1]
            count = 1
        else:
            count += 1
    return encoded_string


def main():
    """Main function to demonstrate encoding and decoding."""
    sample_run = "aaabbbccdaa"
    encoded = encode(sample_run)
    # decoded = decode(encoded)
    print(f"Original: {sample_run}")
    print(f"Encoded: {encoded}")
    # print(f"Decoded: {decoded}")

if __name__ == "__main__":
    main()
