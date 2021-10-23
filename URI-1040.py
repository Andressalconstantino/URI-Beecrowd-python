N1, N2, N3, N4= map(float, input().split())
w1, w2, w3, w4= 2, 3, 4, 1
c1= (N1*w1) + (N2*w2) + (N3*w3) + (N4*w4)
c2= w1 + w2 + w3 + w4
c= c1/c2

if c >= 7.0:
  print("Media: %.1f" %c)
  print("Aluno aprovado.")
if c <= 4.9:
  print("Media: %.1f" %c)
  print("Aluno reprovado.")
if c>=5.0 and c <=6.9:
  print("Media: %.1f" %c)
  print("Aluno em exame.")
  ne= float(input())
  print("Nota do exame: %.1f" %ne)
  ng= (ne + c)/2
  if ng >= 5.0:
    print("Aluno aprovado.")
    print("Media final: %.1f" %ng)
  if ng <= 4.9:
    print("Aluno reprovado.")
    print("Media final: %.1f" %ng)