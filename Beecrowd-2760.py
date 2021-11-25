frase1 = input()
frase2 = input()
frase3 = input()

var1 = frase1+frase2+frase3
var2 = frase2+frase3+frase1
var3 = frase3+frase1+frase2
part1 = ''
part2 = ''
part3 = ''

if len(frase1) <= 10:
    part1 = frase1
else:
    for i in range(10):
        part1 += frase1[i]
if len(frase2) <= 10:
    part2 = frase2
else:
    for i in range(10):
        part2 += frase2[i]
if len(frase3) <= 10:
    part3 = frase3
else:
    for i in range(10):
        part3 += frase3[i]

var4 = part1+part2+part3

print(var1)
print(var2)
print(var3)
print(var4)
