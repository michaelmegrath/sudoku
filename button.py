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
        else:
            return None
        return pygame.image.load(address).convert_alpha()


class MenuButton(Button):
    def loadImage(self,id):
        if(id == 11):
            address = "img/Buttons/igNewgame.png"
        elif(id == 12):
            address = "img/Buttons/igHint.png"
        elif(id == 13):
            address = "img/Buttons/igQuit.png"
        else:
            return None
        return pygame.image.load(address).convert_alpha()
