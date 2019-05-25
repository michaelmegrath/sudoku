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
    def __init__(self):
        self.heightBuffer = int(const.CELLSIZE*1.5)
        self.widthBuffer = int(const.CELLSIZE*3)
        self.noteArray = []
        self.writtenArray = []
        self.starterArray = []
        self.wrongArray = []



    def loadImage(self):
        for i in range(0,9,1):
            self.noteArray.append(pygame.image.load("img/Note" + str(i+1) + ".png").convert_alpha())
            self.writtenArray.append(pygame.image.load("img/Written" + str(i+1) + ".png").convert_alpha())
            self.starterArray.append(pygame.image.load("img/Starter" + str(i+1) + ".png").convert_alpha())
            self.wrongArray.append(pygame.image.load("img/Wrong" + str(i+1) + ".png").convert_alpha())
    #drawNumber draws the number to the pygame window the arguments are as follows:
    #screen, address, to a pygame window
    #number, int, to be printed
    #coord, tuple of two ints(EG: 0,0 or 8,8), that are coordinates of the cell to draw the number to
    #color, tuple of three ints(each int must not surpass 255), color that the number drawn
    def drawNumber(self,screen,number,coord,color = 'darkgrey'):
        if(coord == [-1,-1] or coord == (-1,-1)):
            return False
        if(number == 0):
            return False
        if(color == 'red'):
            image = self.wrongArray[number-1]
        elif(color == 'black'):
            image = self.starterArray[number-1]
        else:
            image = self.writtenArray[number-1]
        screen.blit(image,(coord[0]*const.CELLSIZE+self.widthBuffer,coord[1]*const.CELLSIZE+self.heightBuffer))
        return True

        #label = const.NUFONT.render(str(number), False, color)
        #screen.blit(label,(coord[0]*const.CELLSIZE+((1/4)*const.CELLSIZE),coord[1]*const.CELLSIZE+((1/8)*const.CELLSIZE)))
        return None

    #drawGrid draws the intial grid for the game, it is only called once, its argument is:
    #screen, address, to a pygame window
    def drawGrid(self,screen):
        for x in range(self.widthBuffer,int(const.GRIDWIDTH)+self.widthBuffer, int(const.CELLSIZE)):
            pygame.draw.line(screen, const.GREY, (x,self.heightBuffer),(x,const.GRIDHEIGHT+self.heightBuffer))
        for y in range(self.heightBuffer,int(const.GRIDHEIGHT)+self.heightBuffer, int(const.CELLSIZE)):
            pygame.draw.line(screen, const.GREY, (self.widthBuffer,y), (const.GRIDWIDTH+self.widthBuffer,y))

        for x in range(self.widthBuffer, int(const.GRIDWIDTH)+self.widthBuffer, int(const.BOXSIZE)):
            pygame.draw.line(screen, const.BLACK, (x,self.heightBuffer),(x,const.GRIDHEIGHT+self.heightBuffer))
        pygame.draw.line(screen, const.BLACK,(const.GRIDWIDTH+self.widthBuffer,self.heightBuffer),(const.GRIDWIDTH+self.widthBuffer,const.GRIDHEIGHT+self.heightBuffer))
        for y in range(self.heightBuffer,int(const.GRIDHEIGHT)+self.heightBuffer, int(const.BOXSIZE)):
            pygame.draw.line(screen, const.BLACK, (self.widthBuffer,y), (const.GRIDWIDTH+self.widthBuffer,y))
        pygame.draw.line(screen, const.BLACK,(self.widthBuffer,const.GRIDHEIGHT+self.heightBuffer),(const.GRIDWIDTH+self.widthBuffer,const.GRIDHEIGHT+self.heightBuffer))
        self.loadImage()
        return None

    #toggleSelect paints the selected cell, its arguments are:
    #screen, address, to a pygame window
    #coord, tuple of two ints(EG: 0,0 or 8,8), that are coordinates of the cell to select
    #color, tuple of three ints(each int must not surpass 255), color that the cell will be
    def toggleSelect(self,screen,coord,color):
        if(coord == (-1,-1) or coord == [-1,-1]):
            return False
        else:
            pygame.draw.rect(screen,color,((coord[0]*const.CELLSIZE+1)+self.widthBuffer,(coord[1]*const.CELLSIZE+1)+self.heightBuffer,const.CELLSIZE-1,const.CELLSIZE-1),0)
            return True

    def drawNote(self,screen,coord,number):
        if(coord == [-1,-1] or coord == (-1,-1)):
            return False
        else:
            location = (coord[0]*const.CELLSIZE + const.NOTESIZE*((number-1)%3)+self.widthBuffer,coord[1]*const.CELLSIZE + const.NOTESIZE*((number-1)-((number-1)%3))/3+self.heightBuffer)
            screen.blit(self.noteArray[number-1],location)
            return True

    def eraseNote(self,screen,coord,number):
        if(coord == [-1,-1] or coord == (-1,-1)):
            return False
        else:
            rectangle = (coord[0]*const.CELLSIZE + const.NOTESIZE*((number-1)%3) + 1+self.widthBuffer,coord[1]*const.CELLSIZE + const.NOTESIZE*((number-1)-((number-1)%3))/3 + 1+self.heightBuffer,const.NOTESIZE-1,const.NOTESIZE-1)
            pygame.draw.rect(screen,const.BLUE,(rectangle))
            return True


    def changeBuffer(self,wwidth,wheight):
        self.widthBuffer = int((wwidth/2) - (4.5*const.CELLSIZE))
        self.heightBuffer = int((wheight/2) - (4.5*const.CELLSIZE))



