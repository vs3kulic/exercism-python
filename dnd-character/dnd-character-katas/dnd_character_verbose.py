"""This module contains the Character class and functions for Dungeons & Dragons characters."""
from random import randint

class Character:
    """Dungeons & Dragons character with abilities and hit points."""
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Generate a random ability score using 4d6 drop lowest method."""
        result = [randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)]
        result.remove(min(result))
        return sum(result)

def modifier(num: int) -> int:
    """Modify an ability score to its corresponding modifier."""
    ans = (num - 10) // 2
    return ans
