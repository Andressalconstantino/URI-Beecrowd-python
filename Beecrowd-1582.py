while True:
    try:
        a, b, c = map(int, input().split())

        if ((a*a)==(b*b)+(c*c)) or ((b*b)==(a*a)+(c*c)) or ((c*c)==(b*b)+(a*a)):
            x = min(a, b, c)
            comumdiv = 0
            for i in range(1,x+1):
                if a%i==0 and b%i==0 and c%i==0:
                    comumdiv = i
            if comumdiv==1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')

        else:
            print('tripla')
    except EOFError:
        break
