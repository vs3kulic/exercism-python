"""A module to recite the nursery rhyme 'This is the House that Jack Built'."""

mapping = [
    ("house", "Jack built"),
    ("malt", "lay"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow", "with the crumpled horn that tossed"),
    ("maiden", "all forlorn that milked"),
]

def recite(start_verse: int, end_verse: int) -> list[str]:
    """Recite the verses
    
    param start_verse: The starting verse number
    param end_verse: The ending verse number
    return: A list of verses from start_verse to end_verse
    """
    verse = []

    for line in mapping:
        verse.append(f"This is the {line[start_verse-1]} that {line[end_verse]}.")

    return verse
    
print(recite(1, 1))