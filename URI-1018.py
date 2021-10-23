bk= int(input())
y1= bk/100
m1= bk%100
m2= m1/50
d1= m1%50
d2= d1/20
t1= d1%20
t2= t1/10
f1= t1%10
f2= f1/5
two= f1%5
tw= two/2
on= two%2
oe= on/1
print(bk)
print("%d nota(s) de R$ 100,00" %y1)
print("%d nota(s) de R$ 50,00" %m2)
print("%d nota(s) de R$ 20,00" %d2)
print("%d nota(s) de R$ 10,00" %t2)
print("%d nota(s) de R$ 5,00" %f2)
print("%d nota(s) de R$ 2,00" %tw)
print("%d nota(s) de R$ 1,00" %oe)