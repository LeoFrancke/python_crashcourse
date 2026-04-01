# Looping through a dictionary
character = {
    'name': 'frodo',
    'level': 10,
    'server': 'server2',
    }

for key, value in character.items():
    print(f"{key.title()}: {value}")

