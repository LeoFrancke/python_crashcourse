# While loops

# in the real world, many different events 
# could cause the program to stop running.

prompt = "\nType 'quit' to stop. \nSay something and I'll repeat it: "
active: bool = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

