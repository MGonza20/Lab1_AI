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
        self.goal_tests = []
        self.start = []


    def checkPixel(self, pixel):
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

        # Euclidian Distance in RGB Color
        if (r, g, b) not in [red, green, black, white]:
            rM255, rM0 = math.pow((r - 255), 2), math.pow(r, 2) 
            gM255, gM0 = math.pow((g - 255), 2), math.pow(g, 2) 
            bM255, bM0 = math.pow((b - 255), 2), math.pow(b, 2) 

            dRed   = rM255 + gM0   + bM0
            dGreen = rM0   + gM255 + bM0
            dBlack = rM0   + gM0   + bM0
            dWhite = rM255 + gM255 + bM255

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
        for i in range(self.new_size):
            row = []
            coordX = (i/self.new_size) * self.width
            for j in range(self.new_size):
                coordY = (j/self.new_size) * self.height
                pixel = self.checkPixel(self.image.getpixel((coordX, coordY)))
                # Adding start
                if ((pixel == red) and (len(self.start) == 0)):  
                    self.start.append(coordX, coordY)
                # Adding goal states
                if (pixel == green):  
                    self.goal_tests.append(coordX, coordY)
                row.append(pixel)
            self.grid.append(row)

    def saveImg(self):
        img = Image.new(mode="RGB", size=(self.new_size, self.new_size))
        [img.putpixel((i, j), self.grid[i][j]) for i in range(self.new_size) for j in range(self.new_size)]
        img.save("discretized_img.png")

img = imgProcessing("turing.png")
img.discretizeImg()
img.saveImg()


