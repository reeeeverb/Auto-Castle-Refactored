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
            if piece_arr[square+8] == "EMPTY":
                out.append(square+8)
                if row < 6 and piece_arr[square+16] == "EMPTY" and row == 1:
                    out.append(square+16)
            if col != 0 and piece_arr[square+7] != "EMPTY" and color != color_arr[square+7]:
                out.append(square+7)
            if col != 7 and piece_arr[square+9] != "EMPTY" and color != color_arr[square+9]:
                out.append(square+9)
        else:
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

    return out
