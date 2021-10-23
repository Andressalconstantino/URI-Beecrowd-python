while True:
    try:
        V, T = map(int, input().split())
        vetor = list(map(int, input().split()))
        D = {}
        for i in range(len(vetor)):
            try:
                D[vetor[i]].append(i + 1)
            except KeyError:
                D[vetor[i]] = [i + 1]
        for a in range(T):
            k, v = map(int, input().split())
            if v in D and k <= len(D[v]):
                x = D[v][k -1]
                print(x)
            else:
                print('0')
    except EOFError:
        break   