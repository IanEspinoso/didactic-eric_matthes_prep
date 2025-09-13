class Employee:
    """Simple class with basic employee attributes."""

    def __init__(self, name, family_name, salary):
        """Basic initialization of features."""
        self.name = name
        self.family_name = family_name
        self.salary = salary

    def give_raise(self, increase=5000):
        """Salary raise function"""
        self.salary += increase
        return self.salary