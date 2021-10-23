num  = int(input())
total = []
for i in range(num):
    p, q = map(int, input().split())
    if p==1001:
        x = q*1.50
        total.append(x)
    if p==1002:
        x = q*2.50
        total.append(x)
    elif p==1003:
        x = q*3.50
        total.append(x)
    elif p==1004:
        x = q*4.50
        total.append(x)
    elif p==1005:
        x = q*5.50
        total.append(x)
total = sum(total)
print(f'{total:.2f}')