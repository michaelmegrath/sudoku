import pygame
import grid
import igmenu
import const


class GameController:
    def __init__(self,screen):
        self.screen = screen

        pygame.display.set_caption('Sudoku')
        icon = pygame.image.load("img/largeIcon.png") #If statement for OS, determine best size for each OS
        clock = pygame.time.Clock()
        clock.tick(15)
        pygame.display.set_icon(icon)

        pygame.display.update()
        self.playboard = grid.GridController(screen)
        self.playboard.render(screen)
        self.playboard.newGame(screen)
        self.outerMenu = igmenu.igMenu(screen)


        pygame.display.update()
        self.widthBuffer = int(const.CELLSIZE*3)
        self.heightBuffer = int(const.CELLSIZE*1.5)
        self.noteFlag = False
        self.actionLog = []


    def resizeWindow(self,size):
        width = size[0]
        height = size[1]
        if(width < const.WINDOWWIDTH):
            width = const.WINDOWWIDTH
        if(height < const.WINDOWHEIGHT):
            height = const.WINDOWHEIGHT
        surface = pygame.display.set_mode((int(width), int(height)),pygame.RESIZABLE)

        self.widthBuffer = (width / 2) - (4.5 * const.CELLSIZE)
        self.heightBuffer = (height / 2) - (4.5 * const.CELLSIZE)
        self.playboard.changeBuffer(width,height)
        self.playboard.render(self.screen)
        self.outerMenu.resizeMenu(self.widthBuffer-int(const.CELLSIZE*3),self.heightBuffer-int(const.CELLSIZE*1.5))
        self.outerMenu.setNumberArray(self.screen)
        self.outerMenu.setMenuIcon(self.screen)
        self.outerMenu.drawMenu(self.screen)
        pygame.display.update()


    def mouseClick(self,mpos):
        if(self.isInGrid(mpos)):
            self.playboard.selectCell(mpos,self.screen)
            self.playboard.writeNumber(self.screen,self.playboard.returnNumber(),const.BLUE)
            self.playboard.redrawNotes(self.screen)
        else:
            catch = self.igMenuClick(mpos)
            pygame.display.update()
            return catch


        pygame.display.update()
        return True

    def igMenuClick(self,mpos):
        catch = self.outerMenu.findButton(mpos)
        menu = self.outerMenu.isMenuOpen()
        if(catch == 0 or catch == 11):
            self.outerMenu.toggleMenu(self.screen)
        elif(0<catch<10):
            self.numberKey(catch,False)
        elif(catch == 10):
            if(self.noteFlag):
                self.noteFlag = False
                #Control animation
            else:
                self.noteFlag = True
                #control animation
        elif(catch == 12 and menu):
            self.playboard.newGame(self.screen)
        elif(catch == 13 and menu):
            return 13
        elif(catch == 14 and menu):
            return 25
        elif(catch == 15 and menu):
            print(15)
        elif(catch == 16 and menu):
            self.undo()
        elif(catch == 17 and menu):
            print(17)
        elif(catch == 18 and menu):
            self.playboard.getHint(self.screen)
        else:
            pass
        return 1

    def arrowKey(self,direction):
        if(self.playboard.isSelected()):
            self.playboard.moveSelected(direction,self.screen)
            self.playboard.writeNumber(self.screen,self.playboard.returnNumber())
            self.playboard.redrawNotes(self.screen)
            pygame.display.update()


    def numberKey(self,number,note):
        if(self.playboard.isSelected()):
            if(note != self.noteFlag):
                self.playboard.setNote(self.screen,number)
                pygame.display.update()
            elif(number == self.playboard.returnNumber()):
                self.backspaceKey()
            else:
                catch = self.playboard.returnNumber()
                if(self.playboard.saveNumber(number)):
                    self.actionLog.insert(0,[number,catch,self.playboard.returnSelected(0),self.playboard.returnSelected(1)])
                    self.playboard.writeNumber(self.screen,number)
                    self.playboard.checkCRB()
                    self.playboard.updateGrid(self.screen)
                    pygame.display.update()
        else:
            return False

    def tabKey(self):
        self.playboard.resetSelected(self.screen)
        self.playboard.writeNumber(self.screen,self.playboard.returnNumber(),const.BLUE)
        self.playboard.redrawNotes(self.screen)
        pygame.display.update()

    def backspaceKey(self):
        if(0 != self.playboard.returnNumber()):
            self.actionLog.insert(0,[0,self.playboard.returnNumber(),self.playboard.returnSelected(0),self.playboard.returnSelected(1)])
        self.playboard.eraseNumberGrid(self.screen)
        self.playboard.eraseNumberArray()
        if(self.playboard.gridArray[self.playboard.returnSelected(0)][self.playboard.returnSelected(1)].returnIfAny()):
            self.playboard.checkCRB()
        self.playboard.updateGrid(self.screen)
        pygame.display.update()

    def undo(self):
        if(not self.actionLog):
            return None
        catch = self.actionLog.pop(0)
        selected = [self.playboard.returnSelected(0),self.playboard.returnSelected(1)]
        self.playboard.selectCoord([catch[2],catch[3]])
        self.playboard.saveNumber(catch[1])
        if(catch[1] == 0):
            self.playboard.eraseNumberGrid(self.screen,const.WHITE)
        else:
            self.playboard.writeNumber(self.screen,catch[1],const.WHITE)
        self.playboard.checkCRB()###THIS NNEEDS AN IF STATEMENT
        self.playboard.updateGrid(self.screen)
        #self.playboard.eraseNumberGrid(self.screen,const.WHITE)
        self.playboard.selectCoord([selected[0],selected[1]])
        pygame.display.update()



    #Utility functions

    def isInGrid(self,mpos):
        if((mpos[0] > self.widthBuffer and mpos[0] < (self.widthBuffer + const.GRIDWIDTH)) and (mpos[1] > self.heightBuffer and mpos[1] < (self.heightBuffer + const.GRIDHEIGHT))):
            return True
        else:
            return False
