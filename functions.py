# Function is a piece of code that performs some task. (In a tv remote, each button
# performs a functions, so a function is like that button in code)
# There are 3 types of functions in Python :

# a. In-built functions

# int() str() float() min() range() max()

# b. Module functions

# Module is a file that contains some functions & variables which can be imported
# for use in other files.
# Each module should contain some related tasks

# Example : math, random, string
import math
print(dir(math))
import random
print(dir(random))
import string
print(dir(string))
from math import sqrt
print(sqrt(4))


# c. User-defined functions
def sum(a, b=4):
    sum(1, 2)
    print(a + b)
