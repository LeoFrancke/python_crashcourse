# 7.4 pizza toppings

toppings: list[str] = []
prompt = "\nWhat toppings would you like to add to your pizza?"
prompt += "\nType 'quit' to stop. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"\nAdding {topping} to your pizza...")


print("\nYour pizza will be made with...")
if toppings:
    for item in toppings:
        print(f"\t{item}")
else:
    print("\t...air.")

