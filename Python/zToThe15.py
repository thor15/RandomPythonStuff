import math
from PIL import Image


WIDTH = 800
MAX_INT = 80
VALUEX = []
VALUEY = []
VALUEZ = []
SCALE = 300
A = -.76
B = -.11


cConstant = complex(.09,.62)

#f = open("z.txt", "a")

#rand = Random.seed()
PRESCALE = 800
midA = 0
midB = 1
#midX = 0
#midY = 0
change = 300

#print(midA, midB)
testC = complex(.5,.5)
#print(pow(testC,3/2))
#print(pow(testC*testC*testC,1/2))
#print(pow(testC**3,1/2))
#print(math.sqrt(testC*testC*testC))
#print(math.sqrt(pow(testC,3)))

a1 = (midA-change)/SCALE
a2 = (midA+change)/SCALE
b1 = (midB-change)/SCALE
b2 = (midB+change)/SCALE


aDivisor = (abs(a2-a1)/WIDTH)
bDivisor = (abs(b2-b1)/WIDTH)
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
        z = pow(z*z*z,1/2) + cConstant
        step += 1
    return step

#f = open("z.txt", "a")
for a in range(math.floor(a1f), math.ceil(a2f), 1):
    for b in range(math.floor(b1f), math.ceil(b2f), 1):
        c = complex((a/aScale), (b/bScale))
        e = juliaSet(c)
        VALUEX.append(a)
        VALUEY.append(b)
        # if(c.imag == y/SCALE):
        #     VALUEZ.append(100)
        # else:
        VALUEZ.append(e)
        #f.write(str(e) + ', ')

#print(VALUEZ)
#f.close
count = 0
width = int(math.sqrt(len(VALUEZ)))
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        if(VALUEZ[x*WIDTH+y] == MAX_INT):
            img.putpixel([x,WIDTH-1-y], (0,0,0))
            count += 1
        else:
            #print(VALUEZ[x*WIDTH+y]/7-6)
            img.putpixel([x,WIDTH-1-y], (int(82/(1+pow(math.e,VALUEZ[x*WIDTH+y]/7-6))),int(82/(1+pow(math.e,VALUEZ[x*WIDTH+y]/7-6))),int(215/(1+pow(e,VALUEZ[x*WIDTH+y]/7-6)))))

#print(count)
#if((x >= WIDTH/2 -10 and x <= WIDTH/2 + 10) and (y >= WIDTH/2 -10 and y <= WIDTH/2 + 10)):
            #img.putpixel([x,WIDTH-1-y], (255,0,0))
# if(VALUEZ[a*width+b] == 80):
#     img.putpixel([a,b], (0,0,0))
# else:
#     img.putpixel([a,b], (int((MAX_INT*255/(VALUEZ[a*width+b]+1))/4), int(MAX_INT*255/(VALUEZ[a*width+b]+1)), 0))

# for i in range(280, 300, 1):
#     for b in range(660, 680, 1):
#         img.putpixel([i,b], (255,0,0))


img.show()
fileN = 'zoommingint' + str(cConstant)+ '_' + str(change)+'.png'
#img.save(fileN)
#img.close()