"""
Simple API for the Grains of Wheat problem.
"""
from grains import square, total

# Get the number of grains on specific squares
a = 5
b = square(a)

print(f"Number of grains on square {a}: {b}")

# Get the total number of grains on a chessboard
c = total()
print(f"Total number of grains on a chessboard: {c}")


# Error handling for invalid square number
try:
    square(65)
except ValueError as e:
    print(f"Error: {e}")
