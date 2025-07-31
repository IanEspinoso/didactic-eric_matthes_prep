# Bind a message to a variable
message = "a new message"
# Print the message
print(message)

# Store and print a name of a very good person
person_name = "Samwise Gamgee"
# print(f"Hi {person_name}, would you like to learn some Python today?")
print(f"\t {person_name.title()} is the name properly writen. \n we call him {person_name.lower()}, shily... \n we call him {person_name.upper()}, yelling!")

# Store and print a famous person and citation from her
famous_person = "ada lovelace"
ada_quote = "The analytical engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform."
print(f"{famous_person.title()} once said: '{ada_quote}")

# Use the string strip functions
whitespaced = "\n  Joaozinho \tda Silva "
print(whitespaced)
print(whitespaced.lstrip())
print(whitespaced.rstrip())
print(whitespaced.strip())

# Playing with suffixes
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))

# Working with mathematical operations and strings
mult8, div8 = 2 * 4, int(4 / (0.5))
print("5 + 3=", 5 + 3, "\n10.000 - 9.992=", 10_000 - 9_992, "\n2 x 4=", mult8, "\n4 / (0.5)=", div8)

# Some exercises are being executed ahead of the book prompt, like adding comments as this (page 65)

# Read the Zen of Python
import this