from pathlib import Path
import json

## Exercise 10.1

"""path = Path('learning_python.txt')

contents = path.read_text()
"print(contents)" # First, direct reading

lines = contents.splitlines()

for line in lines: # Second, reading line by line
    print(line)"""


## Exercise 10.2

"""print(contents.replace('Python', 'C'))"""


## Exercise 10.3

"""for line in contents.splitlines():
    print(line)"""


## Exercise 10.4

"""answer = input("What's your name?")
path = Path('guest.txt')
path.write_text(answer)"""


## Exercise 10.5

"""another = 'y'
new_guest = ''

while another == 'y':
    new_guest += input('Enter new guest name.')
    new_guest += '\n'
    another = input('Another? (y/n)')

guests = Path('guests_book.txt')
guests.write_text(new_guest)
guests.read_text()"""


## Exercise 10.6

"""try:
    n1 = input("Enter the first number")
    n1 = int(n1)
    n2 = input("Enter the second number")
    n2 = int(n2)
    print(f"The sum is {n1 + n2}")
except ValueError:
    print("The numbers should be integers, not strings.")"""


## Exercise 10.7

"""n1, n2 = 0, 0

while True:
    try:
        n1 = input("Enter the first number ('q' to quit)")
        if n1 == 'q':
            break
        n1 = int(n1)
        n2 = input("Enter the second number ('q' to quit)")
        if n2 == 'q':
            break
        n2 = int(n2)
        print(f"The sum is {n1 + n2}")
    except ValueError:
        print("The numbers should be integers, not strings.")"""


## Exercise 10.8

"""try:
    print("\nThis are the cats:")
    for cat in Path('cats.txt').read_text().splitlines():
        print(cat)
    print("\nThis are the dogs:")
    for dog in Path('dogs.txt').read_text().splitlines():
        print(dog)
except FileNotFoundError:
    print("File Not Found: document does not exists or is elsewhere.")


## Exercise 10.9

try:
    cats =  Path('cats.txt').read_text().splitlines()
    print("\nThis are the cats:")
    for cat in cats:
        print(cat)
    dogs = Path('dogs.txt').read_text().splitlines()
    print("\nThis are the dogs:")
    for dog in dogs:
        print(dog)
except FileNotFoundError:
    pass"""


## Exercise 10.10

"""def most_frequent_word(path):
    """"Returns the word with the highest count in a txt.""""
   
    try:
        text = Path(path).read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, {path} could not be found.")
    else:
        words = text.split()
        lower_words = [word.lower() for word in words]
        unique_words = set(lower_words)
        occurrence_count = dict.fromkeys(unique_words)
        for key in occurrence_count:
            occurrence_count[key] = text.count(key)
        max_value = max(occurrence_count.values())
        for key, value in occurrence_count.items():
            if max_value == value:
                max_key = key

    max_dict = {max_key: max_value}
    
    return max_dict

moby_dick_word = most_frequent_word('moby_dick.txt')

print('helo world')"""


## Exercise 10.11

# request value

#path = Path('favorite_number.json')

#def get_new_number(path):
"""Requests a new favorite number."""

"""    f_number = input("What is your favorite number?")
    contents = json.dumps(f_number)
    path.write_text(contents)

get_new_number(path)"""

# read value

#def get_stored_number(path):
"""Gets the stored favorite number, if available."""

"""    if path.exists():
        contents = path.read_text()
        f_number = json.loads(contents)
        print(f"I know your favorite number! It is {f_number}.")
    else:
        prinnt("I don't know your favorite number yet!")

get_stored_number(path)"""


## Exercise 10.12

# both in a single function

#def favorite_number():
"""Tells your favorite number, if stored, and requests it, if not."""

"""    path = Path('favorite_number.json')
    if path.exists():
        contents = path.read_text()
        f_number = json.loads(contents)
        print(f"I know your favorite number! It is {f_number}.")
    else:
        f_number = input("What is your favorite number?")
        contents = json.dumps(f_number)
        path.write_text(contents)
        print(f"We'll remember your favorite number is {f_number}!")

favorite_number()"""


## Exercise 10.13

#def remember_me():
"""Gather information on the user, and stores it into a dictionary."""
"""
    path = Path('remember_me.json')
    if path.exists():
        contents = path.read_text()
        me_info = json.loads(contents)
        print("Your information is:")
        for key,val in me_info.items():
            print(f"Your {key} is {val}.")
    else:
        info_remembered = {}
        me_name = input('What is your name?')
        info_remembered['name'] = me_name
        proceed = 'y'
        while proceed == 'y':
            me_key = input('What do you want to tell about yourself? (ex: city, age, etc)')
            me_value = input('What about it?')
            info_remembered[me_key] = me_value
            proceed = input('Do you want to give another information? (y/n)')
        contents = json.dumps(info_remembered)
        path.write_text(contents)
"""
#remember_me()

## Exercise 10.14

#def get_new_user_name(path, info_remembered):
"""Gather information on a new user."""
"""
    proceed = 'y'
    while proceed == 'y':
        me_key = input('What do you want to tell about yourself? (ex: city, age, etc)')
        me_value = input('What about it?')
        info_remembered[me_key] = me_value
        proceed = input('Do you want to give another information? (y/n)')
    contents = json.dumps(info_remembered)
    path.write_text(contents)
"""

#def greet_user():
"""Greet a recorded user."""

"""    path = Path('remember_me.json')
    if path.exists():
        contents = path.read_text()
        me_info = json.loads(contents)
        info_remembered = {}
        me_name = input('What is your name?')
        info_remembered['name'] = me_name
        condition = info_remembered['name'] == me_info['name']
        if condition:
            print("Your information is:")
            for key,val in me_info.items():
                print(f"Your {key} is {val}.")
        else:
            get_new_user_name(path, info_remembered)


greet_user()"""