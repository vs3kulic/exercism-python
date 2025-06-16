"""This is a fourth pass solution for the OCR Numbers kata.
It passes 16/17 tests, including the ones that require handling multiple digits.
"""

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

DIGIT_WIDTH = 3
DIGIT_HEIGHT = 4

def convert(input_grid: list[str]) -> str:
    """Convert a list of strings representing OCR output into a digit.
    
    param input_grid: A list of strings, each representing a line of OCR output.
    return: A string representing the recognized number.
    raises ValueError:  If the number of lines is not a multiple of 4 
                        or if the number of columns is not a multiple of 3.
    """
    # Validation
    if len(input_grid) % DIGIT_HEIGHT != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    for line in input_grid:
        if len(line) % DIGIT_WIDTH != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    
    # Calculate number of 4-row groups
    num_rows = len(input_grid)
    num_groups = num_rows // DIGIT_HEIGHT  # How many 4-row groups?
    
    results = []  # Store results for each group
    
    # Process each 4-row group
    for group_idx in range(num_groups):
        start_row = group_idx * DIGIT_HEIGHT
        end_row = start_row + DIGIT_HEIGHT
        
        # Extract just this 4-row group
        group_grid = input_grid[start_row:end_row]
        
        # Initialize an empty string to hold the matched digit
        matched_digit = ""
        
        # Calculate the number of digits based on the input length
        grid_width = len(group_grid[0])
        number_of_digits = grid_width // DIGIT_WIDTH
        
        # Iterate through each digit position
        for digit_pos in range(number_of_digits):
            start_col = digit_pos * DIGIT_WIDTH # Start column for the digit
            end_col = start_col + DIGIT_WIDTH # End column for the digit

            # Initialize a pattern for the current digit
            digit_pattern = []
            found_digit = "?"  # Default to unknown

            # Extract the pattern for the current digit
            for row in group_grid:
                digit_row = row[start_col:end_col] # slice the row to get the digit
                digit_pattern.append(digit_row)

            # Look up the full pattern in the dictionary
            for digit, pattern in PATTERN_TO_DIGIT.items():
                if digit_pattern == pattern:
                    found_digit = digit
                    break  # Found it, stop looking

            matched_digit += found_digit

        results.append(matched_digit)
    
    # Join results with commas
    return ",".join(results)

# Example usage
if __name__ == "__main__":
    input_example = [
        " _ ",
        "| |",
        "|_|",
        "   "
    ]
    print(convert(input_example))  # Should print "0"
