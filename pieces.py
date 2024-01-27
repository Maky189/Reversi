import pygame
from assets import variables

class Piece:
    def __init__(self, piece):
        self.size = 60
        self.get_piece(piece)
        self.position = None
        
    def get_circular_surface(self):
        # Create a circular surface
        circular_image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(circular_image, self._color, (self.size // 2, self.size // 2), self.size // 2)
        return circular_image
    
    def position_in_table(self, mouse_pos):
        self.position = mouse_pos
    
    def get_piece(self, number_pieces):
        if number_pieces % 2 == 0:
            self._color = variables.WHITE
        else:
            self._color = variables.BLACK
        
    def get_position_in_table(self):
        return self.position
    
    def is_color(self):
        if self._color == variables.WHITE:
            self._color = variables.BLACK
        else:
            self._color = variables.WHITE
            
    def color(self):
        return self._color
