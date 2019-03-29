import pygame
import grid
import const


def main():
    global screen
    screen = pygame.display.set_mode((const.WINDOWWIDTH, const.WINDOWHEIGHT))
    pygame.display.set_caption('Sudoku')
    screen.fill(const.WHITE)
    grid.drawGrid(screen)
    pygame.display.flip()
    running = True
    

    while running: #Main Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                grid.Grid.selectCell(pygame.mouse.get_pos())


if __name__=='__main__':
    main()
