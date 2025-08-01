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

# Make a list of places to visit
places = ['India', 'Colombia', 'New Zealand', 'Ghana', 'Finland']

print("This is the original list.")
for place in places:
  print(place)

print("This is the sorted list.")
for place in sorted(places):
  print(place)

print("This is the list in alphabetically reversed.")
for place in sorted(places, reverse=True):
  print(place)

print("This is the original list.")
for place in places:
  print(place)

# Permanently reverse the list
print("This is the reversed list.")
places.reverse()
for place in places:
  print(place)

# Unreverse the list
print("This is the original list, again.")
places.reverse()
for place in places:
  print(place)

# Save the list in alphabetical order
places.sort()

print("This is the sorted list. Permanent.")
for place in places:
  print(place)

places.sort(reverse=True)
print("Maybe not so permanent. Look at it go.")
for place in places:
  print(place)

# Print out the number of listed countries 
print(f"I'm going to visit {len(places)} countries.")

# Intentionally generate an index error
try:
  print(places[5])
except IndexError:
  print("Index error succesfully generated.")