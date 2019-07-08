import const
import pygame


class Button:
    def __init__(self,id,screen,coord):
        self.tag = id
        self.image = self.loadImage(id)
        self.displayButton(screen,coord)

    def displayButton(self,screen,coord):
        screen.blit(self.image,coord)
        return None
    def onClick(self):
        return self.tag

class IconButton(Button):


    def loadImage(self,id):
        if(id == 10):
            address = "img/Buttons/Note.png"
        elif(0<id<10):
            address = "img/Buttons/Button" + str(id) + ".png"
        elif(id == 0):
            address = "img/Buttons/menuIcon.png"
        elif(id == 11):
            address = "img/Buttons/backIcon.png"
        else:
            return None
        return pygame.image.load(address).convert_alpha()


class MenuButton(Button):
    def loadImage(self,id):
        if(id == 12):
            address = "img/Buttons/igNewgame.png"
        elif(id == 13):
            address = "img/Buttons/igMenu.png"
        elif(id == 14):
            address = "img/Buttons/igLeave.png"
        elif(id == 15):
            address = "img/Buttons/igColorMode.png"
        elif(id == 16):
            address = "img/Buttons/igUndo.png"
        elif(id == 17):
            address = "img/Buttons/igMute.png"
        elif(id == 18):
            address = "img/Buttons/igHint.png"
        else:
            return None
        return pygame.image.load(address).convert_alpha()


class TopMenuButton(Button):
    def loadImage(self,id):
        if(id == 20):
            address = "img/Buttons/topNewgame.png"
        elif(id == 21):
            address = "img/Buttons/topLoadgame.png"
        elif(id == 22):
            address = "img/Buttons/topTutorial.png"
        elif(id == 23):
            address = "img/Buttons/topFreeplay.png"
        elif(id == 24):
            address = "img/Buttons/topSettings.png"
        elif(id == 25):
            address = "img/Buttons/topLeave.png"
        else:
            return None
        return pygame.image.load(address).convert_alpha()
