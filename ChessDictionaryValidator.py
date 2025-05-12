def is_valid_chess_board(board):
    valid_pieces = {
        'wpawn', 'wrook', 'wknight', 'wbishop', 'wqueen', 'wking',
        'bpawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking'
    }
    valid_positions = set()
    for letter in 'abcdefgh':
        for number in '12345678':
            valid_positions.add(letter + number)

    piece_counts = {}
    for pos, piece in board.items():
        if pos not in valid_positions:
            print(f"Error: Invalid position '{pos}'.")
            return False
        if piece not in valid_pieces:
            print(f"Error: Invalid piece '{piece}' at '{pos}'.")
            return False

        piece_counts[piece] = piece_counts.get(piece, 0) + 1
    if piece_counts.get('wking', 0) != 1 or piece_counts.get('bking', 0) != 1:
        print("Error: There must be exactly one white king and one black king.")
        return False

    if piece_counts.get('wqueen', 0) > 1 or piece_counts.get('bqueen', 0) > 1:
        print("Error: There can be at most one white queen and one black queen (initially).")
        return False

    if piece_counts.get('wrook', 0) > 2 or piece_counts.get('brook', 0) > 2:
        print("Error: There can be at most two white rooks and two black rooks (initially).")
        return False

    if piece_counts.get('wknight', 0) > 2 or piece_counts.get('bknight', 0) > 2:
        print("Error: There can be at most two white knights and two black knights (initially).")
        return False

    if piece_counts.get('wbishop', 0) > 2 or piece_counts.get('bbishop', 0) > 2:
        print("Error: There can be at most two white bishops and two black bishops (initially).")
        return False

    if piece_counts.get('wpawn', 0) > 8 or piece_counts.get('bpawn', 0) > 8:
        print("Error: There can be at most eight white pawns and eight black pawns.")
        return False
    if len(board) != len(set(board.keys())):
        print("Error: Multiple pieces on the same position.")
        return False

    return True

if __name__ == "__main__":
    print(' Name: Rahul G \n USN: 1AY24AI088 \n Section: O')
    valid_board = {
        'a1': 'wrook', 'a2': 'wpawn', 'a3': ' ', 'a4': ' ', 'a5': ' ', 'a6': ' ', 'a7': 'bpawn', 'a8': 'brook',
        'b1': 'wknight', 'b2': 'wpawn', 'b3': ' ', 'b4': ' ', 'b5': ' ', 'b6': ' ', 'b7': 'bpawn', 'b8': 'bknight',
        'c1': 'wbishop', 'c2': 'wpawn', 'c3': ' ', 'c4': ' ', 'c5': ' ', 'c6': ' ', 'c7': 'bpawn', 'c8': 'bbishop',
        'd1': 'wqueen', 'd2': 'wpawn', 'd3': ' ', 'd4': ' ', 'd5': ' ', 'd6': ' ', 'd7': 'bpawn', 'd8': 'bqueen',
        'e1': 'wking', 'e2': 'wpawn', 'e3': ' ', 'e4': ' ', 'e5': ' ', 'e6': ' ', 'e7': 'bpawn', 'e8': 'bking',
        'f1': 'wbishop', 'f2': 'wpawn', 'f3': ' ', 'f4': ' ', 'f5': ' ', 'f6': ' ', 'f7': 'bpawn', 'f8': 'bbishop',
        'g1': 'wknight', 'g2': 'wpawn', 'g3': ' ', 'g4': ' ', 'g5': ' ', 'g6': ' ', 'g7': 'bpawn', 'g8': 'bknight',
        'h1': 'wrook', 'h2': 'wpawn', 'h3': ' ', 'h4': ' ', 'h5': ' ', 'h6': ' ', 'h7': 'bpawn', 'h8': 'brook'
    }
    print("Valid Board Check:", is_valid_chess_board(valid_board))

    invalid_position_board = {'a9': 'wpawn'}
    print("Invalid Position Check:", is_valid_chess_board(invalid_position_board))

    invalid_piece_board = {'a1': 'wkingg'}
    print("Invalid Piece Check:", is_valid_chess_board(invalid_piece_board))

    multiple_kings_board = {'a1': 'wking', 'h8': 'bking', 'e5': 'wking'}
    print("Multiple Kings Check:", is_valid_chess_board(multiple_kings_board))

    too_many_pawns_board = {f'{chr(ord("a") + i)}2': 'wpawn' for i in range(9)}
    too_many_pawns_board['a1'] = 'wking'
    too_many_pawns_board['h8'] = 'bking'
    print("Too Many Pawns Check:", is_valid_chess_board(too_many_pawns_board))

    occupied_position_board = {'a1': 'wrook', 'a1': 'wpawn'}
    print("Occupied Position Check:", is_valid_chess_board(occupied_position_board))
