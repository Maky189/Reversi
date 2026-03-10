import pygame
import sys
from assets import variables

'''Function that generates the pieces in the grid and handles the logic behind the game'''

def generate_pieces(surface, mouse_pos, get_pieces, create_piece):

    #Checks if there is the 4 pieces in the grid, if they are, start creating new pieces where the user wants
    if create_piece and variables.is_piece > 3:
        if set_position(set_position_in_table(mouse_pos), get_pieces):
            get_pieces[variables.is_piece].position_in_table(set_position_in_table(mouse_pos))
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


# Helper: return the piece at board coordinates (x_idx, y_idx) or None
def _piece_at(get_pieces, x_idx, y_idx):
    coord = (variables.position[x_idx], variables.position[y_idx])
    for p in get_pieces:
        if p.get_position_in_table() == coord:
            return p
    return None


#This function checks if is a valid position and flips pieces based on where the user played
def set_position(position1, get_pieces):
    # position1 is (x, y) already snapped to table positions
    # Can't place on an occupied square
    for pieces in get_pieces:
        if not(pieces.get_position_in_table() == None) and position1 == pieces.get_position_in_table():
            return False

    try:
        x_idx = variables.position.index(position1[0])
        y_idx = variables.position.index(position1[1])
    except ValueError:
        # click outside grid
        return False

    player_color = get_pieces[variables.is_piece].color()
    opponent_color = variables.BLACK if player_color == variables.WHITE else variables.WHITE

    flipped_any = False

    # directions: 8 neighbors
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx = x_idx + dx
        ny = y_idx + dy
        pieces_to_flip = []

        # first neighbor must be opponent
        if nx < 0 or nx > 7 or ny < 0 or ny > 7:
            continue

        neighbor = _piece_at(get_pieces, nx, ny)
        if neighbor is None or neighbor.color() != opponent_color:
            continue

        # walk along the direction
        while 0 <= nx <= 7 and 0 <= ny <= 7:
            current = _piece_at(get_pieces, nx, ny)
            if current is None:
                # reached empty square -> no capture in this direction
                pieces_to_flip = []
                break
            if current.color() == player_color:
                # bounded by player's piece -> flip collected
                break
            # otherwise it's opponent piece -> collect
            pieces_to_flip.append(current)
            nx += dx
            ny += dy

        # check final bounding piece
        if 0 <= nx <= 7 and 0 <= ny <= 7:
            bounding = _piece_at(get_pieces, nx, ny)
            if bounding is not None and bounding.color() == player_color and len(pieces_to_flip) > 0:
                # flip them
                for p in pieces_to_flip:
                    p.is_color()
                flipped_any = True

    return flipped_any


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
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit("End")

    pygame.display.flip()
