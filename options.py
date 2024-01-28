import pygame
from pygame.locals import*
import sys
from assets import variables

def options(window):
    clock = pygame.time.Clock()

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

    item5 = pygame.image.load(variables.back_icone)
    item5 = pygame.transform.scale(item5, variables.size_image)
    item5_rect = item5.get_rect(topleft = (500, 500)) # changed position of item5

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
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
                    return False

        background_menu = pygame.image.load(variables.menu_image2)
        background_menu = pygame.transform.scale(background_menu, variables.SIZE)
        window.blit(background_menu, (0, 0))

        window.blit(item1, item1_rect)
        window.blit(item2, item2_rect)
        window.blit(item3, item3_rect)
        window.blit(item4, item4_rect)
        window.blit(item5, item5_rect)

        pygame.display.flip()