matriz=[]
operacao = input()

for coluna in range(12):
    matriz.append([])
    for linha in range(12):
        x = float(input())
        matriz[coluna].append(x)

soma = 0
quant = 0
col = 1
for coluna in range(1,11):
    for linha in range(0,col):
        soma += matriz[coluna][linha]
       
        quant += 1
    if coluna < 5:
        col += 1
    if coluna > 5:
        col -= 1
   
   

media = soma / quant

if operacao == "S":
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(media))