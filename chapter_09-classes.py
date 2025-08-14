from restaurant import Restaurant, IceCreamStand
from battery import Battery
from car import ElectricCar, Car
from user import User, Admin

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

## Instantiate the ice cream stand, and test it

napoletice = IceCreamStand('napoletice', 'ice cream stand', 
                           'strawberry', 'vanilla', 'chocolate')
napoletice.display_flavors()

## Instantiate the admin, and test it

the_boss = Admin('bruce', 'wayne', 
                 'creates other users', 'sees all the backlog',
                 'access to admin dashboard', city='gotham')

the_boss.show_privileges()

## Instantiate the electric car, and use the upgrade battery function.

my_green_car = ElectricCar('sonya', 'v0.1', 1898)

my_green_car.battery.get_range()

print('Now updating...')

my_green_car.upgrade_battery()

my_green_car.battery.get_range()