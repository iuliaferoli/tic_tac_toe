
def board_print(game_state: str) -> None:
    print("---------")
    for line in range(0, 3):
        print("| ", end='')
        for column in range(0, 3):
            print(game_state[line * 3 + column] + " ", end='')
        print("|")
    print("---------")


def cell_not_empty(cell: str) -> bool:
    if cell == "-":
        return False
    else:
        return True


def check_same(a: str, b: str, c: str) -> bool:
    if a == b and b == c and cell_not_empty(a):
        return True
    else:
        return False


def win_check(game_state: str) -> str:
    current_state = None
    wins = {"X": 0, "O": 0}

    # player symbols count checker
    if abs(game_state.count("O") - game_state.count("X")) > 1:
        current_state = "Impossible"

    # line checker
    for line in range(0, 3):
        # check_cell will be the player symbol
        check_cell = game_state[3 * line]
        if check_same(game_state[3 * line], game_state[3 * line + 1], game_state[3 * line + 2]):
            wins[check_cell] += 1

    # column checker
    for column in range(0, 3):
        check_cell = game_state[column]
        if check_same(game_state[column], game_state[column + 3], game_state[column + 6]):
            wins[check_cell] += 1

    # diagonals checker
    check_cell = game_state[4]
    if check_same(game_state[0], game_state[4], game_state[8]):
        wins[check_cell] += 1
    if check_same(game_state[2], game_state[4], game_state[6]):
        wins[check_cell] += 1

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

    return current_state


game_state = input("Enter game state: ")
board_print(game_state)
print(win_check(game_state))