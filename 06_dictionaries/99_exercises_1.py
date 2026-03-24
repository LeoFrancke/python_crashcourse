person = {
        'first_name': 'Jens',
        'last_name': 'Johansson',
        'age': 62,
        'city': 'Helsinki',
        }

print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6.2
favorite_number = {
        'john': 10,
        'maria': 15,
        'leo': 1,
        'jens': 77,
        }
for key, value in favorite_number.items():
    print(f"{key.title()}'s favorite number is: {value}\n")

