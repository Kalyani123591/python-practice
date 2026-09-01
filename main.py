import Mymodule
Mymodule.greet() 

from calculator import add, subtract, multiply, divide
print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5)) 

#Import a module using an alias
import math as m
print(m.sqrt(25)) 

#Use the math module
import math
print(math.sqrt(16))
print(math.pow(2, 3))
print(math.pi)

#Use the random module
import random
number = random.randint(1, 10)
print(number)

#Use the datetime module
import datetime
today = datetime.datetime.now()
print(today)

#Rename an imported function
from math import sqrt as square_root
print(square_root(49)) 

#Use dir() to see module contents
import math
print(dir(math)) 