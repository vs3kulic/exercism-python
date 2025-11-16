"""This module contains functions for run-length encoding and decoding of strings."""

def decode(code: str) -> str:
    """Decode a run-length encoded string.
    
    :param code: The run-length encoded string ("2a3b4c")
    :type code: str
    :returns: The decoded string
    :rtype: str
    """
    run = ""
    return run


def encode(run: str) -> str:
    """Encode a string using run-length encoding.
    
    param run: The string to encode ("aabbbcccc")
    :type run: str
    :returns: The run-length encoded string
    :rtype: str
    """
    encoded = []
    for i, char in enumerate(run):
        count = 0
        while i+1 < len(run):
            if run[i] == run[i+1]:
                count += 1
                i += 1
        encoded.append(f"{count}{char}")
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
