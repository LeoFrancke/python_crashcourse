def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# keyword args free you from having to remember which order to insert them.
describe_pet(animal_type="turtle", pet_name="Willie")

