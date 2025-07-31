# Create a list with the name of some people and print them
names = ['arthur dent', 'zaphod beeblebrox', 'ford prefect']

# for name in names:
#     print(name)

# # Print a personalized message for them
# message = "I love you, "
# for name in names:
#     print(f"{message} {name.title()}")

# for name in names:
#     print(f"{name.title()}, you're invited to the party!")

substitutes = ['jane goodall', 'ana primavesi', 'audre lorde']
unavailable = []

for name in names:
    unavailable.append(names.pop())
  # print(f"Saddly, {names.title()} won't be able to attend.\nWelcome to the party, {substitute[-1].title()}")

# Reinvite the people into the party