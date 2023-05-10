import numpy as np
import re


class MyBoard:
    def __init__(self):
        self.board = np.array([["_", "_", "_"],
                               ["_", "_", "_"],
                               ["_", "_", "_"]])
        self.win_state = "in progress"
        self.turn = "X"
        self.game_state = ""

    def read_board(self) -> None:
        self.board = np.array([*self.game_state]).reshape(3, 3)

    def print_board(self) -> None:
        board = self.board
        print("---------")
        for i in range(0, 3):
            print("| ", end='')
            for j in range(0, 3):
                print(board[i, j] + " ", end='')
            print("|")
        print("---------")

    def change_turn(self) -> None:
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"


def check_input(myBoard: MyBoard, play: str) -> str:
    if not bool(re.match(r"([0-9] [0-9])", play)):
        return "You should enter numbers!"
    if not bool(re.match(r"([0-3] [0-3])", play)):
        return "Coordinates should be from 1 to 3!"

    i, j = int(play[0]) - 1, int(play[2])-1
    if cell_not_empty(myBoard.board[i][j]):
        return "This cell is occupied! Choose another one! "

    myBoard.board[i][j] = myBoard.turn
    myBoard.change_turn()
    return "Move made"


def cell_not_empty(cell: str) -> bool:
    if cell == "_":
        return False
    else:
        return True


def check_same(line: np.array) -> bool:
    if line[0] == line[1] and line[1] == line[2] and cell_not_empty(line[0]):
        return True
    else:
        return False


def check_game_state(state: str) -> str:
    if state == "X wins" or state == "O wins" or state == "Draw":
        return "finished"
    else:
        return "in progress"


def win_check(myBoard: MyBoard) -> str:
    current_state = None
    game_state = myBoard.game_state
    board = myBoard.board
    wins = {"X": 0, "O": 0}

    # player symbols count checker
    if abs(game_state.count("O") - game_state.count("X")) > 1:
        current_state = "Impossible"

    lines = [board[0, :], board[1, :], board[2, :],
             board[:, 0], board[:, 1], board[:, 2],
             np.diag(board), np.diag(np.fliplr(board))]

    for line in lines:
        turn = line[0]
        if check_same(line):
            wins[turn] += 1

    if wins["X"] >= 1 and wins["O"] >= 1:
        current_state = "Impossible"
    elif wins["X"] >= 1:
        current_state = "X wins"
    elif wins["O"] >= 1:
        current_state = "O wins"

    if not current_state:
        if game_state.count("_") > 0:
            current_state = "Game not finished"
        else:
            current_state = "Draw"

    myBoard.win_state = check_game_state(current_state)
    return current_state


game_state = input("Enter game state: ")

myBoard = MyBoard()
myBoard.game_state = game_state
myBoard.read_board()
myBoard.print_board()

response = ''
while response != "Move made":
    play = input("Enter move: ")
    response = check_input(myBoard, play)
    if response == "Move made":
        myBoard.print_board()
    else:
        print(response)