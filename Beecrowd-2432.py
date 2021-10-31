n_circulos, n_tentativas = map(int, input().split())

circles = []
for i in range(n_circulos):
    raio = int(input())
    raio = raio * raio
    circles.append(raio)

circles.sort()

total = 0
for i in range(n_tentativas):
    x, y = map(int, input().split())
    ponto = (x*x) + (y*y)
    
    if ponto <= circles[-1]:
        inicio = 0
        fim = len(circles) - 1

        while inicio < fim:
            meio = (inicio + fim) // 2
            
            if ponto <= circles[meio]:
                fim = meio
            else:
                inicio = meio + 1

        total += len(circles) - fim

print(total)
