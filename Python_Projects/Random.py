# Random Number Generator
import random
# import my_module. This is a module that I created to store my favorite number. 
# You can create your own module and import it here.

# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module.my_favorite_number)

# How to create random floating point numbers by using random.random() function. 
# This will give you a random number between 0 and 1.

# random.random() will give you a random number between 0 and 1. 
# You can multiply it by 10 to get a random number between 0 and 10.
#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)

#random.uniform() will give you a random number between the two numbers you specify. 
# For example, if you want a random number between 1 and 10, you can use random.uniform(1, 10).
#random_float = random.uniform(1, 10)
#print(random_float)

heads = 0
tails = 1
coin_flip = random.randint(0, 1)
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")