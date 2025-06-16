"""This is a pre-pass approach to the word count kata."""

# ---------------------------------
# Understanding the problem – I/O:
# ---------------------------------
# INPUT is a string containing words, punctuation, and whitespace.
INPUT = "First: don't laugh. Then: don't cry. You're getting it."

# OUTPUT is a dictionary where each key is a word (case-insensitive)
# and the value is the word count.
OUTPUT = {
        "first": 1,
        "don't": 2,
        "laugh": 1,
        "then": 1,
        "cry": 1,
        "you're": 1,
        "getting": 1,
        "it": 1,
        }

# --------------
# Requirements:
# --------------
# Words properties:
# - case-insensitive (e.g. _Hello_ and _hello_ are the same word).
# - separated by punctuation (e.g. ":", "!", or "?") or whitespace (e.g. "\t", "\n", or " ").
# - include apostrophes (e.g. _don't_, _you're_) or hyphens (e.g. _mother-in-law_)
# - can also be Numbers (e.g. _123_ is a word).

# Words count:
# - as single units, even if they contain punctuation, hyphens or special characters.
# - regardless of their position, length or frequency (e.g. _the_ is counted multiple times).
