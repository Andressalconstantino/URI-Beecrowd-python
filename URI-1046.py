c, f = map(int, input().split())

if c<f:
    f = f-c
    print('O JOGO DUROU %d HORA(S)' %f)
else:
    c = (24-c) + f
    print('O JOGO DUROU %d HORA(S)' %c)