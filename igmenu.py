import const
import button


class igMenu: #In Game Menu
    def __init__(self,screen):
        self.numberArray = []
        self.heightBuffer = 0
        self.widthBuffer = 0
        self.setNumberArray(screen)


    def setNumberArray(self,screen):
        height = int(10.75 * const.CELLSIZE) + self.heightBuffer
        width = int(.25 * const.CELLSIZE) + self.widthBuffer/2
        self.numberArray.append(button.IconButton(1,screen,(width,height)))
        width += int(const.CELLSIZE * 1.5)
        for i in range(1,10,1):
            self.numberArray.append(button.IconButton(i+1,screen,(width,height)))
            width += int(const.CELLSIZE * 1.5)

        pass
    def setTimer(self):
        pass

    def resizeMenu(self,width,height):
        self.widthBuffer = width
        self.heightBuffer = height
        return None

    def findButton(self,mpos):
        pass
