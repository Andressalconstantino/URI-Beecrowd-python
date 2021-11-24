coluna = int(input())
operacao = input()
soma = 0
n = 0
for i in range(12):
    for j in range(12):
        x = float(input())
        if j==coluna:
            soma += x
            n+= 1

if operacao == 'M':
    soma /= n
print(f'{soma:.1f}')

