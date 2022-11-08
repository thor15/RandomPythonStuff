from math import *
from random import randint
from PIL import Image
WIDTH = 800
# some nice colors for the hexigon
# {1 : (162, 126, 255), 2 : (255,75,133), 3: (81,221,231), 4: (66,242,28), 5:(23, 76, 255),6:(214, 24, 78)}
color = {1 : (255, 0, 0), 2 : (255,255,0), 3: (0,255,0), 4: (0,255,255), 5:(0, 0, 255),6:(255, 0, 255)}
goldenRatio = (1 + sqrt(5))/2
randomX = randint(0,WIDTH-1)
randomY = randint(0,WIDTH-1)
pointsLen = 6
previousVertex = -1
points = [(400, 100, 1), (145, 205, 2), (145, 595, 3), (400,700,4), (655, 595, 5), (655,205,6)]
currentPoint = (randomX, randomY)
randomVertex = randint(0,pointsLen-1)
for i in range(1000000):
    randomVertex = randint(0,pointsLen-1)
    midX = int(currentPoint[0]-(currentPoint[0]-points[randomVertex][0])/2)
    midY = int(currentPoint[1]-(currentPoint[1]-points[randomVertex][1])/2)
    currentPoint = (midX, midY)
    points.append((midX, midY, points[randomVertex][2]))
    # can't be last vertex
    # while randomVertex == previousVertex:
    #     randomVertex = randint(0,pointsLen-1)
    # previousVertex = randomVertex

    # if it is the last 
    # while randomVertex == previousVertex:
    #     randomVertex = randint(0,pointsLen-1)
    # previousVertex = randomVertex

    # next vertex
    # randomVertex += 1
    # if(randomVertex == pointsLen):
    #     randomVertex = 0


img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for i in range(len(points)):
    img.putpixel((points[i][0], points[i][1]), color[points[i][2]])
img.show()
fileName = "ChaosGameHexHalfDistance.png"
img.save(fileName)