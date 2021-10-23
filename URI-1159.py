while 1>0:
    soma = []
    x = int(input())
    if x == 0:
        break
    for i in range(x, x+10, 1):
        if i%2==0:
            soma.append(i)
    soma = sum(soma)
    print(soma)