#grid.py is for managing the play grid
#There are two main classes
#GridGraphical which outputs to the screen
#GridController which manages storing data, and calling GridGraphical
#More information can be found for each class on the lines before they are delcared


import pygame
import const
import cell
print("Importing grid...") #Terminal output



#The Gridgraphical object controls output and cleanup of the graphics on the pygame window
#There are No member variables in GridGraphical, all variables needed are passed in as arguments
#Todo:
#check pygame antialias settings
class GridGraphical:
    #drawNumber draws the number to the pygame window the arguments are as follows:
    #screen, address, to a pygame window
    #number, int, to be printed
    #coord, tuple of two ints(EG: 0,0 or 8,8), that are coordinates of the cell to draw the number to
    #color, tuple of three ints(each int must not surpass 255), color that the number drawn
    def drawNumber(self,screen,number,coord,color = const.BLACK):
        if(number == 0):
            return None
        label = const.NUFONT.render(str(number), False, color)
        screen.blit(label,(coord[0]*const.CELLSIZE+((1/4)*const.CELLSIZE),coord[1]*const.CELLSIZE+((1/8)*const.CELLSIZE)))
        return None

    #drawGrid draws the intial grid for the game, it is only called once, its argument is:
    #screen, address, to a pygame window
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

    #toggleSelect paints the selected cell, its arguments are:
    #screen, address, to a pygame window
    #coord, tuple of two ints(EG: 0,0 or 8,8), that are coordinates of the cell to select
    #color, tuple of three ints(each int must not surpass 255), color that the cell will be
    def toggleSelect(self,screen,coord,color):
        pygame.draw.rect(screen,color,(coord[0]*const.CELLSIZE+1,coord[1]*const.CELLSIZE+1,const.CELLSIZE-1,const.CELLSIZE-1),0)
        return None




class GridController:
    #Object Variables
    gridArray = [[cell.Cell((j,i)) for j in range(9)] for i in range(9)]
    #self.gridArray[self.selected[0]][self.selected[1]]  How to reference the selected cell
    selected = (-1,-1)
    #self.selected[0]
    gridgraph = GridGraphical()
    #self.gridgraph.placeholder(args)

    #Constructor & render functions
    def _init_(self):
        self.selected = selected

    def render(self,screen): #Renders gameboard
        screen.fill(const.WHITE)
        self.gridgraph.drawGrid(screen)
        #add feature that puts in givens
        return None

    #Selection functions
    def isSelected(self): #If there is a selected square return true else return false
        if(self.selected == (-1,-1)):
            return False
        else:
            return True

    def selectCell(self,x,screen): # Selects Cell
        if(self.selected != (-1,-1)): # If there is something selected
            #undo graphical selection for current selection
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
        self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
        self.selected = (int(x[0]/const.CELLSIZE),int(x[1]/const.CELLSIZE))
        self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
        return None

    def moveSelected(self,direction,screen):
        if(direction == 'l' and self.selected[0] > 0): #Left Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
            self.selected = (self.selected[0]-1,self.selected[1])
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            self.highlightDuplicates(screen)
            return None
        if(direction == 'r' and self.selected[0] < 8): #Right Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
            self.selected = (self.selected[0]+1,self.selected[1])
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            self.highlightDuplicates(screen)
            return None
        if(direction == 'u' and self.selected[1] > 0): #Up Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
            self.selected = (self.selected[0],self.selected[1]-1)
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            self.highlightDuplicates(screen)
            return None
        if(direction == 'd' and self.selected[1] < 8):#Down Arrow control
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
            self.selected = (self.selected[0],self.selected[1]+1)
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            self.highlightDuplicates(screen)
            return None

    #Number/Cell functions
    def writeNumber(self,screen,number,color = const.BLUE): #Write and save number
        if(self.gridArray[self.selected[0]][self.selected[1]].getNumber() != 0):
            self.eraseNumberGrid(screen,color)

        if(self.gridArray[self.selected[0]][self.selected[1]].returnIfAny() == False):
            self.gridgraph.drawNumber(screen,number,self.selected)
        else:
            self.gridgraph.drawNumber(screen,number,self.selected,const.RED)
        return None
    def saveNumber(self,number):
        self.gridArray[self.selected[0]][self.selected[1]].changeCell(number)


    def eraseNumberGrid(self,screen,color = const.BLUE):
        self.gridgraph.toggleSelect(screen,self.selected,color)

        return None
    def eraseNumberArray(self):
        self.gridArray[self.selected[0]][self.selected[1]].changeCell(0)

    def returnNumber(self): #Returns Cell Number
        return self.gridArray[self.selected[0]][self.selected[1]].getNumber()

    def returnSelected(self,index):
        return self.selected[index]





    #Check Column, Row, and Box

    def toggleList(self,CRB,index): #Come up with a better name
        count = [0,0,0,0,0,0,0,0,0]
        for i in range(0,8,1):
            for j in range(i+1,9,1):
                if(CRB == 'c'):
                    if(self.gridArray[index][i].getNumber() == self.gridArray[index][j].getNumber() and self.gridArray[index][j].getNumber() != 0):
                        count[i] = 1
                        count[j] = 1
                if(CRB == 'r'):
                    if(self.gridArray[i][index].getNumber() == self.gridArray[j][index].getNumber() and self.gridArray[j][index].getNumber() != 0):
                       count[i] = 1
                       count[j] = 1
        print(count)
        if(CRB == 'c'):
            for k in range(0,9,1):
                if(count[k] == 1):
                    self.gridArray[index][k].toggleDuplicate(0)
                else:
                    self.gridArray[index][k].toggleDuplicate(0,False)
        if(CRB == 'r'):
            for k in range(0,9,1):
                if(count[k] == 1):
                    self.gridArray[k][index].toggleDuplicate(1)
                else:
                    self.gridArray[k][index].toggleDuplicate(1,False)


    def checkCRB(self): #Come up with a better name
        self.toggleList('c',self.selected[0])
        self.toggleList('r',self.selected[1])
        #Code for Box

    def checkTotalList(self):
        for i in range(0,9,1):
            self.toggleList('c',i)
            self.toggleList('r',i)
            #self.toggleList('b',i)

        return None



    #Highlight duplicates function
    def highlightDuplicates(self,screen):
        for x in range(0,9,1):
            for y in range(0,9,1):
                if(self.gridArray[x][y].returnIfAny()):
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),const.RED)
                else:
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),const.BLACK)
        if(self.gridArray[self.selected[0]][self.selected[1]].returnIfAny()):
            self.gridgraph.toggleSelect(screen,(self.selected[0],self.selected[1]),const.BLUE)
            self.gridgraph.drawNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),(self.selected[0],self.selected[1]),const.RED)




#create debug functions
print("Finished")#terminal output
