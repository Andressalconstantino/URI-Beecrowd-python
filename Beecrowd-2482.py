n = int(input())
dicionario = {}
for i in range(n):
    lingua = input()
    mc = input()
    dicionario[lingua] = mc

kids = int(input())
for i in range(kids):
    name = input()
    idioma = input()
    print(name)
    print(dicionario[idioma])
    print('')
