# 7.5 Movie tickets

active: bool = True
prompt: str = "\nTell me your age so we can charge you accordingly: "
prompt += "\nEnter 'quit' to stop. "

while active:
    print("\nWelcome to the theater!")
    age = input(prompt).strip()

    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        ticket_price = 0
    elif age >= 3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"Your ticket costs U$ {ticket_price}.")


