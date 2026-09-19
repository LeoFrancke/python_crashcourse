# Return values allow you to move much of your program's grunt work into functions,
# which can simplify the body of your program.

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


programmer = get_formatted_name('linus', 'torvalds')
print(programmer)

musician = get_formatted_name('jens', 'johansson', 'ola')
print(musician)

