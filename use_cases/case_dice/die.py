from random import randint


class Die:
    """Represents a die"""

    def __init__(self, num_sides=6):
        """Initializer"""
        self.num_sides = num_sides

    def roll(self):
        """Return random int between 1 and number of sides"""
        return randint(1, self.num_sides)
