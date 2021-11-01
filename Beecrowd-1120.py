while 1:
    brokennumber, number = map(str, input().split())
    if brokennumber=='0' and number=='0':
        break
    
    finals = ''

    for i in range(len(number)):
        if number[i]!=brokennumber:
            finals += number[i]
    
    if len(finals)>0:
        finals = int(finals)
    else:
        finals = 0
    
    print(finals)
