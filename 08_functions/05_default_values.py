def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Default values can simplify your function calls
# and clarify the ways your functions are typically used.
describe_pet("max")
describe_pet(pet_name="Willie", animal_type="turtle")


# Note: any parameters without a default value need to come first,
#       so that Python continues to interpret positional args correctly.

