import pygame
import grid
import const


def main():
    #Test Code



    print("Running!")
    #Constructing Screen
    global screen
    screen = pygame.display.set_mode((const.WINDOWWIDTH+1, const.WINDOWHEIGHT+1))
    pygame.display.set_caption('Sudoku')

    #Fill in Screen
    #screen.fill(const.WHITE)
    #grid.drawGrid(screen)
    playboard = grid.GridController()
    playboard.render(screen)

    #Display contents of screen
    pygame.display.flip()

    #Sidebar, implement later
    #game_surf = pygame.surface.Surface(((2*const.WINDOWWIDTH)+1, const.WINDOWHEIGHT+1))


    running = True #Variable for gameloop
    while running: #Main Loop
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Selecting Cells w/ mouse
            elif event.type == pygame.MOUSEBUTTONUP:
                playboard.selectCell(pygame.mouse.get_pos(),screen)
                playboard.writeNumber(screen,playboard.returnNumber(),const.BLUE)

            elif event.type == pygame.KEYDOWN:

                #Arrow key Functionallity
                if event.key == pygame.K_LEFT and playboard.isSelected():
                    playboard.moveSelected('l',screen)
                    playboard.writeNumber(screen,playboard.returnNumber())
                if event.key == pygame.K_RIGHT and playboard.isSelected():
                    playboard.moveSelected('r',screen)
                    playboard.writeNumber(screen,playboard.returnNumber())
                if event.key == pygame.K_UP and playboard.isSelected():
                    playboard.moveSelected('u',screen)
                    playboard.writeNumber(screen,playboard.returnNumber())
                if event.key == pygame.K_DOWN and playboard.isSelected():
                    playboard.moveSelected('d',screen)
                    playboard.writeNumber(screen,playboard.returnNumber())

                #add Shift click functionallity for notes here


                #Number Input
                if event.key == pygame.K_1:
                    playboard.writeNumber(screen,1)
                    playboard.saveNumber(1)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_2:
                    playboard.writeNumber(screen,2)
                    playboard.saveNumber(2)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_3:
                    playboard.writeNumber(screen,3)
                    playboard.saveNumber(3)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_4:
                    playboard.writeNumber(screen,4)
                    playboard.saveNumber(4)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_5:
                    playboard.writeNumber(screen,5)
                    playboard.saveNumber(5)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_6:
                    playboard.writeNumber(screen,6)
                    playboard.saveNumber(6)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_7:
                    playboard.writeNumber(screen,7)
                    playboard.saveNumber(7)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_8:
                    playboard.writeNumber(screen,8)
                    playboard.saveNumber(8)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)
                if event.key == pygame.K_9:
                    playboard.writeNumber(screen,9)
                    playboard.saveNumber(9)
                    playboard.checkCRB()
                    playboard.highlightDuplicates(screen)

                #Delete Cell
                if event.key == pygame.K_BACKSPACE:
                    playboard.eraseNumberGrid(screen)
                    print(playboard.gridArray[playboard.returnSelected(0)][playboard.returnSelected(1)].returnIfAny())
                    if(playboard.gridArray[playboard.returnSelected(0)][playboard.returnSelected(1)].returnIfAny()):
                        playboard.checkCRB()
                    playboard.eraseNumberArray()

                    playboard.highlightDuplicates(screen)
    print("Sudoku Closed.")
if __name__=='__main__':
    main()
