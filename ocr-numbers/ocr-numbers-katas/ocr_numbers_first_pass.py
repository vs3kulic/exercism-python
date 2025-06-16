"""This is a first pass solution for the OCR Numbers kata."""

# Define the patterns for each digit
PATTERN_TO_DIGIT = {
    "0": [" _ ", "| |", "|_|", "   "],
    "1": ["   ", "  |", "  |", "   "],
    "2": [" _ ", " _|", "|_ ", "   "],
    "3": [" _ ", " _|", " _|", "   "],
    "4": ["   ", "|_|", "  |", "   "],
    "5": [" _ ", "|_ ", " _|", "   "],
    "6": [" _ ", "|_ ", "|_|", "   "],
    "7": [" _ ", "  |", "  |", "   "],
    "8": [" _ ", "|_|", "|_|", "   "],
    "9": [" _ ", "|_|", " _|", "   "] 
}

def convert(input_grid: list[str]) -> str:
    """Convert a list of strings representing OCR output into a digit.
    
    param input_grid: A list of strings, each representing a line of OCR output.
    return: A string representing the recognized number.
    raises ValueError:  If the number of lines is not a multiple of 4 
                        or if the number of columns is not a multiple of 3.
    """
    # Check if the input is valid
    # - TODO: Check if number of lines is a multiple of 4, raise ValueError if not
    # - TODO: Check if the number of columns is a multiple of 3, raise ValueError if not

    # Initialise an empty string to hold the matched digit
    matched_digit = ""
    
    # TODO: Map the input grid to a string pattern

    return matched_digit
