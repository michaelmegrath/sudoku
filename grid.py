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
    pygame.draw.line(screen, const.BLACK,(const.WINDOWWIDTH-1,0),(const.WINDOWWIDTH-1,const.WINDOWHEIGHT))
    for y in range(0,int(const.WINDOWHEIGHT), int(const.BOXSIZE)):
        pygame.draw.line(screen, const.BLACK, (0,y), (const.WINDOWWIDTH,y))
    pygame.draw.line(screen, const.BLACK,(0,const.WINDOWHEIGHT-1),(const.WINDOWWIDTH,const.WINDOWHEIGHT-1))
    return None

def selectCell(screen,coord):
    print("works")
    pygame.draw.rect(screen,const.BLUE,(0,0,const.CELLSIZE,const.CELLSIZE),0)
    #pygame.draw.rect(screen,const.BLUE,(coord[0]*const.CELLSIZE,coord[1]*const.CELLSIZE,const.CELLSIZE,const.CELLSIZE),)
    return None


class Grid:
    gridArray = [[cell.Cell() for j in range(9)] for i in range(9)]
    selected = (-1,-1)
    
    def _init_(self):
        self.selected = selected
        #add feature that puts in givens
    
    def selectCell(self,x,screen):
        if(self.selected != (-1,-1)): # If there is something selected
            #undo graphical selection for current selection
            pass
            
        self.selected = (int(x[0]/const.CELLSIZE),int(x[1]/const.CELLSIZE))
        selectCell(screen,self.selected)
        #self.gridArray[self.selected[0]][self.selected[1]]  How to reference the selected cell
        print(self.selected)




    
print("Finished")
