## Create a class callde Restaurant, receiving two attributes in its init

class Restaurant:
    """My first class: a restaurant synthetizer."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes name and type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.people_served = 0


## Create two functions within it, calling its attributes

    def describe_restaurant(self):
        """Describes the restaurant, using the given attributes."""
        description = f"{self.restaurant_name.title()} specialty is "\
              f"{self.cuisine_type} cuisine."
        return description

    def open_restaurant(self):
        """Tells if the restaurant is open or not"""
        print("The restaurant is open.")

## Create a method that allows to define the number of people served.

    def set_number_served(self, people_served):
        """Sets the number of people served."""
        self.people_served = people_served

## Create a method that increments that number.

    def increment_number_served(self, more_people_served):
        """Increments the number of people served by a given amount."""
        self.people_served += more_people_served

## Create a class that inherits attributes from another class

class IceCreamStand(Restaurant):
    """Restaurant class daughter, with ice cream specificities."""


    def __init__(self, restaurant_name, 
                 cuisine_type='ice cream stand', *flavors):
        """Initalize the ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

## Create a method in that class that displays the flavors:

    def display_flavors(self):
        """Displays the flavors."""
        print("This are our available flavors:")
        for flavor in self.flavors:
            print(f"{flavor.title()}")