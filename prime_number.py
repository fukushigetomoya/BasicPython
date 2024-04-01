a = [61, 10]
prime = True

for i in a:
    for j in range(2,i):
        if i % j == 0:
            prime = False
            break
        
        else:
            prime = True
    
    if prime == True:
        print(str(i) + "は素数です")
    
    else:
        print(str(i) + "は素数ではありません")


