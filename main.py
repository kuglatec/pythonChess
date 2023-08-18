import numpy as np
from CONSTANTS import init_pieces, board
from algorithm import get_valid_moves, get_best_move


valids = get_valid_moves(init_pieces, board)
for i in valids:
    print(i)
    print('---------------------')
print(get_best_move(valids))
