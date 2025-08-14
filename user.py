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