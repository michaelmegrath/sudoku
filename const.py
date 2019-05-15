#This file contains all constants for the program
import math
print("Importing contants...")


SIZE = 9
SRSIZE = math.sqrt(SIZE)


#Size of Grid and objects in the grid
MULTIPLIER = 7
GRIDSIZE = 81
GRIDWIDTH = GRIDSIZE * MULTIPLIER
GRIDHEIGHT = GRIDSIZE * MULTIPLIER
BOXSIZE = GRIDSIZE * MULTIPLIER / 3
CELLSIZE = BOXSIZE / 3
NOTESIZE = CELLSIZE / 3

WINDOWWIDTH = GRIDWIDTH + (CELLSIZE*3)
WINDOWHEIGHT = GRIDHEIGHT + (CELLSIZE*3)






#Colors
WHITE    =(255,255,255)
BLACK    =(  0,  0,  0)

#Light mode Colors
DARKGREY =(130,130,130)
GREY     =(220,220,220)
LIGHTGREY=(235,235,235)
BLUE     =(210,230,255)
#add Light blue for adjacent
#Dark mode Colors


print("Finished")
