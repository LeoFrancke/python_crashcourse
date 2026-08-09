# List comprehensions ~ Python one-liners
# a list needs to be created around the for loop.

squares = list(number**2 for number in range(11))
print(squares)

cubes = [number**3 for number in range(11)]
print(cubes)


