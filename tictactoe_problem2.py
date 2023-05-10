
def board_print(game_state: str) -> None:
    print("---------")
    for line in range(0, 3):
        print("| ", end='')
        for column in range(0, 3):
            print(game_state[line * 3 + column] + " ", end='')
        print("|")
    print("---------")

# example game_state O_OXXO_XX
game_state = input("Enter game state: ")
board_print(game_state)
