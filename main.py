import numpy as np
class values():
    pawn = 1
    knight = 3
    bishop = 3
    rook = 5
    queen = 9
    king = 20

init_pieces = {

    'rook1': {
        'value': values.rook, #assigns the value
        'owner': 0, #Defines, that this piece belongs to the bot
        'kind': 'rook',
        'position': '11',
        'alive': True,
    },
   'rook2': {
        'value': values.rook,
        'owner': 0, #Defines, that this piece belongs to the bot
        'kind': 'rook', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '81',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'rook3': {
        'value': values.rook, #assigns the value
        'owner': 1, #Defines, that this piece does not belong to the bot
        'kind': 'rook', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '18',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'rook4': {
        'value': values.rook, #assigns the value
        'owner': 1, #Defines, that this pice doesnt belong to the bot
        'kind': 'rook', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '88',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'bishop1': {
        'value': values.bishop, #assigns the value
        'owner': 0, #Defines, that this pice doesnt belong to the bot
        'kind': 'bishop', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '31',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'bishop2': {
        'value': values.bishop, #assigns the value
        'owner': 0, #Defines, that this pice doesnt belong to the bot
        'kind': 'bishop', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '61',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'bishop3': {
        'value': values.bishop, #assigns the value
        'owner': 1, #Defines, that this pice doesnt belong to the bot
        'kind': 'bishop', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '38',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'bishop4': {
        'value': values.bishop, #assigns the value
        'owner': 1, #Defines, that this pice doesnt belong to the bot
        'kind': 'bishop', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '68',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'queen1': {
        'value': values.queen, #assigns the value
        'owner': 0, #Defines, that this pice doesnt belong to the bot
        'kind': 'queen', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '41',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'queen2': {
        'value': values.queen, #assigns the value
        'owner': 1, #Defines, that this pice doesnt belong to the bot
        'kind': 'queen', # defines the type of the piece. This is later relevant to call the matching move function
        'position': '48',# initial position of the piece
        'alive': True, # tells if the piece is still in game or has been captured
    },
    'king1': {
        'value': values.king,
        'owner': 0,
        'kind': 'king',
        'position': '51',
        'alive': True,

    },
     'king2': {
        'value': values.king,
        'owner': 1,
        'kind': 'king',
        'position': '58',
        'alive': True,

    },
    'knight1': {
        'value': values.knight,
        'owner': 0,
        'kind': 'knight',
        'position': '21',
        'alive': True,
    },
    'knight2': {
        'value': values.knight,
        'owner': 0,
        'kind': 'knight',
        'position': '71',
        'alive': True,
    },
    'knight3': {
        'value': values.knight,
        'owner': 1,
        'kind': 'knight',
        'position': '28',
        'alive': True,
    },
    'knight4': {
        'value': values.knight,
        'owner': 1,
        'kind': 'knight',
        'position': '78',
        'alive': True,
    },
    'pawn1': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '12',
        'alive': True,
        'moved': False,
    },
    'pawn2': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '22',
        'alive': True,
        'moved': False,
    },
    'pawn3': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '32',
        'alive': True,
        'moved': False,
    },
    'pawn4': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '42',
        'alive': True,
        'moved': False,
    },
    'pawn5': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '52',
        'alive': True,
        'moved': False,
    },
    'pawn6': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '62',
        'alive': True,
        'moved': False,
    },
    'pawn7': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '72',
        'alive': True,
        'moved': False,
    },
    'pawn8': {
        'value': values.pawn,
        'owner': 0,
        'kind': 'pawn',
        'position': '82',
        'alive': True,
        'moved': False,
    },
        'pawn9': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '17',
        'alive': True,
        'moved': False,
    },
    'pawn10': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '27',
        'alive': True,
        'moved': False,
    },
    'pawn11': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '37',
        'alive': True,
        'moved': False,
    },
    'pawn12': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '47',
        'alive': True,
        'moved': False,
    },
    'pawn13': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '57',
        'alive': True,
        'moved': False,
    },
    'pawn14': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '67',
        'alive': True,
        'moved': False,
    },
    'pawn15': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '77',
        'alive': True,
        'moved': False,
    },
    'pawn16': {
        'value': values.pawn,
        'owner': 1,
        'kind': 'pawn',
        'position': '87',
        'alive': True,
        'moved': False,
    }, 
    
}

INIT_PIECES = init_pieces



board = ['11', '12', '13', '14', '15', '16', '17', '18',
         '21', '22', '23', '24', '25', '26', '27', '28',
         '31', '32', '33', '34', '35', '36', '37', '38',
         '41', '42', '43', '44', '45', '46', '47', '48',
         '51', '52', '53', '54', '55', '56', '57', '58',
         '61', '62', '63', '64', '65', '66', '67', '68',
         '71', '72', '73', '74', '75', '76', '77', '78',
         '81', '82', '83', '84', '85', '86', '87', '88']