class GridController:
    #Object Variables
    gridArray = [[cell.Cell((j,i)) for j in range(9)] for i in range(9)]
    #self.gridArray[self.selected[0]][self.selected[1]]  How to reference the selected cell

    #self.selected[0]
    gridgraph = GridGraphical()
    #self.gridgraph.placeholder(args)


    #Constructor & render functions
    def __init__(self,screen):
        self.selected = (-1,-1)
        self.starters = starter.Starter()
        self.gridgraph.drawGrid(screen)
        self.getStarters(screen)
        self.heightBuffer = int(const.CELLSIZE*1.5)
        self.widthBuffer = int(const.CELLSIZE*3)


    def render(self,screen): #Renders gameboard
        screen.fill(const.WHITE)
        self.gridgraph.drawGrid(screen)
        self.redrawNumbers(screen)
        self.updateGrid(screen)
        return None

    def newGame(self,screen):
        self.resetSelected(screen)
        self.clearGrid(screen)
        self.starters.newGame()
        self.getStarters(screen)
        self.updateGrid(screen)

    def changeBuffer(self,wwidth,wheight):
        self.widthBuffer = int((wwidth/2) - (4.5*const.CELLSIZE))
        self.heightBuffer = int((wheight/2) - (4.5*const.CELLSIZE))
        self.gridgraph.changeBuffer(wwidth,wheight)

    #Selection functions
    def isSelected(self): #If there is a selected square return true else return false
        if(self.selected == (-1,-1) or self.selected == [-1,-1]):
            return False
        else:
            return True

    def selectCell(self,x,screen): # Selects Cell
        if(self.selected != (-1,-1) or self.selected != [-1,-1]): # If there is something selected
            #undo graphical selection for current selection
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
        self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
        self.redrawNotes(screen)
        self.selected = (int((x[0]-self.widthBuffer)/const.CELLSIZE),int((x[1]-self.heightBuffer)/const.CELLSIZE))
        self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
        return None

    def moveSelected(self,direction,screen):
        if(0<=self.selected[0]<9 and 0<=self.selected[1]<9):
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
            #self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
            self.redrawNotes(screen)
            self.moveDirection(direction)
            self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
            self.updateGrid(screen)


    def moveDirection(self,direction):
        if(direction == 'l' and self.selected[0]>0):
            self.selected = (self.selected[0]-1,self.selected[1])
        elif(direction == 'r' and self.selected[0]<8):
            self.selected = (self.selected[0]+1,self.selected[1])
        elif(direction == 'u' and self.selected[1]>0):
            self.selected = (self.selected[0],self.selected[1]-1)
        elif(direction == 'd' and self.selected[1]<8):
            self.selected = (self.selected[0],self.selected[1]+1)
        else:
            pass


    #Number/Cell functions
    def writeNumber(self,screen,number,color = const.BLUE): #Write and save number OVERHAUL THIS FUNCTION
        if(self.gridArray[self.selected[0]][self.selected[1]].getNumber() != 0):
            self.gridArray[self.selected[0]][self.selected[1]].removeNotes()
            self.eraseNumberGrid(screen,color)
        if(self.selected == (-1,-1)):
            return False
        if(self.gridArray[self.selected[0]][self.selected[1]].returnIfAny() == True):
            self.gridgraph.drawNumber(screen,number,self.selected,'red')
        elif(self.gridArray[self.selected[0]][self.selected[1]].starter == True):
            self.gridgraph.drawNumber(screen,number,self.selected,'black')
        else:
            self.gridgraph.drawNumber(screen,number,self.selected)
        return True
    def saveNumber(self,number):
        if(self.selected == (-1,-1)):
            return False
        if(self.gridArray[self.selected[0]][self.selected[1]].changeCell(number)):
            return True
        else:
            return False

    def eraseNumberGrid(self,screen,color = const.BLUE): ##RENAME
        if(self.selected[0] < 0 or self.selected[1] < 0):
            return None
        self.gridgraph.toggleSelect(screen,self.selected,color)


        return None
    def eraseNumberArray(self):
        self.gridArray[self.selected[0]][self.selected[1]].removeNotes()
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


        return None
    def populateBoxArray(self,boxArray,index):
        box = self.returnBox(index)
        for y in range(box[1],box[1]+3,1):
            for x in range(box[0],box[0]+3,1):
                boxArray.append(self.gridArray[x][y].getNumber())



    def clearGrid(self,screen):
        for x in range(0,9,1):
            for y in range(0,9,1):
                self.gridArray[x][y].resetCell()
                self.gridgraph.toggleSelect(screen,(x,y),const.WHITE)


    def updateGrid(self,screen):
        for x in range(0,9,1):
            for y in range(0,9,1):
                if(self.gridArray[x][y].returnIfAny()):
                    self.gridgraph.toggleSelect(screen,(x,y),const.WHITE)
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),'red')
                elif(self.gridArray[x][y].returnStarter()):
                    self.gridgraph.toggleSelect(screen,(x,y),const.WHITE)
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),'black')
                else:
                    #self.gridgraph.toggleSelect(screen,(x,y),const.WHITE)
                    self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y))
        if(self.gridArray[self.selected[0]][self.selected[1]].returnIfAny() and self.selected != (-1,-1)):
            self.gridgraph.toggleSelect(screen,(self.selected[0],self.selected[1]),const.BLUE)
            self.gridgraph.drawNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),(self.selected[0],self.selected[1]),'red')


    def getStarters(self,screen):
        for x in range(0,9,1):
            for y in range(0,9,1):
                if(self.starters.grid[x][y] == 0):
                    pass
                elif(self.starters.grid[x][y] > 9):
                    pass
                else:
                    self.gridArray[x][y].setStarter(self.starters.grid[x][y])
                    #self.gridgraph.drawNumber(screen,self.gridArray[x][y].getNumber(),(x,y),'black')

    def redrawNumbers(self,screen):
        self.selected = [-1,-1]
        for x in range(0,9,1):
            for y in range(0,9,1):
                self.redrawNotes(screen,(x,y))



    def setNote(self,screen,number):
        if(self.gridArray[self.selected[0]][self.selected[1]].toggleNote(number) == True):
            self.gridgraph.drawNote(screen,self.selected,number)
        elif(self.gridArray[self.selected[0]][self.selected[1]].getNumber() == 0):
            self.gridgraph.eraseNote(screen,self.selected,number)
        else:
            return None

    def redrawNotes(self,screen,coord = (-1,-1)):
        if(coord == (-1,-1)):
            temp = self.gridArray[self.selected[0]][self.selected[1]].returnNoteArray()
            for i in range(0,9,1):
                if(temp[i]):
                    self.gridgraph.drawNote(screen,self.selected,i+1)
        else:
            temp = self.gridArray[coord[0]][coord[1]].returnNoteArray()
            for i in range(0,9,1):
                if(temp[i]):
                    self.gridgraph.drawNote(screen,coord,i+1)

    def resetSelected(self,screen):
        if(self.selected != (-1,-1)):
            self.gridgraph.toggleSelect(screen,self.selected,const.WHITE)
        self.writeNumber(screen,self.gridArray[self.selected[0]][self.selected[1]].getNumber(),const.WHITE)
        self.redrawNotes(screen)
        self.selected = (0,0)
        self.gridgraph.toggleSelect(screen,self.selected,const.BLUE)
        return None


print("Finished")#terminal output
