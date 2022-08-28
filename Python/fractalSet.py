from PIL import Image



MAX_INT = 80
VALUEX = []
VALUEY = []
VALUEZ = []
SCALEA = 300
SCALEB = 300
cConstant = complex(0.4,0.21)


poly = [1,0,2,0,1]
def fOfZ(z):
    return pow(z*z+1,2)

derivPoly = [4, 0, -4, 0]
def fPrimeOfZ(z):
    return (4*z*(z*z - 1))

def juliaSet(c):
    z = c
    step = 0
    while(abs(z) <= 2 and step < MAX_INT):
        #print(step)
        z = z*z + cConstant
        step += 1
    return step

max_Num = -1000
min_Num = 1000000000
for a in range(-400, 400, 1):
    for b in range(-400, 400, 1):
        c = complex(a/SCALEA, b/SCALEB)
        d = juliaSet(c)
        e = pow(d.real, 2) + pow(d.imag, 2)
        VALUEZ.append(e)
        if(e > max_Num):
            max_Num = e
        if(e < min_Num ):
            min_Num = e

for  i in range(0, len(VALUEZ), 1):
    VALUEZ[i] = (VALUEZ[i] - min_Num) / (max_Num - min_Num)


