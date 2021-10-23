while 1>0:
    n = int(input())
    if n == 0:
        break
    fila = []
    for i in range(1,n+1):
        fila.append(i)
    discarded = []
    x = 0
    while len(fila)>1:
        for i in range(x, len(fila)):
            if len(fila)==1:
                break
            discarded.append(str(fila[i])) 
            fila.pop(i)
            if i+1==len(fila):
                x = 0
                break
            if i+1>len(fila):
                x= 1
                break
    x = fila[0]     
    print('Discarded cards:', ', '.join(discarded))
    print(f'Remaining card: {x}')