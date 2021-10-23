while True:
    try:
        word = list(input().strip(''))
        aux = set(word)
        infos = []
        if 'x' in locals():
            print('')
        for i in aux:
            rep = word.count(i)
            i = ord(i)
            inf = (i, rep)
            infos.append(inf)
        infos.sort(key= lambda x: (x[1], -int(x[0])))
        for i in infos:
            print(*i)
        x = 1
    except EOFError:
        break