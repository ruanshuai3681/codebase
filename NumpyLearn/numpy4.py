from numpy import random

x = random.randint(100, size=(3, 5))
y = random.randint(100, size=(7))
z = random.choice(y, size=(3, 5))
print(x,y,z)
