import math
from PIL import Image


WIDTH = 2400 #previous width 2400
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
a1 = -51086
a2 = a1 + WIDTH
b2 = 104160
b1 = b2 - WIDTH

for a in range(a1, a2, 1): #-2350, -1950
    for b in range(b1, b2, 1): #4200, 4600 
        c = complex(a/SCALEA, b/SCALEB)
        d = complex(b/SCALEB, a/SCALEA) #11200
        #print(c)
        #print(d)
        e = thing(c, d)
        #print(e)
        VALUEX.append(a/SCALEA)
        VALUEY.append(b/SCALEB)
        VALUEZ.append(e)

img = img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        if(VALUEZ[x*WIDTH+y]):
            img.putpixel([x,WIDTH-1-y], (252,230,36))
        else:
            img.putpixel([x,WIDTH-1-y], (int(184/(1+math.e**(-1*(VALUEZ[x*WIDTH+y]/7-6)))+68),int(229/(1+math.e**(-1*(VALUEZ[x*WIDTH+y]/7-6)))+1),int(48/(1+math.e**((VALUEZ[x*WIDTH+y]/7-6)))+36)))


#logistic regression code: 
# img.putpixel([x,WIDTH-1-y], (int(184/(1+math.e**(-1*(VALUEZ[x*WIDTH+y]/7-6)))+68),int(229/(1+math.e**(-1*(VALUEZ[x*WIDTH+y]/7-6)))+1),
#   int(48/(1+math.e**((VALUEZ[x*WIDTH+y]/7-6)))+36)))
#yellow (252,230,36)
img.show()
#img.save('redyellowgalaxy.png')