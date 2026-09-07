
person_1 = {
        'name': 'Linus',
        'lastname': 'Torvalds',
        'age': 56,
        'city': 'Helsinki',
        }

person_2 = {
        'name': 'Richard',
        'lastname': 'Feynman',
        'age': 69,
        'city': 'Pasadena',
        }

people: list = []
people.append(person_1)
people.append(person_2)


for person in people:
    full_name = (person['name'] + " " + person['lastname']).title()
    print(f"\nFull name: {full_name}")
    print(f"Age: {person['age']}")
    print(f"Lived in {person['city']}")

