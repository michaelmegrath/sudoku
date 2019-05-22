import const
import button
import pygame


class igMenu: #In Game Menu
    def __init__(self,screen):
        self.menuOpen = False
        self.menuIcon = None
        self.numberArray = []
        self.heightBuffer = 0
        self.widthBuffer = 0
        self.setNumberArray(screen)
        self.setMenuIcon(screen)


    def setNumberArray(self,screen):
        height = int(10.75 * const.CELLSIZE) + self.heightBuffer
        width = int(.25 * const.CELLSIZE) + self.widthBuffer
        self.numberArray.append(button.IconButton(1,screen,(width,height)))
        width += int(const.CELLSIZE * 1.5)
        for i in range(1,10,1):
            self.numberArray.append(button.IconButton(i+1,screen,(width,height)))
            width += int(const.CELLSIZE * 1.5)

        return None
    def setTimer(self):
        pass

    def setMenuIcon(self,screen):
        if(self.menuOpen):
            return False
        else:
            width = int(3*const.CELLSIZE) + self.widthBuffer
            height = int(10.5*const.CELLSIZE) + 1 + self.heightBuffer
            pygame.draw.rect(screen,const.WHITE,(0,0,width,height))
            pygame.draw.rect(screen,const.WHITE,(12*const.CELLSIZE+self.widthBuffer+1,0,width,height))

            height = int(const.NOTESIZE)
            width = int(const.NOTESIZE)
            self.menuIcon = button.IconButton(0,screen,(width,height))
            return True



    def resizeMenu(self,width,height):
        self.widthBuffer = width
        self.heightBuffer = height
        return None



    def findButton(self,mpos):
        if(677+self.heightBuffer <= mpos[1] < 740 + self.heightBuffer):
            for i in range(0,10,1):
                temp = (i*94)+15+self.widthBuffer
                if(temp <= mpos[0] < temp+63):
                    return self.numberArray[i].onClick()
        elif(21 <= mpos[1] < 85):
            if(21 <= mpos[0] < 85):
                return self.menuIcon.onClick()
        else:
            pass
        return -1

    def toggleMenu(self,screen):
        self.menuOpen = not self.menuOpen
        if(self.menuOpen):
            self.drawMenu(screen)
        else:
            self.setMenuIcon(screen)



    def drawMenu(self,screen):
        if(self.menuOpen == False):
            return False
        else:
            width = int(3*const.CELLSIZE) + self.widthBuffer
            height = int(10.5*const.CELLSIZE) + 1 + self.heightBuffer
            pygame.draw.rect(screen,const.LIGHTGREY,(0,0,width,height))
            pygame.draw.rect(screen,const.LIGHTGREY,(12*const.CELLSIZE+self.widthBuffer+1,0,width,height))
