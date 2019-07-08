import const
import button

class TopMenu:
    def __init__(self):
        self.widthBuffer = 0;
        self.heightBuffer = 0;
        self.buttonArray = []
    def resizeMenu(self,width,height):
        self.widthBuffer = width
        self.heightBuffer = height
        return None
    def setMenu(self,screen):
        width = int(7.5*const.NOTESIZE) + self.widthBuffer
        height = 4*const.NOTESIZE + self.heightBuffer
        for i in range(0,6,1):
            self.buttonArray.append(button.TopMenuButton(20+i,screen,(width,height+const.NOTESIZE*i*2)))
        return None

    def findButton(self,mpos):
        pass
