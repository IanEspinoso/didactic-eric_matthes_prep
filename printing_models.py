## Create a function called display_message() that tells what I'm learning

def display_message():
    """Display a message telling what I'm learning"""
    print("I'm learning how to code functions!")

# display_message()


## Write  a function called favorite_book(), with a parameter and a message

def favorite_book(title):
    """Display the title of your favorite book"""
    print(f"My favorite book is {title.title()}.")

# favorite_book('the fellowship of the ring')

## Write a function with two variables

def make_shirt(size, frase):
    """Display the size of your shirt with a sentence to be printed on it"""
    print(f"You requested a {size} sized shirt with the sentence"\
          f" '{frase}' printed out on it.")
    
## Call the previous function using positional arguments

# make_shirt('medium', 'the dude abides')


## Call the same function, now using the named arguments (use the switcheroo)

# make_shirt(frase='one does not simply...', size='large')


## Modify the previous function, stablishing standard values

def make_shirt(size='medium', frase='Dobby loves Python'):
    """Display the size of your shirt with a sentence to be printed on.
    Update: function now contains pre-defined values"""
    print(f"You requested a {size} sized shirt with the sentence"\
          f" '{frase}' printed out on it.")
    

## Call it three different ways

# Standard
# make_shirt()

# One modified argument
# make_shirt(frase='One does not simply walks to Mordor')

# Both arguments modified, making use of the position freedom
# make_shirt(frase='Never gonna give you up.', size='humongous')


## Create a function for describing a city in its country, with a standard value

def describe_city(city, country='brazil'):
    """Describes a city in its country"""
    print(f"{city.title()} is a city in {country.title()}.")


## Call it three different ways

#describe_city('salvador')

#describe_city('rio de janeiro')

#describe_city(city='oslo', country='norway')


## Write a similar function, and call it using user inputs

def get_city_info(city, country, state=None):
    """Display a simple message about a city, using state and country"""
    city_info = {'city': city, 'country': country}
    if state:
        city_info['state'] = state
    return(city_info)

#while True:
#     print("\nPlease, provide me some information about your city!"\
#     "\nIf you wish to proceed without providing info, simply press 'Enter'."\
#     "\nIf you wish to stop the program altogether, type 'q', and press 'Enter'")
#     city = input("What is the name of the city? (this is required)")
#    if city == '' or city == 'q':
#         city = None
#         break
#     state = input("What is the name of the state?")
#    if state == 'q':
#         state = None
#         break
#     country = input("What is the name of the country? (this too is required)")
#    if country == 'q' or country == '':
#         country = None
#         break

#     city_info = get_city_info(city, country, state)
#    if state:
#         print(f"{city_info['city'].title()} is a city in "\
#         f"{city_info['state'].title()}, {city_info['country'].title()}.")
#    else:
#         print(f"{city_info['city'].title()} is a city in "\
#               f"{city_info['country'].title()}.")


## Create a list with a series of short messages

# short_quotes = ["lock and load", "affirmative", "you require more vespene gas"]


## Pass the list into a function that shows those messages

def show_messages(messages):
    """Display the messages given in a list."""
    for message in messages:
        print(message)

# show_messages(short_quotes)


## Create a function that passes the displayed messages to another list

# already_sent = []
def send_messages(messages_tasked, messages_sent):
    """Display the messages given in a list.
    Record the displayed messages in another list"""
    while messages_tasked:
        message = messages_tasked.pop()
        print(message)
        messages_sent.append(message)
        
# send_messages(short_quotes, already_sent)
# print("Those were the sent messages. Let's now show the remaining messages.")
# print(short_quotes)
# print("Now, the list of sent messages.")
# print(already_sent)


## Call the function in a way that the original list stays intact
# I'll have to redo it, since it got mangled by the function

# short_quotes = ["lock and load", "affirmative", "you require more vespene gas"]
# already_sent = []

def send_messages_new(messages_tasked, messages_sent):
    """Display the messages given in a list.
    Record the displayed messages in another list"""
    while messages_tasked:
        message = messages_tasked.pop()
        print(message)
        messages_sent.append(message)
        
# send_messages_new(short_quotes[:], already_sent[:])
# print("Those were the sent messages. Let's now show the original list.")
# print(short_quotes)
# print("Now, the original, empty, list of sent messages.")
# print(already_sent)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## Using *args, create a function that asks the user for a series of values

def building_materials(*materials):
    """Receive a list of materials and print them out."""
    print("In this stage of the construction, we'll use:")
    for material in materials:
        print(f"- {material.title()}")
    print("Let's get on with it, boys and gals!")

# building_materials('portland cement', 'gravel', 'water', 'rebar', 'mesh', 'block')
# building_materials('fine sand', 'rapid cement', 'lime')
# building_materials('tiles')


## Recreate the function that calls for city_info data to include a **kwargs

def get_city_info_new(city, country, state=None, **city_info):
    """Display a simple message about a city, using state and country"""
    city_info.update({'city': city, 'country': country})
    if state:
        city_info['state'] = state
    return(city_info)

# sao_paulo_info = get_city_info_new('sao paulo', 'brasil', population=11_900_000, founded=1554)

# print(sao_paulo_info)


## Create a function that stores information on plants
# This should include at least genera and species, but also **kwargs

def get_plant_info(species, genus='piper', **plant_info):
    """Organize and display information of plants, including genus and species.
    The default genus 'piper' can be changed, and other info might be added."""
    plant_info.update({'species': species, 'genus': genus.title()})
    return plant_info

# plant = get_plant_info('nigrum', popular_name='pimenta-do-reino', origin='Kerala')
# print(plant)


# I got ahead of myself, and ended up researching about the main plant genera
"""'piper' ,'nigrum', popular_name='pimenta-do-reino', origin='kerala'
'psychotria' ,'viridis', popular_name='chacrona', origin='amazon'
'ipomoea' ,'batatas', popular_name='batata doce', origin='peru'
'ficus' ,'carica', popular_name='figueira', origin='jordan'
'diospyros' , 'kaki', popular_name='caqui', origin='china'
'allium' ,'cepa', popular_name='cebola', origin='iran'
'syzygium' ,'aromaticum', popular_name='cravo', origin='indonesia'"""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## Cut and paste the previous functions in a doc called printing_models.py
## Then call them during the exercise
# import name_mdl
# from name_mdl import name_fnct
# from name_mdl import name_fnct as nf
# import name_mdl as nm
# from name_mdl import *



