# Rules

number tokens at even indices (0, 2, 4...) must be integers
operation tokens at odd indices (1, 3, 5...) must be valid operations
    
## Number Token Validation
    raise ValueError if:
    1. First token is an operation (syntax error). Example: ["plus", "3"] → initial operation
    2. First token is non-numeric word (unknown operation). Example: ["foo", "3"] → invalid starting word
    3. Non-number in later even positions (syntax error). Example: ["5", "plus", "bar"] → "bar" isn't a number
    
## Operation Token Validation
    raise ValueError if:
    1. Unknown operation word (unknown operation). Example: ["5", "cubed"] → "cubed" not in valid operations
    2. Numeric value in operation position (syntax error). Example: ["5", "3", "plus"] → "3" is a number
    3. Valid operation that's also numeric (syntax error). Example: ["5", "2"] if "2" is a valid operation