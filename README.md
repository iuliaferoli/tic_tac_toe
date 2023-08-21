# Python tic-tac-toe game project

The instructions and interactive course for this project can be found on the Hyperskill website [here.](https://hyperskill.org/projects/73?track=6)

This project takes you along through building a very simple, beginner-oriented game in python. 
Through the different iterative problems, you will go from 0 to command-line game developer in 4 phases.
The course itseld has a lot of additional features, like tests that must be passed for each phase, with more specific descriptions of expected behavious on each level.

However, that is not to say signing up for the course is necessary to play along and build your own tic-tac-toe game. You can use the descriptions bellow as guidelines and build out your own version.

This is by no means the only (or the best) solution to building a tic-tac-toe game! Loads of variations are possible, this is simply an example of a possible interpretation of the game.

### [Phase 1: The board](/tictactoe_probmle1.py)

Build code that prints out a tic-tac-toe board such as:
```
X O X
O X O
X X X
```

### [Phase 2: Taking input](/tictactoe_problem2.py)

Make the board interactive. We're going from a string input such as `O_OXXO_XX` to a printed board that better displays the string representation.

### [Phase 3: What are we?](/tictactoe_problem3.py)

Read the current board standing (similar to the string input in the previous state) and determine the status of the game. The status can be:
* A win for either X or O if a (horizontal, vertical, or diagonal) line has been completed
* A draw if both players have won at the same time
* Unfinished - if the game is still being played
* Invalid - if the current board cannot be the result of a game following tic-tac-toe rules.

### [Phase 4: Making moves](/tictactoe_problem4.py)

Allow players to input the coordinates for a move, execute that move on the board, and display the new state of the game. 

### [Phase 5: It goes on and on and on]()

Create a game loop that takes the previous steps and builds a working tic-tac-toe game. Keep playing move by move until you have a winner!

