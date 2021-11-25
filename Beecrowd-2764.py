dia, mes, ano = map(str, input().split('/'))

var1 = f'{mes}/{dia}/{ano}'
var2 = f'{ano}/{mes}/{dia}'
var3 = f'{dia}-{mes}-{ano}'

print(var1)
print(var2)
print(var3)
