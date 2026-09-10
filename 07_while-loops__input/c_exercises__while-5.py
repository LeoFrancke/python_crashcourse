# 7.5 Movie tickets

while True:
    print("Welcome to the theater!")
    age = input("Tell me your age so we can charge you accordingly: ")
    age = int(age)

    if age < 3:
        ticket_price = 0
    elif age >= 3 and age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    print(f"Your ticket costs U$ {ticket_price}.")


