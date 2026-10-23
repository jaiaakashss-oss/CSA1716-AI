
# Tic-Tac-Toe Game

board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

def check_win(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in line)
               for line in wins)

def computer_move():
    # Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win('O'):
                return
            board[i] = ' '

    # Block the human player
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win('X'):
                board[i] = 'O'
                return
            board[i] = ' '

    # Choose center, corner, or any empty cell
    for i in [4, 0, 2, 6, 8, 1, 3, 5, 7]:
        if board[i] == ' ':
            board[i] = 'O'
            return

print("Tic-Tac-Toe")
print("Positions:")
print("0 | 1 | 2")
print("3 | 4 | 5")
print("6 | 7 | 8")

while True:
    display()

    try:
        move = int(input("Enter your position (0-8): "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move! Try again.")
        continue

    board[move] = 'X'

    if check_win('X'):
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("It's a draw!")
        break

    computer_move()

    if check_win('O'):
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("It's a draw!")
        break
