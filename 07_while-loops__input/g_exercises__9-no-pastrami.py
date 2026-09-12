# 7.9 No Pastrami exercise (base: exercise 7.8)

finished_sandwiches: list[str] = []
sandwich_orders = [
    'pastrami',
    'tuna',
    'special',
    'pastrami',
    'vegan',
    'hamburger',
    'pastrami',
]

print("\nUnfortunately, we ran out of Pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print('removed Pastrami from sandwich orders...')


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Your {current_sandwich} sandwich is being made...")
    finished_sandwiches.append(current_sandwich)


print("\n\t--- The following are ready to be delivered ---")
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich")


