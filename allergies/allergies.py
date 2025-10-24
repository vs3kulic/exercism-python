"""This module contains the Allergies class which determines allergies based on a score."""

ALLERGENS = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}

class Allergies:
    """Determines allergies based on a given score."""

    def __init__(self, score):
        """Initialize the Allergies instance with a score."""
        self.score = score

    def allergic_to(self, item):
        pass

    @property
    def lst(self):
        pass
