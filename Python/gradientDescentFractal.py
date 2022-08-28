import numpy as np
from PIL import Image

X = []
Y = []
THETA = [0, 0, 0]
LEARNINGRATE = .003
MAXSTEPS = 40

def gradientDescent(learningRate):
    step = 0
    cost1 = -1
    cost2 = -1
    cost3 = -1
    while(step < MAXSTEPS and (cost1 != 0 or cost2 != 0 or cost3 != 0)):
        cost1 = costFunctionDeriv(THETA, 0)
        cost2 = costFunctionDeriv(THETA, 0)
        cost3 = costFunctionDeriv(THETA, 0)
        change1 = THETA[0] - learningRate * cost1
        change2 = THETA[0] - learningRate * cost2
        change3 = THETA[0] - learningRate * cost3
        THETA[0] = change1
        THETA[1] = change2
        THETA[2] = change3
        step+=1
    return step

def costFunctionDeriv(theta, thetaNum):
    steps = 0
    sum = 0
    while(steps < len(Y)-3):
        steps += 1
        try:
            sum += (hOfTheta(theta, steps))*X[3*steps+thetaNum]
        except(RuntimeWarning):
            print(sum, (hOfTheta(theta, steps))*X[3*steps+thetaNum])

    return sum

def hOfTheta(theta, position):
    return ((theta[0]*X[3*position] + theta[1] * X[3*position+1] + theta[2]*X[3*position+2]) - Y[position])


file1 = open("chemdata.csv", "r")
allData = file1.read()
file1.close()
img = Image.new(mode="RGB", size=(100, 100))

dataLines = allData.split("\n")
for line in dataLines:
    segments = line.split(",")
    temp = np.array([1, int(segments[0]), int(segments[1])])
    X = np.concatenate((X, temp), axis=0)
    Y.append(int(segments[2]))

for a in range(1, 100, 1):
    b = gradientDescent(a/100)
    for i in range(0, b, 1):
        img.putpixel([a,i], (256,0,0))

img.show()
