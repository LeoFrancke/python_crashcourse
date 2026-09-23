# 8.12 sandwiches

def make_sandwich(*ingredients):
    """Display the ingredients of a sandwich."""
    print("Making your sandwich with the following ingredients:")
    for item in ingredients:
        print(f"- {item}")


make_sandwich('butter')
make_sandwich('cheese', 'bacon', 'sauce')
make_sandwich('cheese', 'bacon', 'sauce', 'hamburger')


