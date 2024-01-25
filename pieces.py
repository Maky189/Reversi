import pygame
from assets import variables

class Piece:
    def __init__(self, piece):
        self.size = 60
        self.get_piece(piece)
        self.position = (277, 277)
        
    def get_circular_surface(self):
        # Create a circular surface
        circular_image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(circular_image, self.color, (self.size // 2, self.size // 2), self.size // 2)
        return circular_image
    
    def position_in_table(self, mouse_pos):
        x, y =  mouse_pos 
        position = variables.position
        
        for i in range(len(position) - 1):
            if x in range(position[i], position[i + 1]):
                x = position[i]
                
        for j in range(len(position) - 1):
            if y in range(position[j], position[j + 1]):
                y = position[j]
                
        self.position = (x, y)
    
    def get_piece(self, number_pieces):
        if number_pieces % 2 == 0:
            self.color = variables.WHITE
        else:
            self.color = variables.BLACK
        
    def get_position_in_table(self):
        return self.position
    
    def is_color(self):
        if self.color == variables.WHITE:
            self.color = variables.BLACK
        else:
            self.color = variables.WHITE
