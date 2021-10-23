while 1:    
    while 1:
        av1 = float(input())
        if av1>10 or av1<0:
            print('nota invalida')
            continue
        else:
            break
    while 1:
        av2 = float(input())
        if av2>10 or av2<0:
            print('nota invalida')
            continue
        else:
            break
    med = (av1+av2)/2
    print(f'media = {med:.2f}')
    print('novo calculo (1-sim 2-nao)')
    while 1>0:            
        resp = int(input())        
        if resp == 1 or resp==2:
            break
        print('novo calculo (1-sim 2-nao)')
    if resp==2:
        break
    elif resp==1:
        continue
