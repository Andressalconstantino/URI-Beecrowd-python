while True:
    try:
        n_atributos = int(input())
        quant_cartas = list(map(int, input().split()))
        baralhoM = []
        baralhoL = []
        #BARALHO DE MARCOS
        for cartasM in range(quant_cartas[0]):
            cartasM = list(map(int, input().split()))
            baralhoM.append(cartasM)
        #BARALHO DE LEONARDO
        for cartasL in range(int(quant_cartas[1])):
            cartasL = list(map(int, input().split()))
            baralhoL.append(cartasL)


        #ESCOLHER CARTAS
        m_l = list(map(int, input().split( )))
        M = m_l[0] - 1
        L = m_l[1] - 1
        atri = int(input())
        atributo = atri - 1

        carta_escolhidaM = baralhoM[M]
        carta_escolhidaL= baralhoL[L]

        #VENCEDOR
        if carta_escolhidaM[atributo] > carta_escolhidaL[atributo]:
            print('Marcos')
        elif carta_escolhidaM[atributo] == carta_escolhidaL[atributo]:
            print('Empate')
        else:
            print('Leonardo')
    except EOFError:
        break