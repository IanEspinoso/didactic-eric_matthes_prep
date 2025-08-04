## Create and print a dictionary with information about a person

person_1 = {'first_name': 'sarah',
            'last_name': 'connor',
            'age': 19,
            'city': 'los angeles',}

for value in person_1.values():
    print(value)

## Pair 5 people with their last names

full_names = {'ginger': 'ventura',
              'sarah': 'connor',
              'kate': 'brewster',
              'tarissa': 'dyson',
              'dani': 'ramos',}

for name, last_name in full_names.items():
    print(f"{name.title()}'s last name is {last_name.title()}.")

## Create a glossary for pythonic expressions

glossary = {'argument': 'a necessary variable for an operation',
            'instruction': 'a set of conditions followed by an action',
            'function': 'a set of arguments subject to instructions',
            'method': 'an function within an instatiated class',
            'operation': 'an instruction followed by an outcome',}

for key in glossary:
    print(f"\n{key.title()} is {glossary.get(key)}.")

## Insert aditional elements in that dictionary

add_to_glossary = 