## Create a function called display_message() that tells what I'm learning

def display_message():
    """Display a message telling what I'm learning"""
    print("I'm learning how to code functions!")

display_message()


## Write  a function called favorite_book(), with a parameter and a message

def favorite_book(title):
    """Display the title of your favorite book"""
    print(f"My favorite book is {title.title()}.")

favorite_book('the fellowship of the ring')

## Write a function with two variables

def make_shirt(size, frase):
    """Display the size of your shirt with a sentence to be printed on it"""
    print(f"You requested a {size} sized shirt with the sentence"\
          f" '{frase}' printed out on it.")
    
## Call the previous function using positional arguments

make_shirt('medium', 'the dude abides')


## Call the same function, now using the named arguments (use the switcheroo)

make_shirt(frase='one does not simply...', size='large')


## Modify the previous function, stablishing standard values

def make_shirt(size='medium', frase='Dobby loves Python'):
    """Display the size of your shirt with a sentence to be printed on.
    Update: function now contains pre-defined values"""
    print(f"You requested a {size} sized shirt with the sentence"\
          f" '{frase}' printed out on it.")
    

## Call it three different ways

# Standard
make_shirt()

# One modified argument
make_shirt(frase='One does not simply walks to Mordor')

# Both arguments modified, making use of the position freedom
make_shirt(frase='Never gonna give you up.', size='humongous')

## Create a function for describing a city in its country, with a standard value

def describe_city(city, country='brazil'):
    """Describes a city in its country"""
    print(f"{city.title()} is a city in {country.title()}.")

## Call it three different ways

describe_city('salvador')

describe_city('rio de janeiro')

describe_city(city='oslo', country='norway')