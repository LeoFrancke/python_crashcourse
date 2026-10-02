from dog import *

my_dog = Dog("Max", 3)
your_dog = Dog("Lucy", 4)

print(f"My dog's name is {my_dog.name}. He's {my_dog.age} years old.")
my_dog.sit()

print(f"Your dog's name is {your_dog.name}. She's {your_dog.age} years old.")
your_dog.roll_over()

