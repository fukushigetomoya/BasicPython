import random
import math


def euclid(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    
    return a


def mutually_prime(a, b):
    if euclid(a, b) == 1:
        return True
    
    else:
        return False


p = 0

for i in range(100000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)

    if mutually_prime(a, b) == True:
        p += 1

print(p / 100000)
print(6 / (math.pi ** 2))