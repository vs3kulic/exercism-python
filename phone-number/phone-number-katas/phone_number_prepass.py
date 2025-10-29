"""This module contains the pre-pass notes for the Phone Number exercise."""

# ----------------------
# INPUT
# ----------------------
# A string that may contain digits, spaces, parentheses, dashes, dots, and alpha characters.
# Examples from the test suite:
# - "(223) 456-7890"
# - "223 456   7890   "
# - "+1 (223) 456-7890"
# - "523-abc-7890"
# - "1 (123) 456-7890"

# ----------------------
# VALIDATION
# ----------------------
# A valid phone number:
# - starts with an optional country code of "1" (US only)
# - has 10 digits: area code (3 digits) + exchange code (3 digits) + subscriber number (4 digits)
# - Examples:
#   "2234567890"
#   "12234567890" (with leading "1" country code)
# Before cleaning, raise an exception if any of the following conditions are met:
# - letters are present
# - punctuation is present
# After cleaning, raise an exception if any of the following conditions are met:
# - number has too few digits (less than 10)
# - number has too many digits (more than 11 with leading "1")
# - if eleven digits and the first digit is not "1"
# - area code is invalid - cannot start with 0 or 1
# - exchange code is invalid - cannot start with 0 or 1

# ----------------------
# PROCESSING
# ----------------------
# 1. Ingest the input (string) and check for invalid characters:
#    If letters are found, raise ValueError with message "letters not permitted".
#    If punctuations are found, raise ValueError with message "punctuations not permitted".
# 2. Remove all non-digit character, strip the leading "1" if present.
# 3. Check the length of the cleaned number:
#    If < 10 digits, raise ValueError with message "must not be fewer than 10 digits"
#    If > 11 digits, raise ValueError with message "must not be greater than 11 digits"
# 4. Split the cleaned number into area code, exchange code, and subscriber number.
# 5. Validate area code and exchange code:
#    If area code starts with "0" or "1", raise ValueError with message
#       "area code cannot start with zero" or "area code cannot start with one".
#    If exchange code starts with "0" or "1", raise ValueError with message
#       "exchange code cannot start with zero" or "exchange code cannot start with one".

# ----------------------
# OUTPUT
# ----------------------
# The number property should return the cleaned version of the phone number,
#   with only the digits and no formatting.
# The class should provide access to:
# - a property to get the full number as a string of digits
# - a property to get the area code (first three digits)
# - a pretty method that formats the number as "(NXX) NXX-XXXX"
# If the number is invalid, an error is raised or an error message is returned.
