# While loops
# break command

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city: str = input(prompt).title()

    if city == 'Quit':
        break
    else:
        print(f"I'd love to go to {city}!")

