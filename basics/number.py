x=2
y=3
z=4

print(x+y)

repr('chai')
str('chai')

print(x ** 100)
 
result = 1/3.0;
print(result)

print(x,y,z)
print(x < y < z)
print(x < y and y < z)

import math

print(math.floor(3.5))
print(math.floor(-3.5))
print(math.trunc(2.8))
print(math.trunc(-2.8))


com = (2+1j)*3
print(com)

print(0o20)
print(0xff)

import random

print(random.random())
print(random.randint(1,10))
print(random.randint(1,10))
print(random.randint(1,10))

l1 = ['lemon','ginger','masala','mint']
print(random.choice(l1))
print(random.choice(l1))
print(random.choice(l1))

random.shuffle(l1)
print(l1)
random.shuffle(l1)
print(l1)

print(0.1+0.1+0.1 - 0.3)
# so we import decimal

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') -Decimal('0.3'))

setone = {1,2,3,4,4}
print(setone & {1,2,3}) #intersection
print(setone | {1,5,3}) #union
print(setone - {1,2,3,4}) #empty set is set() not {} because {} is empty dict

print(True == 1)
print(True is 1)
print(True + 5)


