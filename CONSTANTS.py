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
board = ['11', '12', '13', '14', '15', '16', '17', '18',
         '21', '22', '23', '24', '25', '26', '27', '28',
         '31', '32', '33', '34', '35', '36', '37', '38',
         '41', '42', '43', '44', '45', '46', '47', '48',
         '51', '52', '53', '54', '55', '56', '57', '58',
         '61', '62', '63', '64', '65', '66', '67', '68',
         '71', '72', '73', '74', '75', '76', '77', '78',
         '81', '82', '83', '84', '85', '86', '87', '88']