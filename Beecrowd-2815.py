frase = list(map(str, input().split()))
for i in range(len(frase)):
    if len(frase[i])>4:
        if frase[i][0]==frase[i][2] and frase[i][1]==frase[i][3]:
            test = list(frase[i])
            del(test[1])
            del(test[0])
            frase[i] = ''.join(test)
print(*frase)
