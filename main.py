from PIL import Image
import math 

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)


def checkPixel(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    # Euclidian Distance in RGB Color
    if (r, g, b) not in [red, green, black, white]:
        rMinus255, rMinus0 = math.pow((r - 255), 2), math.pow((r - 0), 2) 
        gMinus255, gMinus0 = math.pow((g - 255), 2), math.pow((g - 0), 2) 
        bMinus255, bMinus0 = math.pow((b - 255), 2), math.pow((b - 0), 2) 

        dRed = rMinus255 + gMinus0 + bMinus0
        dGreen = rMinus0 + gMinus255 + bMinus0
        dBlack = rMinus0 + gMinus0 + bMinus0
        dWhite = rMinus255 + gMinus255 + bMinus255

        minVal = min(dRed, dGreen, dBlack, dWhite)

        if minVal == dRed: 
            return red
        elif minVal == dGreen: 
            return green
        elif minVal == dBlack: 
            return black
        elif minVal == dWhite: 
            return white

    else:
        return pixel


lab = Image.open("turing.png")
width = lab.size[0]
height = lab.size[1]
new_size = math.floor(width/4)

grid = [[checkPixel(lab.getpixel(((i/new_size) * width, (j/new_size) * height))) 
          for j in range(new_size)] for i in range(new_size)]

img = Image.new(mode="RGB", size=(new_size, new_size))
[img.putpixel((i, j), grid[i][j]) for i in range(new_size) for j in range(new_size)]
img.save("discretized_img.png")
