# Copying a list can generate unexpected behavior. Use slices to avoid that.

my_favorite_pizzas = ['four cheese', 'canadian bacon', 'mushrooms']
julia_favorite_pizzas = my_favorite_pizzas[:]
# first_list = list_copy[:]             # slice with indexes omitted.

julia_favorite_pizzas.insert(1, 'chocolate')

print('My favorite pizzas are:')
for pizza in my_favorite_pizzas:
    print(pizza.title())

print("\nJulia's favorite pizzas are:")
for pizza in julia_favorite_pizzas:
    print(pizza.title())


# If we just set first_list = list_copy, we'd have a problem:
#       -> two variables would point to the SAME list.

