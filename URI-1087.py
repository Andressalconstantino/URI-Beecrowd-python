while 1>0:
    x1, x2, a, b = map(int, input().split())
    damas = (x1, x2, a, b)
    if sum(damas) == 0:
        break
    if damas[0]==damas[2] and damas[1]==damas[3]:
        print(0)
    elif abs(damas[0]-damas[2]) == abs(damas[1]-damas[3]):
        print(1)
    elif (damas[0]!=damas[2] and damas[1]==damas[3]) or (damas[0]==damas[2] and damas[1]!=damas[3]):
        print(1)
    else:
        print(2)