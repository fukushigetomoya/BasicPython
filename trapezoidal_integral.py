
from math import sin

import math


def f(x):
    return sin(x)

N = 100
a = 0
b = math.pi / 2
h = (b -  a) / N
S = 0
for i in range(N):
    S += h / 2 * (f(a) + f(a + h))

print(S)