from PIL import Image
from  math import *

WIDTH = 800

def equation(x):
    return 2*sin(2/(2*pi)*x)


img = Image.new(mode="RGB", size=(WIDTH, WIDTH))


for x in range(0 , 799, 1):
    for y in range(0, 799, 1):
        if(y == 10*round(equation(x))+399):
            img.putpixel((x,y), (255, 0, 0))
img.show()