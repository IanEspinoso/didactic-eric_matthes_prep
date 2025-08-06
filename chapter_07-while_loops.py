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


## Create a dictionary with customers and their requested sandwitches

available_sandwitches = ['bauru', 'croque madame', 'choripan', 'blt', 'tuna']
requested_sandwitches = {}
finished_sandwitches = {}
poll_active = True

prompt_name = "What is your name?"
prompkt_sandwitch = "What is your desired sandwitch?"
prompt_activity = "Would you like another request? (yes/no)"

while poll_active:
    name = input(prompt_name)
    sandwitch = input(prompkt_sandwitch)
    requested_sandwitches[name] = sandwitch
    activity = input(prompt_activity)
    if activity == 'no':
        poll_active = False
    else:
        continue


## Restrain the orders to the available sandwitches
## Create another dictionary with while 'doing' the sandwitches

print("At the moment we sadly don't have tuna sandwitch.")

available_sandwitches.remove('tuna')

for name, sandwitch in requested_sandwitches.items():
    if sandwitch in finished_sandwitches:
        finished_sandwitches[sandwitch] += 1
        print(f"{name.title()}, your {sandwitch} sandwitch is ready.")
    elif sandwitch in available_sandwitches:
        finished_sandwitches[sandwitch] = 1
        print(f"{name.title()}, your {sandwitch} sandwitch is ready.")
    else:
        print(f"{name.title()}, saddly we don't serve that sandwitch.")


## Print a dictionary with the finished products

print("Today we did...")
for key, value in finished_sandwitches.items():
    print(f"{value} {key} sandwitches.")


## Make an infinite loop

while True:
    print("All work and no play makes Jack a dull boy.")