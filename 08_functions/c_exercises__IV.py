# 8.4 Large shirts

def make_shirt(size='large', printed_message='I love Python'):
    """Display a summary of the size and message of a shirt"""
    print(f"\nSize: {size}\nMessage: {printed_message}\n")


# positional args
make_shirt()
make_shirt('medium')

# keyword args
make_shirt(printed_message='UNIVESP')

