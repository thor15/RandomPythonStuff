from cmath import sqrt
import math
import rotatingPoints
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUE = []

def splice(array):
    for i in range(0, len(VALUE)):
        VALUE.append(array[i])

#for later
def shift(centerPointX, centerPointY, array):
    changedIndices = []
    for index in range(len(array)-1, -1, -1):
        if(not array[index] == 0 and not index in changedIndices):
            indexNew = round(index-399*WIDTH+centerPointX*WIDTH-399+centerPointY)
            array[int(indexNew)] = array[index]
            array[index] = 0
            changedIndices.append(indexNew)
    return array

# creates a triangle with given dimentions
initialSideLength = 200
initialApothem = initialSideLength/(2*math.sqrt(3))
initialHeight = initialSideLength*math.sqrt(3)/2
twoThridOfHeight = 2/3*initialHeight
initialRadius = math.sqrt(twoThridOfHeight**2)
temp = []

#comment the line bellow to see smaller triangle
temp = rotatingPoints.triangle(0, initialRadius, initialSideLength, 255)

#set VALUE to temp

for i in range(0, len(temp),1):
    VALUE.append(temp[i])

#dimentions for second triangle
secondSideLength = initialSideLength/2
secondApothem = secondSideLength/(2*math.sqrt(3))
secondRadius = math.sqrt(pow(secondSideLength/2, 2)+pow(secondSideLength/(4*math.sqrt(3)),2))

temp = []
#print(temp, VALUE)
counter = 0

angle = [30,180,330]
# for i in range(0, len(angle), 1):

#     temp = rotatingPoints.triangle(angle[i], secondRadius, secondSideLength, 127)

#     #shifts the temp triangle
#     temp = shift(399+(initialApothem+secondApothem)*math.sin(angle[i]*math.pi/180), 399-(initialApothem+secondApothem)*math.cos(angle[i]*math.pi/180), temp)
#     #adds to shape
#     splice(temp)

#places the VALUE array on the image
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for i in range(0, len(VALUE), 1):
    x = VALUE[i]//1000
    y = VALUE[i]%1000
    img.putpixel([x,y], (abs(int(40)),abs(int(40)),abs(int(220))))

#shows the image
img.show()

#if wanted saves the image
#fileN = 'rotatetriangle'+ str(ang) + '.png'
#img.save(fileN)