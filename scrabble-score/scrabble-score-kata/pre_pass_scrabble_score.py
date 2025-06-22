"""A pre-pass solution for the Scrabble score kata."""

# --------------------
# INPUT
# --------------------
# String `word` representing a word in Scrabble.

# --------------------
# VALIDATIONS
# --------------------
# If the input is null or not a string, return 0.

# --------------------
# OUTPUT
# --------------------
# Integer value for the score of the word.

# --------------------
# REQUIREMENTS
# --------------------
# Letters from the English alphabet are used.
# The score for each letter is as follows:
# A, E, I, O, U, L, N, S, T, R, D = 1 point each
# G = 2 points
# B, C, M, P = 3 points each
# F, H, V, W, Y = 4 points each
# K = 5 points
# J, X = 8 points each
# Q, Z = 10 points each