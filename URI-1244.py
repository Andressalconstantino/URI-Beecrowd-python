num = int(input())
aux = 1
for i in range(num):
    final = []
    ennd = []
    string = (input().split())
    for i in string:
        tupla = (1, i)
        final.append(tupla)
    final.sort(key= lambda x: len(x[1]), reverse= True)
    for i in final:
        ennd.append(i[1])
    print(*ennd)