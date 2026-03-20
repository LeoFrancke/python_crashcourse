guest_list = ['richard feynman', 'jordan peterson', 'carl sagan', 'linus torvalds']

print(f"{guest_list[3].title()} won't be able to make it to the party.\n\n")



# Changing a list's element value
guest_list[3] = 'tur1st'



for guest in guest_list:
    print(f"{guest.title()}, you're invited to the party!")


