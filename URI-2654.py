num = int(input())
candidatos = []
for i in range(num):
    nome, p1, p2, p3 = map(str, input().split())
    candidato = (nome, p1, p2, p3)
    candidatos.append(candidato)
candidatos.sort(key= lambda x: (-int(x[1]), -int(x[2]), int(x[3]), x[0]))
print(candidatos[0][0])