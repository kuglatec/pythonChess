import numpy as np
from score_eval import get_num_of_own_pieces, get_score
from copy import deepcopy
def move_bishop(position, destination, pieces):
    pieces = deepcopy(pieces)
    way=[]
    direction = 10
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
    
    moving_piece = ''    
    for piece in pieces:
        if pieces[piece]['position'] == position:
            moving_piece = piece
    
    if moving_piece == '':
        pieces = {}
        return {'valid': False, 'error': 'This move is invalid since there is no piece at ' + position}

    if str(position) == str(destination):
        return {'valid': False, 'error': 'You have to move a piece'}
    
    
    if x_dest > x_pos and y_dest > y_pos and np.abs(x_dest - x_pos) == np.abs(y_dest - y_pos):
        direction = 0


    elif x_dest < x_pos and y_dest < y_pos and np.abs(x_dest - x_pos) == np.abs(y_dest - y_pos):
        ###print('2')
        direction = 1

    elif x_dest < x_pos and y_dest > y_pos and np.abs(x_dest - x_pos) == np.abs(y_dest - y_pos):
        ###print('2')
        direction = 2

    elif x_dest > x_pos and y_dest < y_pos and np.abs(x_dest - x_pos) == np.abs(y_dest - y_pos):
        ###print('3')
        direction = 3

    elif direction == 10:
        return {'valid': False, 'error': 'The bishop cant move like that'}

    if direction == 0:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field + 1
            y_field = y_field + 1

    elif direction == 1:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field - 1
            y_field = y_field - 1

    elif direction == 2:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field - 1
            y_field = y_field + 1


    elif direction == 3:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field + 1
            y_field = y_field - 1


    elif direction == 4:
        ###print("DIR IS 0") debugging
        if int(position[0]) < int(destination[0]):
            for i in range(int(position[0]), int(destination[0])):
                way.append(str(i) + str(position[1]))

        elif int(destination[0]) < int(position[0]):
            for i in range(int(destination[0]), int(position[0])):
                way.append(str(i) + str(position[1]))

    
    elif direction == 5:
        ###print("DIR IS 1") debugging 
        
        if int(position[1]) < int(destination[1]):
            for i in range(int(position[1]), int(destination[1])):
                way.append(str(position[0]) + str(i))

        elif int(destination[1]) < int(position[1]):
            for i in range(int(destination[1]), int(position[1])):
                way.append(str(position[0]) + str(i))

    way.append(destination)
    piece_in_way = ''
    pieces_in_way = []
    in_way = False
    for f in way:
        for p in pieces:
            if pieces[p]['position'] == f and p != moving_piece and pieces[p]['alive'] == True:
                pieces_in_way.append(p)
                in_way = True

    if in_way == True:
        if pieces[pieces_in_way[0]]['owner'] == 0:
             return {'valid': False, 'error': 'Invalid move! Own piece is blocking the way'}
        
        elif pieces[pieces_in_way[0]]['owner'] == 1:
            piece_in_way =  pieces_in_way[0]
    
    if piece_in_way != '':
            pieces[moving_piece]['position'] = pieces[piece_in_way]['position']
            pieces[piece_in_way]['alive'] = False

    if in_way == False:
        pieces[moving_piece]['position'] = destination
    
    
    
    num_of_own_pieces = get_num_of_own_pieces(pieces)
    ret = deepcopy(pieces)
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    #
 #   if in_way == True:
  #      pieces[piece_in_way]['alive'] = True

    return {'valid': True, 'score': score, 'ret': ret}


def move_king(position, destination, pieces):
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
    pieces = deepcopy(pieces)
    for piece in pieces:
        moving_piece = ''
        if position == pieces[piece]['position']:
            moving_piece = piece
            break

    if moving_piece == '':
        return {'valid': False, 'error': 'There is no piece'}
    
    if np.absolute(x_pos - x_dest) > 1 or np.absolute(y_pos - y_dest) > 1:
        return {'valid': False, 'error': 'King cant move like that'}

    if position == destination:
        return {'valid': False, 'error': 'You have to move a piece'}

    in_way = False
    piece_in_way = ''
    for piece in pieces:
        if pieces[piece]['position'] == destination and pieces[piece]['alive'] == True:
            in_way = True
            piece_in_way = piece
            break
    
    if in_way == True:
        if pieces[piece_in_way]['owner'] == 0:
            return {'valid': False, 'error': 'Own piece is blocking the way'}
    if in_way == True:
            pieces[moving_piece]['position'] = pieces[piece_in_way]['position']
            pieces[piece_in_way]['alive'] = False

    if in_way == False:
        pieces[moving_piece]['position'] = destination
    
    num_of_own_pieces = get_num_of_own_pieces(pieces)
    
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    ret = deepcopy(pieces)
    #
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score, 'ret': ret}


