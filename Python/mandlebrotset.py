import math
from PIL import Image

# initialize the constants
WIDTH = 800
MAX_INT = 80
VALUEZ = []
A = -.76
B = -.11

#.4,.21
cConstant = complex(-0.2,-0.67)

# changes c until either steps is greater than MAX_INT or abs(z) > 2
def mandlebrot(c):
    z = 0
    step = 0
    while(abs(z) <= 2 and step < MAX_INT):
        #print(step)
        z = z*z + c
        step += 1
    return step


VALUEZ=[]
SCALE = 300
#sets the initial delta and 
change = 400
PRESCALE = 800
midA = -60
midB = 90

# finds a1, a2, b1, b2 by finding using the mid point and the scale
a1 = (midA-change)/SCALE
a2 = (midA+change)/SCALE
b1 = (midB-change)/SCALE
b2 = (midB+change)/SCALE

# calculate the scales to convert the small decimals into the integers that will go into the range thing
aDivisor = (abs(a2-a1)/WIDTH)
bDivisor = (abs(b2-b1)/WIDTH)
print(aDivisor, bDivisor)
aScale = int(pow(aDivisor, -1))
bScale = int(pow(bDivisor, -1))

# actually convert the floats into the integers
a1f = a1*aScale
a2f = a2*aScale
b1f = b1*bScale
b2f = b2*bScale

#print("x: ", x, "y: ", y)
print(a1f, a2f, aScale, b1f, b2f, bScale, cConstant)
#print(int(-1*(WIDTH/2))/SCALE, int(1*(WIDTH/2))/SCALE)

# the error is not the float, when adding in the float part into the loop the fractal still breaks
aFloat = a1f - int(a1f)
bFloat = b1f - int(b1f)
# Uncomment the following lines to fix the fractal
a1f = math.trunc(a1f*1000)/1000
a2f = math.floor(a2f*1000)/1000
b1f = math.floor(b1f*1000)/1000
b2f = math.floor(b2f*1000)/1000
for a in range(math.floor(a1f), math.ceil(a2f), 1):
    for b in range(math.floor(b1f), math.ceil(b2f), 1):
        c = complex(((a+aFloat)/aScale), ((b+bFloat)/bScale))
        e = mandlebrot(c)
        #print(a1f/aScale, ", ", a/aScale, b1f/bScale, ', ', b/bScale, e)
        VALUEZ.append(e)

#print(VALUEZ)

# inputs c values into the image so that it can be displayed 
width = int(math.sqrt(len(VALUEZ)))
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        color = int(125/(1+e**(VALUEZ[x*WIDTH+y]/7-6)))
        img.putpixel([x,y], (0,0,color))
#fileN = str(i) + "_scale" + str(SCALE)+'_change' + str(change) + '.png'
img.show()
