# Exercise 6.11 - Cities
# a dictionary nested in a dictionary

cities = {
    'Campinas': {
        'country': 'Brazil',
        'population': 1_200_000,
        'fact': 'Known as the Silicon Valley of Brazil.'
        },
    'St. Petesburg': {
        'country': 'Russia',
        'population': 5_600_000,
        'fact': "The world's most northermost city with over 1 million people."
        },
    'Toronto': {
        'country': 'Canada',
        'population': 3_000_000,
        'fact': 'Largest city in Canada.'
        }
    }


for city, city_info in cities.items():
    country = city_info['country']
    pop = city_info['population']
    fact = city_info['fact']

    print(f"\nHere is some information about the city of {city.title()}: ")
    print(f"\tIt's located in {country} and has a population of {pop} people.")
    print(f"\tCurious fact: \n\t\t{fact}")

