pi = 3.14159
A, B, C= map(float, input().split())
Z= (1/2)*(A*C) #triangle rectangled
N= pi*(C*C) #circle
T= (1/2)*(A+B)*C #trapezium
S= B*B #square
R= A*B #rectangle
print("TRIANGULO: %.3f" %Z)
print("CIRCULO: %.3f" %N)
print("TRAPEZIO: %.3f" %T)
print("QUADRADO: %.3f" %S)
print("RETANGULO: %.3f" %R)