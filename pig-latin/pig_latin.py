def translate_word(word):
    """
    Translate a word into Pig Latin.
    """
    vowels = ("a", "e", "i", "o", "u")
    extras = ("xr", "yt")
    consonant_cluster = []

    if word.startswith(vowels) or word.startswith(extras):
        return word + "ay"
    
    while word and word[0] not in vowels:
        if word.startswith("qu"):
            consonant_cluster += word[:2]
            word = word[2:]
        else:
            consonant_cluster += word[0]
            word = word[1:]

        # Treat 'y' as a vowel if it appears after the initial consonants
        if consonant_cluster and word.startswith("y"):
            break

    return word + "".join(consonant_cluster) + "ay"

def translate(text):
    """
    Translate text to pig latin.
    """
    words = text.split() # Split the text into words by spaces and store in a list
    translated_words = [translate_word(word) for word in words] 
    return " ".join(translated_words)