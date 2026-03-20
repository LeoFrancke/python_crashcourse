# Copy of exercise 3.5:
guest_list = ['richard feynman', 'jordan peterson', 'carl sagan', 'linus torvalds']

# Copy of exercise 3.6:
guest_list.insert(0, 'eric matthes')
guest_list.insert(3, 'penetra')
guest_list.append('last guest')



# EXERCISE 3.7: Deleting items
print(f"Original list: {guest_list}")
# removing last item from the list
guest_list.pop()

# I can save the deleted element value
popped_item = guest_list.pop()
print(f"{popped_item} just left the room.")
guest_list.pop()
guest_list.pop()
print(f"List: {guest_list}")

# Popping items from any position
index_zero_item = guest_list.pop(0)

# Removing by value
guest_list.remove('richard feynman')

# Deliting by index
del guest_list[0]


print(guest_list)   # empty
