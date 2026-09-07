current_usernames: list[str] = ['leo', 'ricardo', 'matthew', 'Sofia', 'Richard']
new_users: list[str] = ['Ricardo', 'Steven', 'Matthew', 'SOFIA', 'riCHArd', 'uSER']

current_usernames_lowercase: list[str] = []

# making a copy of all current users in lowercase
for user in current_usernames:
    current_usernames_lowercase.append(user.lower())

# print(current_usernames)
# print(new_users)
# print(current_usernames_lowercase)

for user in new_users:
    if user.lower() in current_usernames_lowercase:
        print(f'Error: username "{user}" already exists.')
    else:
        print(f'The username "{user}" is available.')

