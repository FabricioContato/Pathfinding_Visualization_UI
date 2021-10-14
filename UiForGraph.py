from Matrix import Matrix
import pygame

pygame.init()



clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

matrix = Matrix((800,600),50,50)
#matrix.random_unaccessible_cells()
aux = 0
while(True):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and aux == 0:
            matrix.cell_click_check_for_end()
            aux = 1
        elif event.type == pygame.MOUSEBUTTONDOWN and aux == 1:
            matrix.cell_click_check_for_start()
            aux = 2
        elif event.type == pygame.MOUSEBUTTONDOWN and aux > 1:
            matrix.cell_click_check_for_unaccessible()

        screen.blit(matrix.getSprite(),(0,0))
        pygame.display.flip()

#while(True):
   # clock.tick(30)
   # for event in pygame.event.get():
	#if event.type == pygame.QUIT:
	    #pygame.quit()
	    #break
    # ui.run()
    #pygame.display.flip()
