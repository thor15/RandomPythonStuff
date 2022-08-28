from gettext import lngettext
import math
import matplotlib.pyplot as plt


plt.close()
MAX_ITER = 40
VALUEX = []
VALUEY = []
VALUEZ = []
#please format with sapce between the different xs and the sign attached to the  
INPUT = "87x^8 -30x^6 +x^4 -x^3 +8x^2 -3x +0x"
xMULTIPLESF = []
xMULTIPLESD = []
powers = []
roots =[]
ROOTNUM = 0

TEMPPOLY = INPUT.split(' ')
for i in range(0, len(TEMPPOLY),1):
    ROW = TEMPPOLY[i].split('x')
    if(ROW[0] == "-" or ROW[0] == "+" or ROW[0] == ""):
        ROW[0] = ROW[0] + "1"
    if(ROW[1] == ""):
        ROW[1] = ROW[1] + "1"
    xMULTIPLESF.append(int(ROW[0]))
    power = int(ROW[1].replace("^",""))
    powers.append(power)
    
for a in range(0, len(powers)-1, 1):
    if(powers[a] - 1 > powers[a+1]):
        xMULTIPLESF.insert(a+1, 0)
        powers.insert(a+1, powers[a]-1)

for a in range(0, len(xMULTIPLESF)-1, 1):
    xMULTIPLESD.append(xMULTIPLESF[a]*(len(xMULTIPLESF)-1-a))



ROOTNUM = len(xMULTIPLESF)-1

aFactors = []
cFactors = []

for i in range(1, xMULTIPLESF[0], 1):
    if(xMULTIPLESF[0] % i == 0 and not(i in aFactors)):
        aFactors.append(i)
        aFactors.append(xMULTIPLESF[0]/i)
    else:
        break

for i in range(1, xMULTIPLESF[len(xMULTIPLESF)-1], 1):
    if(xMULTIPLESF[len(xMULTIPLESF)-1] % i == 0 and not(i in cFactors)):
        cFactors.append(i)
        cFactors.append(xMULTIPLESF[len(xMULTIPLESF)-1]/i)
    else:
        break


#print(aFactors)
#print(cFactors)
factoredEquation = xMULTIPLESF
tempEquation = []

seeOuts = []

for p in aFactors:
    for q in cFactors:
        for posNeg in range(-1, 1, 2):
            x = posNeg * float(q/p)
            tempEquation.append(factoredEquation[0])
            for i in range(1, len(factoredEquation), 1):
                tempEquation.append(tempEquation[i-1]*x + factoredEquation[i])
            if(tempEquation[len(tempEquation)-1] == 0):
                tempEquation.pop(len(tempEquation) - 1)
                powers.pop(0)
                factoredEquation = tempEquation
                i -= 2
                roots.append(x)
            seeOuts.append(tempEquation.pop(len(tempEquation) - 1))
            tempEquation = []



#print(seeOuts)
temporaryRoots = []
num = []
newtonOUT = []



#f(x) = x^{5}-3x^{4}+x^{3}\ -\ 3x^{2}-x+2
#(z*z*z*z*z - 3*z*z*z*z + z*z*z - 3*z*z - z + 2)/(5*z*z*z*z - 12*z*z*z + 3*z*z - 6*z - 1)
#f'(x) = 5x^4 - 12x^3 + 3x^2 - 6x - 1
def newton(z, step):
    steps = step
    if(steps < MAX_ITER):
        d = z - ((f(z))/(derivF(z)))
        #print(steps, d)
        steps += 1
        return newton(d, steps)
    else:
        return z

def f(z):
    result = xMULTIPLESF[0]
    for i in range(1, len(xMULTIPLESF), 1):
        result = result*z + xMULTIPLESF[i]
    return result

def derivF(z):
    result = xMULTIPLESD[0]
    for i in range(1, len(xMULTIPLESD), 1):
        result = result*z + xMULTIPLESD[i]
    return result

def nearestRoot(position, cROOTS):
    min = pow(2, 32)
    ind = -1
    for i in range(0, len(cROOTS), 1):
        if(math.sqrt(pow(position.real - cROOTS[i].real,2)+pow(position.imag - cROOTS[i].imag, 2)).real < min):
            min = math.sqrt(pow(position.real - cROOTS[i].real,2)+pow(position.imag - cROOTS[i].imag, 2)).real
            ind = i
    return ind

