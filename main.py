import pygame
import const
import controller
import Sudoku


def main():
    global screen
    screen = pygame.display.set_mode((int(const.WINDOWWIDTH+1), int(const.WINDOWHEIGHT+1)),pygame.RESIZABLE)
    control = controller.Controller(screen)
    clock = pygame.time.Clock()



    running = True #Variable for gameloop
    while running: #Main Loop
        clock.tick(15)
        mouseLocal = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()


            elif event.type == pygame.VIDEORESIZE:
                control.resizeWindow((event.w,event.h))

            #Selecting Cells w/ mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                if(not control.mouseClick(mouseLocal)):
                    running = False




if __name__=='__main__':
    main()
