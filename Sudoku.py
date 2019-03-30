import pygame
import grid
import const


def main():
    global screen
    screen = pygame.display.set_mode((const.WINDOWWIDTH+1, const.WINDOWHEIGHT+1))
    pygame.display.set_caption('Sudoku')
    screen.fill(const.WHITE)
    grid.drawGrid(screen)
    playboard = grid.Grid()
    pygame.display.flip()
    running = True


    

    while running: #Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                playboard.selectCell(pygame.mouse.get_pos(),screen)



if __name__=='__main__':
    main()
