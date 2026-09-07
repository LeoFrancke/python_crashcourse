# Storing a dictionary in a list
# an empty list that will store aliens
aliens = []  # No type hint to avoid creating a mess.
print(aliens)

# make 10 green aliens
for alien_number in range(1, 11):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# make 10 blue aliens
for alien_number in range(1, 11):
    new_alien = {'color': 'blue', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# make 10 red aliens
for alien_number in range(1, 11):
    new_alien = {'color': 'red', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


for alien in aliens:
    print(alien)

print(f"Total number of aliens: {len(aliens)}.")

