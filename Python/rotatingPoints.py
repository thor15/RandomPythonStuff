from math import *
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
SIDE1X = []
SIDE1Y = []
SIDE2X = []
SIDE2Y = []
TEST = []
COUNTER = []
VALUE = [0]*ARRAYLENG
IMG = Image.new(mode="RGB", size=(WIDTH, WIDTH))

def points(x, y):
    global VALUE
    VALUE[(399+round(x))*WIDTH+399+round(y)] = 40
    if(not ((399+round(x))*WIDTH+399+round(y)) in TEST):
        TEST.append((399+round(x))*WIDTH+399+round(y))
    COUNTER.append(0)
    


def lerp(low, high, t):
    return low*(1-t)+high*t


def drawSideHorizantal(ax, ay, bx, by):
    distance = sqrt(pow(bx-ax, 2)+pow(by-ay,2))
    for i in range(0, int(distance), 1):
        x = lerp(ax, bx, i/distance)
        y = lerp(ay, by, i/distance)
        points(round(x), round(y))


def drawSideVertical(ax, ay, bx, by, n):
    distance = sqrt(pow(bx-ax, 2)+pow(by-ay,2))
    for i in range(0, int(distance), 1):
        x = lerp(ax, bx, i/distance)
        y = lerp(ay, by, i/distance)
        points(round(x), round(y))
        if(n == 0):
            SIDE1X.append(x)
            SIDE1Y.append(y)
        else:
            SIDE2X.append(x)
            SIDE2Y.append(y)
    

#starting points a:(-100, 50sqrt(3)), b: (100, 50sqrt(3)), c: (0,-50sqrt(3))
def calculatePoints(angle, radius, sideLength):

    #calculate angles
    rAngle = angle*pi/180
    shiftB = acos(sideLength/(2*radius))
    shiftA = asin(-sideLength/(2*radius))
    # print(rAngle, shiftB, shiftA)
    # print(cos(2*pi+rAngle-shiftA-pi/2))

    # set coordinates
    ax = radius*cos(2*pi-rAngle+shiftA-pi/2)
    ay = radius*sin(2*pi-rAngle+shiftA+pi/2)
    bx = radius*cos(rAngle+shiftB)
    by = radius*sin(rAngle+shiftB)
    cx = radius*sin(rAngle)
    cy = -1*radius*cos(rAngle)

    #draw side
    drawSideHorizantal(ax, ay, bx, by)
    drawSideVertical(ax, ay, cx, cy, 0)
    drawSideVertical(bx, by, cx, cy, 1)




def triangle(angle, radius, sideLength):
    global VALUE
    global IMG
    VALUE.clear()
    VALUE = [0]*ARRAYLENG
    #print(VALUE)
    calculatePoints(angle, radius, sideLength)
    for point in range(0, len(SIDE1X)-1, 1):
        #print("A:", "(" +str(SIDE1X[point]) + ","+ str(SIDE1Y[point]) +")", "   B:", "(" +str(SIDE2X[point]) + ","+ str(SIDE2Y[point]) +")")
        drawSideHorizantal(SIDE1X[point], SIDE1Y[point], SIDE2X[point], SIDE2Y[point])
    IMG = Image.new(mode="RGB", size=(WIDTH, WIDTH))
    numberBlue = 0
    for x in range(0, WIDTH-1, 1):
        for y in range(0, WIDTH, 1):
            count = 0
            if(not VALUE[(x-1)*WIDTH+y] == 0):
                count = count + 1
            if(not VALUE[(x+1)*WIDTH+y] == 0):
                count = count + 1
            if(not VALUE[(x)*WIDTH+y-1] == 0):
                count = count + 1
            if(not VALUE[(x)*WIDTH+y+1] == 0):
                count = count + 1
            if(count > 3):
                VALUE[x*WIDTH+y] = 40
            if(VALUE[(x)*WIDTH+y+1] == 0):
                numberBlue += 1
            IMG.putpixel([x,y], (abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y]))*255))
    print(numberBlue)
    IMG.show()
    
    return VALUE

#print(VALUE)
#triangle(20,20,23)
# VALUE = [0]*(ARRAYLENG)
# SIDE1X = []
# SIDE1Y = []
# SIDE2X = []
# SIDE2Y = []


# calculatePoints(45, radius)

# #print(len(SIDE1X), len(SIDE1Y), len(SIDE2X), len(SIDE2Y))

# for point in range(0, len(SIDE1X)-1, 1):
#     #print("A:", "(" +str(SIDE1X[point]) + ","+ str(SIDE1Y[point]) +")", "   B:", "(" +str(SIDE2X[point]) + ","+ str(SIDE2Y[point]) +")")
#     drawSideHorizantal(SIDE1X[point], SIDE1Y[point], SIDE2X[point], SIDE2Y[point])

# print(len(COUNTER), len(TEST))
#triangle(180, radius, 200)




# print(angle)
# fileN = 'rotating' + str(angle) +  '.png'
# img.save(fileN)



#radius = sqrt(pow(100,2)+pow(50*sqrt(3), 2))
#for printing a cycle
# for angle in range(0, 360, 1):

#     VALUE = [0]*(ARRAYLENG)
#     SIDE1X = []
#     SIDE1Y = []
#     SIDE2X = []
#     SIDE2Y = []


#     calculatePoints(angle, radius, 200, VALUE)

#     #print(len(SIDE1X), len(SIDE1Y), len(SIDE2X), len(SIDE2Y))

#     for point in range(0, len(SIDE1X)-1, 1):
#         #print("A:", "(" +str(SIDE1X[point]) + ","+ str(SIDE1Y[point]) +")", "   B:", "(" +str(SIDE2X[point]) + ","+ str(SIDE2Y[point]) +")")
#         drawSideHorizantal(SIDE1X[point], SIDE1Y[point], SIDE2X[point], SIDE2Y[point])


#     img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

#     for x in range(0, WIDTH-1, 1):
#         for y in range(0, WIDTH, 1):
#             count = 0
#             if(not VALUE[(x-1)*WIDTH+y] == 0):
#                 count = count + 1
#             if(not VALUE[(x+1)*WIDTH+y] == 0):
#                 count = count + 1
#             if(not VALUE[(x)*WIDTH+y-1] == 0):
#                 count = count + 1
#             if(not VALUE[(x)*WIDTH+y+1] == 0):
#                 count = count + 1
#             if(count > 3):
#                 VALUE[x*WIDTH+y] = 40
#             img.putpixel([x,y], (abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y]))*255))


#     print(angle)
#     fileN = 'rotating' + str(angle) +  '.png'
#     img.save(fileN)