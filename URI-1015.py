x1, y1= map(float, input().split())
x2, y2= map(float, input().split())
m1= (x2 -x1) * (x2 -x1)
m2= (y2 -y1) * (y2 -y1)
mm= m1 + m2
import math
d= math.sqrt(mm)
print("%.4f" %d)