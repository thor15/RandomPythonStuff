from math import *
from random import randint
from PIL import Image
WIDTH = 800

color = {1 : (255, 0,0), 2 : (0,255,0), 3: (0,0,255), 4: (255,255,255)}
goldenRatio = (1 + sqrt(5))/2
randomX = randint(0,WIDTH-1)
randomY = randint(0,WIDTH-1)

points = [(400, 100, 1), (100, 700, 2), (700, 700, 3), (400,400,4)]
pointsLen = len(points)
currentPoint = (randomX, randomY)
randomVertex = randint(0,pointsLen-1)
previousVertex = randomVertex
for i in range(100000):
    #randomVertex = randint(0,pointsLen-1)
    # normal
    midX = int((points[randomVertex][0] + currentPoint[0])/2)
    midY = int((points[randomVertex][1] + currentPoint[1])/2)

    #goldenRatio
    # midX = int(currentPoint[0]-(currentPoint[0]-points[randomVertex][0])/goldenRatio)
    # midY = int(currentPoint[1]-(currentPoint[1]-points[randomVertex][1])/goldenRatio)
    
    currentPoint = (midX, midY)
    points.append((midX, midY, points[previousVertex][2]))

    #can't be same
    while randomVertex == previousVertex:
        randomVertex = randint(0,pointsLen-1)
    previousVertex = randomVertex

    

    


img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for i in range(len(points)):
    img.putpixel((points[i][0], points[i][1]), color[points[i][2]])
img.show()
fileName = "ChaosGameMidPointIncludedCantBeSameRandomBeforeColorSelection.png"
# img.save(fileName)