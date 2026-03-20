# Sorting Lists
#   tip: make all lowercase -> avoids problems

# list of cars
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)


# Sorting Temporarily: sorted() Function
print(sorted(cars))
print(sorted(cars, reverse=True))
print(f"Original list again: {cars}\n")



# Sorting PERMANENTLY: sort() Method
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)



# Reversing original list's order: Reverse() Method
list_1 = ['byte', 'ah' , 'thing', 'same thing']
print(list_1)
list_1.reverse()  # permanent
print(list_1)


