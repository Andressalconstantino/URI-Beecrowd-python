while True:
    try:

        n = int(input())
        for i in range(n):
            x = int(input())
            print(f'resposta {i+1}: {x}')

    except EOFError:
        break
