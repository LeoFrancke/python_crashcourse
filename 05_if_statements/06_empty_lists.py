# pizzeria example
requested_toppings = []

requested_toppings.append('cheese')
requested_toppings.append('bacon')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'cheese']

# check if the list is empty.
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f'Adding {requested_topping}.')

        else:
            print(f"Sorry, we don't have {requested_topping}")

    print('Finished making your pizza!')

else:
    print('Are you sure you want a plain pizza?')


