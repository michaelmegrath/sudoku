import pygame
import const

class Cell:
    
    #Object Variables
    cellValue = 0
    duplicateFlag = False
    
    
    #Constructor
    def __init__(self, gridCoord):
        notesArray = [False,False,False,False,False,False,False,False,False]
        coord = gridCoord
    
    #Note Functions
    def toggleNote(self, note):
        notesArray[note] != notesArray[note]
        return None
    
    def removeNotes():
        notesArray = [False,False,False,False,False,False,False,False,False]
        return None
    
    
    #Cell Functions
    def changeCell(self,number):
        self.cellValue = number
        return None
    
    def getNumber(self):
        return self.cellValue
    
    
    #Duplicate Functions
    def toggleDuplicate(self,turnOn = True):
        if(turnOn):
            self.duplicateFlag = True
        else:
            self.duplicateFlag = False
        return None
    
    def returnDuplicate(self):
        return self.duplicateFlag

