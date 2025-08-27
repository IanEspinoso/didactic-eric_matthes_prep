from pathlib import Path

## Exercise 10.1

<<<<<<< HEAD
"""path = Path('learning_python.txt')
=======
path = Path('learning_python.txt')
>>>>>>> a41de5f (Finish exercises from page 243)
contents = path.read_text()
"print(contents)" # First, direct reading

lines = contents.splitlines()
<<<<<<< HEAD
for line in lines: # Second, reading line by line
=======
"""for line in lines: # Second, reading line by line
>>>>>>> a41de5f (Finish exercises from page 243)
    print(line)"""


## Exercise 10.2

"print(contents.replace('Python', 'C'))"


## Exercise 10.3

"""for line in contents.splitlines():
    print(line)"""


## Exercise 10.4

<<<<<<< HEAD
"""answer = input("What's your name?")
path = Path('guest.txt')
path.write_text(answer)"""
=======

>>>>>>> a41de5f (Finish exercises from page 243)


## Exercise 10.5

<<<<<<< HEAD
"""another = 'y'
new_guest = ''

while another == 'y':
    new_guest += input('Enter new guest name.')
    new_guest += '\n'
    another = input('Another? (y/n)')

guests = Path('guests_book.txt')
guests.write_text(new_guest)
guests.read_text()"""
=======

>>>>>>> a41de5f (Finish exercises from page 243)


## Exercise 10.6

<<<<<<< HEAD
"""try:
    n1 = input("Enter the first number")
    n1 = int(n1)
    n2 = input("Enter the second number")
    n2 = int(n2)
    print(f"The sum is {n1 + n2}")
except ValueError:
    print("The numbers should be integers, not strings.")"""
=======

>>>>>>> a41de5f (Finish exercises from page 243)


## Exercise 10.7

<<<<<<< HEAD
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
=======

>>>>>>> a41de5f (Finish exercises from page 243)


## Exercise 10.8

<<<<<<< HEAD
"""try:
    print("\nThis are the cats:")
    for cat in Path('cats.txt').read_text().splitlines():
        print(cat)
    print("\nThis are the dogs:")
    for dog in Path('dogs.txt').read_text().splitlines():
        print(dog)
except FileNotFoundError:
    print("File Not Found: document does not exists or is elsewhere.")"""
=======
>>>>>>> a41de5f (Finish exercises from page 243)



## Exercise 10.9

<<<<<<< HEAD
"""try:
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
=======

>>>>>>> a41de5f (Finish exercises from page 243)


## Exercise 10.10

<<<<<<< HEAD
def most_frequent_word(path):
    """Returns the word with the highest count in a txt."""
   
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

print('helo world')
=======


>>>>>>> a41de5f (Finish exercises from page 243)

## Exercise 10.11




## Exercise 10.12




## Exercise 10.13




## Exercise 10.14



