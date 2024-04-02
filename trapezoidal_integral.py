
from math import sin

import math


def f(x):
    return sin(x)

N = 100
a = 0
b = math.pi / 2
h = (b - a) / N
S = 0
for i in range(1, N + 1):
    S += (h / 2) * (f(a + ((i - 1) * h)) + f(a + (i * h)))

print(S)