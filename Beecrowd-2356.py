while True:
    try:
        x = input()
        y = input()

        if y in x:
            print('Resistente')
        else:
            print('Nao resistente')

    except EOFError:
        break
