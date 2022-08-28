import math
import matplotlib.pyplot as plt


plt.close()
MAX_INT = 80
VALUEX = []
VALUEY = []
VALUEZ = []
SCALEA = 274286
SCALEB = 256000

def thing(c, d):
    z = c
    step = 0
    while(abs(z) <= 2 and step < MAX_INT):
        z = z*z + d
        step += 1
    return step

# near boarder see small galaxy clusters a: -2350, -1950, b: 4200, 4600, scale: 11200
# small scale galaxy like image a: -7450, -7100, b: 15900, 16275, scale: 40000
# attempt 2 large galaxy a: -12771, -12171, b: 27257, 27900, scale: 68571
# increase scale again a: -25542, -24342, b: 50868, 52068 #scalea = 137142, scaleb, 127971
# third increase 
for a in range(-51086, -48686, 1): #-2350, -1950
    for b in range(101760, 104160, 1): #4200, 4600 
        c = complex(a/SCALEA, b/SCALEB)
        d = complex(b/SCALEB, a/SCALEA) #11200
        #print(c)
        #print(d)
        e = thing(c, d)
        #print(e)
        VALUEX.append(a/SCALEA)
        VALUEY.append(b/SCALEB)
        VALUEZ.append(e)
print("adding to the plot")
fig, ax = plt.subplots()

ax.scatter(x=VALUEX, y=VALUEY, c=VALUEZ)
#print(fig)
#print(ax)
plt.show()
plt.savefig("galaxy.png")