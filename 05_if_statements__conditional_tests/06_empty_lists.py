# pizzeria example
requested_toppings: list[str] = []

requested_toppings.append('cheese')
requested_toppings.append('bacon')
requested_toppings.append('olives')

available_toppings: list[str] = [
    'mushrooms', 
    'olives', 
    'green peppers', 
    'pepperoni', 
    'cheese',
]

# check if the list is empty.
if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f'Adding {topping}.')

        else:
            print(f"Sorry, we don't have {topping}")

    print('Finished making your pizza!')

else:
    print('Are you sure you want a plain pizza?')


