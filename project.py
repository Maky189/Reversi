import pygame
import sys
from assets import variables
from board import Grid
from data import get_pieces
from menu import main_menu
from options import options

'''
    This Python implementation of the classic board game Reversi (also known as Othello). 
    The game is played on an 8x8 grid, with two players taking turns placing black and white pieces. 
    The goal of the game is to have more of your color pieces showing when the game ends.
'''
    
    
#Principal Function:   
def main():
    
    #Begins Pygame and give title to screen
    pygame.init()
    pygame.display.set_caption("Reversi")

    #set the window and the clock(fps) of game
    window = pygame.display.set_mode(variables.SIZE)
    clock = pygame.time.Clock()
    
    #Gets the List of pieces
    lista_pecas = get_pieces(64)

    #Render the Menu and checks for the output of it in order to render the game
    image = None
    while not(image := main_menu(window)):
        pass
    render_window(window, lista_pecas, image)
        
    #Get out of pygame after everything
    pygame.quit()
    
#Function of render the window
def render_window(window, get_pieces, image):
    
    #sets the variables that will be used in the loop
    mouse_pos = None
    create_piece = False
    
    #Start main loop to run game
    while True:
        # Get all the events in the event queue
        events = pygame.event.get()

        # Check each event
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Checks for click of the mouse to start creating pieces
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                create_piece = True
                
                # Render the main game
                render_main_game(window, mouse_pos, get_pieces, create_piece, image)
        
#Function to render the main game
def render_main_game(window, mouse_pos, get_pieces, create_piece, image):
    
    #set the background
    background = pygame.image.load(image)
    background = pygame.transform.scale(background, variables.SIZE)
    window.blit(background, (0, 0))
    
    #render the grid
    Grid().build(window, mouse_pos, get_pieces, create_piece)
    
if __name__ == "__main__":
    main()