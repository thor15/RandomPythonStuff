import math
import matplotlib.pyplot as plt

WIDTH = 800
MAX_INT = 80
VALUEX = []
VALUEY = []
VALUEZ = []
SCALE = 300
A = -.76
B = -.11

#.4,.21
cConstant = complex(-0.2,-0.67)

#f = open("z.txt", "a")

#rand = Random.seed()
change = 300
PRESCALE = 800
midA = 0
midB = 1
#midX = 0
#midY = 0


#print(midA, midB)


a1 = (midA-change)/SCALE
a2 = (midA+change)/SCALE
b1 = (midB-change)/SCALE
b2 = (midB+change)/SCALE


aDivisor = (abs(a2-a1)/WIDTH)
bDivisor = (abs(b2-b1)/WIDTH)
print(aDivisor, bDivisor)
aScale = int(pow(aDivisor, -1))
bScale = int(pow(bDivisor, -1))

a1f = a1*aScale
a2f = a2*aScale
b1f = b1*bScale
b2f = b2*bScale
#print("x: ", x, "y: ", y)
print(a1f, a2f, aScale, b1f, b2f, bScale, cConstant)
#print(int(-1*(WIDTH/2))/SCALE, int(1*(WIDTH/2))/SCALE)

def juliaSet(c):
    z = c
    step = 0
    while(abs(z) <= 2 and step < MAX_INT):
        #print(step)
        z = z*z + cConstant
        step += 1
    return step


for a in range(math.floor(a1f), math.ceil(a2f), 1):
    for b in range(math.floor(b1f), math.ceil(b2f), 1):
        c = complex((a/aScale), (b/bScale))
        e = juliaSet(c)
        #print(a/aScale, b/bScale, e)
        VALUEX.append(a/aScale)
        VALUEY.append(b/bScale)
        VALUEZ.append(e)


print("adding to the plot")
fig, ax = plt.subplots()

ax.scatter(x=VALUEX, y=VALUEY, c=VALUEZ)
#print(fig)
#print(ax)
plt.show()
plt.savefig("galaxy.png")