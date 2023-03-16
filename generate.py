def moves(square,board):
    piece_arr = board.piece_arr
    color_arr = board.color_arr
    forward = board.forward
    move = board.move
    piece = piece_arr[square]
    color = color_arr[square]
    row = square//8
    col = square%8
    out = []
    if piece == "PAWN":
        if color == forward:
            if color == "BLACK":
                if board.w_en_passantable == square+7 or board.w_en_passantable == square+9:
                    out.append(board.w_en_passantable)
            if color == "WHITE":
                if board.b_en_passantable == square+7 or board.b_en_passantable == square+9:
                    out.append(board.b_en_passantable)
            if piece_arr[square+8] == "EMPTY":
                out.append(square+8)
                if row < 6 and piece_arr[square+16] == "EMPTY" and row == 1:
                    out.append(square+16)
            if col != 0 and piece_arr[square+7] != "EMPTY" and color != color_arr[square+7]:
                out.append(square+7)
            if col != 7 and piece_arr[square+9] != "EMPTY" and color != color_arr[square+9]:
                out.append(square+9)
        else:
            if color == "BLACK":
                if board.w_en_passantable == square-7 or board.w_en_passantable == square-9:
                    out.append(board.w_en_passantable)
            if color == "WHITE":
                if board.b_en_passantable == square-7 or board.b_en_passantable == square-9:
                    out.append(board.b_en_passantable)
            if piece_arr[square-8] == "EMPTY":
                out.append(square-8)
                if row > 1 and piece_arr[square-16] == "EMPTY" and row == 6:
                    out.append(square-16)
            if col != 7 and piece_arr[square-7] != "EMPTY" and color != color_arr[square-7]:
                out.append(square-7)
            if col != 0 and piece_arr[square-9] != "EMPTY" and color != color_arr[square-9]:
                out.append(square-9)
    elif piece == "KNIGHT":
        if col > 0 and row < 6 and color_arr[square+15] != color:
            out.append(square+15)
        if col < 7 and row < 6 and color_arr[square+17] != color:
            out.append(square+17)
        if col > 1 and row < 7 and color_arr[square+6] != color:
            out.append(square+6)
        if col < 6 and row < 7 and color_arr[square+10] != color:
            out.append(square+10)
        if col > 0 and row > 1 and color_arr[square-17] != color:
            out.append(square-17)
        if col < 7 and row > 1 and color_arr[square-15] != color:
            out.append(square-15)
        if col > 1 and row > 0 and color_arr[square-10] != color:
            out.append(square-10)
        if col < 6 and row > 0 and color_arr[square-6] != color:
            out.append(square-6)
    elif piece == "BISHOP" or piece == "QUEEN":
        t_square1 = col-1
        t_square0 = row-1
        t_tracker = square-9
        dont_stop = True
        while t_square1 >= 0 and t_square0 >= 0 and dont_stop:
            if color_arr[t_tracker] == color:
                break
            elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                dont_stop = False
            out.append(t_tracker)
            t_square1 -= 1
            t_square0 -= 1
            t_tracker -= 9
        t_square1 = col+1
        t_square0 = row+1
        t_tracker = square+9
        dont_stop = True
        while t_square1 <= 7 and t_square0 <= 7 and dont_stop:
            if color_arr[t_tracker] == color:
                break
            elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                dont_stop = False
            out.append(t_tracker)
            t_square1 += 1
            t_square0 += 1
            t_tracker += 9
        t_square1 = col-1
        t_square0 = row+1
        t_tracker = square+7
        dont_stop = True
        while t_square1 >= 0 and t_square0 <= 7 and dont_stop:
            if color_arr[t_tracker] == color:
                break
            elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                dont_stop = False
            out.append(t_tracker)
            t_square1 -= 1
            t_square0 += 1
            t_tracker += 7
        t_square1 = col+1
        t_square0 = row-1
        t_tracker = square-7
        dont_stop = True
        while t_square1 <= 7 and t_square0 >= 0 and dont_stop:
            if color_arr[t_tracker] == color:
                break
            elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                dont_stop = False
            out.append(t_tracker)
            t_square1 += 1
            t_square0 -= 1
            t_tracker -= 7
    if piece == "ROOK" or piece == "QUEEN":
            t_square1 = col-1
            t_square0 = row
            t_tracker = square-1
            dont_stop = True
            while t_square1 >= 0 and t_square0 >= 0 and dont_stop:
                if color_arr[t_tracker] == color:
                    break
                elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                    dont_stop = False
                out.append(t_tracker)
                t_square1 -= 1
                t_tracker -= 1
            t_square1 = col+1
            t_square0 = row
            t_tracker = square+1
            dont_stop = True
            while t_square1 <= 7 and t_square0 <= 7 and dont_stop:
                if color_arr[t_tracker] == color:
                    break
                elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                    dont_stop = False
                out.append(t_tracker)
                t_square1 += 1
                t_tracker += 1
            t_square1 = col
            t_square0 = row-1
            t_tracker = square-8
            dont_stop = True
            while t_square1 >= 0 and t_square0 >= 0 and dont_stop:
                if color_arr[t_tracker] == color:
                    break
                elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                    dont_stop = False
                out.append(t_tracker)
                t_square0 -= 1
                t_tracker -= 8
            t_square1 = col
            t_square0 = row+1
            t_tracker = square+8
            dont_stop = True
            while t_square1 <= 7 and t_square0 <= 7 and dont_stop:
                if color_arr[t_tracker] == color:
                    break
                elif color_arr[t_tracker] != color and color_arr[t_tracker] != "EMPTY":
                    dont_stop = False
                out.append(t_tracker)
                t_square0 += 1
                t_tracker += 8
    if piece == "KING":
            if col < 7 and color_arr[square+1] != color:
                out.append(square+1)
            if col > 0 and color_arr[square-1] != color:
                out.append(square-1)
            if row < 7 and col > 0 and color_arr[square+7] != color:
                out.append(square+7)
            if row < 7 and color_arr[square+8] != color:
                out.append(square+8)
            if row < 7 and col < 7 and color_arr[square+9] != color:
                out.append(square+9)
            if row > 0 and col < 7 and color_arr[square-7] != color:
                out.append(square-7)
            if row > 0 and color_arr[square-8] != color:
                out.append(square-8)
            if row > 0 and col > 0 and color_arr[square-9] != color:
                out.append(square-9)
    return out

