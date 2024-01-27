import pygame
from pieces import Piece


def get_pieces(number_pieces):
    list_of_pieces = []
    for i in range(number_pieces):
        list_of_pieces.append(Piece(i))
        
    list_of_pieces[0].position_in_table((277, 365))
    list_of_pieces[1].position_in_table((365, 365))
    list_of_pieces[2].position_in_table((365, 277))
    list_of_pieces[3].position_in_table((277, 277))
            
    return list_of_pieces


    
    