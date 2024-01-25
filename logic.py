import pygame
from assets import variables

def generate_pieces(surface, mouse_pos, get_pieces, create_piece):

    if create_piece and variables.is_piece >= 3:
        get_pieces[variables.is_piece].position_in_table(mouse_pos)
        variables.is_piece += 1
        create_piece = False
            
    if create_piece and variables.is_piece < 3:
        variables.is_piece += 1
        create_piece = False 
        
        
        surface.blit(get_pieces[0].get_circular_surface(), get_pieces[0].get_position_in_table())
            
    if variables.is_piece >= 3:
        for piece in get_pieces:
            surface.blit(piece.get_circular_surface(), piece.get_position_in_table())