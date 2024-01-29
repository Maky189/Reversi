import pygame
from pieces import Piece

'''This Function gets the number of the pieces and creates a list of pieces
    to be used in the Logic.py file.'''

def get_pieces(number_pieces):
    list_of_pieces = []
    
    #Creates a piece for each index of the list
    for i in range(number_pieces):
        list_of_pieces.append(Piece(i))
        
    #Sets the position of the 4 inicial pieces    
    list_of_pieces[0].position_in_table((277, 365))
    list_of_pieces[1].position_in_table((365, 365))
    list_of_pieces[2].position_in_table((365, 277))
    list_of_pieces[3].position_in_table((277, 277))
            
    return list_of_pieces


    
    