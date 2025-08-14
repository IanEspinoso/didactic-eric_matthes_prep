"""Class representing a car."""
## Import the battery library
from battery import Battery

class Car:
    """Simple attempt to representing a car."""

    def __init__(self, make, model, year):
        """Initialize the attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Returns a descriptive name, elegantly formated."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Displays a sentence showing the the car's mileage."""
        print(f"This car has {self.odemeter_reading} miles on it.")

    def update_odometer(self, mileage):
        """Redefines the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rol back an odometer!")

    def increment_odometer(self, miles):
        """Adds a given amount to the odometer reading."""
        self.odometer_reading += miles

## Code an electric car.

class ElectricCar(Car):
    """Represents aspects of the car, specific from electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initializes the attributes from the father-class.
        Then, initializes the specific attributes from electric vehicles.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def upgrade_battery(self):
        """
        Verifies the size of the battery, setting its capacity as 65, 
        if necessary.
        """
        if self.battery.battery_size < 65:
            self.battery.battery_size = 65