def move_knight(position, destination, pieces):
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
    pieces = deepcopy(pieces)
    for piece in pieces:
        moving_piece = ''
        if position == pieces[piece]['position']:
            moving_piece = piece
            break

    if y_pos - y_dest == -2 and x_pos - x_dest == 1:
        direction = 1

    elif y_pos - y_dest == -2 and x_pos - x_dest == -1:
        direction = 2

    elif y_pos - y_dest == 2 and x_pos - x_dest == 1:
        direction = 3
    
    elif y_pos - y_dest == 2 and x_pos - x_dest == -1:
        direction = 4

    elif y_pos - y_dest == -1 and x_pos - x_dest == 2:
        direction = 5
    
    elif y_pos - y_dest == -1 and x_pos - x_dest == -1:
        direction = 6
    
    elif y_pos - y_dest == 1 and x_pos - x_dest == 2:
        direction = 7

    elif y_pos - y_dest == 1 and x_pos -x_dest == -1:
        direction = 8
    
    else:
        return {'valid': False, 'error': 'the knight cant move like that'}
    
    piece_in_way = ''
    in_way = False
    for piece in pieces:
        if pieces[piece]['position'] == destination:
            piece_in_way = piece
            if pieces[piece_in_way]['owner'] == 0:
                return {'valid': False, 'error': 'Own piece is blocking the way'}
            in_way = True
            pieces[piece_in_way]['alive'] = False
            break

    pieces[moving_piece]['position'] = destination

    num_of_own_pieces = get_num_of_own_pieces(pieces)
    
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    ret = deepcopy(pieces)
    
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
        
    return {'valid': True, 'score': score, 'ret': ret}

def move_pawn(position, destination, pieces):
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
    pieces = deepcopy(pieces)
    for piece in pieces:
        moving_piece = ''
        if position == pieces[piece]['position']:
            moving_piece = piece
            break
    
    piece_in_way = ''
    in_way = False
    for piece in pieces:
        if pieces[piece]['position'] == destination:
            piece_in_way = piece
            if pieces[piece_in_way]['owner'] == 0:
                return {'valid': False, 'error': 'Own piece is blocking the way'}
            in_way = True
            break


    if moving_piece == '':
        return {'valid': False, 'error': 'There is no piece'}
    
    direction = 0
    if y_dest == y_pos + 1 and x_dest == x_pos:
        direction = 1

    if y_dest == y_pos + 2 and x_pos == x_dest:
        if pieces[moving_piece]['moved'] == True:
            return {'valid': False, 'error': 'pawn already moved'}
        
        else:
            direction = 2
    
    if x_dest == x_pos - 1 and y_dest == y_pos + 1:
        if in_way == False:
            return {'valid': False, 'error': 'No piece to take'}
        
        else:
            direction = 3

    if x_dest == x_pos + 1 and y_dest == y_pos + 1:
        if in_way == False:
            return {'valid': False, 'error': 'No piece to take'}
        
        else:
            direction = 4

    if direction == 0:
        return {'valid': False, 'error': 'pawn cant move like that'}

    if direction == 1 or 2:
        pieces[moving_piece]['position'] = destination
        pass
    if in_way == True:
        if direction == 3 or 4:
            pieces[moving_piece]['position'] = destination
            pieces[piece_in_way]['alive'] = False

    num_of_own_pieces = get_num_of_own_pieces(pieces)
    
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])

    ret = deepcopy(pieces)
    #
    #pieces[piece_in_way]['alive'] = True
    #if in_way == True:
    #    pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score, 'ret': ret}

