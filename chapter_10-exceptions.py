from pathlib import Path

## Exercise 10.1

"""path = Path('learning_python.txt')
contents = path.read_text()
"print(contents)" # First, direct reading

lines = contents.splitlines()
for line in lines: # Second, reading line by line
    print(line)"""


## Exercise 10.2

"print(contents.replace('Python', 'C'))"


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




## Exercise 10.7




## Exercise 10.8




## Exercise 10.9




## Exercise 10.10




## Exercise 10.11




## Exercise 10.12




## Exercise 10.13




## Exercise 10.14



