# Parameters are placeholders waiting for input, 
#   created at function definition
def greet_user(username):  # parameter: the variable receiving data
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


# Arguments are the actual values being passed into the function
greet_user("leo")  # "leo" is an argument

