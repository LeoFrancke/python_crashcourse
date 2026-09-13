# exercises I and II:

def display_message():
    """Display a simple message about what I'm learing."""
    message = "\nI'm reviewing some Python fundamentals while studying C++"
    message += "\nI can't wait to start working on some real projects!"
    print(message)


def favorite_book(title):
    """Display a message about a book passed into the function"""
    message = f"\nOne of my favorite books is {title.title()}."
    print(message)


display_message()
favorite_book("A Storm of Swords")
favorite_book("the hobbit")

