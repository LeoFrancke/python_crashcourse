# LIST: a natural way to organize and store data.
#   some languages call them "arrays", but in python: lists.
names = ['ricardo', 'leandro', 'matheus']

# indexes start at 0.
print(f'Hello, {names[0]}!')
print(f'Hello, {names[1]}!')
print(f'Hello, {names[2]}!')

# length of an iterable (list or string)
length = len(names)
print(length)

name_length = len(names[0])
print(name_length)



# SETs: they store only distinct and unique values;
#       duplicates are not allowed.
#       (not in the book, but worth knowing)
distinct_numbers = set([1, 2, 3, 1, 2, 4])
print(distinct_numbers)

# different ways to create sets:
# 1. Using curly braces
fruits = {"apple", "banana", "cherry"}

# 2. Convert a list to a set (removes duplicates)
numbers = set([1, 2, 2, 3])  # Results in {1, 2, 3}

# 3. Create an empty set (MUST use set(), since {} creates an empty dict)
empty_set = set()

