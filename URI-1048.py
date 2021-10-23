a= float(input())
if a<= 400.00:
    b= (a*15)/100
    c= a + b
    print("Novo salario: %.2f" %c)
    print("Reajuste ganho: %.2f" %b)
    print("Em percentual: 15 %")

if 400.01<= a <= 800.00:
    b= (a*12)/100
    c= a + b
    print("Novo salario: %.2f" %c)
    print("Reajuste ganho: %.2f" %b)
    print("Em percentual: 12 %")

if 800.01<= a <=1200.00:
    b= (a*10)/100
    c= a + b
    print("Novo salario: %.2f" %c)
    print("Reajuste ganho: %.2f" %b)
    print("Em percentual: 10 %")

if 1200.01<= a <=2000.00:
    b= (a*7)/100
    c= a + b
    print("Novo salario: %.2f" %c)
    print("Reajuste ganho: %.2f" %b)
    print("Em percentual: 7 %")
    
if a>2000.00:
    b= (a*4)/100
    c= a + b
    print("Novo salario: %.2f" %c)
    print("Reajuste ganho: %.2f" %b)
    print("Em percentual: 4 %")