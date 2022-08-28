import math

c = complex(.09,.62)
value1 = []
value2 = []
z1 = z2 = z3 = z4 = complex(0.5,0.5)
step = 0

while(step < 40 and (abs(z1) <=2 or abs(z2) <= 2)):
    print(z1)
    print(z2)
    
    z1 = (z1**3)**1/2
    z2 =pow(z2,1.5)
    print(z1)
    print(z2)
    z1 = z1+c
    z2 = z2+c
    step = step +1
