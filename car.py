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

class ElectricCar(Car):
    """Represents aspects of the car, specific from electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initializes the attributes from the father-class.
        Then, initializes the specific attributes from electric vehicles.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
