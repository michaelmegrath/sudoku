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
        width = int(6*const.CELLSIZE) + self.widthBuffer / 2
        height = int(5*const.CELLSIZE) + self.heightBuffer / 2
        for i in range(0,6,1):
            self.buttonArray.append(button.TopMenuButton(20+i,screen,(width,height+const.NOTESIZE*i*3)))
        self.drawMenu(screen)
        return None

    def drawMenu(self,screen):
        screen.fill(const.WHITE)
        width = int(6*const.CELLSIZE) + self.widthBuffer / 2
        height = int(5*const.CELLSIZE) + self.heightBuffer / 2
        for i in range(0,6,1):
            self.buttonArray[i].displayButton(screen,(width,height+const.NOTESIZE*i*3))

    def findButton(self,mpos):
        if(mpos[0]>=const.CELLSIZE*6 + (self.widthBuffer/2)and mpos[0]<=const.CELLSIZE*9 + (self.heightBuffer/2)): #ADD BUFFERS!!!!!!!!
            for i in range(0,6,1):
                if(mpos[1] > int((5*const.CELLSIZE)+(i*63)) and mpos[1] <= int((5*const.CELLSIZE)+(i+1)*63)):
                    return self.buttonArray[i].onClick()
        return None
