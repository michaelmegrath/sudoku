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
        else:
            address = "img/Buttons/Menu"
        return pygame.image.load(address).convert_alpha()


class MenuButton(Button):
    pass
