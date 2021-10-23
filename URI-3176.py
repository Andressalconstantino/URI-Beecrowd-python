times = []
num = int(input())
for i in range(num):
    nome, idade = map(str, input().split())
    inf = (nome, idade)
    times.append(inf)

times.sort(key = lambda x:(-int(x[1]), x[0]))
n_times = int(num/3)
for time_atual in range(n_times):
    print('Time', time_atual+1)
    for i in range(time_atual, len(times),n_times):
        print(times[i][0], times[i][1])
    print('')