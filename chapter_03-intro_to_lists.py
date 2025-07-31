# Create a list with the name of some people and print them
names = ['arthur dent', 'zaphod beeblebrox', 'ford prefect']

for name in names:
  print(name)

# Print a personalized message for them
message = "I love you, "
for name in names:
  print(f"{message} {name.title()}")

for name in names:
  print(f"{name.title()}, you're invited to the party!")

substitutes = ['jane goodall', 'ana primavesi', 'audre lorde']

for name in names:
  print(f"Saddly, {names.pop().title()} won't be able to attend.\nWelcome to the party, {substitutes[-1].title()}")
  names.insert(0, substitutes.pop())

# Inserting people into the list of names its end, beginning and middle
invitees = ['bilbo baggins', 'pippin took', 'merry brandybuck']

names.insert(0, invitees.pop())
names.insert(int(len(names)/2), invitees.pop())
names.append(invitees.pop())

for name in names:
  print(f"Welcome to the party, {name.title()}!")

# Removing all people but two, telling those two they are still invited, and deleting the list in the end

for name in names[2:]:
  names.pop()

for name in names:
  print(f"{name.title()}, you are still invited.")

del names

# Checking if the list was deleted
try:
  print(names)
except NameError:
  print("This doesn't seem to exist.")
else:
  print("Something else happened.")