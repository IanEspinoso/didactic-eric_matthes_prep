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


## Write a similar function, and call it using user inputs

def get_city_info(city, country, state=None):
    """Display a simple message about a city, using state and country"""
    city_info = {'city': city, 'country': country}
    if state:
        city_info['state'] = state
    return(city_info)

while True:
    print("\nPlease, provide me some information about your city!"\
    "\nIf you wish to proceed without providing info, simply press 'Enter'."\
    "\nIf you wish to stop the program altogether, type 'q', and press 'Enter'")
    city = input("What is the name of the city? (this is required)")
    if city == '' or city == 'q':
        city = None
        break
    state = input("What is the name of the state?")
    if state == 'q':
        state = None
        break
    country = input("What is the name of the country? (this too is required)")
    if country == 'q' or country == '':
        country = None
        break

    city_info = get_city_info(city, country, state)
    if state:
        print(f"{city_info['city'].title()} is a city in "\
        f"{city_info['state'].title()}, {city_info['country'].title()}.")
    else:
        print(f"{city_info['city'].title()} is a city in "\
              f"{city_info['country'].title()}.")