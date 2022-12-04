# Final-Project-EECE2140

1. I am working alone

2. Sudoku generator and solver

Sudoku is a mathematical puzzle game. Each 9-element row, 9-element column, and 3x3 square in a Sudoku grid should contain the numbers 1-9 with no repeats. 

Write a program to solve a Sudoku grid. Your program should accept both an empty Sudoku grid and a partially filled grid. For an empty Sudoku grid input, your program should randomly generate a valid Sudoku grid. Your program should also be able to randomly remove numbers from a  solved grid to create easy, medium, or difficult solvable Sudoku puzzles. An "easier" puzzle can be defined either as a puzzle that has more solutions, or a puzzle that requires the user to fill in fewer squares.

3. I will use a generator class where I will generate the sodoku grid up until the point where there is only one solution. I could expand upon this by adding more numbers than needed to generate easier puzzles. I would include some sort of constructor so that the class can take in a partially filled or empty grid and throw an exception if there is no solution to the partially filled gird. I would create a method to randomly fill the grid until it has only one solution. This might have several helpers that check whether the horizontal, vertical, and box are correctly filled. I would introduce a solver class where I would fully solve the puzzle. This might extend the generator class.

4. I would probably need numpy to use matricies and might use math to perform square roots if needed.

5. The highest priority feature is to be able to able to solve the puzzle after it is generated. The medium priority would be to randomly generate the puzzle and possibly tell how many solutions there are, and then be able to display one with 1 solution. Being able to play the game through the terminal would be between medium and least priority. The least priority would be the difficulty generation methods, multiple sized sudokus and a fancier display.
