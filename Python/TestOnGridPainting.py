from PIL import Image



WIDTH = 800
img = Image.new(mode="RGB", size=(WIDTH, WIDTH))
for x in range(0, WIDTH-1, 1):
    for y in range(0, WIDTH, 1):
        if(x == WIDTH-1-y):
            img.putpixel([x,WIDTH-1-y], (0,255,255))
        elif(((x/30)%2 == 0 or (y/30)%2 == 0) and (x > 30 or y > 30)):
            img.putpixel([x,WIDTH-1-y], (255,255,255))
            
        else:
            img.putpixel([x,WIDTH-1-y], (0,0,0))

img.show()