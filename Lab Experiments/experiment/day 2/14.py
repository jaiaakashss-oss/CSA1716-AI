
# Alpha-Beta Pruning for Tic-Tac-Toe

board = [' '] * 9

def display():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("---------")

def winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[i] == player for i in line)
               for line in wins)

def alphabeta(is_max, alpha, beta):
    if winner('O'):
        return 1
    if winner('X'):
        return -1
    if ' ' not in board:
        return 0

    if is_max:
        best = -float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = alphabeta(False, alpha, beta)
                board[i] = ' '

                best = max(best, score)
                alpha = max(alpha, best)

                if beta <= alpha:
                    break

        return best

    else:
        best = float('inf')

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = alphabeta(True, alpha, beta)
                board[i] = ' '

                best = min(best, score)
                beta = min(beta, best)

                if beta <= alpha:
                    break

        return best

def best_move():
    best_score = -float('inf')
    move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = alphabeta(
                False, -float('inf'), float('inf')
            )
            board[i] = ' '

            if score > best_score:
                best_score = score
                move = i

    return move

# Main game
while True:
    display()

    try:
        move = int(input("Enter your move (0-8): "))
    except ValueError:
        print("Enter a valid number.")
        continue

    if move < 0 or move > 8 or board[move] != ' ':
        print("Invalid move!")
        continue

    board[move] = 'X'

    if winner('X'):
        display()
        print("You win!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break

    move = best_move()
    board[move] = 'O'
    print("Computer chooses:", move)

    if winner('O'):
        display()
        print("Computer wins!")
        break

    if ' ' not in board:
        display()
        print("Draw!")
        break
