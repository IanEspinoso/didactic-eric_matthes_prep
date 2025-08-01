## Generate a list of my favorit sandwitches

sandwitches = ['bauru', 'croque madame', 'choripan']

## Print a sentence saying that I like them

for sandwitch in sandwitches:
    print(f"I could eat a {sandwitch} anytime.\n")

print("I love sandwitches!\n\n")

## Create a copy of that list, and see how it's kept

friends_sandwitches = sandwitches[:]

sandwitches.append('blt')
friends_sandwitches.append('tuna & mayo')

print('My favorite sandwitches are:')
for sandwitch in sandwitches:
    print(sandwitch)

print("My friend's favorite sandwitches are:")
for sandwitch in friends_sandwitches:
    print(sandwitch)

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

## Print out the even numbers between 1 and 20

numbers = list(range(1,21,2))

for number in numbers:
    print(number)

## Print out the multiples of 3 between 1 and 30

numbers = list(range(3,31,3))

for number in numbers:
    print(number)

## Print out the cubes of the numbers from 1 to 10,
## using a list comprehension

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)

## Print out the three first, middle and last cubes in that list

print(f"The first three cubes are {cubes[:3]}")
print(f"The cubes in the middle are {cubes[4:7]}")
print(f"The last three cubes are {cubes[-3:]}")

## Create a menu with 5 meals in a tuple

meals = ('feijoada carioca', 'arroz carreteiro', 'tutu mineiro',
         'moqueca baiana', 'bife com fritas')

for meal in meals:
    print(meal)

try:
    meals[0] = 'nothingness'
except TypeError:
    print("You can't feed a tuple, not even nothingness!")

## Rewrite two of those meals

meals = ('feijoada carioca', 'arroz carreteiro', 'tutu mineiro',
         'pizza portuguesa', 'falafel com haloumi')

for meal in meals:
    print(meal)

## Configure the editor to show a vertical line around the 80th characters,
## following the PEP 8
## Edit the whole program to follow that rule from the style guide 