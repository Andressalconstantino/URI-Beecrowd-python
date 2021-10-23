while True:
    try:
        n = int(input())
        alunos = []
        for i in range(n):
            nome, reg, dist = map(str, input().split())
            aluno = (nome, reg, dist)
            alunos.append(aluno)
        alunos.sort(key= lambda x:(int(x[2]), x[1], x[0]))
        for i in alunos:
            print(i[0])
    except EOFError:
        break