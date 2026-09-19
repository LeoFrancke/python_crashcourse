# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot arm', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")

        completed_models.append(current_design)


def display_models(completed_models):
    """Display all completed models"""
    print("\nThe following models have been printed: ")
    for model in completed_models:
        print(model)


print_models(unprinted_designs, completed_models)
display_models(completed_models)

