x= int(input())
w= x/3600
h= int(w)
m1= x-(h*3600)
m2= m1/60
m= int(m2)
s1= (m*60)+(h*3600)
s2= x-s1
s= int(s2)
print("%d:"%h+"%d:"%m+"%d"%s)