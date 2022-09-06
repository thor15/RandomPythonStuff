from glob import glob
from math import *
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
SIDE1X = []
SIDE1Y = []
SIDE2X = []
SIDE2Y = []
ARRAYOFVAL = [0]*ARRAYLENG
VALUE = [0]*ARRAYLENG
IMG = Image.new(mode="RGB", size=(WIDTH, WIDTH))
COLOUR = 40

def points(x, y):
    global ARRAYOFVAL
    global COLOUR
    coordinateVal = 1000*(x+399)+y+399
    ARRAYOFVAL.append(coordinateVal)
    


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




def triangle(angle, radius, sideLength, color):
    global ARRAYOFVAL
    global IMG
    global SIDE1X
    global SIDE1Y
    global SIDE2X
    global SIDE2Y
    global COLOUR
    COLOUR = color
    SIDE1X = []
    SIDE1Y = []
    SIDE2X = []
    SIDE2Y = []
    ARRAYOFVAL.clear()
    #print(VALUE)
    calculatePoints(angle, radius, sideLength)
    for point in range(0, len(SIDE1X)-1, 1):
        #print("A:", "(" +str(SIDE1X[point]) + ","+ str(SIDE1Y[point]) +")", "   B:", "(" +str(SIDE2X[point]) + ","+ str(SIDE2Y[point]) +")")
        drawSideHorizantal(SIDE1X[point], SIDE1Y[point], SIDE2X[point], SIDE2Y[point])
    return ARRAYOFVAL