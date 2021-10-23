while 1:    
    num = int(input())
    if num==0:
        break
    numeros = []
    for i in range(1, num+1):
        numeros.append(i)
    print(*numeros)