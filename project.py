import pygame
import sys
from assets import variables
from board import Grid
from data import get_pieces

#Principal function
def main():
    #Begin Pygame and give title to screen
    pygame.init()
    pygame.display.set_caption("Reversi")
    
    #set the window and the clock(fps) of game
    window = pygame.display.set_mode(variables.SIZE)
    clock = pygame.time.Clock()
    lista_pecas = get_pieces(64)
    
    #Call functions
    #Render Menu (Leo):
    ...
    
    #Render the main game:
    render_window(window, lista_pecas)
    clock.tick(60)
    
    #Get out of pygame after everything
    pygame.quit()
    
#Function of render the window
def render_window(window, get_pieces):
    mouse_pos = (277, 277)
    #Start main loop to run game
    while True:
        #Check for the user to click the exit button to get out of loop (game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
        render_main_game(window, mouse_pos, get_pieces)
        
#Function to render the main game
def render_main_game(window, mouse_pos, get_pieces):
    
    #set the background
    background = pygame.image.load(variables.background_image4)
    background = pygame.transform.scale(background, variables.SIZE)
    window.blit(background, (0, 0))
    #render the grid
    Grid().build(window, mouse_pos, get_pieces)
    
if __name__ == "__main__":
    main()