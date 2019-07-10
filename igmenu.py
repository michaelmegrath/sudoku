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
        self.leftMenu = []
        self.rightMenu = []
        self.setNumberArray(screen)
        self.setMenuIcon(screen)


    def setNumberArray(self,screen):
        height = int(10.75 * const.CELLSIZE) + self.heightBuffer*2
        width = int(.25 * const.CELLSIZE) + self.widthBuffer
        self.numberArray.append(button.IconButton(1,screen,(width,height)))
        width += int(const.CELLSIZE * 1.5)
        for i in range(1,10,1):
            self.numberArray.append(button.IconButton(i+1,screen,(width,height)))
            width += int(const.CELLSIZE * 1.5)

        return None
    def setTimer(self):
        pass

    def setBackIcon(self,screen):
        height = int(const.NOTESIZE)
        width = int(const.NOTESIZE)
        self.menuIcon = button.IconButton(11,screen,(width,height))
        return None

    def setMenuIcon(self,screen):#Split function into close menu, and setMenuIcon

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
        elif(31+self.widthBuffer/2<=mpos[0]<31+self.widthBuffer/2+const.CELLSIZE*2):
            return self.findMenuItem(mpos,"left")
        elif(12*const.CELLSIZE + self.widthBuffer*1.5+31<=mpos[0]<14*const.CELLSIZE + self.widthBuffer*1.5 + 31):
            return self.findMenuItem(mpos,"right")
        else:
            pass
        return -1

    def findMenuItem(self,mpos,side):
        if(side == "left"):
            height = (2*const.CELLSIZE+self.heightBuffer)
            for i in range(0,3,1):
                if(height<mpos[1]<=height+2*const.CELLSIZE):
                    return i+12
                height += 3*const.CELLSIZE
        elif(side == "right"):
            height = (1.5*const.CELLSIZE+self.heightBuffer)
            if(height<mpos[1]<=height+2*const.CELLSIZE):
                return 15
            height += 2.5*const.CELLSIZE
            for i in range(0,3,1):
                if(height<mpos[1]<=height+2*const.CELLSIZE):
                    return i+16
                height += 2*const.CELLSIZE

        return -1



    def toggleMenu(self,screen):
        self.menuOpen = not self.menuOpen
        if(self.menuOpen):
            self.drawMenu(screen)
            self.setBackIcon(screen)

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
            self.fillMenu(screen)


    def isMenuOpen(self):
        return self.menuOpen


    def fillMenu(self,screen):
        x = 31+self.widthBuffer/2
        y = 2*const.CELLSIZE
        for i in range(0,3,1):
            self.leftMenu.append(button.MenuButton(i+12,screen,(x,y)))
            y += 3*const.CELLSIZE
        x = 31+self.widthBuffer * 1.5 + const.CELLSIZE*12
        y = int(1.5*const.CELLSIZE)
        self.rightMenu.append(button.MenuButton(15,screen,(x,y)))
        y += int(2.5*const.CELLSIZE)
        for i in range(0,3,1):
            self.rightMenu.append(button.MenuButton(i+16,screen,(x,y)))
            y+=2*const.CELLSIZE