def move_queen(position, destination, pieces):
    direction = 10
    way=[]
    pieces = deepcopy(pieces)
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
 
    for piece in pieces:
        moving_piece = ''
       # print('pos: ' + str(position) + 'piece: ' + str(pieces[piece]['position']) + str(position == pieces[piece]['position']))
        if position == pieces[piece]['position']:
            moving_piece = piece
          #  print(moving_piece)
          #  print(moving_piece + ' ' + str(position) + ' ' + str(pieces[piece]['position']))
            break
    if moving_piece == '':
        return {'valid': False, 'error': 'This move is invalid since there is no piece at ' + position}

    if str(position) == str(destination):
        return {'valid': False, 'error': 'You have to move a piece'}
    
    
    if x_dest > x_pos and y_dest > y_pos and x_dest - x_pos == y_dest - y_pos:
        direction = 0


    elif x_dest < x_pos and y_dest < y_pos and x_dest - x_pos == y_dest - y_pos:
        ###print('2')
        direction = 1

    elif x_dest < x_pos and y_dest > y_pos and x_dest - x_pos == y_dest - y_pos:
        ###print('2')
        direction = 2

    elif x_dest > x_pos and y_dest < y_pos and x_dest - x_pos == y_dest - y_pos:
        ###print('3')
        direction = 3

    elif y_pos == y_dest:
        direction = 4
    
    elif x_pos == x_dest:
        direction= 5

    if direction == 10:
        return {'valid': False, 'error': 'The queen cant move like that'}

    if direction == 0:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field + 1
            y_field = y_field + 1

    elif direction == 1:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field - 1
            y_field = y_field - 1

    elif direction == 2:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field - 1
            y_field = y_field + 1


    elif direction == 3:
        x_field = x_pos
        y_field = y_pos
        field = str(x_field) + str(y_field)
        field = int(field)
        while str(field) != destination:
            field = str(x_field) + str(y_field)
            field = int(field)
            way.append(str(field))
            x_field = x_field + 1
            y_field = y_field - 1

    if direction == 4:
        ####print("DIR IS 0") debugging
        if int(position[0]) < int(destination[0]):
            for i in range(int(position[0]), int(destination[0])):
                way.append(str(i) + str(position[1]))

        elif int(destination[0]) < int(position[0]):
            for i in range(int(destination[0]), int(position[0])):
                way.append(str(i) + str(position[1]))

    
    if direction == 5:
        ####print("DIR IS 1") debugging 
        
        if int(position[1]) < int(destination[1]):
            for i in range(int(position[1]), int(destination[1])):
                way.append(str(position[0]) + str(i))

        elif int(destination[1]) < int(position[1]):
            for i in range(int(destination[1]), int(position[1])):
                way.append(str(position[0]) + str(i))


    way.append(destination)
    piece_in_way = ''
    pieces_in_way = []
    in_way = False
    for f in way:
        for p in pieces:
            if pieces[p]['position'] == f and p != moving_piece and pieces[p]['alive'] == True:
                pieces_in_way.append(p)
                in_way = True

    if in_way == True:
        if pieces[pieces_in_way[0]]['owner'] == 0:
             return {'valid': False, 'error': 'Invalid move! Own piece is blocking the way'}
        
        elif pieces[pieces_in_way[0]]['owner'] == 1:
            piece_in_way = pieces_in_way[0]
    
    if in_way == True:
        if pieces[piece_in_way]['position'] != destination:
            return {'valid': False, 'error': 'Opponent piece blocking way'}

    if piece_in_way != '':
            pieces[moving_piece]['position'] = pieces[piece_in_way]['position']
            pieces[piece_in_way]['alive'] = False

    if in_way == False:
        pieces[moving_piece]['position'] = destination
    
    num_of_own_pieces = get_num_of_own_pieces(pieces)
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    ret = deepcopy(pieces)
    #
 #   if in_way == True:
  #      pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score, 'ret': ret}


def move_rook(position, destination, pieces):
    #direction 0 means, that the piece moves on the x axis, while 1 means, that it moves on y
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
    pieces = deepcopy(pieces)
    moving_piece = ''    
    for piece in pieces:
        if pieces[piece]['position'] == position:
            moving_piece = piece
    
    if moving_piece == '':
        return {'valid': False, 'error': 'This move is invalid since there is no piece at ' + position}

    if str(position) == str(destination):
        return {'valid': False, 'error': 'You have to move a piece'}
    
    elif y_pos == y_dest:
        direction = 0
    
    elif x_pos == x_dest:
        direction= 1

    else:
        return {'valid': False, 'error': 'The queen cant move like that'}

    way = []

    if direction == 0:
        ###print("DIR IS 0") debugging
        if int(position[0]) < int(destination[0]):
            for i in range(int(position[0]), int(destination[0])):
                way.append(str(i) + str(position[1]))

        elif int(destination[0]) < int(position[0]):
            for i in range(int(destination[0]), int(position[0])):
                way.append(str(i) + str(position[1]))

    
    if direction == 1:
        ###print("DIR IS 1") debugging 
        
        if int(position[1]) < int(destination[1]):
            for i in range(int(position[1]), int(destination[1])):
                way.append(str(position[0]) + str(i))

        elif int(destination[1]) < int(position[1]):
            for i in range(int(destination[1]), int(position[1])):
                way.append(str(position[0]) + str(i))

    way.append(destination)
    piece_in_way = ''
    pieces_in_way = []
    in_way = False
    for f in way:
        for p in pieces:
            if pieces[p]['position'] == f and p != moving_piece and pieces[p]['alive'] == True:
                pieces_in_way.append(p)
                in_way = True

    if in_way == True:
        if pieces[pieces_in_way[0]]['owner'] == 0:
             return {'valid': False, 'error': 'Invalid move! Own piece is blocking the way'}
        
        elif pieces[pieces_in_way[0]]['owner'] == 1:
            piece_in_way =  pieces_in_way[0]
    
    if piece_in_way != '':
            pieces[moving_piece]['position'] = pieces[piece_in_way]['position']
            pieces[piece_in_way]['alive'] = False

    if in_way == False:
        pieces[moving_piece]['position'] = destination

    num_of_own_pieces = get_num_of_own_pieces(pieces)
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    ret = deepcopy(pieces)
    #pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score, 'ret': ret}
