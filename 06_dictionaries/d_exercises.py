rivers = {
        'nile': 'egypt',
        'amazon': 'brazil',
        'mississippi': 'usa',
        }

for river, country in rivers.items():
    print(f"\nThe {river.title()} river runs through {country.title()}.")

for river in rivers.keys():
    print(f"Where is {river.title()} located at?")

for country in rivers.values():
    print(f"What famous river runs through {country.title()}?")


