"""Clean, modular OCR Numbers solution."""

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

# =============================================================================
# PUBLIC API
# =============================================================================

def convert(input_grid: list[str]) -> str:
    """Convert OCR grid to recognized digits."""
    validate_input(input_grid)
    groups = split_into_groups(input_grid)
    results = [process_single_group(group) for group in groups]
    return ",".join(results)

# =============================================================================
# PRIVATE HELPERS
# =============================================================================

def validate_input(input_grid: list[str]) -> None:
    """Validate that input grid has correct dimensions."""
    if len(input_grid) % DIGIT_HEIGHT != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    for line in input_grid:
        if len(line) % DIGIT_WIDTH != 0:
            raise ValueError("Number of input columns is not a multiple of three")

def split_into_groups(input_grid: list[str]) -> list[list[str]]:
    """Split input grid into 4-row groups."""
    number_groups = len(input_grid) // DIGIT_HEIGHT
    groups = []
    
    for group_idx in range(number_groups):
        start_row = group_idx * DIGIT_HEIGHT
        end_row = start_row + DIGIT_HEIGHT
        group_grid = input_grid[start_row:end_row]
        groups.append(group_grid)
    
    return groups

def process_single_group(group_grid: list[str]) -> str:
    """Process a single 4-row group and return the recognized digits."""
    grid_width = len(group_grid[0])
    number_of_digits = grid_width // DIGIT_WIDTH
    
    matched_digits = ""
    
    for digit_pos in range(number_of_digits):
        digit_pattern = extract_digit_pattern(group_grid, digit_pos)
        found_digit = lookup_digit(digit_pattern)
        matched_digits += found_digit
    
    return matched_digits

def extract_digit_pattern(group_grid: list[str], digit_pos: int) -> list[str]:
    """Extract the pattern for a single digit from a 4-row group."""
    start_col = digit_pos * DIGIT_WIDTH
    end_col = start_col + DIGIT_WIDTH
    
    digit_pattern = []
    for row in group_grid:
        digit_row = row[start_col:end_col]
        digit_pattern.append(digit_row)
    
    return digit_pattern

def lookup_digit(digit_pattern: list[str]) -> str:
    """Look up a digit pattern in the known patterns dictionary."""
    for digit, pattern in PATTERN_TO_DIGIT.items():
        if digit_pattern == pattern:
            return digit
    return "?"  # Unknown pattern
