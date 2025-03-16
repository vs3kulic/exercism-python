"""
Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Check README.md for more information. 
"""

def response(hey_bob):
    """
    Returns Bob's response to a given input.
    """

    hey_bob = hey_bob.strip()
    
    if not hey_bob:
        return "Fine. Be that way!"
    
    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    
    if hey_bob.endswith("?"):
        return "Sure."
    return "Whatever."