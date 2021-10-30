ct =int(input())
for i in range(ct):
    frase = input()
    caracteres = set()
    for i in range(len(frase)):
        if frase[i] != ',' and frase[i] != ' ':
            caracteres.add(frase[i])
    if len(caracteres) == 26:
        print('frase completa')
    elif len(caracteres) >= 13:
        print('frase quase completa')
    else:
        print('frase mal elaborada')
