import numpy as np
from math import *
from PIL import Image
WIDTH = 800
YVALUES = {}
ARRAYOFVAL = []

def points(x, y):
    global ARRAYOFVAL
    ARRAYOFVAL.append((x+399,y+399))
    


def lerp(low, high, t):
    return low*(1-t)+high*t



def drawHorizontal(ax,ay,bx):
    aInt = int(ax)
    for i in range(0, int(bx-ax), 1):
        x = aInt+i
        points(round(x), round(ay))


def drawNotBase(ax, ay, bx, by):
    global YVALUES
    distance = sqrt(pow(bx-ax, 2)+pow(by-ay,2))
    for i in range(0, int(distance), 1):
        x = round(lerp(ax, bx, i/distance))
        y = round(lerp(ay, by, i/distance))
        points(x, y)
        inDict = False
        for i in YVALUES.keys():
            if(y == i):
                inDict = True
                break
        if(not inDict):
            YVALUES.update({y:x})
        else:
            if(YVALUES[y]-x > 0):
                drawHorizontal(x, y, YVALUES[y])
            else:
                drawHorizontal(YVALUES[y], y, x)

    

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
    points(round(ax), round(ay))
    points(round(bx), round(by))
    points(round(cx), round(cy))
    drawNotBase(ax, ay, bx, by)
    drawNotBase(ax, ay, cx, cy)
    drawNotBase(bx, by, cx, cy)




def triangle(angle, radius, sideLength):
    global YVALUES
    YVALUES = {}
    ARRAYOFVAL.clear()
    #print(VALUE)
    calculatePoints(angle, radius, sideLength)
    # print(YVALUES)
    # for point in range(0, len(SIDE1X)-1, 1):
    #     #print("A:", "(" +str(SIDE1X[point]) + ","+ str(SIDE1Y[point]) +")", "   B:", "(" +str(SIDE2X[point]) + ","+ str(SIDE2Y[point]) +")")
    #     drawHorizontal(SIDE1X[point], SIDE1Y[point], SIDE2X[point])
    return ARRAYOFVAL