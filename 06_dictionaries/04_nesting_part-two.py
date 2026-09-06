# Storing a list in a dictionary

# info about a pizza being ordered
pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'four cheese'],
        }

# Summarize the order:
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings: ")

for top in pizza['toppings']:
    print(f'\t{top}')


