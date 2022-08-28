import math
import numpy
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUE = [0]*(ARRAYLENG)

def triangle(centerPointX, centerPointY, sideLength, angle):


    rAngle = angle*math.pi/180
    x = sideLength/2
    apothem = x/math.sqrt(3)

    height = x*math.sqrt(3)
    
    c = sideLength
    deltaC = (sideLength-1)/height
    count = 0
    
    test = [] 

    sinHor = math.sin(rAngle)
    cosHor = math.cos(rAngle)

    sinVer = math.sin(rAngle+math.pi/2)
    cosVer = math.cos(rAngle+math.pi/2)

    #sinInv = 1/sin
    #cosInv = 1/cos

    #print(sin, cos)
    #print(height, c)

    for i in range(int(-math.ceil(height)/2), int(math.ceil(height)/2), 1):
        for j in range(int(int(-c)/2), int(int(c)/2), 1):
            xDirectionCalc = centerPointX+round(j*cosHor+i*sinHor)
            yDirectionCalc = centerPointY+round(i*cosHor+j*sinHor)

            value = (xDirectionCalc)*WIDTH+(yDirectionCalc)
            # if(value in test):
            #     print(i, j, value, test.index(value))
            if(not (value in test)):
                test.append(value)
            VALUE[int(value)] = c/2
            count += 1
        c = c-deltaC
    print(centerPointX+round(j), centerPointY+round(i))
    #print("Total Calls:", count, "Unique values: ", len(test))
    #print("Total Calls:", count, "Unique values: ", len(test))
    

# def repeat(sideLength, count):
#     apothemOld = sideLength/math.sqrt(12)
#     apothemNew = sideLength/math.sqrt(48)

#     triangle(400,400,sideLength, 45)
#     triangle()
    
VALUE = [0]*(ARRAYLENG)
triangle(399, 399, 200, 45)

img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,y], (abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y]))*255))


img.show()
#fileN = 'rotatetriangle'+ str(ang) + '.png'
#img.save(fileN)