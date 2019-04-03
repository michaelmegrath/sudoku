#grid.py is for managing the play grid
#There are two main classes
#GridGraphical which outputs to the screen
#GridController which manages storing data, and calling GridGraphical



import pygame
import const
import cell
print("Importing grid...")

class GridGraphical:

    def drawNumber(self,screen,number,coord):
        if(number == 0):
            return None
        label = const.NUFONT.render(str(number), False, const.BLACK)
        screen.blit(label,(coord[0]*const.CELLSIZE+((1/4)*const.CELLSIZE),coord[1]*const.CELLSIZE+((1/8)*const.CELLSIZE)))
        return None
    
    
    def drawGrid(self,screen):
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

    def toggleSelect(self,screen,coord,color):
        pygame.draw.rect(screen,color,(coord[0]*const.CELLSIZE+1,coord[1]*const.CELLSIZE+1,const.CELLSIZE-1,const.CELLSIZE-1),0)
        return None




class GridController:
    gridArray = [[cell.Cell((j,i)) for j in range(9)] for i in range(9)]
    selected = (-1,-1)
    gridgraph = GridGraphical()
    def _init_(self):
        self.selected = selected

        #add feature that puts in givens
    
    def render(self,screen): #Renders gameboard
        screen.fill(const.WHITE)
        self.gridgraph.drawGrid(screen)
        return None
    
    
    def isSelected(self): #If there is a selected square return true else return false
        if(self.selected == (-1,-1)):
            return False
        else:
            return True

    
    def selectCell(self,x,screen): # Selects Cell
        if(self.selected != (-1,-1)): # If there is something selected
            #undo graphical selection for current selection
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber())
            pass
            
        self.selected = (int(x[0]/const.CELLSIZE),int(x[1]/const.CELLSIZE))
        self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
        return None
        #self.gridArray[self.selected[0]][self.selected[1]]  How to reference the selected cell

    def moveSelected(self,direction,screen):
        if(direction == 'l' and self.selected[0] > 0): #Left Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber())
            self.selected = (self.selected[0]-1,self.selected[1])
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            return None
        if(direction == 'r' and self.selected[0] < 8): #Right Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber())
            self.selected = (self.selected[0]+1,self.selected[1])
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            return None
        if(direction == 'u' and self.selected[1] > 0): #Up Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber())
            self.selected = (self.selected[0],self.selected[1]-1)
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            return None
        if(direction == 'd' and self.selected[1] < 8):#Down Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber())
            self.selected = (self.selected[0],self.selected[1]+1)
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            return None

    
    def writeNumber(self,screen,number): #Write and save number
        self.gridArray[self.selected[0]][self.selected[1]].changeCell(number)
        self.gridgraph.drawNumber(screen,number,self.selected)
        return None
    def eraseNumber(self,screen):
        self.gridArray[self.selected[0]][self.selected[1]].changeCell(0)
        self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)


    def returnNumber(self): #Returns Cell Number
        return self.gridArray[self.selected[0]][self.selected[1]].getNumber()
    
print("Finished")
