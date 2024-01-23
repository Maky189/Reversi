
import pygame
from pygame.locals import*
import sys



def main_menu(window): 

    item1 = pygame.Rect(200, 200, 200, 50)
    item2 = pygame.Rect(200, 270, 200, 50)
    item3 = pygame.Rect(200, 340, 200, 50)
    item4 = pygame.Rect(200, 410, 200, 50)

    font_style = pygame.font.SysFont("chalkduster", 30)
    titulo = font_style.render("Menu Reversi", True, (0,0,100))

    texto1 = font_style.render("PLAY", True, (255, 255, 255))
    texto2 = font_style.render("LOAD GAME", True, (255, 255, 255))
    texto3 = font_style.render("OPTIONS", True, (255, 255, 255))
    texto4 = font_style.render("EXIT", True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(event.button == 1):
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
            window.fill((0, 155, 155))
            window.blit(titulo, (230, 150))

            pygame.draw.rect(window, (214, 0, 79), item1) 
            pygame.draw.rect(window, (214, 0, 79), item2)  
            pygame.draw.rect(window, (214, 0, 79), item3)  
            pygame.draw.rect(window, (214, 0, 79), item4)     

            window.blit(texto1, (270, 215))
            window.blit(texto2, (240, 285))
            window.blit(texto3, (250, 355))
            window.blit(texto4, (270, 425))

            pygame.display.flip()








#Code everything into one function to be imported in project
#Have in mind that the function will work inside the main while loop of the game
#In project.py is the place where the function should go
#Only render the menu of the game, begin game will end the work of the function
#That's all for now
