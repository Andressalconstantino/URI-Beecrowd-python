bk=float(input())
V=bk
cem=V/100 #100
b=V%100 
c=b/50  #50
d=b%50
e=d/20  #20
f=d%20
g=f/10  #10
h=f%10
i=h/5  #5
j=h%5
k=j/2  #2
l=j%2  #1

E=V*100
B=(int(E))
m=B%100
n=m/50  #0,5
o=m%50  
p=o/25  #0,25
q=o%25
r=q/10  #0,10
s=q%10
t=s/5 #0,05
u=s%5 #0,01
print("NOTAS:")
print(f"{int(cem)} nota(s) de R$ 100.00")
print(f"{int(c)} nota(s) de R$ 50.00")
print(f"{int(e)} nota(s) de R$ 20.00")
print(f"{int(g)} nota(s) de R$ 10.00")
print(f"{int(i)} nota(s) de R$ 5.00")
print(f"{int(k)} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{int(l)} moeda(s) de R$ 1.00")
print(f"{int(n)} moeda(s) de R$ 0.50")
print(f"{int(p)} moeda(s) de R$ 0.25")
print(f"{int(r)} moeda(s) de R$ 0.10")
print(f"{int(t)} moeda(s) de R$ 0.05")
print(f"{int(u)} moeda(s) de R$ 0.01")