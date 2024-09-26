def print_board(board):
    print("\n")
    print(f" {board[0] if board[0] != ' ' else 1} | {board[1] if board[1] != ' ' else 2} | {board[2] if board[2] != ' ' else 3} ")
    print("---|---|---")
    print(f" {board[3] if board[3] != ' ' else 4} | {board[4] if board[4] != ' ' else 5} | {board[5] if board[5] != ' ' else 6} ")
    print("---|---|---")
    print(f" {board[6] if board[6] != ' ' else 7} | {board[7] if board[7] != ' ' else 8} | {board[8] if board[8] != ' ' else 9} ")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    return all([spot != ' ' for spot in board])

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'

    while True:
        print_board(board)
        move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

        if board[move] == ' ':
            board[move] = current_player
        else:
            print("\nThat spot is already taken. Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

tic_tac_toe()
