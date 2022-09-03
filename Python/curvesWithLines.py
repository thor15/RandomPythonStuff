from math import *
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
SIDE1X = []
SIDE1Y = []
SIDE2X = []
SIDE2Y = []
PIXELVALUES = [0]*ARRAYLENG

def points(x, y):
    global PIXELVALUES
    global COLOUR
    PIXELVALUES[(399+round(x))*WIDTH+399+round(y)] = 40
    


def lerp(low, high, t):
    return low*(1-t)+high*t


def drawSideHorizantal(ax, ay, bx, by):
    distance = sqrt(pow(bx-ax, 2)+pow(by-ay,2))
    for i in range(0, int(distance), 1):
        x = lerp(ax, bx, i/distance)
        y = lerp(ay, by, i/distance)
        points(round(x), round(y))


def drawSideVertical(ax, ay, bx, by, n):
    global SIDE1X
    global SIDE1Y
    global SIDE2X
    global SIDE2Y
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
    drawSideVertical(ax, ay, cx, cy, 0)
    drawSideVertical(cx, cy, bx, by, 1)


sideLength = 600
radius = sqrt(pow(sideLength/2, 2)+pow(sideLength/(4*sqrt(3)),2))
calculatePoints(0, radius, sideLength)
for point in range(0, len(SIDE1X)-1, 1):
    drawSideHorizantal(SIDE1X[point], SIDE1Y[point], SIDE2X[point], SIDE2Y[point])

img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,y], (abs(int(PIXELVALUES[x*WIDTH+y])),abs(int(PIXELVALUES[x*WIDTH+y])),abs(int(PIXELVALUES[x*WIDTH+y]))*255))


img.show()