"""This module contains the Allergies class which determines allergies based on a score."""

ALLERGENS = {
    "cats": 128,
    "pollen": 64,
    "chocolate": 32,
    "tomatoes": 16,
    "strawberries": 8,
    "shellfish": 4,
    "peanuts": 2,
    "eggs": 1,
}


class Allergies:
    """Determines allergies based on a given score."""

    def __init__(self, score: int) -> None:
        """Initialize the Allergies instance with a score."""
        self.score = score

    def _build_allergy_list(self) -> list[str]:
        """Helper method to build the list of allergies based on the score."""
        # Normalize score to valid range (0-255)
        remaining_score = self.score % 256

        # Build list of allergens using greedy subtraction from highest to lowest
        allergies = []
        for allergen, value in ALLERGENS.items():
            if remaining_score >= value:
                remaining_score -= value
                allergies.append(allergen)
        return allergies

    def allergic_to(self, item: str) -> bool:
        """Check if allergic to a specific item.
        
        :param item: The allergen to check
        :type item: str
        :returns: True if allergic to the item, False otherwise
        :rtype: bool
        """
        # Check if the item is a known allergen
        return item in self._build_allergy_list()

    @property
    def lst(self):
        """Get the list of allergies based on the score."""
        return self._build_allergy_list()

def main():
    """Main function to demonstrate the Allergies class."""
    allergy_score = 509
    allergen = "Peanuts"
    patient = Allergies(allergy_score)
    print(f"Allergic to {allergen.lower()}: {patient.allergic_to(allergen)}")

if __name__ == "__main__":
    main()
