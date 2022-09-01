from cmath import sqrt
import math
import rotatingPoints
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUE = [0]*(ARRAYLENG)

def splice(array):
    for i in range(0, len(VALUE)):
        if(VALUE[i] == 0 and not array[i] == 0):
            VALUE[i] = array[i]

#for later
def shift(centerPointX, centerPointY, array):
    changedIndices = []
    for index in range(0, len(array), 1):
        if(not array[index] == 0 and not index in changedIndices):
            indexNew = round(index-399*WIDTH+centerPointX*WIDTH-399+centerPointY)
            array[int(indexNew)] = array[index]
            array[index] = 0
            changedIndices.append(indexNew)
    return array

#triangle(399, 399, 200, 45)

# creates a triangle with given dimentions
initialSideLength = 200
initialApothem = initialSideLength/(2*math.sqrt(3))
initialHeight = initialSideLength*math.sqrt(3)/2
initialRadius = math.sqrt(pow(initialSideLength/2, 2)+pow(initialSideLength/4*math.sqrt(3),2))
temp = []

#comment the line bellow to see smaller triangle
temp = rotatingPoints.triangle(0, initialRadius, initialSideLength)

#dimentions for second triangle
secondSideLength = initialSideLength/2
secondApothem = secondSideLength/(2*math.sqrt(3))
secondRadius = math.sqrt(pow(secondSideLength/2, 2)+pow(secondSideLength/4*math.sqrt(3),2))

temp = []
print(temp)
#print(temp, VALUE)
counter = 0



temp = rotatingPoints.triangle(180, secondRadius, secondSideLength)
for i in range(0, len(temp)-1,1):
    if(not temp[i] == 0):
        #print(i)
        counter += 1
print(counter)

#shifts the temp triangle
#temp = shift(399, 399+initialApothem+secondApothem, temp)

for i in range(0, len(temp),1):
    VALUE[i] = temp[i]

#splice(temp)
#for i in range(0, len(temp)):



#places the VALUE array on the image
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        img.putpixel([x,y], (abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y])),abs(int(VALUE[x*WIDTH+y]))*255))

#shows the image
img.show()

#if wanted saves the image
#fileN = 'rotatetriangle'+ str(ang) + '.png'
#img.save(fileN)