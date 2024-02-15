#File to store the board of the game and its options

import pygame
from assets import variables
from pieces import Piece
from assets import variables
from logic import generate_pieces

#Create the grid
file = open('./assets/user.txt', 'a')

def grid(surface, mouse_pos, get_pieces, create_piece):
    size = variables.SIZE[0] / 8
    #Draws a line in x and in y of the screen
    for i in range(12):
        pygame.draw.line(surface, variables.BLACK, start_pos=(0, i * size), end_pos=(variables.SIZE[0], i * size), width=5)
        for j in range(12):
            pygame.draw.line(surface, variables.BLACK, start_pos=(j * size, 0), end_pos=(j * size, variables.SIZE[1]), width=5)

        #Call the function to generate the pieces in the grid
    generate_pieces(surface, mouse_pos, get_pieces, create_piece)
        
    pygame.display.update()
        
        
        
        
