while 1>0:
    entrada = list(map(int, input().split()))
    if entrada[0]==0:
        break
    A = entrada[0]
    B = entrada[1]
    C = entrada[2]
    calc = ((A*B*(C/100))**(1/2))/(C/100)
    print(int(calc))
    