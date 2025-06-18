"""A module to reverse a string."""

def reverse(text: str) -> str:
    """Reverse the input string and return it.
    
    param text: The string to be reversed.
    return: The reversed string.
    """
    reversed_text = ''.join(reversed(text))
    
    return reversed_text

# Example usage:
if __name__ == "__main__":
    sample_text = "robot"
    print(reverse(sample_text))  # Output: 'tobor'
