
cell_to_board_map = {
    (0,0):'7',
    (1,0):'4',
    (2,0):'1',
    (0,1):'8',
    (1,1):'5',
    (2,1):'2',
    (0,2):'9',
    (1,2):'6',
    (2,2):'3',
}

BOARD_TO_CELL = {v:k for k,v in cell_to_board_map.items()}

def get_empty_board():
    return {v:" " for v in cell_to_board_map.values()}


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


scoreMap = {"X": 1, "O": -1}

def checkWinner(theBoard):
    result = None # None not finished 0 draw, 1 X won, -1 O won
    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
        return scoreMap[theBoard['7']]
    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
        return scoreMap[theBoard['4']]
    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
        return scoreMap[theBoard['1']]
    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
        return scoreMap[theBoard['1']]
    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
        return scoreMap[theBoard['2']]
    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
        return scoreMap[theBoard['3']]
    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
        return scoreMap[theBoard['7']]
    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
        return scoreMap[theBoard['1']]
    
    if all([value!=" " for value in theBoard.values()]):
        return 0
    return result

def current_moves_to_board(current_moves):
    board = get_empty_board()

    for row in current_moves:
        for move in row:
            row_ind, col_ind =  move.row, move.col
            label = move.label
            if label in ("X", "O"):
                board[cell_to_board_map[(row_ind,col_ind)]] = label
    printBoard(board)
    return board 


def get_next_func(turn):
    return min if turn == "X" else max

next_turn = lambda turn : "O" if turn == "X" else "X"

def minimax(board, turn, func=max):
    my_score = None
    best_move = None
    
    table_score = checkWinner(board)
    if table_score is not None:
        return table_score, None
    for x in range(1,10):
        x = str(x)
        if board[x] != " ":
            continue
        board[x] = turn
        opponent = next_turn(turn)
        score, move = minimax(board,opponent,get_next_func(turn))
#         print(board, x, score, move)
        if my_score is None or score == func([my_score,score]):
            my_score= score
            best_move= str(x)
        board[x] = " "
    return my_score, best_move

tictactoe_move_count = lambda board : sum([1 if v!=" " else 0 for v in board.values() ])
tmc = tictactoe_move_count

def minimax_with_length(board, turn, func=max):
        my_score = None
        best_move = None

        table_score = checkWinner(board)
        if table_score is not None:
            table_score = table_score * 10
            move_count = tmc(board)
            if table_score == -10:
                table_score =  table_score + move_count
            elif table_score == 10:
                table_score =  table_score - move_count
            
            return table_score, None
        for x in range(1,10):
            x = str(x)
            if board[x] != " ":
                continue
            board[x] = turn
            opponent = next_turn(turn)
            score, move = minimax_with_length(board,opponent,get_next_func(turn))
    #         print(board, x, score, move)
            if my_score is None or score == func([my_score,score]):
                my_score= score
                best_move= str(x)
            board[x] = " "
        return my_score, best_move
