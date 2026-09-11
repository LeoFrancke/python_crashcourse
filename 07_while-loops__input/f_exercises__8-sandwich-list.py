# 7.8 Deli

finished_sandwiches: list[str] = []
sandwich_orders = [
    'tuna',
    'special',
    'vegan',
    'hamburger',
]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} sandwich is being made...")
    finished_sandwiches.append(current_sandwich)


print("\n\t--- The following are ready to be delivered ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")

