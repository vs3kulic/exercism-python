# CALL 1: build_single_verse(3) starts
def build_single_verse(3):
    # verse_number = 3
    if 3 == 1:  # No, continue
    
    current_item = "rat"
    current_action = "ate" 
    
    # "I need verse 2 to continue!" - MAKES ANOTHER CALL
    previous_verse = build_single_verse(2)  # ← PAUSE HERE, go do this first!
    
    # [Function 1 PAUSES and waits...]

    # CALL 2: build_single_verse(2) starts  
    def build_single_verse(2):
        # verse_number = 2
        if 2 == 1:  # No, continue
        
        current_item = "malt"
        current_action = "lay in"
        
        # "I need verse 1 to continue!" - MAKES ANOTHER CALL
        previous_verse = build_single_verse(1)  # ← PAUSE HERE, go do this first!
        
        # [Function 2 PAUSES and waits...]

        # CALL 3: build_single_verse(1) starts
        def build_single_verse(1):
            # verse_number = 1  
            if 1 == 1:  # YES! BASE CASE!
            return "This is the house that Jack built."  # ← DONE! Go back up!
        
        # [Function 2 RESUMES with the result]
        previous_tail = "the house that Jack built."  # (after removing "This is ")
        return f"This is the malt that lay in {previous_tail}"
        # Returns: "This is the malt that lay in the house that Jack built."
    
    # [Function 1 RESUMES with the result]
    previous_tail = "the malt that lay in the house that Jack built."  # (after removing "This is ")
    return f"This is the rat that ate {previous_tail}"
    # Returns: "This is the rat that ate the malt that lay in the house that Jack built."