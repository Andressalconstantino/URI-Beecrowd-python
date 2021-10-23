casos_teste = int(input())
for i in range(casos_teste):
    string = list(input())
    quant = int(input())
    for i in range(len(string)):
        if (ord(string[i]) - quant) < 65:
            string[i] = chr(90 - (64 -(ord(string[i]) - quant)))
        else:
            string[i] = chr((ord(string[i]) - quant))
    print(''.join(string))