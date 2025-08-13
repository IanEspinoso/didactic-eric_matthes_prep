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

##Instantiate it and call it for testing

restaurant = Restaurant('the bear', 'sbasguetti')

print(restaurant.describe_restaurant())

restaurant.open_restaurant()


## Create three more instances of it, and call 'describe restaurant' for them

restaurant_1 = Restaurant('habibs', 'bad arab')

restaurant_2 = Restaurant('macdonalds', 'trash')

restaurant_3 = Restaurant('my mom', 'the best')

print(restaurant_1.describe_restaurant())

print(restaurant_2.describe_restaurant())

print(restaurant_3.describe_restaurant())


## Create a class called User using two attributes and a kwargs

class User:
    """Store and display user profile information."""

    def __init__(self, first_name, last_name, **kwargs):
        """Initializes the user's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.kwargs = kwargs
        self.login_attempts = 0
  
    def describe_user(self):
        """Simlpy displays the given attributes."""
        print(f"User name is {self.first_name.title()}"\
              f" {self.last_name.title()}")
        if self.kwargs:
            print("User attributes:")
            for key, value in self.kwargs.items():
                print(key, ":", value)

    def greet_user(self):
        """Send a personalized greeting message to the user."""
        print(f"Welcome back, {self.first_name.title()} {self.last_name.title()}!")

## Add a login attempts atribute in the User class and then create two methods
## One for incrementing it.

    def increment_login_attempts(self, increment):
        """Increments the number of login attempts."""
        self.login_attempts += increment


## Another for resetting it
    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0


## Create three instances of it and call both methods

user_0 = User('ian', 'espinoso')

user_1 = User('gandalf', 'the grey', daddy='eru iluvatar')

user_2 = User('escherichia', 'coli', 
              hometown='intestinal tract', reign='bacteria')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()


## Change the init method in Restaurant to include the number of people served
## It should have a default number of '0'
## Instantiate that class, then display the default number

restaurant = Restaurant('los pollos hermanos', 'mexican')
print(restaurant.people_served)


## Show that number again, after changing it directly.

restaurant.people_served = 1
print(restaurant.people_served)


## Call the method that allows to define the number of people served.

restaurant.set_number_served(10)
print(restaurant.people_served)


## Call the method that increments the number of people served.

restaurant.increment_number_served(10)
print(restaurant.people_served)


## Add a login attempts atribute in the User class and then create two methods
## Create two methods: one to update it, and another to reset it. Call them.

print(user_0.login_attempts)
user_0.increment_login_attempts(10)
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)

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

napoletice = IceCreamStand('napoletice', 'ice cream stand', 
                           'strawberry', 'vanilla', 'chocolate')
napoletice.display_flavors()

## Create an Admin class, daughter of User, with a privileges attribute

class Admin(User):
    """Class derived from User, with admin privileges."""

    def __init__(self, first_name, last_name, *privileges, **kwargs):
        """Initiates the Admin class."""
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = privileges

## Write a method called show_privileges(), instantiate and call it

    def show_privileges(self):
        """Displays listed privileges."""
        print("This are the admin privileges:")
        for privilege in self.privileges:
            print(privilege)

the_boss = Admin('bruce', 'wayne', 
                 'creates other users', 'sees all the backlog',
                 'access to admin dashboard', city='gotham')

the_boss.show_privileges()

## Code an electric car.

from car import Car

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

    def upgrade_battery(self):
        """
        Verifies the size of the battery, setting its capacity as 65, 
        if necessary.
        """
        if self.battery.battery_size < 65:
            self.battery.battery_size = 65


## Instantiate the electric car, and use the upgrade battery function.

my_green_car = ElectricCar('sonya', 'v0.1', 1898)

my_green_car.battery.get_range()

print('Now updating...')

my_green_car.upgrade_battery()

my_green_car.battery.get_range()

