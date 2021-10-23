operacao = input()
matriz = []
for linha in range(12):
  matriz.append([])
  for i in range(12):
      coluna = float(input())
      matriz[linha].append(coluna)

soma = 0
quant = 0

for linha in range(12):
  for coluna in range(12):
    if (coluna > linha):
      soma += matriz[linha][coluna]
      quant += 1

if operacao == 'S':
  print("%.1" %soma)
else:
  x= soma/quant
  print("%.1f" %x)