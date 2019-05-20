import pygame
import const
import controller


def main():



    print("Running!")
    #Constructing Screen
    global screen
    screen = pygame.display.set_mode((int(const.WINDOWWIDTH+1), int(const.WINDOWHEIGHT+1)),pygame.RESIZABLE)
    control = controller.Controller(screen)


    #TEST FUNCTIONS



    running = True #Variable for gameloop
    while running: #Main Loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                running = False

            elif event.type == pygame.VIDEORESIZE:
                control.resizeWindow((event.w,event.h))

            #Selecting Cells w/ mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                control.mouseClick(pygame.mouse.get_pos())

            elif event.type == pygame.KEYDOWN:

                #Arrow key Functionallity
                if event.key == pygame.K_LEFT:
                    control.arrowKey('l')
                if event.key == pygame.K_RIGHT:
                    control.arrowKey('r')
                if event.key == pygame.K_UP:
                    control.arrowKey('u')
                if event.key == pygame.K_DOWN:
                    control.arrowKey('d')

                if event.key == pygame.K_TAB:
                    control.tabKey()

                #Number is pressed
                if event.key >= pygame.K_1 and event.key <= pygame.K_9:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(event.key - 48,True) # K_1 = 49, so for the integer 1, subtract 48 (1 = 49 - 48)
                    else:
                        control.numberKey(event.key - 48,False)
                elif event.key >= pygame.K_KP1 and event.key <= pygame.K_KP9:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(event.key - 256,True) # K_KP1 = 257, so for the integer 1, subtract 48 (1 = 257 - 256)
                    else:
                        control.numberKey(event.key - 256,False)

                #Delete Cell
                if event.key == pygame.K_BACKSPACE:
                    control.backspaceKey()


    print("Sudoku Closed.")
if __name__=='__main__':
    main()
