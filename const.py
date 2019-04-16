#This file contains all constants for the program

import pygame
print("Importing contants...")




#Size of Grid and objects in the grid
MULTIPLIER = 7
WINDOWSIZE = 81
WINDOWWIDTH = WINDOWSIZE * MULTIPLIER
WINDOWHEIGHT = WINDOWSIZE * MULTIPLIER
BOXSIZE = WINDOWSIZE * MULTIPLIER / 3
CELLSIZE = BOXSIZE / 3
NOTESIZE = CELLSIZE / 3

#Font
pygame.font.init()


#Number Font
NUFONT = pygame.font.SysFont("arial", 90)
#NUFONT = pygame.font.Font("calibri.ttf", 70)

#Note Font
NOFONT = pygame.font.SysFont("Comic Sans MS", 30)

#Colors
WHITE    =(255,255,255)
BLACK    =(  0,  0,  0)
RED      =(255, 33, 33) #Fix color

#Light mode Colors
GREY     =(220,220,220)
LIGHTGREY=(235,235,235)
BLUE     =(210,230,255)
#add Light blue for adjacent
#Dark mode Colors


print("Finished")
