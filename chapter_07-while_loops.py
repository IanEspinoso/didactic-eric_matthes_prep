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

## Write a code to ask for the ages of attending tourists
## Then give a sum of the tiket price

prompt = "What is the age of the next attendant?"
prompt += "(write 'quit' whenever you are done)"
attendants = []
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        try: 
            int(age)
            attendants.append(age)
        except ValueError:
            print("Enter only whole numbers, please.")        

ticket = 0
for attendant in attendants:
    attendant = int(attendant)
    if attendant > 12:
        ticket += 15
    elif attendant >= 3:
        ticket += 10
    else:
        continue
print(f"The entry cost of the {len(attendants)} attendants is R${ticket}.")

## Make an infinite loop

while True:
    print("All work and no play makes Jack a dull boy.")