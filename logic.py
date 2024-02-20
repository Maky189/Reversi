import pygame
import sys
from assets import variables

'''Function that generates the pieces in the grid and handles the logic behind the game'''

def generate_pieces(surface, mouse_pos, get_pieces, create_piece):

    #Checks if there is the 4 pieces in the grid, if they are, start creating new pieces where the user wants
    if create_piece and variables.is_piece > 3:
        
        if set_position(set_position_in_table(mouse_pos), get_pieces):
            get_pieces[variables.is_piece].position_in_table(set_position_in_table(mouse_pos))
        #check color
            variables.is_piece += 1
        create_piece = False
        
        if variables.is_piece == 64:
            
            you_win(surface, variables.is_piece, get_pieces)
            
            
    #Starts by placing the 4 inicial pieces in the board and increments pieces variable
    if create_piece and variables.is_piece <= 3:
        variables.is_piece += 1
        create_piece = False 
        
        for i in range(3):
            surface.blit(get_pieces[i].get_circular_surface(), get_pieces[i].get_position_in_table())
    
    #blits the created pieces in the screen         
    if variables.is_piece >= 3:
        for piece in get_pieces:
            if not(piece.get_position_in_table() == None):
                surface.blit(piece.get_circular_surface(), piece.get_position_in_table())
            

#This function checks if is a valid position and changes a piece color based on where the user played
def set_position(position1, get_pieces):
    
    for pieces in get_pieces:
        if not(pieces.get_position_in_table() == None) and position1 == pieces.get_position_in_table():
            return False
    
    #Iterates over all the pieces in the moment and then checks if is a position in x , y or diagonal
    for piece in get_pieces[0 : variables.is_piece]:
        
        if not(piece.get_position_in_table() == None):
            x_piece = variables.position.index(position1[0])
            x_reference = variables.position.index(piece.get_position_in_table()[0])
                
            
            y_piece = variables.position.index(position1[1])
            y_reference = variables.position.index(piece.get_position_in_table()[1])
            
            #in x    
            if x_reference == x_piece:
                if (y_reference + 1 == y_piece) or (y_reference - 1 == y_piece):
                       if piece.color() != get_pieces[variables.is_piece].color():
                           
                            for other in get_pieces[0:variables.is_piece]:
                                if other.get_position_in_table() != None:
                                    
                                    x = other.get_position_in_table()[0]
                                    y = other.get_position_in_table()[1]
                                    
                                    if x == piece.get_position_in_table()[0]:
                                        if y in variables.position[(y_reference + 1): ] or y in variables.position[0:y_reference]:
                                            if other.color() != piece.color():
                                                piece.is_color()
                                                return True

            #in y
            elif y_reference == y_piece:
                if (x_reference + 1 == x_piece) or (x_reference - 1 == x_piece):
                    if not(piece.color == get_pieces[variables.is_piece].color()):
                        if piece.color() != get_pieces[variables.is_piece].color():
                            
                            for other in get_pieces[0:variables.is_piece]:
                                if other.get_position_in_table() != None:
                                    
                                    x = other.get_position_in_table()[0]
                                    y = other.get_position_in_table()[1]
                                    
                                    if y == piece.get_position_in_table()[1]:
                                        if x in variables.position[(x_reference + 1): ] or x in variables.position[0:x_reference]:
                                            if other.color() != piece.color():
                                                piece.is_color()
                                                return True
                            
            
            #diagonal1
            elif (x_reference - 1 == x_piece) and (y_reference - 1 == y_piece):
                if not(piece.color() == get_pieces[variables.is_piece].color()):
                    if piece.color() != get_pieces[variables.is_piece].color():
                        place = 1
                        
                        for other in get_pieces[0: variables.is_piece]:
                            if other.get_position_in_table() != None:
                                
                                if diagonal(piece, other, get_pieces, place):
                                    piece.is_color()
                                    return True
            
            #diagonal2
            elif (x_reference + 1 == x_piece) and (y_reference - 1 == y_piece):
                if not(piece.color() == get_pieces[variables.is_piece].color()):
                    if piece.color() != get_pieces[variables.is_piece].color():
                        place = 2
                        
                        for other in get_pieces[0: variables.is_piece]:
                            if other.get_position_in_table() != None:
                                
                                if diagonal(piece, other, get_pieces, place):           
                                    piece.is_color()
                                    return True
            
            #diagonal3
            elif (x_reference - 1 == x_piece) and (y_reference + 1 == y_piece):
                if not(piece.color() == get_pieces[variables.is_piece].color()):
                    if piece.color() != get_pieces[variables.is_piece].color():
                        place = 3

                        for other in get_pieces[0: variables.is_piece]:
                            if other.get_position_in_table() != None:
                                
                                if diagonal(piece, other, get_pieces, place):
                    
                                    piece.is_color()
                                    return True
            
            #diagonal4
            elif (x_reference + 1 == x_piece) and (y_reference + 1 == y_piece):
                
                if not(piece.color() == get_pieces[variables.is_piece].color()):
                    if piece.color() != get_pieces[variables.is_piece].color():
                        place = 4
                        
                        for other in get_pieces[0: variables.is_piece]:
                            if other.get_position_in_table() != None:
                                
                                if diagonal(piece, other, get_pieces, place):
                                    piece.is_color()
                                    return True
                
