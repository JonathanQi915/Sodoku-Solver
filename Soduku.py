import numpy as np;
class Sudoku:
  def __init__(self, num):
    if num == 1:
      self.board = [[8,9,0,0,6,2,0,0,0],
                    [0,0,0,0,8,0,0,4,0],
                    [0,1,7,0,0,5,2,0,0],
                    [7,0,0,0,0,1,0,0,0],
                    [0,6,8,0,0,0,0,5,4],
                    [0,0,0,0,5,0,8,0,7],
                    [6,3,1,5,2,0,9,0,8],
                    [5,8,0,7,3,0,4,1,2],
                    [0,0,0,9,1,0,0,6,0]]
    elif num == 2:
      self.board = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0,0]]
    elif num == 3: 
      self.board = [[8,9,0,0,6,2,0,0,0],
                    [0,0,0,0,8,0,0,4,0],
                    [0,1,7,0,0,5,2,0,0],
                    [7,0,0,0,0,1,0,0,0],
                    [0,6,8,0,0,0,0,5,4],
                    [0,0,0,0,5,0,8,0,7],
                    [6,3,1,5,2,0,0,0,8],
                    [5,8,0,7,3,0,4,1,2],
                    [0,0,0,9,1,0,0,6,0]]
  def make_empty_board(self):
    self.board = [[0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0,0,0]]

  def place(self, x, y, n):
    self.board[y][x] = n

  # easy print method, will improve later
  def print_board(self):
    print(np.matrix(self.board))

  def is_valid_move(self, x, y, n) : 
    x = x - 1
    y = y - 1
    for i in range(9):
      if i != x and self.board[y][i] == n: # checks the row for the number, ignores the original square
        return False
    for i in range(9):
      if i != y and self.board[i][x] == n: # checks the column for the number, ignores the original square
        return False
    for i in range(3):
      for j in range(3): 
        if (not (((y // 3) * 3) + i == y and ((x // 3) * 3) + j == x)) and self.board[((y // 3) * 3) + i][((x // 3) * 3) + j] == n: 
          # checks the square for the number; ((x // 3) * 3) will floor the variable to the nearest multiple of 3, ignores the original square
          return False 
    return True

  def is_board_correct(self):
    for y in range(9):
      for x in range(9):
       if self.board[y][x] != 0:     
        if not (self.is_valid_move(x + 1, y + 1, self.board[y][x])):
          return False 
    return True


  def generate_board(self):
    pass
  
  count = 0
  def solutions_count(self):
    self.solutions_count_helper()
    countCopy = self.count
    self.count = 0
    return countCopy
  
  def solutions_count_helper(self):
    for y in range(9):
      for x in range(9): # checks every square on the board
       if self.board[y][x] == 0: # terminates on the condition that all squares are non zero
        for n in range(1, 10):
          if self.is_valid_move(x + 1, y + 1, n): # tests every number in the empty square to see if it is valid
            self.place(x, y, n) # sets the valid number to the square
            self.solutions_count_helper() # recurses and goes to the next unsolved square
            self.place(x, y, 0) # back tracking, if there is no solution it resets the empty square and tries to solve it
                                 # while all the other squares are valid
        return # void method (just mutates the board)
    self.count = self.count + 1 # increases the count for every solution

  def solve(self):
    for y in range(9):
      for x in range(9): # checks every square on the board
       if self.board[y][x] == 0: # terminates on the condition that all squares are non zero
        for n in range(1, 10):
          if self.is_valid_move(x + 1, y + 1, n): # tests every number in the empty square to see if it is valid
            self.place(x, y, n) # sets the valid number to the square
            self.solve() # recurses and goes to the next unsolved square
            self.place(x, y, 0) # back tracking, if there is no solution it resets the empty square and tries to solve it
                                 # while all the other squares are valid
        return # void method (just mutates the board)
    print(np.matrix(self.board)) # prints every solution
    print()

  def start(self):
    pass

# print debugging
MySudoku = Sudoku(3)
MySudoku.print_board()
MySudoku.solve()
print(MySudoku.solutions_count())
print(MySudoku.count)
MySudoku.board[0][0]
print(MySudoku.is_board_correct())
print(MySudoku.is_valid_move(1,1,1))
print(MySudoku.is_valid_move(2,2,2))
print(MySudoku.is_valid_move(4,2,5))
print(MySudoku.is_valid_move(2,4,5))
print(MySudoku.is_valid_move(2,2,4))
print(MySudoku.is_valid_move(2,2,7))
print(MySudoku.is_valid_move(2,2,3))