def in_check(square,board,detail=False):
        color = board.color_arr
        piece = board.piece_arr

        if color[square] == "WHITE":
            white = 1
        elif color[square] == "BLACK":
            white = 0

        king_row = square//8
        king_col = square%8

        # From above check
        if king_row < 7:
            temp_row = king_row+1
            temp_pos = temp_row*8+king_col
            while temp_row < 7 and piece[temp_pos] == "EMPTY":
                temp_row+=1;
                temp_pos+=8;
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From front: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "ROOK" or hit_p == "QUEEN"):
                    print("In check")
                    return True

        # From below check
        if king_row > 0:
            temp_row = king_row-1
            temp_pos = temp_row*8+king_col
            while temp_row > 0 and piece[temp_pos] == "EMPTY":
                temp_row-=1;
                temp_pos-=8;
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From back: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "ROOK" or hit_p == "QUEEN"):
                    print("In check")
                    return True

        # From right check
        if king_col < 7:
            temp_col = king_col+1
            temp_pos = king_row*8+temp_col
            while temp_col < 7 and piece[temp_pos] == "EMPTY":
                temp_col+=1;
                temp_pos+=1;
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From right: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "ROOK" or hit_p == "QUEEN"):
                    print("In check")
                    return True

        # From left check
        if king_col > 0:
            temp_col = king_col-1
            temp_pos = king_row*8+temp_col
            while temp_col > 0 and piece[temp_pos] == "EMPTY":
                temp_col-=1;
                temp_pos-=1;
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From left: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "ROOK" or hit_p == "QUEEN"):
                    print("In check")
                    return True

        # From diagonal top right check
        if king_row < 7 and king_col < 7:
            temp_count = 1
            temp_row = king_row+1
            temp_col = king_col+1
            temp_pos = temp_row*8+temp_col
            while temp_col < 7 and temp_row < 7 and piece[temp_pos] == "EMPTY":
                temp_col+=1;
                temp_row+=1;
                temp_pos+=9;
                temp_count += 1
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From upper right: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "BISHOP" or hit_p == "QUEEN"):
                    print("In check")
                    return True
                elif (temp_count == 1 and (hit_p == "PAWN" or hit_p == "KING") and board.forward != hit_c):
                    print("Pawn Check")
                    return True

        # From diagonal top left check
        if king_row < 7 and king_col > 0:
            temp_count = 0
            temp_row = king_row+1
            temp_col = king_col-1
            temp_pos = temp_row*8+temp_col
            while temp_col > 0 and temp_row < 7 and piece[temp_pos] == "EMPTY":
                temp_col-=1;
                temp_row+=1;
                temp_pos+=7;
                temp_count+=1
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From upper left: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "BISHOP" or hit_p == "QUEEN"):
                    print("In check")
                    return True
                elif (temp_count == 1 and (hit_p == "PAWN" or hit_p == "KING") and board.forward == hit_c):
                    print("Pawn Check")
                    return True

        # From diagonal bottom right check
        if king_row > 0 and king_col < 7:
            temp_count = 0
            temp_row = king_row-1
            temp_col = king_col+1
            temp_pos = temp_row*8+temp_col
            while temp_col < 7 and temp_row > 0 and piece[temp_pos] == "EMPTY":
                temp_col+=1;
                temp_row-=1;
                temp_pos-=7;
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From lower right: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "BISHOP" or hit_p == "QUEEN"):
                    print("In check")
                    return True
                elif (temp_count == 1 and (hit_p == "PAWN" or hit_p == "KING") and board.forward != hit_c):
                    print("Pawn Check")
                    return True

        # From diagonal bottom left check
        if king_row > 0 and king_col > 0:
            temp_count = 0
            temp_row = king_row-1
            temp_col = king_col-1
            temp_pos = temp_row*8+temp_col
            while temp_col > 0 and temp_row > 0 and piece[temp_pos] == "EMPTY":
                temp_col-=1;
                temp_row-=1;
                temp_pos-=9;
            hit_p = piece[temp_pos]
            hit_c = color[temp_pos]
            #print("From lower left: ",hit_c, hit_p)
            if (hit_c == "BLACK" and white == 1) or (hit_c == "WHITE" and white == 0):
                if (hit_p == "BISHOP" or hit_p == "QUEEN"):
                    print("In check")
                    return True
                elif (temp_count == 1 and (hit_p == "PAWN" or hit_p == "KING") and board.forward != hit_c):
                    print("Pawn Check")
                    return True
        # Knight checks
        if white == 1:
            temp_c = "WHITE"
        else:
            temp_c = "BLACK"
        if king_row < 7 and king_col > 1:
            temp_col=king_col-2
            temp_row=king_row+1
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row < 7 and king_col < 6:
            temp_col=king_col+2
            temp_row=king_row+1
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row > 0 and king_col > 1:
            temp_col=king_col-2
            temp_row=king_row-1
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row > 0 and king_col < 6:
            temp_col=king_col+2
            temp_row=king_row-1
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row > 1 and king_col < 7:
            temp_col=king_col+1
            temp_row=king_row-2
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row > 1 and king_col > 0:
            temp_col=king_col-1
            temp_row=king_row-2
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row < 6 and king_col > 0:
            temp_col=king_col-1
            temp_row=king_row+2
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True

        if king_row < 6 and king_col < 7:
            temp_col=king_col+1
            temp_row=king_row+2
            temp_pos = temp_row*8+temp_col
            if piece[temp_pos] == "KNIGHT" and color[temp_pos] != temp_c:
                print("Check dectected, knight at ", temp_pos)
                return True
        return False


