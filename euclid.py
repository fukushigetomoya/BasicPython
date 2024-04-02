list = [[10, 20], [14, 91], [91, 14]]


# TODO
for a, b in list:
    while b != 0:
        r = a % b
        a = b
        b = r

    print(a)