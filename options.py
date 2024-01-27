import pygame
from pygame.locals import*
import sys
from assets import variables

def options(window):
    clock = pygame.time.Clock()

    item1 = pygame.image.load(variables.background_image1)
    item1 = pygame.transform.scale(item1, variables.size_image)
    item1_rect = item1.get_rect()

    item2 = pygame.image.load(variables.background_image2)
    item2 = pygame.transform.scale(item2, variables.size_image)
    item2_rect = item2.get_rect()

    item3 = pygame.image.load(variables.background_image3)
    item3 = pygame.transform.scale(item3, variables.size_image)
    item3_rect = item3.get_rect()

    item4 = pygame.image.load(variables.background_image4)
    item4 = pygame.transform.scale(item4, variables.size_image)
    item4_rect = item4.get_rect()

    font_style = pygame.font.SysFont("chalkduster",65)
    titulo = font_style.render("Options", True, (variables.purple))

    click = False
    while True:
        # Limit the frame rate to 60 FPS
        clock.tick(60)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                click = True

        if click:
            mouse_pos = pygame.mouse.get_pos()
            if item1_rect.collidepoint(mouse_pos):
                variables.default_image = item1
            elif item2_rect.collidepoint(mouse_pos):
                variables.default_image = item2
            elif item3_rect.collidepoint(mouse_pos):
                variables.default_image = item3
            elif item4_rect.collidepoint(mouse_pos):
                variables.default_image = item4

        background_menu = pygame.image.load(variables.menu_image2)
        background_menu = pygame.transform.scale(background_menu, variables.SIZE)
        window.blit(background_menu, (0, 0))

        window.blit(titulo, (265, 100))

        window.blit(item1, (50, 200))
        window.blit(item2, (210, 200))
        window.blit(item3, (370, 200))
        window.blit(item4, (530, 200))

        pygame.display.flip()

        click = False