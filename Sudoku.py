import pygame
import const
import gameController


def Sudoku(screen):



    #Constructing Screen
    #global screen
    #screen = pygame.display.set_mode((int(const.WINDOWWIDTH+1), int(const.WINDOWHEIGHT+1)),pygame.RESIZABLE)
    gameControl = gameController.GameController(screen)
    clock = pygame.time.Clock()

    #TEST FUNCTIONS



    running = True #Variable for gameloop
    while running: #Main Loop
        clock.tick(15)
        mouseLocal = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.display.quit()


            elif event.type == pygame.VIDEORESIZE:
                gameControl.resizeWindow((event.w,event.h))

            #Selecting Cells w/ mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                if(not gameControl.mouseClick(mouseLocal)):
                    running = False


            elif event.type == pygame.KEYDOWN:

                #Arrow key Functionallity
                if event.key == pygame.K_LEFT:
                    gameControl.arrowKey('l')
                if event.key == pygame.K_RIGHT:
                    gameControl.arrowKey('r')
                if event.key == pygame.K_UP:
                    gameControl.arrowKey('u')
                if event.key == pygame.K_DOWN:
                    gameControl.arrowKey('d')

                if event.key == pygame.K_TAB:
                    gameControl.tabKey()

                #Number is pressed
                if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        gameControl.numberKey(event.key - 48,True) # K_1 = 49, so for the integer 1, subtract 48 (1 = 49 - 48)
                    else:
                        gameControl.numberKey(event.key - 48,False)
                elif event.key >= pygame.K_KP1 and event.key <= pygame.K_KP9:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        gameControl.numberKey(event.key - 256,True) # K_KP1 = 257, so for the integer 1, subtract 48 (1 = 257 - 256)
                    else:
                        gameControl.numberKey(event.key - 256,False)

                #Delete Cell
                if event.key == pygame.K_BACKSPACE:
                    gameControl.backspaceKey()


#if __name__=='__main__':
#    main()
