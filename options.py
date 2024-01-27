
import pygame
from pygame.locals import*
import sys
from assets import variables




def options(window):
    clock = pygame.time.Clock()

    item1 = pygame.image.load(variables.background_image1)
    item1 = pygame.transform.scale(item1, variables.size_image)
    
    item2 = pygame.image.load(variables.background_image2)
    item2 = pygame.transform.scale(item2, variables.size_image)
    
    item3 = pygame.image.load(variables.background_image3)
    item3 = pygame.transform.scale(item3, variables.size_image)
    
    item4 = pygame.image.load(variables.background_image4)
    item4 = pygame.transform.scale(item4, variables.size_image)
    
    

    font1 = pygame.font.SysFont("chalkduster", 45)
    font_style = pygame.font.SysFont("chalkduster",65)
    titulo = font_style.render("Options", True, (variables.purple))

    while True:
        # Limit the frame rate to 60 FPS
        clock.tick(60)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                click = True

        if click == True:
            mouse_pos = pygame.mouse.get_pos()
            if(item1.):
                variables.default_image = item1
            elif(item2.collidepoint(mouse_pos)):
                variables.default_image = item2
            elif(item3.collidepoint(mouse_pos)):
                variables.default_image = item3
            elif(item4.collidepoint(mouse_pos)):
                variables.default_image = item4

        background_menu = pygame.image.load(variables.menu_image2)
        background_menu = pygame.transform.scale(background_menu, variables.SIZE)
        window.blit(background_menu, (0, 0))

        window.blit(titulo, (208, 130))

        window.blit(item1, (315, 225))
        window.blit(item2, (265, 325))
        window.blit(item3, (285, 425))
        window.blit(item4, (315, 525))

        pygame.display.flip()