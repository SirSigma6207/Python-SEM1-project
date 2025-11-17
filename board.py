import random

class Board:
    def __init__(self, size=9, num_mines=10):
        self.size = size
        self.num_mines = num_mines
        self.grid = []
        self.player_grid = []

        self._init_grids()       
        self._place_mines()
        self._calc_num()

    def _init_grids(self):
    
        self.grid = [['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0'],['0','0','0','0','0','0','0','0','0']]

        self.player_grid = [['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H'],['H','H','H','H','H','H','H','H','H']]

    

    def _place_mines(self): 
        curr_mines = 0
        while (curr_mines < 10):
            row = random.randint(0, 8)
            col = random.randint(0, 8)            
            
            if self.grid[row][col] != '*':
                self.grid[row][col] = '*'
                curr_mines+=1

    def is_valid(self, row, col):
        if ((row>=0 and row<9) and (col>=0 and col<9)):
            return True
        else:
            return False

    def _neighbours(self, row, col):
        neighbours = [] #list of lists of all the neighbours of the cell
        for nr in [0,1,-1]:
            for nc in [0,1,-1]: #to check all 8 possible combinations
                if nr==0 and nc==0:
                    continue  
                else:                
                    nrow = row + nr
                    ncol = col + nc                 
                    if self.is_valid(nrow, ncol):
                        neighbours.append([nrow,ncol])
        return neighbours
    
    def _calc_num(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == '*':
                    continue
                
                mine_count = 0
                for nr, nc in self._neighbours(r,c): #neighbours = [(nr,nc)]
                    if self.grid[nr][nc] == '*':
                        mine_count+=1 
                
                self.grid[r][c] = str(mine_count)        

    def print_board(self):
        print("   " + " ".join([str(i) for i in range(self.size)]))
        print("  " + "-" * (self.size * 2))
        
        for rindex, r in enumerate(self.player_grid):
            print(f"{rindex} |" + " ".join(r))
        print()

    def reveal(self):
        for r in range(9):
            for c in range(9):
                self.player_grid[r][c] = self.grid[r][c]