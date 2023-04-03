import copy
import random
import generate
import main
from kivy.app import App

SEARCH_DEPTH = 3

def evaluate(board,depth=SEARCH_DEPTH,count=1):
    for x,c in enumerate(board.color_arr):
        if c == board.current_move:
            temp_moves = generate.moves(x,board)
            for move in temp_moves:
                test_board = copy.deepcopy(board)
                test_board.clear_square(x)
                test_board.set_piece(move,board.piece_arr[x],board.current_move)
                if board.current_move == "BLACK":
                    opp_color = "WHITE"
                    king_loc = test_board.b_king_location
                elif board.current_move == "WHITE":
                    opp_color = "BLACK"
                    king_loc = test_board.w_king_location
                check_pos = generate.in_check(king_loc,test_board) 
                if check_pos != -1:
                    print(check_pos, "<= CHECK POS")
                if check_pos != -1 and generate.checkmate(test_board,check_pos,test_board.b_king_location,opp_color):
                    print(board.current_move, "has M",count, board.piece_arr[x], decode(move))
                elif depth > 1:
                    print(depth)
                    evaluate(test_board,depth-1,count+1)

def play_random(board):
    ## Add check finding and work around it
    app = App.get_running_app()
    piece_temp_arr = []
    for x,c in enumerate(board.color_arr):
        if c == board.current_move:
            piece_temp_arr+=[(x,s) for s in generate.moves(x,board)]
    rand_num = random.randint(0,len(piece_temp_arr)-1)
    soi = piece_temp_arr[rand_num]
    board.move_piece(soi[0],soi[1])
    return(board)

def play_capture(board):
    piece_temp_arr = []
    capture_move_arr = []
    highest_capture = 0
    for x,c in enumerate(board.color_arr):
        if c == board.current_move:
            for s in generate.moves(x,board):
                piece_temp_arr.append((x,s))
                if move_include_capture(board,s) > highest_capture:
                    capture_move_arr = []
                    capture_move_arr.append((x,s))
                elif move_include_capture(board,s) == highest_capture:
                    capture_move_arr.append((x,s))
    if len(capture_move_arr) > 0:
        rand_num = random.randint(0,len(capture_move_arr)-1)
        soi = capture_move_arr[rand_num]
    else:
        rand_num = random.randint(0,len(piece_temp_arr)-1)
        soi = piece_temp_arr[rand_num]
    board.move_piece(soi[0],soi[1])
    return(board)


def move_include_capture(board, square):
    #tests if a move to a square would include a capture, returns value
    if board.piece_arr[square] == "EMPTY":
        return -1
    elif board.piece_arr[square] == "PAWN":
        return 1
    elif board.piece_arr[square] == "BISHOP":
        return 4
    elif board.piece_arr[square] == "KNIGHT":
        return 3
    elif board.piece_arr[square] == "ROOK":
        return 5
    elif board.piece_arr[square] == "QUEEN":
        return 9
    return False

def decode(square):
    return str(chr(65+square//8))+ str(square%8)
