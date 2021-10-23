paises = set()
ouro = []
prata = []
bronze = []
while True:
    try:
        disc = input()
        n1 = input()
        n2 = input()
        n3 = input()
        ouro.append(n1)
        prata.append(n2)
        bronze.append(n3)
        paises.add(n1)
        paises.add(n2)
        paises.add(n3)
    except EOFError:
        break
ranking = []

for i in paises:
    qo = ouro.count(i)
    qp = prata.count(i)
    qb = bronze.count(i)
    rank = (i, qo, qp, qb)
    ranking.append(rank)
ranking.sort(key= lambda x: (-int(x[1]), -int(x[2]), -int(x[3]), x[0]))
print('Quadro de Medalhas')
for i in ranking:
    print(*i)