def reveal(board, row, col):
    if not board.is_valid(row, col) or board.player_grid[row][col] != 'H':
        return True
    
    board.player_grid[row][col] = board.grid[row][col]

    if board.grid[row][col] == '*':
        return False 

    elif board.grid[row][col] == '0':
        for nr, nc in board._neighbours(row, col):
            reveal(board, nr, nc)

    return True 

def flag(board, row, col):
    if not board.is_valid(row, col):
        print("Invalid position.")
        return

    if board.player_grid[row][col] == 'H':
        board.player_grid[row][col] = 'F'
    elif board.player_grid[row][col] == 'F':
        board.player_grid[row][col] = 'H'
    else:
        print("Cannot flag that cell.")

def check_win(board):
    for r in range(9):
        for c in range(9):
            mine = (board.grid[r][c] == '*')
            hidden = (board.player_grid[r][c] == 'H')            
            if ((not mine) and hidden):
                return False                
    return True