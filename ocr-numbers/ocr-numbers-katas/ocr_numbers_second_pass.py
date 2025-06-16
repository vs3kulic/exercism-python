"""This is a second pass solution for the OCR Numbers kata."""

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
    if len(input_grid) % 4 != 0:
        raise(ValueError("Number of lines must be a multiple of 4."))

    for line in input_grid:
        if len(line) % 3 != 0:
            raise(ValueError("Number of columns must be a multiple of 3."))

    # Initialise an empty string to hold the matched digit
    matched_digit = ""
    
    # Check if the input grid matches the pattern for '0'
    if input_grid == PATTERN_TO_DIGIT['0']:
        matched_digit = "0"
        
    # DEBUG: Let's see what we're comparing
    print(f"Input grid:     {input_grid}")
    print(f"Pattern for 0:  {PATTERN_TO_DIGIT['0']}")
    print(f"Are they equal? {input_grid == PATTERN_TO_DIGIT['0']}")

    return matched_digit

# Example usage
if __name__ == "__main__":
    input_example = [
        " _ ",
        "| |",
        "|_|",
        "   "
    ]
    print(convert(input_example))  # Should print "0"
