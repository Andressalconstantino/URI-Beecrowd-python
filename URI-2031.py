num  = int(input())
for i in range(num):
    j1 = input()
    j2 = input()
    if j1=='ataque' and j2=='pedra':
        print('Jogador 1 venceu')
    elif j2=='ataque' and j1=='pedra':
        print('Jogador 2 venceu')
    elif j2=='ataque' and j1=='ataque':
        print('Aniquilacao mutua')
    elif j2=='papel' and j1=='papel':
        print('Ambos venceram')
    elif j2=='pedra' and j1=='pedra':
        print('Sem ganhador')
    elif j2=='papel' and j1=='pedra':
        print('Jogador 1 venceu')
    elif j1=='papel' and j2=='pedra':
        print('Jogador 2 venceu')
    elif j1=='ataque' and j2=='papel':
        print('Jogador 1 venceu')
    elif j2=='ataque' and j1=='papel':
        print('Jogador 2 venceu')