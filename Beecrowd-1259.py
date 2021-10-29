n = int(input())
pares = []
impar = []
for i in range(n):
    x = int(input())
    if x%2==0:
        pares.append(x)
    else:
        impar.append(x)


pares = sorted(pares)
impar = sorted(impar)

for j in range(len(pares)):
    print(pares[j])

y = len(impar)-1
for i in range(len(impar)):
    print(impar[y-i])
    
