magicians = ['alice', 'david', 'carolina']


# In python, it's pretty straightforward to loop through a list
#   if you don't need the index: use the No-Index Syntax
for magician in magicians:
    print(magician)


# In other languages, like C, you need to create a loop the size of the array;
#    then access each item by its index
for i in range(0, len(magicians)):
    print(magicians[i])




# Simple exercise: no-index syntax
favorite_pizzas = ['four cheese', 'canadian bacon', 'mushrooms']

for pizza in favorite_pizzas:
    print(f"I love {pizza.title()} pizza!")

print("I really love pizza!")


