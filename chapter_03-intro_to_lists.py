# Create a list with the name of some people and print them
names = ['arthur dent', 'zaphod beeblebrox', 'ford prefect']

for name in names:
    print(name)

# Print a personalized message for them
message = "I love you, "
for name in names:
    print(f"{message} {name.title()}")