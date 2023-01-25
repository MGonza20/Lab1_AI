from PIL import Image
import math 

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

class imgProcessing:
    def __init__(self, img_path):
        self.image = Image.open(img_path)
        self.width, self.height = self.image.size
        self.new_size = math.floor(self.width/4)
        self.grid = []


    def checkPixel(self, pixel):
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

    def discretizeImg(self):
        self.grid = [[ self.checkPixel(self.image.getpixel(((i/self.new_size) * self.width, (j/self.new_size) * self.height))) 
                  for j in range(self.new_size)] for i in range(self.new_size)]

    def saveImg(self):
        img = Image.new(mode="RGB", size=(self.new_size, self.new_size))
        [img.putpixel((i, j), self.grid[i][j]) for i in range(self.new_size) for j in range(self.new_size)]
        img.save("discretized_img.png")

img = imgProcessing("turing.png")
img.discretizeImg()
img.saveImg()


