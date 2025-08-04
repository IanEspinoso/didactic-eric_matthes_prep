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

## Create three different loops for three different rivers

rivers = {'nile': 'epypt',
          'yangtze': 'china',
          'amazonas': 'brazil',}

for key, value in rivers.items():
    print(f"The river {key.title()} runs in {value.title()}.")

for key in rivers:
    print(f"{key.title()} is a river.")

for value in rivers.values():
    print(f"{value.title()} is a country.")

## Create a list with people and their favorite languages

people_code = {'archimedes': 'sql',
          'arthur': 'python',
          'merlin': 'rust',
          'madam mim': 'java',
          'sir kay': '',
          'sir ector': '',
          'little lady squirrel': 'javascript',
          'old girl squirrel': 'golang'}

## Creating an (unnecessary) list, just because the question told me to

people = list(people_code.keys())

## Going through the dictionary and commenting the languages people code

for person in people_code:
    if people_code[person] != '':
        print(f"{person.title()}, you code in {people_code[person].title()}!")
    else:
        print(f"{person.title()}, learn to code. Is useful and fun!")



## The exercises in the end of the chapter are kind of redundant
## Still, nesting dictionaries and lists is a fun exercise. Let's do it

people_code = {'archimedes': {'languages': ['sql', 'rust'],
                              'age': 62,
                              'origin': 'magical forest',},
            'arthur': {'languages': ['python'],
                              'age': 11,
                              'origin': 'tintagel',},
            'merlin': {'languages': ['rust', 'c', 'assembly'],
                              'age': 358,
                              'origin': 'carmarthen',},
            'madam mim': {'languages': ['java', 'sql', 'c', 'cpp'],
                              'age': 64,
                              'origin': 'dark forest',},
            'sir kay': {'languages': [],
                              'age': 19,
                              'origin': 'tintagel',},
            'sir ector': {'languages': [],
                              'age': 42,
                              'origin': 'unknown',},
            'little girl squirrel': {'languages': ['javascript'],
                              'age': 2,
                              'origin': "merlin's cottage",},
            'old lady squirrel': {'languages': ['golang'],
                              'age': 5,
                              'origin': "merlin's cottage",},}

for person, person_info in people_code.items():
    print(f"\n{person.title()} was born in {person_info['origin'].title()} "
          f"{person_info['age']} years ago")
    if len(person_info['languages']) != 0:
        print("and knows how to code in:")
        for language in person_info['languages']:
            print(language.title())
    else:
        print('and already learned something, I...guess?!?')