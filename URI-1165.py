num = int(input())
for i in range(num):
    def eh_primo(numero):
        if numero > 1:
            if numero > 3:
                for i in range(2, numero):
                    if numero % i == 0:
                        return False
            return True
        return False
    x= int(input())
    if eh_primo(x):
        print('%d eh primo'%x)
    else:
        print('%d nao eh primo'%x)