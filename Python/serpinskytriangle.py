import math
from PIL import Image
import rotatingPoints
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUES = []

def splice(array):
    global VALUES
    for i in range(0, len(array)):
        VALUES.append(array[i])

# takes an array that has 
def shift(centerPointX, centerPointY, array):
    changedIndices = []
    for index in range(len(array)-1, -1, -1):
        array[index] = (math.floor(array[index][0] + centerPointX), round(array[index][1] + centerPointY))
    return array
    

temp = []
initialSideLength = 400
initialApothem = initialSideLength/(2*math.sqrt(3))
initialHeight = initialSideLength*math.sqrt(3)/2
twoThridOfHeight = 2/3*initialHeight
initialRadius = math.sqrt(twoThridOfHeight**2)

# first triangle
# temp = rotatingPoints.triangle(180, initialRadius, initialSideLength)
# splice(temp)

previousCenter = initialApothem
angle = [0, 60, 300]
for i in range(1, 2, 1):
    sideLength = initialSideLength/(2*i)
    apothem = sideLength/(2*math.sqrt(3))
    height = sideLength*math.sqrt(3)/2
    twoThridOfHeight = 2/3*height
    radius = math.sqrt(twoThridOfHeight**2)
    temp = rotatingPoints.triangle(180, radius, sideLength)
    for j in range(0,3,1):
        print((initialApothem + apothem)*math.sin(angle[j]*math.pi/180), -1*(initialApothem + apothem)*math.cos(angle[j]*math.pi/180))
        temp = shift((initialApothem + apothem)*math.sin(angle[j]*math.pi/180), -1*(initialApothem + apothem)*math.cos(angle[j]*math.pi/180), temp)
        splice(temp)
    #previousCenter += apothem*2



img = Image.new(mode="RGB", size=(WIDTH, WIDTH))

for i in range(len(VALUES)):
    img.putpixel(VALUES[i], (255,255,255))


img.show()
#fileN = 'rotatetriangle'+ str(ang) + '.png'
#img.save(fileN)