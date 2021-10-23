C = []
R = []
S = []
num = int(input())
for i in range(num):
    n, a = map(str, input().split())
    if a == 'C':
        C.append(int(n))
    elif a == 'R':
        R.append(int(n))
    elif a == 'S':
        S.append(int(n))

Coelho = sum(C)
Rato = sum(R)
Sapo = sum(S)
Total = Coelho + Rato + Sapo

P_C = (Coelho*100)/Total
P_R = (Rato*100)/Total
P_S = (Sapo*100)/Total

print('Total: %d cobaias' %Total)
print('Total de coelhos: %d' %Coelho)
print('Total de ratos: %d' %Rato)
print('Total de sapos: %d' %Sapo)
print(f'Percentual de coelhos: {P_C:.2f} %')
print(f'Percentual de ratos: {P_R:.2f} %')
print(f'Percentual de sapos: {P_S:.2f} %')