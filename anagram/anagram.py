def find_anagrams(word, candidates):
    sorted_word = sorted(list(word))
    sorted_candidates = [sorted(list(candidate)) for candidate in candidates]
    anagrams = [candidate for candidate, sorted_candidate in zip(candidates, sorted_candidates) if sorted_candidate == sorted_word]
    
    return anagrams
