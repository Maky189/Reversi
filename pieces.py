import pygame

class Piece:
    def __init__(self, color):
        self.color = color

    def get_circular_surface(self, size):
        # Create a circular surface
        circular_image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(circular_image, self.color, (size // 2, size // 2), size // 2)
        return circular_image
