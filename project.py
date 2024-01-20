import pygame
import sys
from assets import variables
from board import Grid
from pieces import Piece

#Principal function
def main():
    #Begin Pygame and give title to screen
    pygame.init()
    pygame.display.set_caption("Reversi")
    
    #set the window and the clock(fps) of game
    window = pygame.display.set_mode(variables.SIZE)
    clock = pygame.time.Clock()
    
    #Call function
    render_window(window)
    clock.tick(60)
    
    #Get out of pygame after everything
    pygame.quit()
    
#Function of render the window
def render_window(window):
    mouse_pos = (15, 15)
    #Start main loop to run game
    while True:
        #Check for the user to click the exit button to get out of loop (game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
        
        render_main_game(window, mouse_pos)
        
#Function to render the main game
def render_main_game(window, mouse_pos):
    
    #set the background
    background = pygame.image.load(variables.background_image4)
    background = pygame.transform.scale(background, variables.SIZE)
    window.blit(background, (0, 0))
    #render the grid
    Grid().build(window, mouse_pos)

def position_pieces(window):
    peca = Piece(variables.BLACK)
    window.blit(peca.get_circular_surface(60), (460, 15))
    
if __name__ == "__main__":
    main()