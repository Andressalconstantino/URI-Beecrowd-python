ct = int(input())

for i in range(ct):
    tr, rn = map(int, input().split())
    renas = []
    for j in range(tr):
        nome, peso, idade, altura = map(str, input().split())
        peso = int(peso)
        idade = int(idade)
        altura = float(altura)
        tupla = (nome, peso, idade, altura)
        renas.append(tupla)
    
    renas.sort(key = lambda x: (-x[1], x[2], x[3], x[0]))
    x = i+1
    print('CENARIO {%d}' %x)
    for h in range(rn):
        print(f'{h+1} - {renas[h][0]}')
