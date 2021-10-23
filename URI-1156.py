soma = 1
x = 2
for i in range(3, 41, 2):
    soma += i/x
    x *= 2
print('%.2f' %soma)