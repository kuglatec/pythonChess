class values():
    pawn = 1
    knight = 3
    bishop = 3
    rook = 5
    queen = 9
    king = 20

def get_score(num_of_pawns, num_of_knights, num_of_bishops, num_of_rooks, num_of_queens, num_of_kings, num_of_op_pawns, num_of_op_knights, num_of_op_bishops, num_of_op_rooks, num_of_op_queens, num_of_op_kings):
    score = ((num_of_pawns) + (values.bishop * num_of_bishops) + (values.knight * num_of_knights) + (values.rook * num_of_rooks) + (values.queen * num_of_queens) + (values.king * num_of_kings)) - ((num_of_op_pawns) + (values.bishop * num_of_op_bishops) + (values.knight * num_of_op_knights) + (values.rook * num_of_op_rooks) + (values.queen * num_of_op_queens) + (values.king * num_of_op_kings))
    
    return score

def get_num_of_own_pieces(pieces):
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


