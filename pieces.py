import pygame
from assets import variables

'''This is the class of the Pieces, where it creates each instance of it'''

class Piece:
    
    #The inicialization of the class
    def __init__(self, piece):
        self.size = 60
        self.get_piece(piece)
        self.position = None
    
    #Method to define and return the circular shape of the piece as a surface
    def get_circular_surface(self):
        circular_image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.circle(circular_image, self._color, (self.size // 2, self.size // 2), self.size // 2)
        return circular_image
    
    #Sets the position of the piece acordingly to the mouse
    def position_in_table(self, mouse_pos):
        self.position = mouse_pos
    
    #Gets the color of the piece based if it is even or odd
    def get_piece(self, number_pieces):
        if number_pieces % 2 == 0:
            self._color = variables.WHITE
        else:
            self._color = variables.BLACK
            
    #Method to just return the position of the piece
    def get_position_in_table(self):
        return self.position
    
    #Method to change the color of the piece
    def is_color(self):
        if self._color == variables.WHITE:
            self._color = variables.BLACK
        else:
            self._color = variables.WHITE
            
    #Just returns the color of the piece
    def color(self):
        return self._color
