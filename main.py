from PIL import Image
import numpy as np
import math 


def checkPixel(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]

    # Euclidian Distance in RGB Color
    if (pixel != (255, 0, 0) and pixel != (0, 255, 0) and pixel != (0, 0, 0) and pixel != (255, 255, 255)):
        dRed =  math.pow((r - 255), 2) + math.pow((g - 0), 2) + math.pow((b - 0), 2)
        dGreen = math.pow((r - 0), 2) + math.pow((g - 255), 2) + math.pow((b - 0), 2)
        dBlack = math.pow((r - 0), 2) + math.pow((g - 0), 2) + math.pow((b - 0), 2)
        dWhite = math.pow((r - 255), 2) + math.pow((g - 255), 2) + math.pow((b - 255), 2)
        minVal = min(dRed, dGreen, dBlack, dWhite)

        if minVal == dRed: return (255, 0, 0)
        elif minVal == dGreen: return (0, 255, 0)
        elif minVal == dBlack: return (0, 0, 0)
        elif minVal == dWhite: return (255, 255, 255)

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
