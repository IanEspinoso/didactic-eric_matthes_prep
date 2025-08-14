"""Simple class attempting to represent dice."""

class Die:
    """Simple class attempting to represent dice."""
    from random import randint

    def __init__(self, sides):
        """Initializes the class attributes."""
        self.sides = sides

    def roll_die(self):
        """Rolls a random number, depending on the number of sides."""
        return randint(1, self.sides)