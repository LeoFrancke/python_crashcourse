usernames = ['leo', 'ricardo', 'admin', 'user', 'hello, friend']
# usernames = []

# if the list is not empty
if usernames:
    for user in usernames:
        if 'admin' == user.lower():
            print(f'Hello, {user.title()}. Would you like a status report?')
        else:
            print(f'Hello, {user.title()}.')
else:
    print('We need to find some users!')



