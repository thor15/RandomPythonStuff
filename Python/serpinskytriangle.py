import math
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUES = [0]*(ARRAYLENG)

def triangle(centerPointX, centerPointY, sideLength, angle):


    rAngle = angle*math.pi/180
    x = sideLength/2
    apothem = x/math.sqrt(3)

    height = x*math.sqrt(3)
    
    c = sideLength
    deltaC = (sideLength-1)/height
    count = 0
    
    test = []

    sinVal = math.sin(rAngle)
    cosVal = math.cos(rAngle)

    #sinInv = 1/sin
    #cosInv = 1/cos

    # print(sin, cos)
    # print(height, c)

    for i in range(int(-math.ceil(height)/2), int(math.ceil(height)/2), 1):
        for j in range(int(int(-c)/2), int(int(c)/2), 1):
            value = (centerPointY+round(i*sinVal+j*cosVal))*WIDTH+(centerPointY+round(i*cosVal+j*sinVal))
            # if(len(test) == 0):
            #     print(value)
            # if(value in test):
            #     print(i, j, value, test.index(value))
            if(not (value in test)):
                test.append(value)
            VALUES[int(value)] = int(c/8)
            count += 1
        c = c-deltaC
    #print(value)
    print("Total Calls:", count, "Unique values: ", len(test))
    

# def repeat(sideLength, count):
#     apothemOld = sideLength/sqrt(12)
#     apothemNew = sideLength/sqrt(48)

#     triangle(400,400,sideLength, 45)
#     triangle()
    
VALUES = [0]*(ARRAYLENG)
triangle(WIDTH/2, WIDTH/2, WIDTH/2, 0)

img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,y], (abs(int(VALUES[x*WIDTH+y])),abs(int(VALUES[x*WIDTH+y])),abs(int(VALUES[x*WIDTH+y]))*255))


img.show()
#fileN = 'rotatetriangle'+ str(ang) + '.png'
#img.save(fileN)