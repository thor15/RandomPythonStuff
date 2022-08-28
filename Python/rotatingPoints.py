from math import *
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUE = [0]*(ARRAYLENG)


def points(x, y):
    for i in range(int(x)-4, int(x)+4,1):
        for j in range(int(y)-4, int(y)+4,1):
            VALUE[(399-i)*WIDTH+399-j]=40


#starting points a:(-100, 50sqrt(3)), b: (100, 50sqrt(3)), c: (0,-50sqrt(3))
def calculatePoints(angle, radius):
    rAngle = angle*pi/2
    shiftB = acos(100/radius)
    shiftA = asin(-100/radius)

    ax = radius*cos(2*pi-rAngle+shiftA-pi/2)
    ay = radius*sin(2*pi-rAngle+shiftA+pi/2)
    bx = radius*cos(rAngle+shiftB)
    by = radius*sin(rAngle+shiftB)
    cx = radius*sin(rAngle)
    cy = -1*radius*cos(rAngle)

    print(ax, ay)
    print(bx, by)
    print(cx, cy)
    points(ax, ay)
    points(bx, by)
    points(cx, cy)

radius = sqrt(pow(100,2)+pow(50*sqrt(3), 2))
calculatePoints(90, radius)
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,y], (abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y]))*255))


img.show()