def move_pawn(position, destination, pieces):
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
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
        #pieces[moving_piece]['position'] = destination
        pass
    if in_way == True:
        if direction == 3 or 4:
            #pieces[moving_piece]['position'] = destination
            pieces[piece_in_way]['alive'] = False

    num_of_own_pieces = get_num_of_own_pieces()
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    pieces[moving_piece]['position'] = position
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score}


def move_knight(position, destination, pieces):
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
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

    num_of_own_pieces = get_num_of_own_pieces()
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    pieces[moving_piece]['position'] = position
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
        
    return {'valid': True, 'score': score}
    

       




    






















def move_king(position, destination, pieces):
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
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
    
    num_of_own_pieces = get_num_of_own_pieces()
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    pieces[moving_piece]['position'] = position
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score}

            

def move_queen(position, destination, pieces):
    direction = 10
    way=[]
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
            piece_in_way =  pieces_in_way[0]
    
    if piece_in_way != '':
            pieces[moving_piece]['position'] = pieces[piece_in_way]['position']
            pieces[piece_in_way]['alive'] = False

    if in_way == False:
        pieces[moving_piece]['position'] = destination
    
    num_of_own_pieces = get_num_of_own_pieces()
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    pieces[moving_piece]['position'] = position
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score}

    #return num_of_own_pieces
def move_bishop(position, destination, init_pieces):
    pieces = init_pieces
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
    
    
    
    num_of_own_pieces = get_num_of_own_pieces()
    pieces[moving_piece]['position'] = position
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    if in_way == True:
        pieces[piece_in_way]['alive'] = True

    return {'valid': True, 'score': score}
    
    
def move_rook(position, destination, pieces):
    #direction 0 means, that the piece moves on the x axis, while 1 means, that it moves on y
    x_pos = int(position[0])
    y_pos = int(position[1])
    x_dest = int(destination[0])
    y_dest = int(destination[1])
    
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

    num_of_own_pieces = get_num_of_own_pieces()
    score = get_score(num_of_own_pieces['pawn_counter'], num_of_own_pieces['knight_counter'], num_of_own_pieces['bishop_counter'], num_of_own_pieces['rook_counter'], num_of_own_pieces['queen_counter'], num_of_own_pieces['king_counter'], num_of_own_pieces['op_pawn_counter'], num_of_own_pieces['op_knight_counter'], num_of_own_pieces['op_bishop_counter'], num_of_own_pieces['op_rook_counter'], num_of_own_pieces['op_queen_counter'], num_of_own_pieces['op_king_counter'])
    pieces[moving_piece]['position'] = position
    #pieces[piece_in_way]['alive'] = True
    if in_way == True:
        pieces[piece_in_way]['alive'] = True
    return {'valid': True, 'score': score}

def get_score(num_of_pawns, num_of_knights, num_of_bishops, num_of_rooks, num_of_queens, num_of_kings, num_of_op_pawns, num_of_op_knights, num_of_op_bishops, num_of_op_rooks, num_of_op_queens, num_of_op_kings):
    score = ((num_of_pawns) + (values.bishop * num_of_bishops) + (values.knight * num_of_knights) + (values.rook * num_of_rooks) + (values.queen * num_of_queens) + (values.king * num_of_kings)) - ((num_of_op_pawns) + (values.bishop * num_of_op_bishops) + (values.knight * num_of_op_knights) + (values.rook * num_of_op_rooks) + (values.queen * num_of_op_queens) + (values.king * num_of_op_kings))
    
    return score

