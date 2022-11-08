from random import randint
from PIL import Image
from math import *
WIDTH = 800
# colors of coners {1 : (162, 126, 255), 2 : (255,75,133), 3: (81,221,231), 4: (66,242,28)}
color = {1 : (162, 126, 255), 2 : (255,75,133), 3: (81,221,231), 4: (66,242,28), 5:(255,0,255), 6:(0,255,255), 7:(255,255,0),8:(255,255,255)}

goldenRatio = (1 + sqrt(5))/2
randomX = randint(0,WIDTH-1)
randomY = randint(0,WIDTH-1)

previousVertex = -1
points = [(100, 100, 5), (100, 700, 6), (700, 700, 7), (700,100,8),(100,400,1),(400,700,2),(700,400,3),(400, 100, 4)]
pointsLen = len(points)
currentPoint = (randomX, randomY)
randomVertex = randint(0,pointsLen-1)
previousVertex = randomVertex
for i in range(100000):
    midX = int(points[randomVertex][0]+(currentPoint[0] - points[randomVertex][0])/3)
    midY = int(points[randomVertex][1]+(currentPoint[1] - points[randomVertex][1])/3)
    currentPoint = (midX, midY)
    points.append((midX, midY, points[randomVertex][2]))
    randomVertex = randint(0,pointsLen-1)
    
    # previousVertex = randomVertex

    # previousVertex -= 1
    # if(previousVertex == -1):
    #     previousVertex = 3
    
    # while randomVertex == previousVertex:
    #     randomVertex = randint(0,pointsLen-1)

    # if(randomVertex == previousVertex):
    #     match randomVertex:
    #         case 0:
    #             randomVertex = 2
    #         case 1:
    #             randomVertex = 3
    #         case 2:
    #             randomVertex = 0
    #         case 3:
    #             randomVertex = 1
    # previousVertex = randomVertex


img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for i in range(len(points)):
    img.putpixel((points[i][0], points[i][1]), color[points[i][2]])
img.show()
fileName = "ChaosGameSquareGoldenRatioCantBeSame.png"
#img.save(fileName)