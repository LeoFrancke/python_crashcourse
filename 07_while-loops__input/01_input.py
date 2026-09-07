# How input works in Python
# it pauses the execution and waits for the user to Enter something.

# default Type: string
mood_variable = input('How are you today? ')


# multi-line prompts
prompt  = 'Share your name, so we can personalize the messages you see.'
prompt += "\nWhat's your name? "
name: str = input(prompt)
print(f'Hello, {name}!')

