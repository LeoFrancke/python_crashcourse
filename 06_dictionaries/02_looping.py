# Looping through a dictionary (keys and values)
character = {
    'name': 'frodo',
    'level': 10,
    'server': 'server#2',
    }

## the method .items() returns a sequence of key-value pairs.
for key, value in character.items():
    print(f"\n{key.title()}: {value}")

print('', end='\n\n')


# Looping through a dictionary (only keys)
for k in character.keys():
    print(f"Key: {k}")


# Looping through a dictionary (only values)
for v in character.values():
    print(f"Values: {v}")

