import pygame
import const

class Cell:
    def _init_(self, gridCoord):
        cellValue = 0
        notesArray = [False,False,False,False,False,False,False,False,False]
        coord = gridCoord


