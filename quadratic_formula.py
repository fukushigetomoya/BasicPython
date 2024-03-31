a = [1, 1, 8, 1]
b = [-6, 2, -6, 0]
c = [9, -8, -35 ,1]
print(a,b,c)
# TODO
for i in range(4):
    x1 = (-b[i] + (b[i] ** 2 - 4 * a[i] * c[i]) ** 0.5) / (2 * a[i])
    x2 = (-b[i] - (b[i] ** 2 - 4 * a[i] * c[i]) ** 0.5) / (2 * a[i])
   

    print(x1, x2)