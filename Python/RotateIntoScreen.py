import math
import numpy
from PIL import Image
WIDTH = 800
VALUE = [0]*640000

def triangle(centerPointX, centerPointY, sideLength, angle):


    rAngle = angle*math.pi/180
    x = sideLength/2
    apothem = x/math.sqrt(3)

    height = x*math.sqrt(3)
    
    c = sideLength
    deltaC = (sideLength-1)/height
    count = 0
    
    test = []

    sin = math.sin(rAngle)
    cos = math.cos(rAngle)

    #sinInv = 1/sin
    #cosInv = 1/cos

    print(sin, cos)
    print(height, c)

    for i in range(int(-math.ceil(height)/2), int(math.ceil(height)/2), 1):
        for j in range(int(int(-c)/2), int(int(c)/2), 1):
            value = (centerPointY+round(i*sin+j*cos))*WIDTH+(centerPointY+round(i*cos+j*sin))
            # if(value in test):
            #     print(i, j, value, test.index(value))
            if(not (value in test)):
                test.append(value)
            VALUE[value] = c/2
            count += 1
        c = c-deltaC
    print("Total Calls:", count, "Unique values: ", len(test))
    

# def repeat(sideLength, count):
#     apothemOld = sideLength/math.sqrt(12)
#     apothemNew = sideLength/math.sqrt(48)

#     triangle(400,400,sideLength, 45)
#     triangle()
    

triangle(400, 400, 400, 180)

img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,y], (abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y]))*255))


img.show()
#fileN = 'nicePlus'+'.png'
#img.save(fileN) 