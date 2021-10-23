while 1>0:
    num = int(input())
    if num==0:
        break
    if num!=0 and 'camisetas' in locals():
        print('')
    camisetas = []
    for i in range(num):
        nome= input()
        cor, tam = map(str, input().split())
        inf = (cor, tam, nome)
        camisetas.append(inf)
    camisetas.sort(key= lambda x: (x[0], x[1]=='G', x[1]=='M', x[1]=='P', x[2]))
    for i in camisetas:
        print(*i)