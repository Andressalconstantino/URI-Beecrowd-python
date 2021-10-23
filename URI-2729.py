quant_testes = int(input())
for lista in range(quant_testes):
    lista = set(map(str, input().split()))
    lista = sorted(lista)
    print(*lista)