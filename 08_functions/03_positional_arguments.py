def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# The position of the arguments matter.
describe_pet("turtle", "Willie")

