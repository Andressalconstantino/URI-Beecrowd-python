nums = list(map(float, input().split()))
nums.sort(reverse=True)
A = nums[0]
B = nums[1]
C = nums[2]

if A>=(B+C):
    print('NAO FORMA TRIANGULO')
    from sys import exit
    exit()
if (A*A)==((B*B) + (C*C)):
    print('TRIANGULO RETANGULO')
if (A*A)>((B*B) + (C*C)):
    print('TRIANGULO OBTUSANGULO')
if (A*A)<((B*B) + (C*C)):
    print('TRIANGULO ACUTANGULO')
if A==B==C:
    print('TRIANGULO EQUILATERO')
if (A==B and A!=C) or (A==C and B!=C) or (B==C and B!=A):
    print('TRIANGULO ISOSCELES')