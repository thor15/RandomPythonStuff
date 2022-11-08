from PIL import Image



MAX_INT = 80
VALUEX = []
VALUEY = []
VALUEZ = []
SCALEA = 300
SCALEB = 300
cConstant = complex(0.62,0.24)


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


for a in range(-400, 400, 1):
    for b in range(-400, 400, 1):
        c = complex(a/SCALEA, b/SCALEB)
        d = juliaSet(c)
        e = pow(d.real, 2) + pow(d.imag, 2)
        VALUEX.append(a/SCALEA)
        VALUEY.append(b/SCALEB)
        VALUEZ.append(e)

