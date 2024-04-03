def prime_number(n):
    if type(n) is not  int:
        return("error")
    
    elif n <= 0:
        return("error")
    
    prime = True
    if n == 1:
        prime = False

    for i in range(2,n):

        if n % i == 0:
            prime = False
            break

        else:
            prime = True

    return(prime)

list = [61, 10, 3.14, -1, 0, 1, "0"]
for i in list:
    print(prime_number(i))


