## Write 10 conditional tests, printing the predicted result before

algae = 'chlorela'
print("Is algae = 'chlorela'? I predict True.")
print(algae == 'chlorela')

print("\nIs algae = 'spirulina'? I predict False.")
print(algae == 'spirulina')

numbers = [1,1,2,3,5,8]

print("\nDoes the list of numbers have more than 5 numbers? " 
      "\nI predict True.")
print(len(numbers) > 5)
print("\nDoes the list of numbers have more than 6 numbers? "
      "\nI predict False.")
print(len(numbers) > 6)

print("\nIs the biggest number in the list bigger or equal to 8? "
      "\nI predict True.")
print(max(numbers) >= 8)
print("\nIs the biggest number in the list bigger or equal to 9? "
      "\nI predict False.")
print(max(numbers) >= 9)

print("\nIs the smallest number in the list smaller or equal to 1?"
      "\nI predict True.")
print(min(numbers) <= 1)
print("\nIs the smallest number in the list smaller or equal to 0?"
      "\nI predict False.")
print(min(numbers) <= 0)

print("\nIs the sum of the numbers in the list different from 21?"
      "\nI predict True.")
print(sum(numbers) != 21)
print("\nIs the sum of thte numbers in the list different from 21?"
      "\nI predict False.")
print(sum(numbers) != 20)

## More tests, now using 'lower', 'and', 'or', 'in' and 'not in'

print("\nIs 'Chlorela' in lower case the same as that algae?" "I predict True.")
print('Chlorela'.lower() == algae)
print("\nIs 'Spirulina' in lower case the same as the algae"
      "I predict False.")
print('Spirulina'.lower() == algae)

print("\nAre the numbers 1 and 2 in the list? I predict True.")
print(1 and 2 in numbers)
print("\nAre the numbers 1 and 11 in the list? I predict False")
print(1 and 11 in numbers)

print("\nAre the numbers 3 or 11 in the list? I predict True.")
print(3 in numbers or 11 in numbers)
print("\nAre the numbers 7 or 21 in the list? I predict False.")
print(7 in numbers or 21 in numbers)

print("\nIs 5 not in the list? I predict False.")
print(5 not in numbers)
print("\nIs 99 not in the list? I predict True.")
print(99 not in numbers)

## Test the color of the alien

alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    points = 0
print(f"\nYou gained {points} points!")

## Attribute a life stage acording to the person's age

age = 36

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'child'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'
    
print(f"\nYou are in the {stage} stage of life.")

## Create a series of tests for a list

favorite_fruits = ['strawberry', 'jackfruit', 'apple', 'banana']

if len(favorite_fruits) < 3:
    print("\nYou don't realy like fruits, do you?")
elif 'blueberry' in favorite_fruits:
    print("\nYou love blueberries!")
elif 'guava' in favorite_fruits:
    print("\nYou love guava!")
elif 'tamarind' in favorite_fruits:
    print("\nYou love tamarind!")
else:
    print("\nI don't seem to know what you like.")

## Evaluate the list of Discworld's current users, saying hi to them
## with a special shoutout to Death

## Also test with an empty 'current_users = []'
 
current_users = ['Death', 'Rincewind', 'Sam Vines', 'Twoflower', 'Ysabell']

if current_users:
    for current_user in current_users:
        if current_user is 'Death':
            print(f"\nHi, {current_user}. Would you like to see a status report?")
        else:
            print(f"\nHi, {current_user}. Thank you for logging in again.")
else:
    print("\\nWe need to find more users!")


## Verify the availability for users

current_users_low = []

for current_user in current_users:
    current_users_low.append(current_user.lower())    

new_users = ['Rincewind', 'Twoflower', 'Angua', 'Weatherwax', 'Nanny Ogg']

for new_user in new_users:
    if new_user.lower() in current_users_low:
        print(f"\nUser {new_user.title()} is not available.")
    else:
        print(f"\nWelcome, {new_user.title()}!")

## Add the appropriate suffix to the ordinal number

numbers = list(range(1,10))
common_suffix = 'th'

for number in numbers:
    if number is 1:
        print(number, 'st', sep='')
    elif number is 2:
        print(number, 'nd', sep='')
    elif number is 3:
        print(number, 'rd', sep='')
    else:
        print(number, common_suffix, sep='')