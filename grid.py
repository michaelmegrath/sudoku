import pygame
import const
import cell
print("Importing grid...")

def drawGrid(screen):
    for x in range(0,int(const.WINDOWWIDTH), int(const.CELLSIZE)):
        pygame.draw.line(screen, const.GREY, (x,0),(x,const.WINDOWHEIGHT))
    for y in range(0,int(const.WINDOWHEIGHT), int(const.CELLSIZE)):
        pygame.draw.line(screen, const.GREY, (0,y), (const.WINDOWWIDTH,y))

    for x in range(0, int(const.WINDOWWIDTH), int(const.BOXSIZE)):
        pygame.draw.line(screen, const.BLACK, (x,0),(x,const.WINDOWHEIGHT))
    pygame.draw.line(screen, const.BLACK,(const.WINDOWWIDTH-1,0),(const.WINDOWWIDTH-1,const.WINDOWHEIGHT))
    for y in range(0,int(const.WINDOWHEIGHT), int(const.BOXSIZE)):
        pygame.draw.line(screen, const.BLACK, (0,y), (const.WINDOWWIDTH,y))
    pygame.draw.line(screen, const.BLACK,(0,const.WINDOWHEIGHT-1),(const.WINDOWWIDTH,const.WINDOWHEIGHT-1))
    return None
class Grid:
    def _init_():
        gridArray = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    def selectCell(x):
        print(x)



    
print("Finished")
