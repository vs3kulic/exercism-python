"""This module contains the Character class and functions for Dungeons & Dragons characters."""
import random

ABILITIES = (
    'strength', 'dexterity', 'constitution',
    'intelligence', 'wisdom', 'charisma')

class Character:
    """Dungeons & Dragons character with abilities and hit points."""

    def __init__(self):
        # Dynamically set each ability as an attribute
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        # Calculate hitpoints based on constitution
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Generate a random ability score using 4d6 drop lowest method."""
        dices = sorted(random.randint(1, 6) for _ in range(4)) # sort lowest first (low-to-high)
        return sum(dices[1:])

def modifier(num: int) -> int:
    """Modify an ability score to its corresponding modifier."""
    ans = (num - 10) // 2
    return ans

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