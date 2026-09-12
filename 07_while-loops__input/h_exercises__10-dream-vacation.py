# 7.10 exercise

vacation_poll: dict[str, str] = {}
print("Vacation Poll \nEnter 'quit' anytime to exit.\n")

while True:
    name: str = input("What's your name? ").strip()
    if name == 'quit':
        break
    vacation: str = input("If you could visit anywhere, where would you go? ")
    if vacation == 'quit':
        break
    print("\nType 'quit' to exit\n")

    vacation_poll[name] = vacation


print("\n\n\t--- Poll Results ---\n")
for name, vacation in vacation_poll.items():
    print(f"{name.title()} would like to go to {vacation.title()}.")

