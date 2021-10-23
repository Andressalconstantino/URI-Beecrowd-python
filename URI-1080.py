v = []
for i in range(100):
    n = int(input())
    v.append(n)
y = max(v)
x = v.index(y)
print(y)
print(x+1)