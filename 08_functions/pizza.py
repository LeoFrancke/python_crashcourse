def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-size pizza with the following toppings:")
    for top in toppings:
        print(f"- {top}")

