# Copy of exercise 3.5:
guest_list = ['richard feynman', 'asimov', 'carl sagan', 'linus torvalds']

print(guest_list)
print(f"{guest_list[3].title()} won't be able to make it to the party.\n\n")

# Changing a list's element value
guest_list[3] = 'tur1st'



# EXERCISE 3.6: Adding elements to a list
guest_list.insert(0, 'eric matthes')
print(guest_list)

guest_list.insert(3, 'penetra')
print(guest_list)

guest_list.append('last guest')  # append at the end of the list
print(guest_list)



