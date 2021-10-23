aid= int(input())
y1= aid/365
y= int(y1) #years
m1= aid%365
m2= m1/30
m= int(m2) #months
d1= m1%30
d2= d1/1
d3= int(d2) #days
print("%d ano(s)" %y)
print("%d mes(es)" %m)
print("%d dia(s)" %d3)