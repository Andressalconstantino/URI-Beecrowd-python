while 1>0:
    n, m = map(int, input().split())
    if n==0 or m==0 or n<0 or m<0:
        break
    numeros = []
    if n>m:
        for i in range(m,n+1):
            numeros.append(i)
    elif m>n:
        for i in range(n, m+1):
            numeros.append(i)
    soma = sum(numeros)

    print(*numeros, 'Sum=%d' %soma)