# 5.8 ~ 5.9
usernames: list[str] = ['leofrancke', 'admin', 'mrRobot', 'tour1st', 'linustorvalds']
# usernames = []

if usernames:
    for user in usernames:
        if user.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print('We need to find some users!')



print('\n\n')
# 5.10
current_users = usernames[:]
current_users_lowercase: list[str] = []
for user in current_users:
    current_users_lowercase.append(user.lower())

new_users = ['neo', 'LeoFrancke', 'Mrrobot', 'carlsen', 'tour1st']

for user in new_users:
    if user.lower() not in current_users_lowercase:
        print(f"The username {user} is available.")
    else:
        print(f"I'm sorry, but '{user}' already exists. Choose a new username.")

