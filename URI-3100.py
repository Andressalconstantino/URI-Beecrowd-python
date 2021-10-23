N = list(input().strip())
for n in range(len(N)):
    if N[n] == '5':
        N.pop(n)
        N.insert(0, '5')

for n in range(len(N)):
    if (N[n] == '3'):
        ind_n = n - 1
        while ind_n >= 0 and N[ind_n] != '7':
            aux_N = N[ind_n]   
            N[ind_n] = N[ind_n + 1]
            N[ind_n + 1] = aux_N
    
            ind_n -= 1

print(''.join(N))