#might need to do this with a secodn for loop
#if(NEWTONOUT[i].real*1000000 in range(TEMPORARYROOTS[i].real*1000000-1,TEMPORARYROOTS[i].real*1000000 +1) 
#           and NEWTONOUT[i].imag*1000000 in range(TEMPORARYROOTS[i].imag*1000000-1,TEMPORARYROOTS[i].imag*1000000 +1)):
#            NUM[TEMPORARYROOTS.index(NEWTONOUT[i])] += 1   

def findRoots(fEquation):
    #print(len(NEWTONOUT))
    currentRoots = roots
    for i in range(0, len(newtonOUT), 1):
        if(newtonOUT[i] in temporaryRoots):
            num[temporaryRoots.index(newtonOUT[i])] += 1   
        else:
            temporaryRoots.append(newtonOUT[i])
            num.append(1)
    currentEquation = fEquation
    tEquation = []
    while(len(powers) > 5):
        for i in range(0, len(temporaryRoots), 1):
            x = temporaryRoots[i]
            tEquation.append(currentEquation[0])
            for a in range(1, len(currentEquation), 1):
                tEquation.append(tEquation[a-1]*x + currentEquation[a])
            if(tEquation[len(tEquation)-1] == 0):
                tEquation.pop(len(tEquation)-1)
                currentEquation = tEquation
                tEquation = []
                powers.pop(0)
                currentRoots.append(x)
    
    # ax4+bx3+cx2+dx+e=0
    if(len(powers) == 5):
        funca = currentEquation[0]
        funcb = currentEquation[1]
        funcc = currentEquation[2]
        funcd = currentEquation[3]
        funce = currentEquation[4]
        p1 = 2*funcc - 9*funcb*funcc*funcd + 27*funca*pow(funcd,2) + 27*pow(funcb,2)*funce - 72*funca*funcc*funce
        p2 = p1 + math.sqrt((-4*pow((pow(funcc,2)-3*funcb*funcd+12*funca*funce),3))+pow(p1,2))
        p3 = ((pow(funcc, 2)-3*funcb*funcd+12*funca*funce)/(3*funca*pow(p2/2,1./3.)))+((pow(p2/2,1./3.))/(3*funca))
        p4 = pow((pow(funcb, 2)/(4*pow(funca,2))-(2*funcc)/(3*funca)),1./2.)
        p5 = (pow(funcb, 2))/(2*pow(funca,2)) - ((4*funcc)/(3*funca)) - p3
        p6 = ((-1*pow(funcb,3)/pow(funca,3))+((4*funcb*funcc)/pow(funca,2))-((8*d)/a))/(4*p4)
        x1 = -1*(funcb/(4*funca)) - (p4/2) - (math.sqrt(p5-p6)/2)
        x2 = -1*(funcb/(4*funca)) - (p4/2) + (math.sqrt(p5-p6)/2)
        x3 = -1*(funcb/(4*funca)) + (p4/2) - (math.sqrt(p5-p6)/2)
        x4 = -1*(funcb/(4*funca)) + (p4/2) + (math.sqrt(p5-p6)/2)
        currentRoots.append(x1)
        currentRoots.append(x2)
        currentRoots.append(x3)
        currentRoots.append(x4)
        #roots.append()
    # #print(TEMPORARYROOTS)
    # tempDict = dict(zip(temporaryRoots, num))
    # #print(tempDict)
    # sorted_values = sorted(tempDict.values(), reverse=True)
    # sorted_dict = {}
    # # Traverse through all array elements
    # for i in sorted_values:
    #     for k in tempDict.keys():
    #         if tempDict[k] == i:
    #             sorted_dict[k] = tempDict[k]
    #             break
    
    
    # sorted_keys = []
    # for i in sorted_dict.keys():
    #     sorted_keys.append(i)
    
    # for i in range(ROOTNUM, len(sorted_dict), 1):
    #     sorted_dict.pop(sorted_keys[i])
    #     #i -= 1
            
    # cROOTS = []
    # for i in sorted_dict.keys():
    #     cROOTS.append(i)
    # #print(cROOTS)
    # return cROOTS
    
fig, ax = plt.subplots()
for a in range(-200, 200, 1):
    for b in range(-200, 200, 1):
        c = complex(a/10, b/10)
        d = newton(c,0)
        newtonOUT.append(complex(round(d.real,8),round(d.imag,8)))
        
        
roots = findRoots(factoredEquation)
print(roots)
for a in range(0, 400, 1):
    for b in range(0, 400, 1):
        VALUEX.append(a-200)
        VALUEY.append(b-200)
        e = nearestRoot(newtonOUT[a*400+b], roots)
        VALUEZ.append(e)

#print(NEWTONOUT)
#print(VALUEZ)
ax.scatter(x=VALUEX, y=VALUEY, c=VALUEZ)
plt.show()