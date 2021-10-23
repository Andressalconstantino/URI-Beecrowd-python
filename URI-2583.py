c_testes = int(input())
for caso in range(c_testes):
    q_listas = int(input())
    lista = set()
    lista_f = set()
    for listas in range(q_listas):
        caso = input()
        if 'chirrin' in caso:
            caso = caso.split(' ')
            lista.add(caso[0])
        if 'chirrion' in caso:
            caso = caso.split(' ')
            lista_f.add(caso[0])
    lista_final = set(lista - lista_f)
    lista_final = sorted(lista_final)
    print('TOTAL')
    for item in lista_final:
        print(item)
