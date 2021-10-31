def arredondamento(x):
    z = int(x)
    if (z<x):
        return z+1
    else:
        return z


V, N = map(int, input().split())
vetor = []

#10%
dez = ((V*N)*10)/100
vetor.append(arredondamento(dez))

#20%
v = ((V*N)*20)/100
vetor.append(arredondamento(v))

#30%
tr = ((V*N)*30)/100
vetor.append(arredondamento(tr))

#40%
quarenta = ((V*N)*40)/100
vetor.append(arredondamento(quarenta))

#50%
cinquenta = ((V*N)*50)/100
vetor.append(arredondamento(cinquenta))

#60%
sessenta = ((V*N)*60)/100
vetor.append(arredondamento(sessenta))

#70%
setenta = ((V*N)*70)/100
vetor.append(arredondamento(setenta))

#80%
oitenta = ((V*N)*80)/100
vetor.append(arredondamento(oitenta))

#90%
noventa = ((V*N)*90)/100
vetor.append(arredondamento(noventa))

print(*vetor)
