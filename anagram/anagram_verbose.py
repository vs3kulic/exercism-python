"""
A module to find anagrams of a given word from a list of candidates.
"""

def find_anagrams(word, candidates):
    """
    Find all anagrams of a given word from a list of candidates.

    param word: str representing the word to find anagrams for.
    param candidates: list of strings representing the candidates to check against.
    return: list of strings representing the anagrams of the given word found in the candidates.
    """
    not_anagram = [candidates.remove(candidat) for candidat in candidates if candidat.lower() == word.lower()]
    sorted_word = sorted(list(word.lower()))
    sorted_candidates = [sorted(list(candidate.lower())) for candidate in candidates]
    anagrams = [candidate for candidate, sorted_candidate in zip(candidates, sorted_candidates) if sorted_candidate == sorted_word]
    
    return anagrams
