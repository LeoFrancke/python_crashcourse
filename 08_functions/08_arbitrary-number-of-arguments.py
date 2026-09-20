# Passing an arbitrary number of toppings

### The asterisk tells python to make a tuple 
#   containing all the values the function receives.

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-size pizza with the following toppings:")
    for top in toppings:
        print(f"- {top}")


make_pizza('medium', 'mussarela')
make_pizza('large', 'cheese', 'pepperoni', 'brocoli')

