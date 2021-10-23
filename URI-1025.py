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
case = 1
while 1>0:
    n, q = map(int, input().split())
    marbles = []
    if n==0 and q==0:
        break
    for i in range(n):
        m = int(input())
        marbles.append(m)
    marbles = sorted(marbles)
    print(f'CASE# {case}:')
    for i in range(q):
        x = int(input()) 
        y = busca_Binaria(x, marbles)    
        if y != -1:      
            print(f'{x} found at {1+y}')
        else:
            print(f'{x} not found')
    case += 1
