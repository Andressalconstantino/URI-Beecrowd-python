ct = int(input())

for i in range(ct):
    gaps = {}
    sg = []
    ganhador = False
    a, number = map(int, input().split())
    y = list(map(int, input().split()))
    for i in range(len(y)):
        if y[i]==number:
            print(i+1)
            ganhador = True
            break
        elif y[i]>number:
            gap = y[i] - number
            if gap not in gaps:
                gaps[gap] = i+1
                sg.append(gap)
        
        elif y[i]<number:
            gap = number - y[i]
            if gap not in gaps:
                gaps[gap] = i+1
                sg.append(gap)

    if not ganhador:
        sg = sorted(sg)
        wins = sg[0]
        print(gaps[wins])
