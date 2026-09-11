# While loops and dictionaries

responses: dict[str, str] = {}
polling_active: bool = True

while polling_active:
    name: str = input("\nWhat's your name? ")
    response: str = input("If you could create anything, what would you build? ")

    # Store the response in the dictionary
    responses[name] = response

    repeat: str = input("Is there another person to answer the poll? (yes / no) ")
    if repeat == 'no':
        polling_active = False


print("\n\n\t --- Poll results ---")
for name, response in responses.items():
    print(f"\n{name} would like to build {response}.")

