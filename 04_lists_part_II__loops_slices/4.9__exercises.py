# 1 to 20
for n in range(21):
    print(n)

# 1 million numbers
one_million = list(range(0, 1_000_001))
# for number in one_million:
#     print(number)

# math functions with 1 mi
print(min(one_million))
print(max(one_million))
print(sum(one_million))

# odd numbers
odd_numbers = list(range(1, 20, 2))
for n in odd_numbers:
    print(n)

# multiples of 3: (exercise 4.7)
multiples_of_3 = list(range(3, 31, 3))
for cube in multiples_of_3:
    print(cube)

# cubes
cubes = list(range(0, 11))
for cube in cubes:
    print(cube**3)

print('list comprehension of squares:')
squares = [value**2 for value in range(11)]
print(squares)




# slices
simple_list = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
print('first three:')
print(simple_list[:3])
print('three in the middle:')
print(simple_list[3:6])
print('last three:')
print(simple_list[-3:])



# tuples
menu = ('food 1', 'food 2', 'food 3')
for food in menu:
    print(food)

# menu[0] = 'altered food'
menu = ('altered food', 'food 2', 'food 3')
for food in menu:
    print(food)

