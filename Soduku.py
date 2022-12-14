import numpy as np
import copy
from random import shuffle
from random import sample
class Sudoku:
  def __init__(self, arr = [[0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0]]): #default to empty unless given an array
    self.board = arr
  def make_empty_board(self):
    self.board = [[0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]

  def place(self, x, y, n):
    self.board[y][x] = n

  def remove(self, x, y):
    self.board[y][x] = 0

  # easy print method, will improve later
  def print_board(self):
    print(np.matrix(self.board))

  def is_empty(self, x, y):
    return self.board[y][x] == 0

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

  def is_board_solved(self):
    for y in range(9):
      for x in range(9):
       if self.board[y][x] == 0:     
        return False 
    return True
  
  def numbers_count(self):
    count = 0
    for y in range(9):
      for x in range(9): # checks every square on the board
        if not self.board[y][x] == 0: # for every square that is not 0 increase the count
          count += 1
    return count

  def generate_board(self):
    self.generate_solved_board()
    not_empty = []
    for i in range(9):
      for j in range(9):
        if self.board[i][j] != 0:
          not_empty.append((i, j)) # stores all not empty squares as tuples
    shuffle(not_empty)
    not_empty_count = len(not_empty)
    rounds = 3
    while rounds > 0 and not_empty_count >= 17:
      x, y = not_empty.pop()
      not_empty_count -= 1
      removed_square = self.board[y][x]
      self.remove(x,y)
      if self.solutions_count() != 1:
        self.board[y][x] = removed_square
        not_empty_count += 1
        rounds -= 1
    return
  
  def generate_solved_board(self):
    # pattern for what the solution should be 
    def pattern(r,c): return (3 * (r % 3) + r // 3 + c) % 9
    # randomize everything, but make sure its the same pattern
    def shuffle(s): return sample(s,len(s)) 
    rows  = [ g * 3 + r for g in shuffle(range(3)) for r in shuffle(range(3)) ] 
    cols  = [ g * 3 + c for g in shuffle(range(3)) for c in shuffle(range(3)) ]
    nums  = shuffle(range(1, 3 * 3 + 1))
    self.board = [[nums[pattern(r,c)] for c in cols] for r in rows]

  
  count = 0
  def solutions_count(self):
    board_copy = copy.deepcopy(self.board) # copy so that it doesn't mess up the actual board
    self.solutions_count_helper()
    countCopy = self.count
    self.count = 0
    self.board = copy.deepcopy(board_copy)
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
    self.generate_board()
    print("Your sudoku board is: ")
    print()
    self.print_board()
    while not self.is_board_solved():
      n = int(input("Enter the number you wish to place: "))
      x = int(input("Enter the column you wish to place the number in: "))
      y = int(input("Enter the row you wish to place the number in: "))
      if self.is_valid_move(x, y, n) and self.is_empty(x - 1, y - 1):
        self.place(x - 1, y - 1, n)
        self.print_board()
      else:
        print("Number unable to be placed in that spot")
        flag = input("Would you like the solution? 'Y' if yes, 'N' if no: ")
        if flag == "Y":
          print("The solution is: ")
          self.solve()
          return
    print("Congratulations! You won!")
    return

MySudoku = Sudoku()
MySudoku.start()
    
