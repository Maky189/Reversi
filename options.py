import pygame
from pygame.locals import *
import sys
from assets import variables

'''
    This is the options file, where  we can change the background of the board.
'''

def options(window):
    clock = pygame.time.Clock()

    #Load the images and get a rectangle for them
    item1 = pygame.image.load(variables.background_image1)
    item1 = pygame.transform.scale(item1, variables.size_image)
    item1_rect = item1.get_rect(topleft = (50, 200))

    item2 = pygame.image.load(variables.background_image2)
    item2 = pygame.transform.scale(item2, variables.size_image)
    item2_rect = item2.get_rect(topleft = (210, 200))

    item3 = pygame.image.load(variables.background_image3)
    item3 = pygame.transform.scale(item3, variables.size_image)
    item3_rect = item3.get_rect(topleft = (370, 200))

    item4 = pygame.image.load(variables.background_image4)
    item4 = pygame.transform.scale(item4, variables.size_image)
    item4_rect = item4.get_rect(topleft = (530, 200))
    
    item5 = pygame.image.load(variables.background_image5)
    item5 = pygame.transform.scale(item5, variables.size_image)
    item5_rect = item5.get_rect(topleft = (50, 365))
    
    item6 = pygame.image.load(variables.background_image6)
    item6 = pygame.transform.scale(item6, variables.size_image)
    item6_rect = item6.get_rect(topleft = (210, 365))
    
    item7 = pygame.image.load(variables.background_image7)
    item7 = pygame.transform.scale(item7, variables.size_image)
    item7_rect = item7.get_rect(topleft = (370, 365))
    
    item8 = pygame.image.load(variables.background_image8)
    item8 = pygame.transform.scale(item8, variables.size_image)
    item8_rect = item8.get_rect(topleft = (530, 365))

    #This item is the go back icon
    item9 = pygame.image.load(variables.back_icone)
    item9 = pygame.transform.scale(item9, variables.size_image)
    item9_rect = item9.get_rect(topleft = (500, 500)) # changed position of item5

    while True:
        
        # to limit the fps at 60
        
        clock.tick(60)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
                
            #Mouse click to change the background of the game
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_pos = pygame.mouse.get_pos()
                if item1_rect.collidepoint(mouse_pos):
                    return variables.background_image1
                elif item2_rect.collidepoint(mouse_pos):
                    return variables.background_image2
                elif item3_rect.collidepoint(mouse_pos):
                    return variables.background_image3
                elif item4_rect.collidepoint(mouse_pos):
                    return variables.background_image4
                elif item5_rect.collidepoint(mouse_pos):
                    return variables.background_image5
                elif item6_rect.collidepoint(mouse_pos):
                    return variables.background_image6
                elif item7_rect.collidepoint(mouse_pos):
                    return variables.background_image7
                elif item8_rect.collidepoint(mouse_pos):
                    return variables.background_image8
                elif item9_rect.collidepoint(mouse_pos):
                    return False

        # options background
        
        background = pygame.image.load(variables.menu_image2)
        background = pygame.transform.scale(background, variables.SIZE)
        window.blit(background, (0, 0))

        #render everything
        
        window.blit(item1, item1_rect)
        window.blit(item2, item2_rect)
        window.blit(item3, item3_rect)
        window.blit(item4, item4_rect)
        window.blit(item5, item5_rect)
        window.blit(item6, item6_rect)
        window.blit(item7, item7_rect)
        window.blit(item8, item8_rect)
        window.blit(item9, item9_rect)

        pygame.display.flip()