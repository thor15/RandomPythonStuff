from asyncore import read
from cmath import sqrt
from math import floor
from PIL import Image
WIDTH = 800

MAX_ITER = 20
ROOTS = [complex(0.63956, 0), complex(0.6999*-1,0), complex(3.0111,0), complex(0.0246,1.2179), complex(0.0246, 1.2179*-1)]
VALUEZ = []


# f(x)/f'(x) = (z*z*z*z*z - 3*z*z*z*z + z*z*z - 3*z*z - z +2)/(5*z*z*z*z - 12*z*z*z + 3*z*z - 6*z - 1)

def newton(z, step):
    steps = step
    if(steps < MAX_ITER):
        z = z - (fOfZ(z))/(fPrimeOfZ(z))
        steps += 1
        return newton(z, steps)
    else:
        return z

poly = [1,0,2,0,1]
def fOfZ(z):
    return pow(z*z+1,2)

derivPoly = [4, 0, -4, 0]
def fPrimeOfZ(z):
    return (4*z*(z*z - 1))

def nearestRoot(position):
    min = pow(2,24)
    ind = -1
    for i in range(0, len(ROOTS), 1):
        if(sqrt(pow(position.real-ROOTS[i].real, 2)+pow(position.imag-ROOTS[i].imag, 2)).real < min):
            min = sqrt(pow(position.real-ROOTS[i].real, 2)+pow(position.imag-ROOTS[i].imag, 2)).real
            ind = i
    return ind
    
max_Num = -1000
min_Num = 1000000000
iterations = 4
def juliaSet(z):
    n = 0
    while(n < iterations):
        a = fOfZ(z)
        b = fPrimeOfZ(z)
        if(b == 0):
            break
        c = a/b
        z = c
        n += 1
    #print(MAX_NUM)
    
    return z

img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for a in range(int(-1*(WIDTH/2)), int(1*(WIDTH/2)), 1):
    for b in range(int(-1*WIDTH/2), int(1*WIDTH/2), 1):
        c = complex(a/10,b/10)
        d = juliaSet(c)
        e = pow(d.real, 2) + pow(d.imag, 2)
        VALUEZ.append(e)
        if(e > max_Num):
            max_Num = e
        if(e < min_Num ):
            min_Num = e


        # d = newton(c, 0)
        # e = nearestRoot(d)
        # if(e == 0):
        #     img.putpixel([a+int((WIDTH/2)),b+int((WIDTH/2))], (255,255,255))
        # if(e==1):
        #     img.putpixel([a+int((WIDTH/2)),b+int((WIDTH/2))], (255,0,0))
        # if(e==2):
        #     img.putpixel([a+int((WIDTH/2)),b+int((WIDTH/2))], (0,255,0))
        # if(e==3):
        #     img.putpixel([a+int((WIDTH/2)),b+int((WIDTH/2))], (0,0,255))
        #if(e==4):
            #VALUEZ.append((255,255,255))
        #print(c, d, nearestRoot(d))


print(len(VALUEZ))

for  i in range(0, len(VALUEZ), 1):
    VALUEZ[i] = (VALUEZ[i] - min_Num) / (max_Num - min_Num)


#img.putpixel([a+int((WIDTH/2)),b+int((WIDTH/2))], (255/max,255,255))
for a in range(0, WIDTH, 1):
    for b in range(0, WIDTH, 1):
        img.putpixel([a,b], (int(VALUEZ[a*WIDTH+b]*255),int(VALUEZ[a*WIDTH+b]*255),int(VALUEZ[a*WIDTH+b]*255)))

img.show()
#img.save('fractal1.png')