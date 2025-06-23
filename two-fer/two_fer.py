"""A module to generate a two-fer string.
The two-fer (or "two for one") is a phrase used to indicate that one person"""

def two_fer(name: str = "you") -> str:
    """Generate a two-fer string.
    
    param name (str): the name of the person to share with.
    return (str): A string in the format "One for {name}, one for me."
    """
    validate_name(name)
    sentence = f"One for {name}, one for me."

    return sentence


# Helper function to validate the name parameter
def validate_name(name: str) -> bool:
    """Validate the name parameter."""
    if not all(isinstance(char, str) for char in name):
        raise ValueError("Name must be a non-empty string containing only characters.")
    return True
