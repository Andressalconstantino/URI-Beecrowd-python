n, t = map(int, input().split())
jogadores = []
timesin = []
for i in range(n):
    nome, skill = map(str, input().split())
    jogador = (nome, skill)
    jogadores.append(jogador)
jogadores.sort(key= lambda x: -int(x[1]))
for time_atual in range(t):
    print('Time', time_atual+1)
    for i in range(time_atual, len(jogadores),t):
        timesin.append(jogadores[i][0])
    timesin.sort()
    for i in timesin:
        print(i)
    timesin = []      
    print('')
