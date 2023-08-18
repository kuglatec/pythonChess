from moves import move_bishop, move_king, move_knight, move_pawn, move_queen, move_rook
from score_eval import get_num_of_own_pieces, get_score
import numpy as np


def get_valid_moves(pieces, board):
    queens = []
    rooks = []
    bishops = []
    kings = []
    valid_moves = []
    knights = []
    pawns = []
    for piece in pieces:
        if pieces[piece]['kind'] == 'queen' and pieces[piece]['owner'] == 0 and pieces[piece]['alive'] == True:
            queens.append(piece)
    
    for i in queens:
        var = pieces[i]['position']
        for b in board:
            move = move_queen(str(var), str(b), pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],
                                    'func': 'que',
                                    'ret_pieces': move['ret'],                
                                    })
    for piece in pieces:
        if pieces[piece]['kind'] == 'bishop' and pieces[piece]['owner'] == 0 and pieces[piece]['alive'] == True:
            bishops.append(piece)
    
    for i in bishops:
        var = pieces[i]['position']
        for b in board:
            move = move_bishop(str(var), str(b), pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],
                                    'func': 'bis',     
                                    'ret_pieces': move['ret'],             
                                    })
    
    for piece in pieces:
        if pieces[piece]['kind'] == 'rook' and pieces[piece]['owner'] == 0 and pieces[piece]['alive'] == True:
            rooks.append(piece)
    for i in rooks:
        var = pieces[i]['position']
        for b in board:
            move = move_rook(str(var), str(b), pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],    
                                    'func': 'rok',   
                                    'ret_pieces': move['ret'],           
                                    })

    for piece in pieces:
        if pieces[piece]['kind'] == 'king' and pieces[piece]['owner'] == 0 and pieces[piece]['alive'] == True:
            kings.append(piece)
    for i in kings:
        var = pieces[i]['position']
        for b in board:
            move = move_king(str(var), str(b), pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],
                                    'func': 'kin', 
                                    'ret_pieces': move['ret'],                 
                                    })

    for piece in pieces:
        if pieces[piece]['kind'] == 'knight' and pieces[piece]['owner'] == 0 and pieces[piece]['alive'] == True:
            knights.append(piece)
    
    #print(knights)
    for i in knights:
        var = pieces[i]['position']
        for b in board:
            move = move_knight(str(var), str(b), pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],
                                    'func': 'kni',      
                                    'ret_pieces': move['ret'],            
                                    })

    for piece in pieces:
        if pieces[piece]['kind'] == 'pawn' and pieces[piece]['owner'] == 0 and pieces[piece]['alive'] == True:
            pawns.append(piece)
    for i in pawns:
        var = pieces[i]['position']
        for b in board:
            move = move_pawn(str(var), str(b), pieces)
            if move['valid'] == True:
                valid_moves.append({'move': [str(var), str(b)],
                                    'score': move['score'],
                                    'func': 'pwn',  
                                    'ret_pieces': move['ret'],                 
                                    })

    return valid_moves           



def get_best_move(valids):
    moves_sorted = sorted(valids, key=lambda d: d['score'],  reverse=True)
    return moves_sorted[0]
