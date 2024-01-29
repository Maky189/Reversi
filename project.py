import pygame
import sys
from assets import variables
from board import Grid
from data import get_pieces
from menu import main_menu
from options import options

'''This Python implementation of the classic board game Reversi (also known as Othello). 
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

    #Render the Menu and checks for the output of it, leading to each part of the program:
    while main_menu(window) == 0:
        pass
    if main_menu(window) == 1:
        image = variables.default_image
        
        #Render the main game:
        render_window(window, lista_pecas, image)
        clock.tick(60)
        
    elif main_menu(window) == 3:
        
        #Render the options if the user choses to go there, and checks for its output:
        image = options(window)
        if image:
            render_window(window, lista_pecas, image)
        else:
            render_window(window, lista_pecas, variables.default_image)
        

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