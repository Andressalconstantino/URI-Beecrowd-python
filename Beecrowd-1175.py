vetor = []
for i in range(20):
    x = int(input())
    vetor.append(x)

for i in range(10):
    aux = 19-i
    vetor[i], vetor[aux] = vetor[aux], vetor[i]

for i in range(20):
    print(f'N[{i}] = {vetor[i]}')