def diagonal(piece, other, get_pieces, place):
    x1, y1 = other.get_position_in_table()
    x1 = variables.position.index(x1)
    y1 = variables.position.index(y1)
    match place:
        case 1:
            x2, y2 = piece.get_position_in_table()
            x2 = variables.position.index(x2)
            y2 = variables.position.index(y2)
            
            if (x2 - 1 == x1) and (y2 - 1 == y1):
                if other.color() != piece.color():
                    return True
                else:
                    for new in get_pieces[0: variables.is_piece]:
                        if new.get_position_in_table() != None:
                            if diagonal(other, new, get_pieces, 1):
                                other.is_color()
                    return False
        
        case 2:
            x2, y2 = piece.get_position_in_table()
            x2 = variables.position.index(x2)
            y2 = variables.position.index(y2)
            
            if (x2 - 1 == x1) and (y2 - 1 == y1):
                if other.color() != piece.color():
                    return True
                else:
                    for new in get_pieces[0: variables.is_piece]:
                        if new.get_position_in_table() != None:
                            if diagonal(other, new, get_pieces, 2):
                                other.is_color()
                    return False
                
                            
        case 3:
            x2, y2 = piece.get_position_in_table()
            x2 = variables.position.index(x2)
            y2 = variables.position.index(y2)
            
            if (x2 - 1 == x1) and (y2 - 1 == y1):
                if other.color() != piece.color():
                    return True
                else:
                    for new in get_pieces[0: variables.is_piece]:
                        if new.get_position_in_table() != None:
                            if diagonal(other, new, get_pieces, 3):
                                other.is_color()
                    return False
                
        
        case 4:
            x2, y2 = piece.get_position_in_table()
            x2 = variables.position.index(x2)
            y2 = variables.position.index(y2)
            
            if (x2 - 1 == x1) and (y2 - 1 == y1):
                if other.color() != piece.color():
                    return True
                else:
                    for new in get_pieces[0: variables.is_piece]:
                        if new.get_position_in_table() != None:
                            if diagonal(other, new, get_pieces, 4):
                                other.is_color()
                    return False
    
                    
#Function to convert the position of the mouse to a valid position oin the grid
def set_position_in_table(mouse_pos):
    x, y =  mouse_pos 
    position = variables.position
        
    for i in range(len(position) - 1):
        if x in range(position[i], position[i + 1]):
            x = position[i]
                
    for j in range(len(position) - 1):
        if y in range(position[j], position[j + 1]):
            y = position[j]
                
    return (x, y)

#Function to check if the user won, and display the winner       
def you_win(surface, n, get_pieces):
    font = pygame.font.Font(None, 36)
    
    white = 0
    black = 0
    
    for piece in get_pieces:
        if piece.color() == variables.WHITE:
            white += 1
        else:
            black += 1
    
    if black > white:
        text = "Black Wins"
    else:
        text = "White Wins"
    
    text = font.render(text, True, variables.BLUE_GREEN)
    text_rect = text.get_rect(center=(variables.SIZE[0] // 2, variables.SIZE[1] // 2))
    surface.blit(text, text_rect)
    
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT():
            pygame.quit()
            sys.exit("End")
            
    pygame.display.flip()
    