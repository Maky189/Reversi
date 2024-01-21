#File to store the board of the game and its options

import pygame
from assets import variables
from pieces import Piece

#Create the grid
file = open('./assets/user.txt', 'a')


class Grid:
    def __init__(self):
        #define the dimension of the square
        self.size = variables.SIZE[0] / 8
        self.store_pieces = []

        #loops over horizontaly in 12
    
    def build(self, surface, mouse_pos, piece):
        for i in range(12):
            pygame.draw.line(surface, variables.WHITE, start_pos=(0, i * self.size), end_pos=(variables.SIZE[0], i * self.size), width=5)
            for j in range(12):
                pygame.draw.line(surface, variables.WHITE, start_pos=(j * self.size, 0), end_pos=(j * self.size, variables.SIZE[1]), width=5)
        
        now = Piece(piece)        
        self.store_pieces.append({"piece": now, "position": now.position_in_table(mouse_pos)})
        
        for dictionary in self.store_pieces:
            surface.blit(dictionary.get("piece").get_circular_surface(), dictionary.get("position"))      
                
        pygame.display.update()
        
        
