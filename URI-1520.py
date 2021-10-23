def busca_Binaria(alvo, vetor):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] >= alvo:
            fim = meio - 1
        elif vetor[meio] < alvo:
            inicio = meio + 1

    if inicio < len(vetor) and vetor[inicio] == alvo:
        return inicio
    else:
        return -1
def busquinha_Binaria(alvo, vetor):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] > alvo:
            fim = meio - 1
        elif vetor[meio] <= alvo:
            inicio = meio + 1

    if fim <= len(vetor) and vetor[fim] == alvo:
        return fim
    else:
        return -1
while True:
    try:
        n = input()
        numbers = []
        if n.isdigit():
            for i in range(int(n)):
                x, y = map(int, input().split())
                for i in range(x, y+1):
                    numbers.append(i)
            numbers.sort()
            num = int(input())
            z = busca_Binaria(num, numbers)
            w = busquinha_Binaria(num, numbers)
            if z != -1 and w != -1:
                print(f'{num} found from {z} to {w}')
            else:
                print(f'{num} not found')
    except EOFError:
        break