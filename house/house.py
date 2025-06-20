"""A module to recite the nursery rhyme 'This is the House that Jack Built'."""
# Dictionary of tuples to hold the verse data
verse_data = {
    1: ("house", "Jack built"),
    2: ("malt", "lay in"),
    3: ("rat", "ate"),
    4: ("cat", "killed"),
    5: ("dog", "worried"),
    6: ("cow with the crumpled horn", "tossed"),
    7: ("maiden all forlorn", "milked"),
    8: ("man all tattered and torn", "kissed"),
    9: ("priest all shaven and shorn", "married"),
    10: ("rooster", "crowed in the morn that woke"),
    11: ("farmer sowing his corn", "kept"),
    12: ("horse and the hound and the horn", "belonged to"),
}

# Constants for the prefix and verse limits
PREFIX = "This is "
MIN_VERSE = 1
MAX_VERSE = len(verse_data)

# Main function to recite the verses
def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite multiple verses
    
    param: start_verse: The starting verse number (1-indexed).
    param: end_verse: The ending verse number (1-indexed).

    return: a list of strings containing the verses from start_verse to end_verse.
    """
    # Validate the input verse numbers
    if start_verse < MIN_VERSE or start_verse > MAX_VERSE or end_verse < MIN_VERSE or end_verse > MAX_VERSE:
        raise ValueError("Verse numbers must be between 1 and 12 inclusive.")
    if start_verse > end_verse:
        raise ValueError("Start verse must be less than or equal to end verse.")

    # Initialize an empty list to hold the verses
    verses = []

    # Loop through verses, building them by calling the helper function
    for verse in range(start_verse, end_verse + 1):
        single_verse = build_single_verse(verse)
        verses.append(single_verse)

    return verses

# Helper function to build a single verse recursively
def build_single_verse(verse_number: int) -> str:
    """Build a single verse recursively"""
    # Base case for recursion
    if verse_number == 1:
        return "This is the house that Jack built."

    # Unpack the current item and action from the verse data
    current_item, current_action = verse_data[verse_number]
    
    # Recursively build the previous verse and remove the prefix to get the tail
    previous_verse = build_single_verse(verse_number - 1) # Recursive call to get the previous verse
    previous_tail = previous_verse.removeprefix(PREFIX)

    return f"This is the {current_item} that {current_action} {previous_tail}"
