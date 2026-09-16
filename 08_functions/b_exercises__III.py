# 8.3 T-shirt

def make_shirt(size, printed_message):
    """Display a summary of the size and message of a shirt"""
    print(f"\nSize: {size}\nMessage: {printed_message}\n")


# positional args
make_shirt(15, "Small steps, big dreams")

# keyword args
make_shirt(printed_message='UNIVESP', size=12)

