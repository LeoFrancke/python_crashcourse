guest_list = ['richard feynman', 'asimov', 'carl sagan', 'linus torvalds']

print(f"{guest_list[2].title()} won't be able to make it to the party.\n\n")



# Changing a list's element value
guest_list[2] = 'tur1st'



for guest in guest_list:
    print(f"{guest.title()}, you're invited to the party!")


