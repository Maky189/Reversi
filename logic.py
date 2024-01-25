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
        surface.blit(get_pieces[1].get_circular_surface(), get_pieces[1].get_position_in_table())
        surface.blit(get_pieces[2].get_circular_surface(), get_pieces[2].get_position_in_table())
        surface.blit(get_pieces[3].get_circular_surface(), get_pieces[3].get_position_in_table())
            
    if variables.is_piece >= 3:
        for piece in get_pieces:
            surface.blit(piece.get_circular_surface(), piece.get_position_in_table())
            
    
    #for piece1 in get_pieces:
    #       check_position(piece1.get_position_in_table(), piece2.get_position_in_table(), get_pieces)
            
            
            
            
#def check_position(piece1, piece2, get_pieces):
#    if get_pieces.index(piece2[0]) - 1 == get_pieces.index(piece1[0]) and get_pieces.index(piece2[1]) - 1 == get_pieces.index(piece1[1] - 1):
#       return True
        
    