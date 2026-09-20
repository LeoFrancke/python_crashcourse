# 8.11 Archived Messages

def send_messages(list_of_msgs):
    """Send each text message in the list, moving it to a new list."""
    while list_of_msgs:
        current_msg = list_of_msgs.pop()
        print(current_msg)
        sent_messages.append(current_msg)


short_messages = [
    'hello world python',
    'short text message',
    'python crash course is a great book',
]
sent_messages: list[str] = []

send_messages(short_messages[:])
print(short_messages)
print(sent_messages)

