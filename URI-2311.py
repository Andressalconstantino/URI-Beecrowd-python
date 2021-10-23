num = int(input())
for i in range(num):
    nome = input()
    dificuldade = float(input())
    notas = list(map(float, input().split()))
    notas.remove(min(notas))
    notas.remove(max(notas))
    res = []
    for i in notas:
        x = i*dificuldade
        res.append(x)
    res = sum(res)
    print(f'{nome} {res:.2f}')