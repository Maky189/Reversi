#File to store the board of the game and its options

import pygame
from assets import variables
from pieces import Piece
from assets import variables

#Create the grid
file = open('./assets/user.txt', 'a')

class Grid():
    def __init__(self):
        #define the dimension of the square
        self.size = variables.SIZE[0] / 8

    def build(self, surface, mouse_pos, get_pieces, create_piece):
        for i in range(12):
            pygame.draw.line(surface, variables.WHITE, start_pos=(0, i * self.size), end_pos=(variables.SIZE[0], i * self.size), width=5)
            for j in range(12):
                pygame.draw.line(surface, variables.WHITE, start_pos=(j * self.size, 0), end_pos=(j * self.size, variables.SIZE[1]), width=5)

            if create_piece:
                get_pieces[variables.is_piece].position_in_table(mouse_pos)
                variables.is_piece += 1
                create_piece = False
            
            for piece in get_pieces:
                surface.blit(piece.get_circular_surface(), piece.get_position_in_table())
            
        
        
        pygame.display.update()
        
        
        
        
