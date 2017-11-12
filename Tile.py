
class Tile(object):
    def __init__ (self, x_, y_):
        self.x = x_
        self.y = y_

        self.value = -1
        self.imageKey = "blank"
        
    def activate(self, value):
        self.value = value
        self.updateImages()

    def updateImages(self):
        if self.value in range(0,9):
            self.imageKey = 'number-' + str(self.value)
        elif self.value == 9:
            self.imageKey = 'mine-0'
        elif self.value == -2:
            self.imageKey = 'flag'
        elif self.value == -3:
            self.imageKey = 'unknown'
        elif self.value == -1:
            self.imageKey = 'blank'

    def rotateMarking(self):
        print("AH")
        self.value -= 1
        if self.value == -4:
            self.value = -1
        self.updateImages()

    def draw(self, x0, y0, images, scale):
        images[self.imageKey].blit(x0 + self.x*16*scale, y0 + 16*scale*self.y)



