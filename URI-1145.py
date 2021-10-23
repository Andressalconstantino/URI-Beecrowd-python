seq, Y = map(int, input().split())
numero = 1
rangesin = int((Y/seq)+1)
for i in range(1, rangesin):
    resposta = ''
    for i in range(seq):
        resposta = resposta + str(numero) + ' '
        numero += 1
    print(resposta[:-1])