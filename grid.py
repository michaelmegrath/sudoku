#grid.py is for managing the play grid
#There are two main parts to the file, the drawGrid Method and the Grid class
#The Method draws the grid
#The class is the main controller behind the grid, takes in user input and outputs on screen

import pygame
import const
import cell
print("Importing grid...")

#
def drawGrid(screen):
    for x in range(0,int(const.WINDOWWIDTH), int(const.CELLSIZE)):
        pygame.draw.line(screen, const.GREY, (x,0),(x,const.WINDOWHEIGHT))
    for y in range(0,int(const.WINDOWHEIGHT), int(const.CELLSIZE)):
        pygame.draw.line(screen, const.GREY, (0,y), (const.WINDOWWIDTH,y))

    for x in range(0, int(const.WINDOWWIDTH), int(const.BOXSIZE)):
        pygame.draw.line(screen, const.BLACK, (x,0),(x,const.WINDOWHEIGHT))
    pygame.draw.line(screen, const.BLACK,(const.WINDOWWIDTH,0),(const.WINDOWWIDTH,const.WINDOWHEIGHT))
    for y in range(0,int(const.WINDOWHEIGHT), int(const.BOXSIZE)):
        pygame.draw.line(screen, const.BLACK, (0,y), (const.WINDOWWIDTH,y))
    pygame.draw.line(screen, const.BLACK,(0,const.WINDOWHEIGHT),(const.WINDOWWIDTH,const.WINDOWHEIGHT))
    return None

def toggleSelect(screen,coord,color):
    pygame.draw.rect(screen,color,(coord[0]*const.CELLSIZE+1,coord[1]*const.CELLSIZE+1,const.CELLSIZE-1,const.CELLSIZE-1),0)
    #pygame.display.flip()

    #pygame.draw.rect(screen,const.BLUE,(coord[0]*const.CELLSIZE,coord[1]*const.CELLSIZE,const.CELLSIZE,const.CELLSIZE),)
    return None


class Grid:
    gridArray = [[cell.Cell() for j in range(9)] for i in range(9)]
    selected = (-1,-1)
    
    def _init_(self):
        self.selected = selected
        #add feature that puts in givens
    
    def isSelected(self):
        if(self.selected == (-1,-1)):
            return False
        else:
            return True

    
    def selectCell(self,x,screen):
        if(self.selected != (-1,-1)): # If there is something selected
            #undo graphical selection for current selection
            toggleSelect(screen,self.selected,const.WHITE)
            pass
            
        self.selected = (int(x[0]/const.CELLSIZE),int(x[1]/const.CELLSIZE))
        toggleSelect(screen,self.selected,const.BLUE)
        #self.gridArray[self.selected[0]][self.selected[1]]  How to reference the selected cell
        print(self.selected)

    def moveSelected(self,direction,screen):
        if(direction == 'l' and self.selected[0] > 0):
            toggleSelect(screen,self.selected,const.WHITE)
            self.selected = (self.selected[0]-1,self.selected[1])
            toggleSelect(screen,self.selected,const.BLUE)
            return None
        if(direction == 'r' and self.selected[0] < 8):
            toggleSelect(screen,self.selected,const.WHITE)
            self.selected = (self.selected[0]+1,self.selected[1])
            toggleSelect(screen,self.selected,const.BLUE)
            return None
        if(direction == 'u' and self.selected[1] > 0):
            toggleSelect(screen,self.selected,const.WHITE)
            self.selected = (self.selected[0],self.selected[1]-1)
            toggleSelect(screen,self.selected,const.BLUE)
            return None
        if(direction == 'd' and self.selected[1] < 8):
            toggleSelect(screen,self.selected,const.WHITE)
            self.selected = (self.selected[0],self.selected[1]+1)
            toggleSelect(screen,self.selected,const.BLUE)
            return None




    
print("Finished")
