import time
from board import Board
import game_logic
import file_manager

def user_input(board_size):
    try:
        user_inp = input("Press r to reveal or f to flag a cell followed by the coordinates: ").split()
        
        if len(user_inp)!=3:
            print("Invalid input.")
            return None, None, None

        cmd = user_inp[0].lower()
        row = int(user_inp[1])
        col = int(user_inp[2])

        if (cmd!='r' and cmd !='f'):
            print("Command should be 'r' or 'f' only")
            return None,None,None

        if not ((row < board_size and row>=0) and (col>=0 and col < board_size)):
            print(f"Invalid coordinates.")
            return None,None,None            
        return cmd,row,col

    except ValueError:
        print("Row and col must be integers.")
        return None,None,None

def run_game():
    board = Board(size=9, num_mines=10)
    g_over = False
    g_won = False

    best_time = file_manager.load_time()
    if best_time:
        print(f"The best time to beat is: {best_time:.2f} seconds.")

    start_time = time.time()

    while not g_over and not g_won:
        board.print_board()        
        cmd,row,col = user_input(board.size)
        
        if cmd=="":
            continue  
        if cmd=='r':
            if not game_logic.reveal(board, row, col):
                print("You hit a bloody mine. GOODBYEEE !!!.")
                g_over = True                        
        elif cmd=='f':
            game_logic.flag(board, row, col)            
        if not g_over:
            g_won = game_logic.check_win(board)
            
    end_time = time.time()
    time_taken = end_time - start_time
    board.reveal()
    board.print_board()

    if g_won:
        print(f"YOU WIN!!! You took {time_taken:.2f} seconds to complete.")
        file_manager.save_time(time_taken)    
    
if __name__ == "__main__":
    print("*****MINESWEEPER (CLI)*****")
    run_game()