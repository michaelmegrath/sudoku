#Michael Megrath 2019
#This File, controls the indivdual cells via the Cell object in the Sudoku grid
#The cells have 2 Major values:

#cellValue which holds the value of what is in the cell

#duplicateFlag which holds the value True or False, based on
#if other cells in the row, column, or box. The logic is controlled in grid.py ******UPDATE********



import const #const.py includes all of the Constants used in this program



class Cell:

    #Object Variables
    #cellValue = 0


    #Constructor
    def __init__(self, gridCoord):
        self.notesArray = [False,False,False,False,False,False,False,False,False]
        self.coord = gridCoord
        self.duplicateFlag = [False,False,False]
        self.starter = False
        self.cellValue = 0


    #Note Functions
    def toggleNote(self, note): #note - int that is the index for the note that needs to be toggled
        if(self.cellValue != 0):
            return self.notesArray[note-1]
        else:
            self.notesArray[note-1] = not self.notesArray[note-1]
            return self.notesArray[note-1]

    def removeNotes(self):
        self.notesArray = [False,False,False,False,False,False,False,False,False]
        return None

    def hasNotes(self):
        if(any(self.notesArray)):
            return True
        else:
            return False


    #Cell Functions
    def changeCell(self,number): #number - int that sets the value for the cell
        if(self.starter == True):
            return False
        else:
            self.removeNotes()
            self.cellValue = number
            return True

    def getNumber(self):
        return self.cellValue #Returns int value within cellValue

    def setStarter(self,number):
        if(number == 0):
            self.cellValue = 0
            return None
        else:
            self.starter = True
            self.cellValue = number
            return None

    def returnNoteArray(self):
        return self.notesArray


    #Duplicate Functions
    def toggleDuplicate(self,index,turnOn = True): #turnOn - boolean that sets the value for the duplicateFlag automatically True
        if(turnOn):
            self.duplicateFlag[index] = True

        else:
            self.duplicateFlag[index] = False
        return None

    def returnDuplicate(self,index):
        return self.duplicateFlag[index] #Returns boolean value of duplicateFlag

    def returnIfAny(self):
        if(self.duplicateFlag[0] or self.duplicateFlag[1] or self.duplicateFlag[2]):
            return True
        else:
            return False

    def returnStarter(self):
        return self.starter


    ## DEBUG:
