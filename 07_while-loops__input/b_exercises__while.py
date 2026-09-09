# 7.4 pizza ingredients

ingredients: list[str] = []
prompt = "What ingredients would you like to add to your pizza?"
prompt += "\nType 'quit' to stop. "

while True:
    ingredient = input(prompt)

    if ingredient == 'quit':
        break
    else:
        ingredients.append(ingredient)
        print(f"Adding {ingredient} to your pizza...")


print("\nYour pizza will be made with...")
if ingredients:
    for item in ingredients:
        print(f"\t{item}")
else:
    print("\t...air.")

