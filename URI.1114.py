senha = 2002
while 1>0:
    tentativa = int(input())
    if tentativa == senha:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')
        continue