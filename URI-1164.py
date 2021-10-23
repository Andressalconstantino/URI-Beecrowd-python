num = int(input())
for i in range(num):
    numero = int(input())
    soma = []
    for i in range(1, numero, 1):
        if numero%i==0:
            soma.append(i)
    soma = sum(soma)
    if soma == numero:
        print('%d eh perfeito' %numero)
    else:
        print('%d nao eh perfeito' %numero)
