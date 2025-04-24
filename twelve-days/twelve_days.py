"""
A module to generate the lyrics of the song "The Twelve Days of Christmas".
The song describes a series of gifts given on each day of Christmas.
"""

def recite(start_verse, end_verse):
    """
    Function to generate the lyrics of "The Twelve Days of Christmas" song.
    
    Args:
        start_verse (int): The starting verse number (1-12).
        end_verse (int): The ending verse number (1-12).
    Returns:
        list: A list of strings, each string is a verse of the song.
    Raises:
        ValueError: if start_verse is greater than end_verse.
    Example:
        >>> recite(1, 1)
        ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."]
        >>> recite(3, 1) 
        start_verse cannot be greater than end_verse.
    """
    if start_verse > end_verse:
        raise ValueError("start_verse cannot be greater than end_verse.")

    # List to store the verses
    song = []

    # List of gifts
    gifts = (
        "a Partridge in a Pear Tree.", "two Turtle Doves", "three French Hens", 
        "four Calling Birds", "five Gold Rings", "six Geese-a-Laying", 
        "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", 
        "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"
    )

    # Tuple with ordinal numbers
    ordinals = (
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    )

    # Template for the verse
    template = "On the {day} day of Christmas my true love gave to me: {gifts}"

    # Iterate through the verses
    for verse in range(start_verse, end_verse + 1):
        # Collect gifts for the current verse in reverse order
        gifts_list = list(gifts[verse-1::-1])

        # Add "and" before the last gift if there are multiple gifts
        if len(gifts_list) > 1:
            gifts_list[-1] = "and " + gifts_list[-1]

        # Join the gifts with a comma and space
        gifts_str = ", ".join(gifts_list)

        # Format the verse
        verse_str = template.format(day = ordinals[verse-1], gifts = gifts_str)

        # Add the verse to the song
        song.append(verse_str)

    return song

print(recite(2, 2))