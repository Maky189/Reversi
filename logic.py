import pygame
from assets import variables

def generate_pieces(surface, mouse_pos, get_pieces, create_piece):

    if create_piece and variables.is_piece >= 3:
        get_pieces[variables.is_piece].position_in_table(mouse_pos)
        if set_position(get_pieces[variables.is_piece].get_position_in_table(), get_pieces):
        #check color
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
            
    
def set_position(position1, get_pieces):
    for piece in get_pieces[0 : variables.is_piece + 1]:
            #in x
        x_piece = variables.position.index(position1[0])
        x_reference = variables.position.index(piece.get_position_in_table()[0])
            
            #in y
        y_piece = variables.position.index(position1[1])
        y_reference = variables.position.index(piece.get_position_in_table()[1])
            
        if (x_reference + 1 == x_piece or x_reference - 1 == x_piece) and (y_reference + 1 == y_piece or y_reference - 1 == y_piece):
            return True
        
