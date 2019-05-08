#grid.py is for managing the play grid
#There are two main classes
#GridGraphical which outputs to the screen
#GridController which manages storing data, and calling GridGraphical
#More information can be found for each class on the lines before they are delcared


import pygame
import const
import cell
import starter
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
    def drawNumber(self,screen,number,coord,color = const.DARKGREY):
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

    #self.selected[0]
    gridgraph = GridGraphical()
    #self.gridgraph.placeholder(args)


    #Constructor & render functions
    def __init__(self):
        self.selected = (-1,-1)
        self.starters = starter.Starter()

    def render(self,screen): #Renders gameboard
        screen.fill(const.WHITE)
        self.gridgraph.drawGrid(screen)
        self.getStarters(screen)
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
    def writeNumber(self,screen,number,color = const.BLUE): #Write and save number OVERHAUL THIS FUNCTION
        if(self.gridArray[self.selected[0]][self.selected[1]].getNumber() != 0):
            self.eraseNumberGrid(screen,color)

        if(self.gridArray[self.selected[0]][self.selected[1]].returnIfAny() == True):
            self.gridgraph.drawNumber(screen,number,self.selected,const.RED)
        elif(self.gridArray[self.selected[0]][self.selected[1]].starter == True):
            self.gridgraph.drawNumber(screen,number,self.selected,const.BLACK)
        else:
            self.gridgraph.drawNumber(screen,number,self.selected)
        return None
    def saveNumber(self,number):
        if(self.gridArray[self.selected[0]][self.selected[1]].changeCell(number)):
            return True
        else:
            return False

    def eraseNumberGrid(self,screen,color = const.BLUE):
        self.gridgraph.toggleSelect(screen,self.selected,color)

        return None
    def eraseNumberArray(self):
        self.gridArray[self.selected[0]][self.selected[1]].changeCell(0)

    def returnNumber(self): #Returns Cell Number
        return self.gridArray[self.selected[0]][self.selected[1]].getNumber()

    def returnSelected(self,index):
        return self.selected[index]





    #Check Column, Row, and Box, THIS ENTIRE SECTION NEEDS BETTER FUNCTION NAMES

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
                if(CRB == 'b'):
                    boxArray = []
                    self.populateBoxArray(boxArray,index)
                    if(boxArray[i] == boxArray[j] and boxArray[j] != 0):
                        count[i] = 1
                        count[j] = 1

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
        if(CRB == 'b'):
            for k in range(0,9,1):
                if(count[k] == 1):
                    coord = self.returnCoordInBox(index,k)
                    self.gridArray[coord[0]][coord[1]].toggleDuplicate(2)
                else:
                    coord = self.returnCoordInBox(index,k)
                    self.gridArray[coord[0]][coord[1]].toggleDuplicate(2,False)



    def returnCoordInBox(self,index,increment):
        start = self.returnBox(index)
        coord = [int(start[0] + (increment % 3)),int(start[1] + (increment - (increment % 3)) / 3)]
        return coord


    def returnSelectedBox(self):
        x = self.selected[0] - (self.selected[0] % 3)
        y = self.selected[1] - (self.selected[1] % 3)
        return (y + ((x+3)/3)) - 1

    def returnBox(self,index):
        x = int((index % 3) * 3)
        y = int(index - (index % 3))
        return (x,y)

    def checkCRB(self): #Come up with a better name
        self.toggleList('c',self.selected[0])
        self.toggleList('r',self.selected[1])
        self.toggleList('b',self.returnSelectedBox())

    def checkTotalBoard(self):
        for i in range(0,9,1):
            self.toggleList('c',i)
            self.toggleList('r',i)
            self.toggleList('b',i)

        return None
    def populateBoxArray(self,boxArray,index):
        box = self.returnBox(index)
        for y in range(box[1],box[1]+3,1):
            for x in range(box[0],box[0]+3,1):
                boxArray.append(self.gridArray[x][y].getNumber())




    #Highlight duplicates function
    def highlightDuplicates(self,screen):
        for x in range(0,9,1):
            for y in range(0,9,1):
                if(self.gridArray[x][y].returnIfAny()):
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),const.RED)
                elif(self.gridArray[x][y].returnStarter()):
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),const.BLACK)
                else:
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y))
        if(self.gridArray[self.selected[0]][self.selected[1]].returnIfAny()):
            self.gridgraph.toggleSelect(screen,(self.selected[0],self.selected[1]),const.BLUE)
            self.gridgraph.drawNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),(self.selected[0],self.selected[1]),const.RED)


    def getStarters(self,screen):
        for x in range(0,9,1):
            for y in range(0,9,1):
                if(self.starters.grid[x][y] == 0):
                    pass
                elif(self.starters.grid[x][y] > 9):
                    pass
                else:
                    self.gridArray[x][y].setStarter(self.starters.grid[x][y])
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),const.BLACK)


#create debug functions

    def isStarter(self):
        for x in range(0,9,1):
            for y in range(0,9,1):
                print(self.gridArray[x][y].returnStarter())

print("Finished")#terminal output
