while True:
    try:
        n = int(input())
        a = []
        r = []
        for i in range(n):
            carne, val = map(str, input().split())
            inf = (carne, val)
            a.append(inf)
        a.sort(key = lambda x: int(x[1]))
        for inf in a:
            r.append(inf[0])
        print(*r)
    except EOFError:
        break