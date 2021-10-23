entrada = input()
entrada = list(entrada)
fila = []
for i in entrada:
    if i == '(':
        fila.append(i)
    elif i == ')' and len(fila)>0:
        fila.pop()
if len(fila) == 0:
    print('Partiu RU!')
else:
    print(f'Ainda temos {len(fila)} assunto(s) pendente(s)!')