def get_num_of_own_pieces():
    pieces = init_pieces
    pawn_counter = 0
    knight_counter = 0
    bishop_counter = 0
    rook_counter = 0
    queen_counter = 0
    king_counter = 0
    op_pawn_counter = 0
    op_knight_counter = 0
    op_bishop_counter = 0
    op_rook_counter = 0
    op_queen_counter = 0
    op_king_counter = 0

    for piece in pieces:
        if pieces[piece]['kind'] == 'pawn':
            if pieces[piece]['owner'] == 0:
                if pieces[piece]['alive'] == True:
                    pawn_counter = pawn_counter + 1
            
            elif pieces[piece]['owner'] == 1:
                if pieces[piece]['alive'] == True:
                    op_pawn_counter = op_pawn_counter + 1
        
        elif pieces[piece]['kind'] == 'knight':
            if pieces[piece]['owner'] == 0:
                if pieces[piece]['alive'] == True:
                    knight_counter = knight_counter + 1
            
            elif pieces[piece]['owner'] == 1:
                if pieces[piece]['alive'] == True:
                    op_knight_counter = op_knight_counter + 1
            

        elif pieces[piece]['kind'] == 'bishop':
            if pieces[piece]['owner'] == 0:
                if pieces[piece]['alive'] == True:
                    bishop_counter = bishop_counter + 1
                   # print(bishop_counter)

            elif pieces[piece]['owner'] == 1:
                if pieces[piece]['alive'] == True:
                    op_bishop_counter = op_bishop_counter + 1
                  #  print('count_opb')
                   # print('op' + str(op_bishop_counter))

        elif pieces[piece]['kind'] == 'rook':
            if pieces[piece]['owner'] == 0:
                if pieces[piece]['alive'] == True:
                    rook_counter = rook_counter + 1

            elif pieces[piece]['owner'] == 1:
                if pieces[piece]['alive'] == True:
                    op_rook_counter = op_rook_counter + 1

        elif pieces[piece]['kind'] == 'queen':
            if pieces[piece]['owner'] == 0:
                if pieces[piece]['alive'] == True:
                    queen_counter = queen_counter + 1
            
            elif pieces[piece]['owner'] == 1:
                if pieces[piece]['alive'] == True:
                    op_queen_counter = op_queen_counter + 1

        elif pieces[piece]['kind'] == 'king':
            if pieces[piece]['owner'] == 0:
                if pieces[piece]['alive'] == True:
                    king_counter = king_counter + 1

            elif pieces[piece]['owner'] == 1:
                if pieces[piece]['alive'] == True:
                    op_king_counter = op_king_counter + 1

    return  {'pawn_counter': pawn_counter, 
             'knight_counter': knight_counter, 
             'bishop_counter': bishop_counter, 
             'rook_counter': rook_counter, 
             'queen_counter': queen_counter, 
             'king_counter': king_counter, 
             'op_pawn_counter': op_pawn_counter, 
             'op_knight_counter': op_knight_counter,
             'op_bishop_counter': op_bishop_counter, 
             'op_rook_counter': op_rook_counter, 
             'op_queen_counter': op_queen_counter, 
             'op_king_counter': op_king_counter}

def get_valid_moves():
    queens = []
    rooks = []
    bishops = []
    kings = []
    valid_moves = []
    knights = []
    pawns = []
    for piece in init_pieces:
        if init_pieces[piece]['kind'] == 'queen' and init_pieces[piece]['owner'] == 0 and init_pieces[piece]['alive'] == True:
            queens.append(piece)
    
    for i in queens:
        var = init_pieces[i]['position']
        for b in board:
            move = move_queen(str(var), str(b), init_pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],                 
                                    })
    for piece in init_pieces:
        if init_pieces[piece]['kind'] == 'bishop' and init_pieces[piece]['owner'] == 0 and init_pieces[piece]['alive'] == True:
            bishops.append(piece)
    
    for i in bishops:
        var = init_pieces[i]['position']
        for b in board:
            move = move_bishop(str(var), str(b), init_pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],                 
                                    })
    
    for piece in init_pieces:
        if init_pieces[piece]['kind'] == 'rook' and init_pieces[piece]['owner'] == 0 and init_pieces[piece]['alive'] == True:
            rooks.append(piece)
    for i in rooks:
        var = init_pieces[i]['position']
        for b in board:
            move = move_rook(str(var), str(b), init_pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],                 
                                    })

    for piece in init_pieces:
        if init_pieces[piece]['kind'] == 'king' and init_pieces[piece]['owner'] == 0 and init_pieces[piece]['alive'] == True:
            kings.append(piece)
    for i in kings:
        var = init_pieces[i]['position']
        for b in board:
            move = move_king(str(var), str(b), init_pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],                 
                                    })

    for piece in init_pieces:
        if init_pieces[piece]['kind'] == 'knight' and init_pieces[piece]['owner'] == 0 and init_pieces[piece]['alive'] == True:
            knights.append(piece)
    
    #print(knights)
    for i in knights:
        var = init_pieces[i]['position']
        for b in board:
            move = move_knight(str(var), str(b), init_pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],                 
                                    })

    for piece in init_pieces:
        if init_pieces[piece]['kind'] == 'pawn' and init_pieces[piece]['owner'] == 0 and init_pieces[piece]['alive'] == True:
            pawns.append(piece)
    for i in pawns:
        var = init_pieces[i]['position']
        for b in board:
            move = move_pawn(str(var), str(b), init_pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],                 
                                    })

    return valid_moves           



def get_best_move(valids):
    moves_sorted = sorted(valids, key=lambda d: d['score'],  reverse=True)
    return moves_sorted[0]


valids = get_valid_moves()
for i in valids:
    print(i)
    print('---------------------')
print(get_best_move(valids))
print(len(valids))
