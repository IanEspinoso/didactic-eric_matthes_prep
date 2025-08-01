## Generate a list of my favorit sandwitches

sandwitches = ['bauru', 'croque madame', 'choripan']

## Print a sentence saying that I like them

for sandwitch in sandwitches:
    print(f"I could eat a {sandwitch} anytime.\n")

print("I love sandwitches!\n\n")

## Generate a list of animals with similar characteristics

animals = ['crab', 'vinegar-scorpion', 'armadillo']

## Print some sentences about them

for animal in animals:
    print(f"The {animal} has an exoescheleton.\n")

print("With that, they support the carcinotropic theory.\n\n")

## Print the numbers from 1 to 20

numbers = list(range(1,21))

for number in numbers:
    print(number)

## Now, with 1 to 1 million

numbers = list(range(1,1_000_001))

for number in numbers:
    print(number)

## Find the min, max and sum of that list of numbers

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Print out the even numbers between 1 and 20

numbers = list(range(1,21,2))

for number in numbers:
    print(number)

# Print out the multiples of 3 between 1 and 30

numbers = list(range(3,31,3))

for number in numbers:
    print(number)

# Print out the cubes of the numbers from 1 to 10, using a list comprehension

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)