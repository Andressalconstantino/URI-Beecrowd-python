A, B, C, D= map(int, input().split())

jafoi = False

if (A!=B and C!=D):
    inicio = A
    fim = C

    for i in range(inicio, fim+1, A):
        if i%A==0 and i%B!=0 and C%i==0 and D%i!=0:
            print(i)
            jafoi = True
            break

if not jafoi:
    print(-1)