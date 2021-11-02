lista1 = list(map(str, input().split()))
lista2 = list(map(str, input().split()))
friend = input()
new = []

if friend=='nao':
    for i in range(len(lista1)):
        new.append(lista1[i])
    for i in range(len(lista2)):
        new.append(lista2[i])

else:
    for i in range(len(lista1)):
        if lista1[i]==friend:
            for j in range(len(lista2)):
                new.append(lista2[j])
        new.append(lista1[i])

print(*new)
