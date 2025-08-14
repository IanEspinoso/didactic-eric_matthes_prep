class Battery:
    """Simple attepmt to model an electric car battery."""

    def __init__(self, battery_size=40):
        """Initializes the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Displays a message describing the battery's size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """
        Displays a sentence on the distance that the car run 
        with that battery.
        """
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")