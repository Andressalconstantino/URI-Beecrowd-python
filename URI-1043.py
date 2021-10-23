n1, n2, n3= map(float, input().split())
if (n1+n2)>n3 and  (n1+n3)>n2 and (n2+n3)>n1:
    p= n1+n2+n3
    print("Perimetro = %.1f" %p)
else:
    a= 1/2*(n1+n2)*n3
    print("Area = %.1f" %a)