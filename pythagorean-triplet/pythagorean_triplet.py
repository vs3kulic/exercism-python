"""This module provides functions to generate Pythagorean triplets."""

def triplets_with_sum(number):
    triplets = []
    for a in range(1, number):
        for b in range(a, number - a):
            c = number - a - b
            if a * a + b * b == c * c:
                triplets.append([a, b, c])
    return triplets
