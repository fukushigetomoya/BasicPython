def prime_number(n):
    if not isinstance(n, int):
        return("error")
    
    elif n <= 0:
        return("error")
    
    prime = True
    if n == 1:
        return False

    for i in range(2,n):

        if n % i == 0:
            return False
    
    return True

li = [61, 10, 3.14, -1, 0, 1, "0"]

for i in li:
    print(prime_number(i))


