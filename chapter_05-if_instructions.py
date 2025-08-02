# Write 10 conditional tests, printing the predicted result before

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

# More tests, now using 'lower', 'and', 'or', 'in' and 'not in'

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