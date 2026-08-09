
simple_list = [
    'один', 'два', 'три', 
    'четыре', 'пять', 'шесть', 
    'семь', 'восемь', 'девять'
]

# slices
print('first three:')
print(simple_list[0:3])     # index 0, 1 and 2. (not index 3)
print(simple_list[:3])      # same result

print('three in the middle:')
print(simple_list[3:6])

print('last three:')
print(simple_list[-3:10])   # starting from 3rd last item
print(simple_list[-3:])     # same result


# skipping items
print(f'\nSkip items in a list: {simple_list[0:10:2]}')
print(f'Skip items in a list: {simple_list[1:9:2]}')

