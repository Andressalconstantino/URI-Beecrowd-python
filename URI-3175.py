quant = int(input())
b_a = list(map(int, input().split(' ')))
b_aq = set(b_a)
b_aq = sorted(b_aq)
cont = 1
presentes = {}
for a in b_aq:
    presentes[a] = cont
    cont += 1
for i in range(len(b_a)):
    if b_a[i] in presentes:
        b_a[i] = presentes[b_a[i]]
print(sum(b_a))