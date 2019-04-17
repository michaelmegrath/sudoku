#Michael Megrath 2019
#This File, controls the indivdual cells via the Cell object in the Sudoku grid
#The cells have 2 Major values:

#cellValue which holds the value of what is in the cell

#duplicateFlag which holds the value True or False, based on
#if other cells in the row, column, or box. The logic is controlled in grid.py ******UPDATE********



import const #const.py includes all of the Constants used in this program



class Cell:

    #Object Variables
    cellValue = 0
    duplicateFlag = [False,False,False]


    #Constructor
    def __init__(self, gridCoord):
        notesArray = [False,False,False,False,False,False,False,False,False]
        coord = gridCoord

    #Note Functions
    def toggleNote(self, note): #note - int that is the index for the note that needs to be toggled
        notesArray[note] != notesArray[note]
        return None

    def removeNotes():
        notesArray = [False,False,False,False,False,False,False,False,False]
        return None


    #Cell Functions
    def changeCell(self,number): #number - int that sets the value for the cell
        self.cellValue = number
        return None

    def getNumber(self):
        return self.cellValue #Returns int value within cellValue


    #Duplicate Functions
    def toggleDuplicate(self,index,turnOn = True): #turnOn - boolean that sets the value for the duplicateFlag automatically True
        if(turnOn):
            self.duplicateFlag[index] = True
            return None
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
