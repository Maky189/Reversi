#File to store the board of the game and its options

import pygame
from assets import variables
from pieces import Piece

#Create the grid
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

        # Check if the mouse position is within the grid boundaries
        if self.position_in_table(mouse_pos):
            x, y = self.position_in_table(mouse_pos)
            # Create a new piece and add it to the grid
            piece = self.get_piece(piece)
            self.store_pieces.append({"piece": piece, "position": (x, y)})

        for dict in self.store_pieces:
            piece_value = dict.get("piece")
            surface.blit(piece_value.get_circular_surface(60), dict.get("position"))

        pygame.display.update()
        
    def position_in_table(self, mouse_pos):
        x, y =  mouse_pos 
        position = [15, 103, 190, 277, 365, 451, 539, 627, 700]
        
        for i in range(len(position) - 1):
            if x in range(position[i], position[i + 1]):
                x = position[i]
                
        for j in range(len(position) - 1):
            if y in range(position[j], position[j + 1]):
                y = position[j]
                
        return (x, y)

    def get_piece(self, piece):
        if piece % 2 == 0:
            piece = Piece(variables.WHITE)
        else:
            piece = Piece(variables.BLACK)
            
        return piece
            
        
        
