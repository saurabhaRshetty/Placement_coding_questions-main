def solve_n_queens(board, row, n, count):
    if row == n:
        print_board(board)
        count[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, n, count)
            board[row][col] = '.'

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    count = [0]
    solve_n_queens(board, 0, n, count)
    print(f"Total solutions: {count[0]}")

# Set your desired number of queens here
n = 4
n_queens(n)
