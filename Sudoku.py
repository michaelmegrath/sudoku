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


                #Number Input
                if event.key == pygame.K_1:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(1,True)
                    else:
                        control.numberKey(1,False)
                if event.key == pygame.K_2:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(2,True)
                    else:
                        control.numberKey(2,False)
                if event.key == pygame.K_3:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(3,True)
                    else:
                        control.numberKey(3,False)
                if event.key == pygame.K_4:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(4,True)
                    else:
                        control.numberKey(4,False)
                if event.key == pygame.K_5:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(5,True)
                    else:
                        control.numberKey(5,False)
                if event.key == pygame.K_6:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(6,True)
                    else:
                        control.numberKey(6,False)
                if event.key == pygame.K_7:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(7,True)
                    else:
                        control.numberKey(7,False)
                if event.key == pygame.K_8:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(8,True)
                    else:
                        control.numberKey(8,False)
                if event.key == pygame.K_9:
                    if(pygame.key.get_mods() & pygame.KMOD_SHIFT or pygame.key.get_mods() & pygame.KMOD_CAPS):
                        control.numberKey(9,True)
                    else:
                        control.numberKey(9,False)

                #Delete Cell
                if event.key == pygame.K_BACKSPACE:
                    control.backspaceKey()


    print("Sudoku Closed.")
if __name__=='__main__':
    main()
