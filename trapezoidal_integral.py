
from math import sin

import math


def f1(x):
    y = 4 / (1 + (x ** 2))
    return y


def f2(x):
    y = (math.pi ** 0.5) * math.exp(-x ** 2)
    return y


def trapezoidal_integral(f, a = 0, b = 1, n = 100):
    
    h = (b - a) / n
    S = 0
    for i in range(1, n + 1):
        S += (h / 2) * (f(a + ((i - 1) * h)) + f(a + (i * h)))

    return S


li = [[sin, 0, math.pi / 2, 50],
        [f1, 0, 1, 100],
        [f2, -100, 100, 1000]
        ]

for i in li:
    print(trapezoidal_integral(*i))