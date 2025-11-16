"""This module contains functions for run-length encoding and decoding of strings."""

def decode(encoded_string: str) -> str:
    """Decode a run-length encoded string.
    
    :param code: The run-length encoded string ("2a3b4c")
    :type code: str
    :returns: The decoded string
    :rtype: str
    """
    run = ""
    return run


def encode(decoded_string: str) -> str:
    """Encode a string using run-length encoding."""
    if not decoded_string:
        return ""

    encoded = []
    i = 0
    while i < len(decoded_string):
        char = decoded_string[i]
        count = 1
        while (
            i + 1 < len(decoded_string) and
            decoded_string[i] == decoded_string[i+1]
        ):
            count += 1
            i += 1
        if count == 1:
            encoded.append(char)
        else:
            encoded.append(f"{count}{char}")
        i += 1
    return "".join(encoded)


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
