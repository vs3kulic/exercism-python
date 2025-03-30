"""
A module to find anagrams of a given word from a list of candidates.
"""

def find_anagrams(word, candidates):
    """
    Find all anagrams of a given word from a list of candidates.

    Parameters:
    word (str): The word to find anagrams for.
    candidates (list of str): The candidates to check against.
    Returns:
    list of str: The anagrams of the given word found in the candidates.
    """
    # Convert the word to lowercase and sort its characters
    sorted_word = sorted(word.lower())
    
    # Filter candidates that are not the same word and are anagrams
    anagrams = [candidate for candidate in candidates 
                if candidate.lower() != word.lower() 
                and sorted(candidate.lower()) == sorted_word]
    
    return anagrams