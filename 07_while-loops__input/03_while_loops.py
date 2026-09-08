# While loops
# it runs as long as, or WHILE, a certain condition is True.

prompt = "\nTell me something, and I'll repeat it back to you: "
prompt += "\nEnter 'q' to end the program. "
message: str = None

while message != 'q':
    message = input(prompt)
    print(message)


