def find_anagrams(word, candidates):
    not_anagram = [candidates.remove(candidat) for candidat in candidates if candidat.lower() == word.lower()]
    sorted_word = sorted(list(word.lower()))
    sorted_candidates = [sorted(list(candidate.lower())) for candidate in candidates]
    anagrams = [candidate for candidate, sorted_candidate in zip(candidates, sorted_candidates) if sorted_candidate == sorted_word]
    
    return anagrams
