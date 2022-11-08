import math
import rotatingPoints
from PIL import Image
WIDTH = 800
ARRAYLENG= WIDTH*WIDTH
VALUE = []

def splice(array):
    for i in range(0, len(array)):
        VALUE.append(array[i])

# takes an array that has 
def shift(centerPointX, centerPointY, array):
    changedIndices = []
    for index in range(len(array)-1, -1, -1):
        array[index] = (math.floor(array[index][0] + centerPointX), round(array[index][1] + centerPointY))
    return array

# creates a triangle with given dimentions
initialSideLength = 400
initialApothem = initialSideLength/(2*math.sqrt(3))
initialHeight = initialSideLength*math.sqrt(3)/2
twoThridOfHeight = 2/3*initialHeight
initialRadius = math.sqrt(twoThridOfHeight**2)

temp = rotatingPoints.triangle(0, initialRadius, initialSideLength)

#set VALUE to temp for the center triangle
for i in range(0, len(temp),1):
    VALUE.append(temp[i])
blue = len(VALUE)
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))


#dimentions for second triangle
secondSideLength = initialSideLength/2
secondApothem = secondSideLength/(2*math.sqrt(3))
secondHeight = secondSideLength*math.sqrt(3)/2
twoThridOfHeight = 2/3*secondHeight
secondRadius = math.sqrt(twoThridOfHeight**2)

temp = []
counter = 0
firstCenter = initialApothem+secondApothem
angle = [60, 300, 180]
# creates, shifts, and splices the triangles that have half of the side length
for i in range(0, len(angle), 1):

    temp = rotatingPoints.triangle(angle[i], secondRadius, secondSideLength)

    #shifts the temp triangle
    temp = shift((firstCenter)*math.sin(angle[i]*math.pi/180), -1*(firstCenter)*math.cos(angle[i]*math.pi/180), temp)
    #adds to shape
    splice(temp)
red = len(VALUE)

# set up for third round of triangles
angle2 = []
angle2.append(0)
angle2.append(0)
thirdSideLength = secondSideLength/2
thirdApothem = thirdSideLength/(2*math.sqrt(3))
thridHeight = thirdSideLength*math.sqrt(3)/2
twoThridOfHeight = 2/3*thridHeight
thirdRadius = math.sqrt(twoThridOfHeight**2)

# creates the triangles with 1/4 the side length of the original triangle then shift them and splice them witht the image
for i in range(0, 3, 1):
    angle2[0] = angle[i] + 60
    angle2[1] = angle[i] - 60
    for t in range(0, len(angle2), 1):
        temp = rotatingPoints.triangle(angle2[t], thirdRadius, thirdSideLength)
        firstSin = math.sin(angle[i]*math.pi/180)
        firstCos = math.cos(angle[i]*math.pi/180)
        #shifts the temp triangle
        temp = shift(firstCenter*firstSin+(secondApothem+thirdApothem)*math.sin(angle2[t]*math.pi/180), -1*(firstCenter*firstCos+(secondApothem+thirdApothem)*math.cos(angle2[t]*math.pi/180)), temp)
        #adds to shape
        splice(temp)

#places the VALUE array on the image
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for i in range(0, len(VALUE), 1):
    #print(VALUE[i])
    if(i < blue):
        img.putpixel(VALUE[i], (abs(int(40)),abs(int(40)),abs(int(220))))
    elif(i < red):
        img.putpixel(VALUE[i], (abs(int(220)),abs(int(40)),abs(int(40))))
    else:
        img.putpixel(VALUE[i], (abs(int(40)),abs(int(220)),abs(int(40))))



#shows the image
img.show()

# for i in range(0, len(VALUE), 1):
#     img.putpixel(VALUE[i], (abs(int(40)),abs(int(40)),abs(int(220))))

# img.show()

# to create a bunch of images 1 degree appart
# for ang in range(0, 360, 1):
#     temp = []
#     VALUE=[]

#     #comment the line bellow to see smaller triangle
#     temp = rotatingPoints.triangle(ang, initialRadius, initialSideLength)

#     #set VALUE to temp
#     for i in range(0, len(temp),1):
#         VALUE.append(temp[i])

#     img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
#     for i in range(0, len(VALUE), 1):
#         img.putpixel(VALUE[i], (abs(int(40)),abs(int(40)),abs(int(220))))

#if wanted saves the image
fileN = 'triangle_fractle' + '.png'
img.save(fileN)