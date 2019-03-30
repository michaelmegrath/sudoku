import pygame
import grid
import const


def main():
    global screen
    screen = pygame.display.set_mode((const.WINDOWWIDTH, const.WINDOWHEIGHT))
    pygame.display.set_caption('Sudoku')
    #screen.fill(const.WHITE)
    grid.drawGrid(screen)
    playboard = grid.Grid()
    pygame.display.flip()
    running = True
    print("Cell:",const.CELLSIZE)
    rectangle = (30,30,63,63)
    pygame.draw.rect(screen,const.WHITE,rectangle,5)
    #gameSurface = pygame.surface.Surface(int(const.WINDOWWIDTH),int(const.WINDOWHEIGHT))
    

    while running: #Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                playboard.selectCell(pygame.mouse.get_pos(),screen)



if __name__=='__main__':
    main()
