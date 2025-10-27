"""This module contains the Allergies class which determines allergies based on a score."""

ALLERGIES = {
    "eggs": 1, # lowercase for consistency
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128
}


class Allergies:
    """Determines allergies based on a given score."""
    def __init__(self, score):
        """Initialize the Allergies instance with a score."""
        self.score = score

    def allergic_to(self, item):
        """Check if allergic to a specific item 
        using bitwise AND operation.
        
        :param item: The allergen to check
        :type item: str
        :returns: True if allergic to the item, False otherwise
        :rtype: bool
        """
        return self.score & ALLERGIES[item] != 0

    @property
    def lst(self):
        """Get the list of allergies based on the score."""
        return [allergy for allergy in ALLERGIES
                if self.allergic_to(allergy)
        ]

def main():
    """Main function to demonstrate the Allergies class."""
    allergy_score = 509
    patient = Allergies(allergy_score)
    allergen = "peanuts"
    print(f"Allergic to {allergen}: {patient.allergic_to(allergen)}")

if __name__ == "__main__":
    main()
