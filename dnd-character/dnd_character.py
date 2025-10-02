"""This module contains the Character class and functions for Dungeons & Dragons characters."""
import random

# ----------------------------
# CONSTANTS
# ----------------------------
NUMBER_OF_DICE = 4
INITIAL_HITPOINTS = 10
DICE_MIN = 1
DICE_MAX = 6 # 6-sided dice

class Character:
    """Dungeons & Dragons character with abilities and hit points."""
    def __init__(self):
        self.strength = self.ability() # set attr value by calling (class) method
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = INITIAL_HITPOINTS + modifier(self.constitution)

    def ability(self):
        """Generate a random ability score using 4d6 drop lowest method."""
        dice_rolls = (random.randint(DICE_MIN, DICE_MAX) for _ in range(NUMBER_OF_DICE)) # creates generator object
        dice_results = sorted(dice_rolls) # sorts low-to-high and returns a list
        ability = sum(dice_results[1:]) # drop lowest
        return ability

def modifier(ability_score: int) -> int:
    """Modify an ability score to its corresponding modifier."""
    modifier_value = (ability_score - INITIAL_HITPOINTS) // 2 # round down
    return modifier_value

# ----------------------------
# DEMONSTRATION
# ----------------------------

def main():
    """Main function to demonstrate the Character class."""
    char = Character()
    print("Character Abilities and Modifiers:")
    print(f"Strength: {char.strength}, Modifier: {modifier(char.strength)}")
    print(f"Dexterity: {char.dexterity}, Modifier: {modifier(char.dexterity)}")
    print(f"Constitution: {char.constitution}, Modifier: {modifier(char.constitution)}")
    print(f"Intelligence: {char.intelligence}, Modifier: {modifier(char.intelligence)}")
    print(f"Wisdom: {char.wisdom}, Modifier: {modifier(char.wisdom)}")
    print(f"Charisma: {char.charisma}, Modifier: {modifier(char.charisma)}")
    print(f"Hitpoints: {char.hitpoints}")

if __name__ == "__main__":
    main()
