import pygame
from pieces import Piece


def get_pieces(number_pieces):
    list_of_pieces = []
    for i in range(number_pieces):
        list_of_pieces.append(Piece(i))    
    return list_of_pieces
    
    