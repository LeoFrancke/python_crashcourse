# While loops
# continue command: go back to the beginning of the loop

current_number: int = 0

while current_number < 10:
    current_number += 1

    # skip printif number is even
    if current_number % 2 == 0:
        continue

    print(current_number)

