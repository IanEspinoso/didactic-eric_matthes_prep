## Create a program that asks the user his/her car preference

prompt = "Which car would you like to drive?"

car = input(prompt)

print(f"Let me find out if we have a {car.title()} here for you.")

## Create a table clerk for a restaurant with a condition

prompt = "Table for how many?"

clients = input(prompt)

if int(clients) >= 8:
    print(f"Table for {clients}. Current waiting time is 20 minutes, ok?")
else:
    print(f"We have a table for {clients} available. Please, follow me.")

## Ask the user for a number and tell if it is a multiple of 10 or not

prompt= "Tell me a number."

number = input(prompt)

if int(number) % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

## Another way of doing it, but with strings

if number[-1] == "0":
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")
