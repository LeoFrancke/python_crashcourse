favorite_languages = {
        'leo': 'c++',
        'linus': 'c',
        'monty': 'python',
        }


people_to_take_the_poll = ['leo', 'matheus', 'linus']

for person in people_to_take_the_poll:

    # if the key exists, it returns something and the condition is True;
    if (favorite_languages.get(person)):
        print(f"You already took the poll, {person.title()}, thank you!")
    else:
        print(f"Please, take our Favorite Language poll, {person.title()}!")

