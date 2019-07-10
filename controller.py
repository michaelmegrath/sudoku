import pygame
import Sudoku
import const
import topMenu

class Controller:
    def __init__(self,screen):
        self.screen = screen
        self.widthBuffer = int(6 * const.NOTESIZE)
        self.heightBuffer = int(2 * const.NOTESIZE)
        pygame.display.set_caption('Sudoku')
        icon = pygame.image.load("img/largeIcon.png") #If statement for OS, determine best size for each OS
        pygame.display.set_icon(icon)
        self.mainMenu = topMenu.TopMenu()
        self.mainMenu.setMenu(screen)
        pygame.display.update()

    def drawWindow(self):
        self.mainMenu.drawMenu(self.screen)
        pygame.display.update()

    def resizeWindow(self,size):
        width = size[0]
        height = size[1]
        if(width < const.WINDOWWIDTH):
            width = const.WINDOWWIDTH
        if(height < const.WINDOWHEIGHT):
            height = const.WINDOWHEIGHT
        surface = pygame.display.set_mode((int(width), int(height)),pygame.RESIZABLE)
        self.widthBuffer = width - const.WINDOWWIDTH
        self.heightBuffer = height - const.WINDOWHEIGHT
        self.mainMenu.resizeMenu(self.widthBuffer,self.heightBuffer)
        self.drawWindow()


    def mouseClick(self,mpos):
        catch = self.mainMenu.findButton(mpos)
        if(catch == 20):
            catch = Sudoku.Sudoku(self.screen)
            if(catch == 13):
                self.drawWindow()
            elif(catch == 25):
                return catch
            else:
                pass
        elif(catch == 21):
            print(catch)
            return None
        elif(catch == 22):
            print(catch)
            return None
        elif(catch == 23):
            print(catch)
            return None
        elif(catch == 24):
            print(catch)
            return None
        else:
            return catch
