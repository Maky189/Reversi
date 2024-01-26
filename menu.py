
import pygame
from pygame.locals import*
import sys
from assets import variables




def main_menu(window):
    clock = pygame.time.Clock()

    item1 = pygame.Rect(230, 200, 250, 75)
    item2 = pygame.Rect(230, 300, 250, 75)
    item3 = pygame.Rect(230, 400, 250, 75)
    item4 = pygame.Rect(230, 500, 250, 75)

    font1 = pygame.font.SysFont("chalkduster", 45)
    font_style = pygame.font.SysFont("chalkduster",65)
    titulo = font_style.render("Menu Reversi", True, (variables.purple))

    texto1 = font1.render("PLAY", True, (255, 255, 255))
    texto2 = font1.render("LOAD GAME", True, (255, 255, 255))
    texto3 = font1.render("OPTIONS", True, (255, 255, 255))
    texto4 = font1.render("EXIT", True, (255, 255, 255))

    while True:
        # Limit the frame rate to 60 FPS
        clock.tick(60)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_pos = pygame.mouse.get_pos()
            if(item1.collidepoint(mouse_pos)):
                return True
            elif(item2.collidepoint(mouse_pos)):
                print("Carregandojogo")
            elif(item3.collidepoint(mouse_pos)):
                print("Opcoes")
            elif(item4.collidepoint(mouse_pos)):
                pygame.quit()
                sys.exit()

        background_menu = pygame.image.load(variables.menu_image2)
        background_menu = pygame.transform.scale(background_menu, variables.SIZE)
        window.blit(background_menu, (0, 0))

        window.blit(titulo, (208, 130))

        pygame.draw.rect(window, (214, 0, 79), item1) 
        pygame.draw.rect(window, (214, 0, 79), item2)  
        pygame.draw.rect(window, (214, 0, 79), item3)  
        pygame.draw.rect(window, (214, 0, 79), item4)     

        window.blit(texto1, (315, 225))
        window.blit(texto2, (265, 325))
        window.blit(texto3, (285, 425))
        window.blit(texto4, (315, 525))

        pygame.display.flip()