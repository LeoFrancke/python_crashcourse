# range()
# min() / max() / sum()

digits = [1, 2, 3, 4, 5, 0]
print(digits)
print(f'minimum value: {min(digits)}')
print(f'maximum value: {max(digits)}')
print(f'sum: {sum(digits)}')



print('\nEven numbers:')
# from 0 until 10 (not 11), count by 2
for n in range(0, 11, 2):
    print(n)



print('\nList of squares:')
squares = []
for n in range(0, 11):
    squares.append(n ** 2)

print(squares)


