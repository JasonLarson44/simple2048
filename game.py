from random import randint


def display(board):
    i = 0
    j = 0
    max_size = len(board)
    while i < max_size:
        j = 0
        while j < len(board[i]):
            value = board[i][j]
            print(board[i][j], end="\t")
            # if value is None or value >= 1000:
            #     print(board[i][j], end="\t")
            # else:
            #     print(board[i][j], end="\t\t")
            j += 1
        print("")
        i += 1
    print("")


def get_player_input():
    valid_moves = ['up', 'down', 'left', 'right', 'exit']
    move = input("Make your move: ")
    tries = 0
    while move not in valid_moves and tries < 4:
        print("Please select from: ", valid_moves)
        tries += 1
        move = input("Make your move: ")
    if move == 'exit':
        exit(0)
    elif move in valid_moves:
        return move
    else:
        return 'up'


def get_open_spaces(board):
    i = 0
    max_size = len(board)
    available = []
    while i < max_size:
        j = 0
        while j < max_size:
            if board[i][j] is None:
                available.append((i, j))
            j += 1
        i += 1
    return available


def spawn_num(board):
    num = randint(1, 2)
    available_spots = get_open_spaces(board)
    rand = randint(0, len(available_spots)-1)
    spot = available_spots[rand]
    board[spot[0]][spot[1]] = num * 2
    return board


def move_row_left(row):
    i = 0
    max = len(row) - 1
    while i < max:
        j = i + 1
        while row[j] is None and j < max:
            j += 1
        if row[i] is None:
            row[i] = row[j]
            row[j] = None
        elif i + 1 != j:
            row[i+1] = row[j]
            row[j] = None
        i += 1
    return row


def merge_row_left(row):
    i = 0
    max = len(row) - 1
    while i < max:
        j = i + 1
        while row[j] is None and j < max:
            j += 1
        if row[i] is not None and row[i] == row[j]:
            row[i] = row[i]*2
            row[j] = None
        i += 1
    return row


def move_row_right(row):
    max = len(row) - 1
    i = max
    while i > 0:
        j = i - 1
        while row[j] is None and j > 0:
            j -= 1
        if row[i] is None:
            row[i] = row[j]
            row[j] = None
        elif i - 1 != j:
            row[i-1] = row[j]
            row[j] = None
        i -= 1
    return row


def merge_row_right(row):
    max = len(row) - 1
    i = max
    while i > 0:
        j = i - 1
        while row[j] is None and j > 0:
            j -= 1
        if row[i] is not None and row[i] == row[j]:
            row[i] = row[i]*2
            row[j] = None
        i -= 1
    return row


def move_left(board):
    for row in board:
        row = merge_row_left(row)
        row = move_row_left(row)
    return board


def move_right(board):
    for row in board:
        row = merge_row_right(row)
        row = move_row_right(row)
    return board


def move_up(board):
    i = 0
    while i < len(board):
        column = []
        for row in board:
            column.append(row[i])
        merge_row_left(column)
        move_row_left(column)
        column_i = 0
        for row in board:
            row[i] = column[column_i]
            column_i += 1
        i += 1
    return board


def move_down(board):
    i = 0
    while i < len(board):
        column = []
        for row in board:
            column.append(row[i])
        column = merge_row_right(column)
        column = move_row_right(column)
        column_i = 0
        for row in board:
            row[i] = column[column_i]
            column_i += 1
        i += 1
    return board


if __name__ == "__main__":
    gameboard = [
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]
    playing = True
    gameboard = spawn_num(gameboard)
    display(gameboard)
    while playing:
        move = get_player_input()
        if move == "up":
            gameboard = move_up(gameboard)
        elif move == "down":
            gameboard = move_down(gameboard)
        elif move == "right":
            gameboard = move_right(gameboard)
        elif move == "left":
            gameboard = move_left(gameboard)
        gameboard = spawn_num(gameboard)
        display(gameboard)
