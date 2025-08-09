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